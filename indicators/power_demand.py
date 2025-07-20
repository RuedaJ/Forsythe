
from indicators.base import BaseIndicator
import geopandas as gpd

class PowerDemandIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Estimate relative power demand based on land cover codes.
        """
        def classify_demand(code):
            if str(code).startswith("1"):  # urban
                return "High"
            elif str(code).startswith("2"):  # industrial/infrastructure
                return "Very High"
            elif str(code).startswith("3"):  # agricultural
                return "Medium"
            elif str(code).startswith("4"):  # forest/natural
                return "Low"
            else:
                return "Unknown"

        gdf["power_demand_level"] = gdf["CODI_COBER"].apply(classify_demand)
        return gdf
