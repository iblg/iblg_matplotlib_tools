import numpy as np


def ian_ticks(ax, kind, ticks):
    start = ticks[0]
    end = ticks[1]
    n = ticks[2]
    nminor = 2 * n - 1
    major = np.linspace(start, end, n)
    minor = np.linspace(start, end, nminor)

    if kind == "x":
        ax.set_xticks(major, minor=False)
        ax.set_xticks(minor, minor=True)
    elif kind == "y":
        ax.set_yticks(major, minor=False)
        ax.set_yticks(minor, minor=True)
    elif kind == "both":
        ax.set_xticks(major, minor=False)
        ax.set_xticks(minor, minor=True)
        ax.set_yticks(major, minor=False)
        ax.set_yticks(minor, minor=True)
    return ax
