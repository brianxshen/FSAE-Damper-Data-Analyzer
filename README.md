# FSAE-Damper-Data-Analyzer
This code is used to clean up the data from the damper dyno and then approximate damping ratios using curve fitting tools.

## Features
- Removes text and stray data from .dat file
- Instantaneous velocity is calculated for every datapoint
- Data is separated into compression and rebound for separate analysis
- Data is "sliced" into a configurable slice width to remove outliers using 
  - IQR with configurable range (ex. [40,60])
  - Z Scores with configurable limit (ex. 2 SD)
  - Median (reduces data points as well)

Made for Terps Racing: Formula SAE @ University of Maryland: College Park
