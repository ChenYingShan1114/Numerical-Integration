import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl
def format(fig):
    mpl.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['xtick.labelsize'] = 19
    plt.rcParams['ytick.labelsize'] = 19
    plt.rcParams['font.size'] = 19
    plt.rcParams['figure.figsize'] = [5.6*6, 4*3]
    plt.rcParams['axes.titlesize'] = 18
    plt.rcParams['axes.labelsize'] = 18
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markersize'] = 6
    plt.rcParams['legend.fontsize'] = 15
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['axes.linewidth'] = 1.5
    # plt.style.use('dark_background')


def ax_format(ax, xmaj, xmin, ymaj, ymin):
    ax.xaxis.set_tick_params(which='major', size=5, width=1,
                            direction='in', top='on')
    ax.xaxis.set_tick_params(which='minor', size=3, width=1,
                            direction='in', top='on')
    ax.yaxis.set_tick_params(which='major', size=5, width=1,
                            direction='in', right='on')
    ax.yaxis.set_tick_params(which='minor', size=3, width=1,
                            direction='in', right='on')
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(xmaj))
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(xmin))
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(ymaj))
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(ymin))



path = 'Xout.txt'
list = []
fo = open(path, 'r')
for line in fo:
    list.append(float(line))
fo.close()
x = np.array(list)

path = 'Yout.txt'
data_list = []
list = []
fo = open(path, 'r')
for line in fo:
    s = line.split(',')
    for i in range(len(s)):
        data_list.append(float(s[i]))
    list.append(data_list)
    data_list = []
fo.close()
Y = np.array(list)

print(x.shape, Y.shape)

fig1 = plt.figure(figsize=(16,8))
format(fig1)
ax = fig1.add_subplot(1, 1, 1)
ax_format(ax, 5, 1, 0.5, 0.1)
for i in range(5):
    ax.plot(x, Y[i, :], label = r'$Y_{%i}(x)$' % i)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$Y_m(x)$')
ax.set_title("second solution of Bessel's equation")
ax.set_xlim(0, 50)
ax.set_ylim(-3.2, 0.7)
ax.legend()
ax.grid()
plt.savefig('Bessel.png')
plt.show()
