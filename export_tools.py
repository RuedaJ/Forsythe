
import geopandas as gpd
import zipfile
import os

def export_geojson(gdf: gpd.GeoDataFrame, out_path: str):
    gdf.to_file(out_path, driver="GeoJSON")

def export_shapefile(gdf: gpd.GeoDataFrame, base_path: str):
    temp_dir = os.path.join(base_path, "shp_export")
    os.makedirs(temp_dir, exist_ok=True)
    shp_path = os.path.join(temp_dir, "export.shp")
    gdf.to_file(shp_path)
    zip_path = os.path.join(base_path, "export_shapefile.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in os.listdir(temp_dir):
            zipf.write(os.path.join(temp_dir, file), arcname=file)
    return zip_path
