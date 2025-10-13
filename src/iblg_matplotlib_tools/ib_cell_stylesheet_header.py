import matplotlib.pyplot as plt
from iblg_matplotlib_stylesheet.ib_cell_stylesheet import ib_cell_style

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
