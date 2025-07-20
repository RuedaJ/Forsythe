
from indicators.base import BaseIndicator
import geopandas as gpd

class LandCoverIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        def classify_landcover(code):
            code = str(code).lower()
            if "nau" in code or "hua" in code or "had" in code:
                return "Urban"
            return "Non-Urban"

        gdf["landcover_type"] = gdf["CODI_COBER"].apply(classify_landcover)
        return gdf
