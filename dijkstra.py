import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 28,
})

G = {
    "A": [("B", 2), ("C", 8)],
    "B": [("C", 1), ("D", 6)],
    "C": [("D", 4), ("E", 1)],
    "D": [],
    "E": [("D", 2)],
}
pos = {
    "A": (0, 0),
    "B": (0, 2),
    "C": (2, 0),
    "D": (2, 2),
    "E": (3, 1),
}

fig, ax = plt.subplots()
ax.set_facecolor('white')
ax.axis('off')

dist = { v: float("inf") for v in G }
vus = { v: False for v in G }
dist["A"] = 0

def dist_to_str(d):
    if d == float("inf"):
        return "$\infty$"
    return str(d)

P, T, A = {}, {}, {}

for u in G:
    for v, w in G[u]:
        A[(u, v)] = ax.arrow(pos[u][0], pos[u][1], pos[v][0] - pos[u][0], pos[v][1] - pos[u][1],
                            length_includes_head=True,
                            head_width=.09,
                            width=.012,
                            color="black")
        ax.text((pos[u][0] + pos[v][0])/2, (pos[u][1] + pos[v][1])/2 + .05, str(w)) 

for v in pos:
    x, y = pos[v]
    P[v] = ax.scatter(x, y, s=150, color="black")
    if y < .5:
        y -= .3
    else:
        y += .1
    T[v] = ax.text(x - .05, y, dist_to_str(dist[v]))

def dijkstra():
    yield
    while True:
        v_min = -1
        for v in dist:
            if not vus[v] and (v_min == -1 or dist[v] < dist[v_min]):
                v_min = v
        if v_min == -1:
            yield
            continue
        vus[v_min] = True
        T[v_min].set_color("red")
        P[v_min].set_color("red")
        yield
        for v, w in G[v_min]:
            A[(v_min, v)].set_color("red")
            yield
            modif = False
            if dist[v_min] + w < dist[v]:
                dist[v] = dist[v_min] + w
                T[v].set_text(dist_to_str(dist[v]))
                yield
                modif = True
            if modif:
                A[(v_min, v)].set_color("green")
            else:
                A[(v_min, v)].set_color("black")
        T[v_min].set_color("green")
        P[v_min].set_color("green")
        yield

dij = dijkstra()
def update(i):
    next(dij)

anim = FuncAnimation(fig, update, frames=25, interval=1200, blit=False)
anim.save('dijkstra.gif', dpi=200)
# HTML(anim.to_html5_video())
