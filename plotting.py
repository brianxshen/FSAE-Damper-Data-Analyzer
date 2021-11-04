import matplotlib.pyplot as plt

def scatter(x,y,*,title='',xLabel='Velocity (in/sec)',yLabel='Force (lbf)',s=5,alpha=0.5):
  plt.figure()
  plt.scatter(x,y,s=s,alpha=alpha)
  plt.title(title)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.show()