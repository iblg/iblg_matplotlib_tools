import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def generate_figax():
    fig = plt.figure()
    gs = GridSpec(1, 1, left=0.25, right=0.97, top=0.97, bottom=0.15)
    ax = fig.add_subplot(gs[0, 0])
    return fig, ax, gs
