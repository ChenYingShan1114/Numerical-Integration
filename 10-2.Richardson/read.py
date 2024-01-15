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

path = 'error1out.txt'
list = []
fo = open(path, 'r')
for line in fo:
    list.append(float(line))
fo.close()
error1 = np.array(list)

path = 'error2out.txt'
list = []
fo = open(path, 'r')
for line in fo:
    list.append(float(line))
fo.close()
error2 = np.array(list)

fig1 = plt.figure(figsize=(16,8))
format(fig1)
ax = fig1.add_subplot(1, 1, 1)
#ax_format(ax, 5, 1, 0.5, 0.1)
ax.plot(error1, '-o', label = r"$\left| f'(x)-D_{i,1} \right|$")
ax.plot(error2, '-o', label = r"$\left| f'(x)-D_{i,i} \right|$")
ax.set_xlabel(r'$i$')
ax.set_ylabel('error')
ax.set_title("Richardson extrapolation for $f(x)=e^x$ at $x=10$")
ax.legend()
ax.grid()
plt.savefig('Richardson.png')
plt.show()
