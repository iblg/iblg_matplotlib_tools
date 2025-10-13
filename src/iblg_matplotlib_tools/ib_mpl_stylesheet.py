from matplotlib import cycler
from distutils.spawn import find_executable


ib_mpl_style = {
    ####################
    # lines properties #
    ####################
    "lines.linewidth": 2.50,
    "lines.markeredgewidth": 0.25,
    "lines.markersize": 6.00,
    "lines.solid_capstyle": "round",
    ###################
    # font properties #
    ###################
    "font.size": 80.0,
    "font.family": ["sans-serif"],
    "font.sans-serif": [
        "DejaVu Sans",
        "Bitstream Vera Sans",
        "Computer Modern Sans Serif",
        "Lucida Grande",
        "Verdana",
        "Geneva",
        "Lucid",
        "Arial",
        "Helvetica",
        "Avant Garde",
        "sans-serif",
        "cm",
    ],
    ###################
    # axes properties #
    ###################
    "axes.titlesize": 20.0,
    # "font.size": 20.0,
    "axes.labelsize": 20.0,
    "axes.labelcolor": "k",
    "axes.linewidth": 2.0,
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
    "xtick.labelsize": 20.0,
    "xtick.minor.width": 2.5,
    "xtick.minor.size": 4.0,
    "xtick.major.width": 2.5,
    "xtick.major.size": 7.0,
    "xtick.major.pad": 5.0,
    ####################
    # ytick properties #
    ####################
    "ytick.right": True,
    "ytick.direction": "in",
    "ytick.color": "k",
    "ytick.labelsize": 20.0,
    "ytick.minor.width": 2.5,
    "ytick.minor.size": 4.0,
    "ytick.major.width": 2.5,
    "ytick.major.size": 7.0,
    "ytick.major.pad": 5.0,
    ###################
    # grid properties #
    ###################
    "grid.color": "#b2b2b2",
    "grid.linestyle": "--",
    "grid.linewidth": 1.0,
    #####################
    # figure properties #
    #####################
    "figure.facecolor": "w",
    ####################
    # legend properties #
    ####################
    "legend.fontsize": 22.0,
    "legend.fancybox": False,
    "legend.labelspacing": 0.1,
    "legend.title_fontsize": 22.0,
    "legend.handlelength": 0.5,
    "legend.handletextpad": 0.1,
    "legend.borderpad": 0.1,
    # "legend.labelspacing": 0,
    "legend.columnspacing": 0.4,
}

if find_executable("latex"):

    tex = {
        ###################
        # text properties #
        ###################
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage[cm]{sfmath}",
        "mathtext.fontset": "stixsans",
    }

    ib_mpl_style.update(tex)
