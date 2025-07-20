
from indicators.base import BaseIndicator
import geopandas as gpd

class FloodRiskIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        def flood_risk(code):
            code = str(code).lower()
            if "wb" in code or "wl" in code or "wa" in code:
                return "Potential Flood Risk"
            return "Low Risk"

        gdf["flood_risk_zone"] = gdf["CODI_COBER"].apply(flood_risk)
        return gdf
