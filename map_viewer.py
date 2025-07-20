
import streamlit as st
import pydeck as pdk

def display_map(gdf):
    """
    Display a GeoDataFrame using Pydeck with enhanced 3D visualization.
    """
    if gdf.empty:
        st.warning("GeoDataFrame is empty.")
        return

    # Convert to WGS84 for map compatibility
    gdf_wgs84 = gdf.to_crs(epsg=4326)
    gdf_wgs84["lat"] = gdf_wgs84.geometry.centroid.y
    gdf_wgs84["lon"] = gdf_wgs84.geometry.centroid.x

    # Add dummy elevation for extrusion (proxy for realism)
    gdf_wgs84["elevation"] = gdf_wgs84["population_density_est"].map({
        "High": 3000,
        "Medium": 2000,
        "Low": 1000,
        "Very Low": 500
    }).fillna(800)

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/satellite-streets-v12",
        initial_view_state=pdk.ViewState(
            latitude=gdf_wgs84["lat"].mean(),
            longitude=gdf_wgs84["lon"].mean(),
            zoom=12,
            pitch=50,
            bearing=20,
        ),
        layers=[
            pdk.Layer(
                "PolygonLayer",
                data=gdf_wgs84,
                get_polygon="geometry.coordinates",
                get_fill_color="[100, 200, 100, 140]",
                get_elevation="elevation",
                extruded=True,
                wireframe=True,
                pickable=True,
                auto_highlight=True,
            )
        ],
        tooltip={"html": "<b>Land Cover:</b> {CODI_COBER}<br><b>Density:</b> {population_density_est}"}
    ))
