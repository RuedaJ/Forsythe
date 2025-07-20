
# Indicator Extraction – Technical Documentation

## Overview
This module implements basic proxy indicators using only land cover data from the ICGC `TERRITORI_M_COBERTES_SOL_V4` shapefile. These indicators are intended to support rapid desk studies and due diligence assessments when more detailed datasets are not yet available.

## Implemented Indicators

### 1. Land Cover Type
**Goal**: Identify urban vs. non-urban areas.
**Method**: Uses `CODI_COBER` code prefix:
- Starts with '1': Urban
- Else: Non-Urban

### 2. Power Demand Level
**Goal**: Estimate relative energy demand intensity.
**Method**: Based on land cover types:
- Urban (code starts with '1'): High
- Industrial/infrastructure ('2'): Very High
- Agricultural ('3'): Medium
- Forest/Natural ('4'): Low

### 3. Population Density Estimate
**Goal**: Roughly approximate population distribution.
**Method**: Proxy categories based on land cover:
- Urban: High
- Industrial: Medium
- Agricultural: Low
- Forest: Very Low

## Rationale
- Land cover codes often correlate with human activity and infrastructure needs.
- When no census or energy data is available, this can guide early planning and prioritization.

## Limitations
- Does **not** use actual population, energy, or hazard datasets.
- Classification is **heuristic** and may vary significantly from ground truth.
- Flood, seismic, and geotechnical indicators are not yet supported.

## Future Work
- Ingest real hazard layers (seismic, floodplains, slope/soil).
- Integrate census-based population rasters or vector data.
- Calculate real energy load maps using demand models or utility overlays.
- Allow user-defined indicator logic or weightings via a config system.

