import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sys
import functions as f
import plotting as p

# To Do
# Logging MID
# General Clean Up MID
# Reading from Folder LOW
# Averaging Values HIGH
# Trendline Generator HIGH
# Combine outlierObliterators into one LOW
# Add DBSCAN outlier removal method HIGH
# DONE: Add Median Only Method HIGH
# Make dX and dmax required in functions
# Add caching of previously run data

filePath = 'TR22-FC0739/TR22-FC0739-1-4-1-4.dat'

finalData = f.dataParser(filePath)

reboundDataIndex,compressionDataIndex = f.dataSeparator(finalData)

# cleanCompression = f.outlierObliteratorZScore(compressionDataIndex,finalData,dX=0.1,SD=1,
#                                           dataIndex=compressionDataIndex)
# cleanCompression = f.outlierObliteratorIQR(finalData,
#                                            dX=0.01,
#                                            iqrRange=(25, 75),
#                                            dataIndex=compressionDataIndex)
cleanCompression = f.outlierObliteratorMedian(finalData,dX=0.05,dMax=12,dataIndex=compressionDataIndex)

lowSpeedDataIndex,highSpeedDataIndex = f.dataSeparator(cleanCompression,lowerBound=2,upperBound=2,dataColumn=3)

x = f.dataFilter(highSpeedDataIndex,cleanCompression)[:, 3]
y = f.dataFilter(highSpeedDataIndex,cleanCompression)[:, 1]

fit = np.polyfit(x,y,1)
xp = np.linspace(2,12,100)
p1 = np.poly1d(fit)

t = plt.scatter(f.dataFilter(highSpeedDataIndex,cleanCompression)[:, 3],f.dataFilter(highSpeedDataIndex,cleanCompression)[:, 1],s=5,alpha=0.5)
_ = plt.plot(xp,p1(xp))
plt.show()


# p.scatter(f.dataFilter(highSpeedDataIndex,cleanCompression)[:, 3],
#           f.dataFilter(highSpeedDataIndex,cleanCompression)[:, 1],
#           np.linspace(2,12,100),
#           p1(np.linspace(2,12,100)),
#           title=filePath + ' IQR x2 dX 0.01/0.2')

# print(finalData) # only numbers, with positive velocity 4th [:,3] column

# Plotting
# plt.figure(figsize=(9, 6))
# plt.title(filePath)
# plt.xlabel('Velocity (in/sec)')
# plt.ylabel('Force (lbf)')
# plt.scatter(finalData[:,3],finalData[:,1],s=5,alpha=0.5)
# plt.show()
