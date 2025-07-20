
from indicators.landcover import LandCoverIndicator
from indicators.power_demand import PowerDemandIndicator
from indicators.population_density import PopulationDensityIndicator

def run_indicators(gdf):
    """
    Apply all configured indicators to the input GeoDataFrame.
    """
    indicators = [
        LandCoverIndicator(),
        PowerDemandIndicator(),
        PopulationDensityIndicator()
    ]

    for indicator in indicators:
        gdf = indicator.extract(gdf)

    return gdf
