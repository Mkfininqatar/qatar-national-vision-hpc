import numpy as np
import matplotlib.pyplot as plt

# Apply dark mode style
plt.style.use('dark_background')

# Initialize 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Configure holographic background & deep space color
ax.set_facecolor('#05050a')
ax.w_xaxis.set_pane_color((0.0, 0.05, 0.1, 1.0))
ax.w_yaxis.set_pane_color((0.0, 0.05, 0.1, 1.0))
ax.w_zaxis.set_pane_color((0.0, 0.05, 0.1, 1.0))

# Generate spherical wireframe mesh (Earth topology)
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 30)
R = 1.0
x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot holographic cyan wireframe grid
ax.plot_wireframe(x, y, z, color='cyan', alpha=0.15, linewidth=0.6)

# Geodetic coordinates (Latitude, Longitude)
locations = {
    "Doha": (25.2854, 51.5310),
    "Giza": (29.9773, 31.1325),
    "Jerusalem": (31.7683, 35.2137)
}

def latlon_to_cartesian(lat, lon, R=1.0):
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    x = R * np.cos(lat_rad) * np.cos(lon_rad)
    y = R * np.cos(lat_rad) * np.sin(lon_rad)
    z = R * np.sin(lat_rad)
    return np.array([x, y, z])

coords = {name: latlon_to_cartesian(lat, lon) for name, (lat, lon) in locations.items()}

# Plot nodes on the sphere
for name, pt in coords.items():
    ax.scatter(pt[0], pt[1], pt[2], color='cyan', s=120, depthshade=False, edgecolor='white', linewidth=0.8)
    ax.text(pt[0]*1.12, pt[1]*1.12, pt[2]*1.12, f"  {name}", color='cyan', fontsize=11, fontweight='bold')

# Spherical linear interpolation (SLERP) for Great Circle Arcs connecting locations
def plot_great_circle(ax, p1, p2, color='cyan', lw=2, alpha=0.9):
    dot = np.dot(p1, p2)
    dot = np.clip(dot, -1.0, 1.0)
    theta = np.arccos(dot)
    if theta < 1e-6:
        return
    t = np.linspace(0, 1, 60)
    sin_theta = np.sin(theta)
    arc = (np.sin((1 - t) * theta)[:, None] * p1 + np.sin(t * theta)[:, None] * p2) / sin_theta
    ax.plot(arc[:, 0], arc[:, 1], arc[:, 2], color=color, linewidth=lw, alpha=alpha)

# Draw vector links from Doha to Giza and Jerusalem
plot_great_circle(ax, coords["Doha"], coords["Giza"], color='cyan', lw=2.5, alpha=0.9)
plot_great_circle(ax, coords["Doha"], coords["Jerusalem"], color='deepskyblue', lw=2.0, alpha=0.8)

# Styling and view settings
ax.set_title("TMX-1 Master Matrix: Geodetic Holographic Grid\n(Doha -> Giza & Jerusalem)", color='cyan', fontsize=14, pad=20)
ax.view_init(elev=30, azim=45)
ax.axis('off')

# Save visualization
plt.tight_layout()
plt.savefig('holographic_graph.png', dpi=300, facecolor='#05050a', edgecolor='none')
print("Successfully generated and saved holographic_graph.png!")
