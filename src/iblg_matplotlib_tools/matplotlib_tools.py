import numpy as np


def convert_ticklabels_to_strings(ax, which="both"):
    if which == "both":
        do_x = True
        do_y = True
    elif which == "x":
        do_x = True
        do_y = False
    elif which == "y":
        do_x = False
        do_y = True
    else:
        print(
            "Invalid which parameter passed to convert_ticklabels_to_strings"
        )
        return

    if do_x:
        x_ticks = ax.get_xticks()
        x_ticklabels = process_ticks(x_ticks)

    if do_y:
        y_ticks = ax.get_yticks()
        y_ticklabels = process_ticks(y_ticks)

    if do_x and not do_y:
        return x_ticklabels
    if do_y and not do_x:
        return y_ticklabels
    if do_x and do_y:
        return x_ticklabels, y_ticklabels
    else:
        return


def process_ticks(ticks):
    ticklabels = [str(i) for i in ticks]
    ticklabels = [i.replace("-", "–") for i in ticklabels]
    return ticklabels


def ian_ticks(ax, kind, ticks):
    """
    ax: matplotlib.Axes object
    kind: str
        'x', 'y', or 'both'
    ticks: tuple
        first should be tick minimum
        second should be tick maximum
        third should be number of ticks
    """
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


# Set size of axes object (not figure)
def set_axis_size(ax, w, h):
    """Sets size of axes, not total figure.

    ax: matplotlib.pyplot.Axes object
    w: width, inches
    h: height in inches
    """

    left = ax.figure.subplotpars.left
    right = ax.figure.subplotpars.right
    top = ax.figure.subplotpars.top
    bottom = ax.figure.subplotpars.bottom
    figw = float(w) / (right - left)
    figh = float(h) / (top - bottom)
    ax.figure.set_size_inches(figw, figh)

    return ax
