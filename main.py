import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sys
import functions as f
import plotting as p

# To Do
# Logging
# General Clean Up
# Reading from Folder
# Averaging Values
# Trendline Generator

filePath = 'TR22-FC0739/TR22-FC0739-1-4-1-4.dat'

finalData = f.dataParser(filePath)

compressionDataIndex = np.array([])
reboundDataIndex = np.array([])

for i in range(0,len(finalData[:,0])):
  if finalData[i,1] > 0:
    compressionDataIndex = np.append(compressionDataIndex,i).astype(int)
  elif finalData[i,1] < 0:
    reboundDataIndex = np.append(reboundDataIndex,i).astype(int)

# cleanCompression = f.outlierObliteratorZScore(compressionDataIndex,finalData,dX=0.1,SD=1)
cleanCompression = f.outlierObliteratorIQR(compressionDataIndex,finalData,dX=0.01,iqrRange=(40,60))

p.scatter(cleanCompression[:,3],cleanCompression[:,1],title=filePath + ' IQR [40,60] dX 0.01')

# print(finalData) # only numbers, with positive velocity 4th [:,3] column

# Plotting
# plt.figure(figsize=(9, 6))
# plt.title(filePath)
# plt.xlabel('Velocity (in/sec)')
# plt.ylabel('Force (lbf)')
# plt.scatter(finalData[:,3],finalData[:,1],s=5,alpha=0.5)
# plt.show()

# z = np.abs(stats.zscore(finalData))
# print(z)