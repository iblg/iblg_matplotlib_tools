from matplotlib import cycler
from distutils.spawn import find_executable
import matplotlib.pyplot as plt

# matplotlib.font_manager.findfont('/System/Library/Fonts/Avenir.ttc')
# matplotlib.font_manager.fontManager.addfont('/System/Library/Fonts/Avenir.ttc')
fs = 14
lw = 2

default_asp_ratio = 5.0 / 4
default_fig_width = 4.409
tick_length_maj = 5
tick_length_min = 3
ib_cell_style = {
    ####################
    # figure properties #
    ####################
    "figure.figsize": (
        default_fig_width,
        default_fig_width / default_asp_ratio,
    ),
    "figure.facecolor": "w",
    # 'figure.max_open_warning': False,
    "figure.subplot.left": 0.15,
    "figure.subplot.bottom": 0.15,
    "figure.subplot.right": 0.99,
    "figure.subplot.top": 0.99,
    ####################
    # lines properties #
    ####################
    "lines.linewidth": lw,
    "lines.markeredgewidth": 0.25,
    "lines.markersize": 6.00,
    "lines.solid_capstyle": "round",
    ###################
    # font properties #
    ###################
    "font.size": fs,
    "font.family": ["Avenir"],
    # 'font.sans-serif': ['Avenir',
    #                     'DejaVu Sans',
    #                     'Bitstream Vera Sans',
    #                     'Computer Modern Sans Serif',
    #                     'Lucida Grande',
    #                     'Verdana',
    #                     'Geneva',
    #                     'Lucid',
    #                     'Arial',
    #                     'Helvetica',
    #                     'Avant Garde',
    #                     'sans-serif',
    #                     'cm'],
    ###################
    # axes properties #
    ###################
    "axes.titlesize": fs,
    "axes.labelsize": fs,
    "axes.labelcolor": "k",
    "axes.linewidth": lw,
    "axes.edgecolor": "k",
    "axes.prop_cycle": cycler(
        "color",
        [
            "#0B3C5D",
            "#B82601",
            "#328CC1",
            "#a8b6c1",
            "#D9B310",
            "#984B43",
            "#76323F",
            "#626E60",
            "#AB987A",
            "#cf7508",
            "#b0b0b0",
        ],
    ),
    ####################
    # xtick properties #
    ####################
    "xtick.top": True,
    "xtick.direction": "in",
    "xtick.color": "k",
    "xtick.labelsize": fs,
    "xtick.minor.width": lw,
    "xtick.minor.size": tick_length_min,
    "xtick.major.width": lw,
    "xtick.major.size": tick_length_maj,
    "xtick.major.pad": 5.0,
    ####################
    # ytick properties #
    ####################
    "ytick.right": True,
    "ytick.direction": "in",
    "ytick.color": "k",
    "ytick.labelsize": fs,
    "ytick.minor.width": lw,
    "ytick.minor.size": tick_length_min,
    "ytick.major.width": lw,
    "ytick.major.size": tick_length_maj,
    "ytick.major.pad": 5.0,
    ###################
    # grid properties #
    ###################
    "grid.color": "#b2b2b2",
    "grid.linestyle": "--",
    "grid.linewidth": 1.0,
    ####################
    # legend properties #
    ####################
    "legend.fontsize": fs - 2,
    "legend.fancybox": False,
    "legend.labelspacing": 0.1,
    "legend.title_fontsize": fs,
    "legend.handlelength": 1,
    "legend.handletextpad": 0.1,
    "legend.borderpad": 0.1,
    # "legend.labelspacing": 0,
    "legend.columnspacing": 0.4,
    # 'mathtext.fontset':'Avenir',
    # 'mathtext.it':'Avenir:italic'
}

if find_executable("latex"):

    tex = {
        ###################
        # text properties #
        ###################
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage[cm]{sfmath}",
        # 'text.latex.preamble': r'\usepackage{Avenir}',
        "mathtext.fontset": "stixsans",
    }

    ib_cell_style.update(tex)


def use_cell_style():
    plt.style.use("default")

    for k, v in ib_cell_style.items():
        if "lines." in k:
            plt.rcParams.update({k: v})
        if "xtick." in k:
            plt.rcParams.update({k: v})
        if "ytick." in k:
            plt.rcParams.update({k: v})
        if "axes." in k:
            plt.rcParams.update({k: v})
        if "grid." in k:
            plt.rcParams.update({k: v})
        if "figure." in k:
            plt.rcParams.update({k: v})
        if "legend." in k:
            plt.rcParams.update({k: v})
        if "font." in k:
            plt.rcParams.update({k: v})
        # if 'mathtext.' in k:
        #     plt.rcParams.update({k:v})
