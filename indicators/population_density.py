
from indicators.base import BaseIndicator
import geopandas as gpd

class PopulationDensityIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Estimate population density category from land cover codes.
        """
        def estimate_density(code):
            if str(code).startswith("1"):  # residential urban
                return "High"
            elif str(code).startswith("2"):  # industrial/infrastructure
                return "Medium"
            elif str(code).startswith("3"):  # rural/agricultural
                return "Low"
            elif str(code).startswith("4"):  # forest
                return "Very Low"
            else:
                return "Unknown"

        gdf["population_density_est"] = gdf["CODI_COBER"].apply(estimate_density)
        return gdf
