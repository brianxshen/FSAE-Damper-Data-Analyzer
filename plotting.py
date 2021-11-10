import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)


def scatter(x1,
            y1,
            x2,
            y2,
            *,
            title='',
            xLabel='Velocity (in/sec)',
            yLabel='Force (lbf)',
            s=5,
            alpha=0.5):
    plt.figure()
    # plt.scatter(x1, y1, s=s, alpha=alpha)
    plt.plot(x2, y2, s=s, alpha=alpha)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()


def finalPlot(xp1,yp1):
  fig, axs = plt.subplots(2, 2)
  axs[0, 0].plot(xp1, yp1)
  axs[0, 0].scatter(x, y, s=5, alpha=0.5)
  axs[0, 0].set_title('1-4-1-4')
  axs[0, 1].plot(x, y, 'tab:orange')
  axs[0, 1].scatter(x, y, s=5, alpha=0.5)
  axs[0, 1].set_title('3-4-3-4')
  axs[1, 0].plot(x, y, 'tab:green')
  axs[1, 0].scatter(x, y, s=5, alpha=0.5)
  axs[1, 0].set_title('6-4-6-4')
  axs[1, 1].plot(x, y, 'tab:red')
  axs[1, 1].scatter(x, y, s=5, alpha=0.5)
  axs[1, 1].set_title('Table')

  for ax in axs.flat:
      ax.set(xlabel='Velocity (in/sec)', ylabel='Load (lbf)')

  # Hide x labels and tick labels for top plots and y ticks for right plots.
  for ax in axs.flat:
      ax.label_outer()

  plt.show()
