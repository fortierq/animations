from utils import html5, dist, line
import matplotlib.pyplot as plt
from celluloid import Camera  # pour l'animation
from IPython.display import HTML  # pour la vidéo
import numpy as np


def kmeans(k, X, n):
    '''
    k: nombre de classes
    X: données
    n: nombre d'itérations
    '''
    Y = np.zeros((len(X)), dtype=np.int64)  # classes
    fig = plt.figure()
    fig.tight_layout()
    plt.axis('off')
    camera = Camera(fig)
    rng = np.random.default_rng()
    centres = rng.choice(
        X, size=k, replace=False)  # centres choisis initialement parmi les données (d'autres choix sont possibles)
    plt.scatter(X[:, 0], X[:, 1], c="blue")
    camera.snap()
    plt.scatter(X[:, 0], X[:, 1], c="blue")
    plt.scatter(centres[:, 0], centres[:, 1], s=200, c="orange")
    camera.snap()
    for i in range(n):
        plt.scatter(X[:, 0], X[:, 1], c="blue")
        plt.scatter(centres[:, 0], centres[:, 1], s=200, c="orange")
        for j in range(len(X)):
            Y[j] = np.argmin([dist(c, X[j]) for c in centres])  # X[j] est assigné au centre le plus proche
            line(centres[Y[j]], X[j])
        camera.snap()
        centres = np.array([X[Y == i].mean(0) for i in range(k)])
    return camera.animate(interval=2000, repeat=True, repeat_delay=500)


X1 = np.array([2, 2]) + np.random.randn(10, 2)
X2 = np.array([-2, -2]) + np.random.randn(10, 2)
X3 = np.array([-2, 2]) + np.random.randn(10, 2)
X4 = np.array([2, -2]) + np.random.randn(10, 2)

anim = kmeans(4, np.concatenate((X1, X2, X3, X4)), 5)
html5(anim, "html/kmeans.html")
