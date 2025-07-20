
from indicators.base import BaseIndicator
import geopandas as gpd

class PowerDemandIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        def classify_demand(code):
            code = str(code).lower()
            if "nau" in code:
                return "Very High"
            elif "hua" in code or "had" in code:
                return "High"
            elif "cg" in code or "mdun" in code:
                return "Medium"
            elif "co" in code or "mr" in code or "chr" in code:
                return "Low"
            elif "wl" in code or "wb" in code:
                return "Minimal"
            return "Unknown"

        gdf["power_demand_level"] = gdf["CODI_COBER"].apply(classify_demand)
        return gdf
