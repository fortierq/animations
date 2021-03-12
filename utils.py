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
