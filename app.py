
import streamlit as st
from data_loader import load_shapefile
from map_viewer import display_map
from folium_map_viewer import display_folium_map
from indicator_engine import run_indicators
from export_tools import export_geojson, export_shapefile
import os

st.set_page_config(layout="wide")
st.title("GeoApp – Streamlit Geospatial Viewer")

uploaded_file = st.file_uploader("Upload a Shapefile (.shp)", type=["shp"])

if uploaded_file:
    st.info("Please upload all shapefile components (.shp, .dbf, .shx, .prj) in one folder.")
else:
    test_file_path = os.path.join("data", "TERRITORI_M_COBERTES_SOL_V4.shp")
    gdf = load_shapefile(test_file_path)
    gdf = run_indicators(gdf)

    st.subheader("Enriched Attribute Table")
    st.dataframe(gdf.drop(columns="geometry").head(10))

    st.subheader("Map Viewer")

    viewer_type = st.radio("Select Map Type", options=["2D (Fast - Folium)", "3D (Pydeck)"])
    indicator_layer = st.selectbox("Select Indicator to Display", [
        "landcover_type",
        "population_density_est",
        "power_demand_level",
        "flood_risk_zone"
    ])

    if viewer_type == "2D (Fast - Folium)":
        from streamlit_folium import st_folium
        import folium

        gdf = gdf.to_crs(epsg=4326)
        centroid = gdf.geometry.unary_union.centroid
        m = folium.Map(location=[centroid.y, centroid.x], zoom_start=12, tiles="CartoDB positron")

        folium.GeoJson(
            gdf,
            tooltip=folium.GeoJsonTooltip(fields=[indicator_layer]),
            name="Indicator"
        ).add_to(m)

        st_folium(m, width=1000, height=600)

    else:
        import pydeck as pdk
        gdf = gdf.to_crs(epsg=4326)
        gdf["lat"] = gdf.geometry.centroid.y
        gdf["lon"] = gdf.geometry.centroid.x

        elevation_map = {
            "Very High": 4000,
            "High": 3000,
            "Medium": 2000,
            "Low": 1000,
            "Very Low": 500,
            "Minimal": 200,
            "Potential Flood Risk": 2500,
            "Low Risk": 800,
            "Urban": 3500,
            "Non-Urban": 1000
        }

        gdf["elevation"] = gdf[indicator_layer].map(elevation_map).fillna(800)

        st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/satellite-streets-v12",
            initial_view_state=pdk.ViewState(
                latitude=gdf["lat"].mean(),
                longitude=gdf["lon"].mean(),
                zoom=12,
                pitch=50,
                bearing=20,
            ),
            layers=[
                pdk.Layer(
                    "PolygonLayer",
                    data=gdf,
                    get_polygon="geometry.coordinates",
                    get_fill_color="[100, 200, 100, 140]",
                    get_elevation="elevation",
                    extruded=True,
                    wireframe=True,
                    pickable=True,
                    auto_highlight=True,
                )
            ],
            tooltip={"html": f"<b>{{{indicator_layer}}}</b>"}
        ))

    st.subheader("Export Options")

    if st.button("Download GeoJSON"):
        geojson_path = "exported_data/export.geojson"
        export_geojson(gdf, geojson_path)
        with open(geojson_path, "rb") as f:
            st.download_button("Download GeoJSON", f, file_name="export.geojson")

    if st.button("Download Shapefile (ZIP)"):
        zip_path = export_shapefile(gdf, "exported_data")
        with open(zip_path, "rb") as f:
            st.download_button("Download Shapefile", f, file_name="export_shapefile.zip")
