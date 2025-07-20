
import geopandas as gpd

def load_shapefile(file_path: str) -> gpd.GeoDataFrame:
    """
    Load a shapefile and return a GeoDataFrame.
    """
    try:
        gdf = gpd.read_file(file_path)
        return gdf
    except Exception as e:
        raise RuntimeError(f"Error loading shapefile: {e}")
