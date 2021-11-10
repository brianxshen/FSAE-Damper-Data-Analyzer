import numpy as np
from scipy import stats


def dataParser(path,
               *,
               filterList=[
                   'Data Acquisition', 'Stroke', 'Load', 'Time', 'in', 'lbf',
                   'Sec'
               ],
               skipRows=5):
    rawdata = np.loadtxt(path,
                         dtype='str',
                         delimiter='\t',
                         usecols=(0, 1, 2),
                         skiprows=skipRows)
    deleteIndex = []

    for i in range(0, len(rawdata[:, 0])):  # rows
        if rawdata[i, 0] in filterList:
            # print('Row ' + str(i))
            # print(rawdata[i,0])
            deleteIndex.append(i)

    data = np.delete(rawdata, deleteIndex,
                     0).astype(float)  # removes entire rows, converts to float
    # print(str(type(data[10,0])))

    velocity = np.array([0])  # blank array with 0 for 1st row

    for i in range(1, len(data[:, 0])):  # calculate instantaneous velocity
        velocity = np.append(velocity, (data[i, 0] - data[i - 1, 0]) /
                             (data[i, 2] - data[i - 1, 2]))

    velocity = velocity.reshape(velocity.shape[0], -1)  # 1D to 2D array
    velocity = np.absolute(velocity)  # all positive velocity

    return np.append(data, velocity, axis=1)  # add velocity column [:,3]


def dataSeparator(dataArray,*,lowerBound=0,upperBound=0,dataColumn=1):
  lowerDataIndex = np.array([])
  upperDataIndex = np.array([])
  for i in range(0, len(dataArray[:, dataColumn])):
      if dataArray[i, dataColumn] > upperBound:
          upperDataIndex = np.append(upperDataIndex, i).astype(int)
      elif dataArray[i, dataColumn] <= lowerBound:
          lowerDataIndex = np.append(lowerDataIndex, i).astype(int)
  return lowerDataIndex,upperDataIndex


def dataFilter(dataIndex, dataArray):
  indexedData = np.empty((0, 4), float)

  for i in dataIndex:
        # print('Indexing: ' + str(i))
        # print(dataArray[i])
        indexedData = np.vstack((indexedData, dataArray[i]))

  return indexedData


def outlierObliteratorZScore(dataArray, *, dX, dMax, SD, dataIndex=[]):
    tempData = np.empty((0, 4), float)  # used when calculating z scores
    cleanData = np.empty((0, 4), float)  # output

    if len(dataIndex) != 0:
      dataArray = dataFilter(dataIndex,dataArray)

    # print(indexedData)

    # sys.exit()

    for i in np.arange(0, dMax, dX):
        tempData = np.empty((0, 4), float)
        # print('Sexy Sliver of the Minute: ' + str(i))
        for j in range(0, len(dataArray[:, 3])):
            if dataArray[j, 3] <= (i + dX) and dataArray[j, 3] > (i):
                tempData = np.vstack((tempData, dataArray[j]))

        #print('Judging')
        z = np.abs(stats.zscore(tempData[:, 1]))
        #print(z)

        for i in range(0, len(z)):
            # print('Discrimination: ' + str(i))
            if z[i] < SD:
                cleanData = np.vstack((cleanData, tempData[i]))
            # else:
            #   print("dumbass data point wasn't in fuckin range: " + str(tempData[i]))

    return cleanData


def outlierObliteratorIQR(
                          dataArray,
                          *,
                          dX=1,
                          dMax=12,
                          iqrRange=(25, 75), dataIndex=[]):
    cleanData = np.empty((0, 4), float)  # output

    if len(dataIndex) != 0:
      dataArray = dataFilter(dataIndex,dataArray)

    # print(indexedData)

    for i in np.arange(0, dMax, dX):
        print('Sexy Sliver of the Minute: ' + str(i))
        tempData = np.empty((0, 4), float)
        for j in range(0, len(dataArray[:, 3])):
            if dataArray[j, 3] <= (i + dX) and dataArray[j, 3] > (i):
                tempData = np.vstack((tempData, dataArray[j]))

        #print('Judging')
        iqr = stats.iqr(tempData[:, 1], rng=iqrRange)
        median = np.median(tempData[:, 1])
        # print('IQR: ' + str(iqr) + ' | Median: ' + str(median))

        for i in range(0, len(tempData[:, 1])):
            # print('Discrimination: ' + str(i))
            if tempData[i, 1] >= (median -
                                  (iqr / 2)) and tempData[i, 1] <= (median +
                                                                    (iqr / 2)):
                cleanData = np.vstack((cleanData, tempData[i]))
            # else:
            #   print("dumbass data point wasn't in fuckin range: " + str(tempData[i]))

    return cleanData


def outlierObliteratorDBSCAN(
                          dataArray,
                          *,
                          dX=1,
                          dMax=12,
                          iqrRange=(25, 75),dataIndex=[]):
    cleanData = np.empty((0, 4), float)  # output

    if len(dataIndex) != 0:
      dataArray = dataFilter(dataIndex,dataArray)

    # print(indexedData)

    for i in np.arange(0, dMax, dX):
        # print('Sexy Sliver of the Minute: ' + str(i))
        tempData = np.empty((0, 4), float)
        for j in range(0, len(dataArray[:, 3])):
            if dataArray[j, 3] <= (i + dX) and dataArray[j, 3] > (i):
                tempData = np.vstack((tempData, dataArray[j]))

        #print('Judging')
        iqr = stats.iqr(tempData[:, 1], rng=iqrRange)
        median = np.median(tempData[:, 1])
        # print('IQR: ' + str(iqr) + ' | Median: ' + str(median))

        for i in range(0, len(tempData[:, 1])):
            # print('Discrimination: ' + str(i))
            if tempData[i, 1] >= (median -
                                  (iqr / 2)) and tempData[i, 1] <= (median +
                                                                    (iqr / 2)):
                cleanData = np.vstack((cleanData, tempData[i]))
            # else:
            #   print("dumbass data point wasn't in fuckin range: " + str(tempData[i]))

    return cleanData


def outlierObliteratorMedian(
                          dataArray,
                          dX,
                          dMax,*, dataIndex=[]):
    cleanData = np.empty((0,4),float)  # output

    if len(dataIndex) != 0:
      dataArray = dataFilter(dataIndex,dataArray)

    # print(indexedData)

    for i in np.arange(0, dMax, dX):
        # print('Sexy Sliver of the Minute: ' + str(i))
        tempData = np.empty((0,4),float)
        for j in range(0, len(dataArray[:, 3])):
            if dataArray[j, 3] <= (i + dX) and dataArray[j, 3] > (i):
                tempData = np.vstack((tempData, dataArray[j]))

        if len(tempData) > 0:
          cleanData = np.vstack((cleanData, np.array([0,np.median(tempData[:, 1]),0,i+(dX/2)])))

    return cleanData
