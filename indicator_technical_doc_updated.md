# Indicator Extraction – Technical Documentation

## Overview
This module implements proxy indicators using symbolic land cover codes from the ICGC `TERRITORI_M_COBERTES_SOL_V4` shapefile. These indicators support early desk studies and due diligence workflows before detailed datasets are available.

## Implemented Indicators

### 1. Land Cover Type
**Goal**: Identify urban vs. non-urban areas  
**Method**: Uses symbolic substrings in `CODI_COBER`:
- Contains 'nau', 'hua', or 'had': Urban
- Otherwise: Non-Urban

### 2. Power Demand Level
**Goal**: Estimate relative energy demand  
**Method**: Symbolic substring match from `CODI_COBER`:
- 'nau': Very High
- 'hua', 'had': High
- 'cg', 'mdun': Medium
- 'co', 'mr', 'chr': Low
- 'wl', 'wb': Minimal

### 3. Population Density Estimate
**Goal**: Estimate population distribution  
**Method**: Based on `CODI_COBER` patterns:
- 'nau': High
- 'hua', 'had': Medium
- 'mr', 'co', 'wl': Low
- 'wb', 'chr': Very Low

### 4. Flood Risk Zone
**Goal**: Identify flood-prone land types  
**Method**: Code contains 'wb', 'wl', or 'wa' → Potential Flood Risk  
All other codes → Low Risk

## Rationale
These heuristics offer rapid, low-cost spatial insights:
- Urban patterns suggest energy/population loads
- Forest and water areas often correspond to low demand or risk zones

## Limitations
- Does **not** use actual hazard, census, or elevation data
- Substring matching can lead to ambiguous classifications
- Results are suitable for **screening only**, not engineering decisions

## Future Work
- Integrate official seismic, floodplain, and soil layers
- Use real population and utility data
- Export maps as image tiles or PDFs
- Add user-defined indicators and weighting