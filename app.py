
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
    import os
    test_file_path = os.path.join("data", "TERRITORI_M_COBERTES_SOL_V4.shp")
    gdf = load_shapefile(test_file_path)
    gdf = run_indicators(gdf)

    st.subheader("Enriched Attribute Table")
    st.dataframe(gdf.drop(columns="geometry").head(10))

    st.subheader("Map Viewer")
    viewer_type = st.radio("Select Map Type", options=["2D (Fast - Folium)", "3D (Pydeck)"])

    if viewer_type == "2D (Fast - Folium)":
        display_folium_map(gdf)
    else:
        display_map(gdf)

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
