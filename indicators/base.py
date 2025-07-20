
from abc import ABC, abstractmethod
import geopandas as gpd

class BaseIndicator(ABC):
    @abstractmethod
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Extract indicators and add them as new columns to the GeoDataFrame.
        """
        pass
