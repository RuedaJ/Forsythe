
from indicators.base import BaseIndicator
import geopandas as gpd

class PopulationDensityIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        def estimate_density(code):
            code = str(code).lower()
            if "nau" in code:
                return "High"
            elif "hua" in code or "had" in code:
                return "Medium"
            elif "mr" in code or "co" in code or "wl" in code:
                return "Low"
            elif "wb" in code or "chr" in code:
                return "Very Low"
            return "Unknown"

        gdf["population_density_est"] = gdf["CODI_COBER"].apply(estimate_density)
        return gdf
