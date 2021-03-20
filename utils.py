import matplotlib.pyplot as plt
import numpy as np


def new_ax():
    fig, ax = plt.subplots()
    
    fig.subplots_adjust(left=.05,right=.95,bottom=.1,top=.9)
    # fig.tight_layout()
    ax.set_facecolor('white')
    ax.axis('off')
    ax.axis('equal')
    ax.axis('auto')
    return fig, ax


def html5(anim, file, width=320, height=240):
    s = (anim.to_html5_video()
        .replace('width="640"', f'width="{str(width)}"', 1)
        .replace('height="480"', f'height="{height}"', 1)
        .replace('autoplay loop', '')
        )

    with open(file, "w") as f:
        print(s, file=f)


def line(p1, p2):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], "b:", linewidth=1)


def dist(p1, p2):
    return np.sum((p1 - p2)**2)**.5
