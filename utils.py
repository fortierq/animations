import matplotlib.pyplot as plt


def new_ax():
    fig, ax = plt.subplots()
    
    fig.subplots_adjust(left=.05,right=.95,bottom=.1,top=.9)
    # fig.tight_layout()
    ax.set_facecolor('white')
    ax.axis('off')
    ax.axis('equal')
    ax.axis('auto')
    
    return fig, ax


def html5(anim, file, width=160, height=120):
    s = anim.to_html5_video().replace('width="640"', f'width="{str(width)}"', 1).replace('height="480"', f'height="{height}"', 1)
    with open(file, "w") as f:
        print(s, file=f)
