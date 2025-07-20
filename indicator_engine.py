
from indicators.landcover import LandCoverIndicator
from indicators.power_demand import PowerDemandIndicator
from indicators.population_density import PopulationDensityIndicator
from indicators.flood_risk import FloodRiskIndicator

def run_indicators(gdf):
    indicators = [
        LandCoverIndicator(),
        PowerDemandIndicator(),
        PopulationDensityIndicator(),
        FloodRiskIndicator()
    ]
    for indicator in indicators:
        gdf = indicator.extract(gdf)
    return gdf
