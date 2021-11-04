import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sys

# To Do
# Logging

filePath = 'TR22-FC0739/TR22-FC0739-1-4-1-4.dat'

forbiddenWords = ['Data Acquisition','Stroke','Load','Time','in','lbf','Sec']
deleteIndex = []

rawdata = np.loadtxt(filePath, dtype='str', delimiter='\t', usecols=(0,1,2), skiprows=5)

for i in range(0,len(rawdata[:,0])): # rows
  if rawdata[i,0] in forbiddenWords:
    # print('Row ' + str(i))
    # print(rawdata[i,0])
    deleteIndex.append(i)

data = np.delete(rawdata,deleteIndex,0).astype(float) # removes entire rows, converts to float
# print(str(type(data[10,0])))

velocity = np.array([0]) # blank array with 0 for 1st row

for i in range(1,len(data[:,0])): # calculate instantaneous velocity
  velocity = np.append(velocity,(data[i,0]-data[i-1,0])/(data[i,2]-data[i-1,2]))

velocity = velocity.reshape(velocity.shape[0],-1) # 1D to 2D array
velocity = np.absolute(velocity) # all positive velocity

finalData = np.append(data, velocity, axis=1) # add velocity column [:,3]

compressionDataIndex = np.array([])
reboundDataIndex = np.array([])

for i in range(0,len(finalData[:,0])):
  if finalData[i,1] > 0:
    compressionDataIndex = np.append(compressionDataIndex,i).astype(int)
  elif finalData[i,1] < 0:
    reboundDataIndex = np.append(reboundDataIndex,i).astype(int)
  else:
    print('fuck it, no value')

dx = 1
dmax = 12

def outlierObliterator(dataIndex,dataArray,*,dX=dx,dMax=dmax): 
  indexedData = np.empty((0, 4), float)
  tempData = np.empty((0, 4), float) # used when calculating z scores
  cleanData = np.empty((0, 4), float) # output

  for i in dataIndex:
    # print('Indexing: ' + str(i))
    # print(dataArray[i])
    indexedData = np.vstack((indexedData,dataArray[i]))
  
  # print(indexedData)

  # sys.exit()

  for i in np.arange(0,dMax,dX):
    print('Sexy Sliver of the Minute: ' + str(i))
    for j in range(0,len(indexedData[:,3])):
      if indexedData[j,3] <= (i+dX) and indexedData[j,3] > (i):
        tempData = np.vstack((tempData,indexedData[j]))

    #print('Judging')
    z = np.abs(stats.zscore(tempData[:,1]))
    #print(z)

    for i in range(0,len(z)):
      # print('Discrimination: ' + str(i))
      if z[i] < 3:
        cleanData = np.vstack((cleanData,tempData[i]))
      else:
        print("dumbass data point wasn't in fuckin range: " + str(tempData[i]))

  return cleanData

cleanCompression = outlierObliterator(compressionDataIndex,finalData)

plt.figure()
plt.xlabel('Velocity (in/sec)')
plt.ylabel('Force (lbf)')
plt.scatter(cleanCompression[:,3],cleanCompression[:,1],s=5,alpha=0.5)
plt.show()

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