import numpy as np
from matplotlib.colors import Normalize
from matplotlib import colormaps as cmaps


def get_color_list_from_array_vals(
    x: np.array, colormap="viridis", norm=None, vmin=None, vmax=None
):
    """

    :param x: The array of values that you wish to use to generate the colors
    :param colormap: The name of the matplotlib colormap that you wish to use
    :param norm: default None. Option to use a user-defined norm.
    If None, defaults to  linear norm.
    :param vmin: default None.
    If None, uses minimum of x.
    :param vmax: default None.
    If None, uses maximum of x.
    :return:
    """
    if norm is None:
        if vmin is None:
            vmin = x.min()
        else:
            pass

        if vmax is None:
            vmax = x.max()
        else:
            pass

        norm = Normalize(vmin=vmin, vmax=vmax)
    else:
        pass
    colormap = cmaps[colormap]
    color_list = [colormap(norm(i)) for i in x]
    return color_list
