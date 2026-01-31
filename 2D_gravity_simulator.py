import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 6.67430e-11  # gravitational constant

class Body:
    def __init__(self, name, mass, pos, vel, radius, color):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.radius = radius
        self.color = color
        self.trail_x = []
        self.trail_y = []

    def update(self, bodies, dt):
        force = np.zeros(2)
        for b in bodies:
            if b is self: 
                continue
            r = b.pos - self.pos
            dist = np.linalg.norm(r)
            if dist == 0:
                continue
            force += G * self.mass * b.mass * r / dist**3
        
        acc = force / self.mass
        self.vel += acc * dt
        self.pos += self.vel * dt
        
        self.trail_x.append(self.pos[0])
        self.trail_y.append(self.pos[1])

# ----------- Define System --------------
sun = Body("Sun", 1.989e30, [0,0], [0,0], 30, 'yellow')
earth = Body("Earth", 5.972e24, [1.5e11,0], [0, 29780], 8, 'cyan')
mars = Body("Mars", 6.39e23, [2.2e11,0], [0, 24000], 6, 'red')
venus = Body("Venus", 4.87e24, [1.1e11,0], [0, 35000], 7, 'orange')

bodies = [sun, earth, mars, venus]

# ---------- Plot Setup ----------
fig, ax = plt.subplots(figsize=(8,8))
ax.set_facecolor("black")
ax.set_xlim(-3e11, 3e11)
ax.set_ylim(-3e11, 3e11)
ax.set_aspect("equal")
ax.set_title("Realistic 2D Solar System Simulation", color="white")
ax.tick_params(colors="white")

# Add star background
for _ in range(300):
    ax.plot(np.random.uniform(-3e11, 3e11),
            np.random.uniform(-3e11, 3e11),
            marker='.', color='white', markersize=np.random.uniform(0.5,2))

# Create planet markers
points = []
trails = []
for b in bodies:
    p, = ax.plot([], [], marker='o', color=b.color, markersize=b.radius)
    t, = ax.plot([], [], color=b.color, linewidth=1)
    points.append(p)
    trails.append(t)

# ------------ Animation update -----------
def update(frame):
    dt = 60 * 60 * 8  # 8 hours per frame

    for b in bodies:
        b.update(bodies, dt)

    for i, b in enumerate(bodies):
        points[i].set_data([b.pos[0]], [b.pos[1]])   # FIXED
        trails[i].set_data(b.trail_x, b.trail_y)

    return points + trails

ani = FuncAnimation(fig, update, frames=20000, interval=20, blit=True)
plt.show()
