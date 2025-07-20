
from indicators.base import BaseIndicator
import geopandas as gpd

class LandCoverIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        # Dummy logic: Classify urban vs non-urban from `CODI_COBER` code
        gdf["landcover_type"] = gdf["CODI_COBER"].apply(
            lambda x: "Urban" if str(x).startswith("1") else "Non-Urban"
        )
        return gdf
