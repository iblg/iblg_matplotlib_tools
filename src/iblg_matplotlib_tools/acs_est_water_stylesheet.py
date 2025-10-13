from matplotlib import cycler
from distutils.spawn import find_executable

fs = 12.0
est_water_style = {
    # 'text.usetex': True,
    # # 'font.family': 'Helvetica',
    # 'mathtext.fontset': 'custom',
    # 'mathtext.rm': 'Helvetica',
    # 'mathtext.it':'Helvetica:italic',
    # 'mathtext.bf':'Helvetica:bold',
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
    "font.size": fs,
    "font.family": ["Helvetica"],
    # "font.family": ["sans-serif"],
    "font.sans-serif": [
        "Helvetica",
        # "DejaVu Sans",
        # "Bitstream Vera Sans",
        # "Computer Modern Sans Serif",
        # "Lucida Grande",
        # "Verdana",
        # "Geneva",
        # "Lucid",
        # "Arial",
        # "Avant Garde",
        # "sans-serif",
        # "cm",
    ],
    ###################
    # axes properties #
    ###################
    "axes.titlesize": fs + 3,
    "axes.labelsize": fs + 3,
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
    "xtick.labelsize": fs,
    "xtick.minor.width": 2.0,
    "xtick.minor.size": 3.0,
    "xtick.major.width": 2.0,
    "xtick.major.size": 5.0,
    "xtick.major.pad": 5.0,
    ####################
    # ytick properties #
    ####################
    "ytick.right": True,
    "ytick.direction": "in",
    "ytick.color": "k",
    "ytick.labelsize": fs,
    "ytick.minor.width": 2.0,
    "ytick.minor.size": 3.0,
    "ytick.major.width": 2.0,
    "ytick.major.size": 5.0,
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
    "legend.fontsize": fs,
    "legend.fancybox": False,
    "legend.labelspacing": 0.1,
    "legend.title_fontsize": fs + 3,
    "legend.handlelength": 0.5,
    "legend.handletextpad": 0.1,
    "legend.borderpad": 0.1,
    "legend.columnspacing": 0.4,
}

if find_executable("latex"):

    tex = {
        ###################
        # text properties #
        ###################
        "text.usetex": True,
        # change helvet to other if preferred
        "text.latex.preamble": r"\usepackage[helvet]{sfmath}",
        # 'mathtext.fontset': 'stixsans'
        # 'mathtext.fontset': 'dejavusans'
        "mathtext.fontset": "custom",
        "mathtext.rm": "Helvetica",
    }

    est_water_style.update(tex)
