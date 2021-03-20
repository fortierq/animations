import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from utils import html5, new_ax
from graph import G, pos

plt.style.use(".mplstyle")

fig, ax = new_ax()

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
                            head_width=.07,
                            color="black")
        ax.text((pos[u][0] + pos[v][0])/2, (pos[u][1] + pos[v][1])/2 + .05, str(w)) 

for v in pos:
    x, y = pos[v]
    P[v] = ax.scatter(x, y, color="black")
    if y < .2:
        y -= .3
    else:
        y += .1
    T[v] = ax.text(x - .05, y, dist_to_str(dist[v]))

def set_vertex_color(v, color):
    T[v].set_color(color)
    P[v].set_color(color)

def set_arc_color(u, v, color):
    A[(u, v)].set_color(color)
    T[v].set_color(color)

def dijkstra():
    yield
    while True:
        v_min = -1
        for v in dist:
            if not vus[v] and (v_min == -1 or dist[v] < dist[v_min]):
                v_min = v
        if v_min == -1:
            return None
        vus[v_min] = True
        set_vertex_color(v_min, "red")
        yield
        for v, w in G[v_min]:
            set_arc_color(v_min, v, "red")
            yield
            if dist[v_min] + w < dist[v]:
                dist[v] = dist[v_min] + w
                T[v].set_text(dist_to_str(dist[v]))
                set_vertex_color(v, "red")
                yield
                set_vertex_color(v, "black")
            set_arc_color(v_min, v, "black")
        set_vertex_color(v_min, "green")
        yield

anim = FuncAnimation(fig, lambda _: None, frames=dijkstra, interval=1200, blit=False)
# anim.save('dijkstra.gif', dpi=200)
html5(anim, "dijkstra.html")
