
import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

def display_folium_map(gdf: gpd.GeoDataFrame):
    """
    Display a GeoDataFrame using Folium for faster 2D visualization.
    """
    if gdf.empty:
        st.warning("GeoDataFrame is empty.")
        return

    # Convert to WGS84
    gdf = gdf.to_crs(epsg=4326)

    # Center map
    centroid = gdf.geometry.unary_union.centroid
    m = folium.Map(location=[centroid.y, centroid.x], zoom_start=12, tiles="CartoDB positron")

    # Add polygons with tooltips
    folium.GeoJson(
        gdf,
        tooltip=folium.GeoJsonTooltip(fields=["CODI_COBER", "population_density_est", "power_demand_level"]),
        name="Land Cover"
    ).add_to(m)

    # Display map
    st_folium(m, width=1000, height=600)
