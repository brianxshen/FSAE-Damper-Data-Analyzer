import matplotlib.pyplot as plt


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
