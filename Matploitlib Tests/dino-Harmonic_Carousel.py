# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import itertools

# Create the tkinter root window
root = tk.Tk()
root.wm_title("Harmonic Carousel Visualization")

# Create a second tkinter window for the average direction visualization
root2 = tk.Tk()
root2.wm_title("Average Direction Visualization")

# Create a third tkinter window for the heatmap visualization
root3 = tk.Tk()
root3.wm_title("Heatmap Visualization")

# Create a figure and axes for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a second figure and axes for the average direction plot
fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})

# Create a third figure and axes for the heatmap plot
fig3, ax3 = plt.subplots()

# Create a meshgrid for the x, y, and z values
x, y, z = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))

# Initialize the u, v, and w vectors
u = np.sin(2 * x * np.pi / 20 * x)
v = np.cos(2 * y * np.pi / 25  * x)
w = np.sin(2 * z * np.pi / 30 * z)

# Flatten the colors array
colors = np.sqrt(u**2 + v**2 + w**2).flatten()

# Create the quiver plot with lines and arrows
Q = ax.quiver(x, y, z, u, v, w, colors, length=0.1, normalize=True)

# Create a line for the average direction plot
L, = ax2.plot([], [])

# Create an empty image for the heatmap plot
I = ax3.imshow(np.zeros((len(x), len(y))), cmap='hot', interpolation='nearest')

# Create a canvas for the plot and add it to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a second canvas for the average direction plot and add it to the second tkinter window
canvas2 = FigureCanvasTkAgg(fig2, master=root2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a third canvas for the heatmap plot and add it to the third tkinter window
canvas3 = FigureCanvasTkAgg(fig3, master=root3)
canvas3.draw()
canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def update(num):
    # Update the u, v, and w vectors for the new frame
    u = np.sin(2 * x * np.pi / 20 * (x + num))
    v = np.cos(2 * y * np.pi / 25  * (x + num))
    w = np.sin(2 * z * np.pi / 30 * (z + num))
    # Update and flatten the color array for the new frame
    colors = np.sqrt(u**2 + v**2 + w**2).flatten()
    # Update the u, v, and w components of the quiver plot
    Q.set_segments(np.array([x, y, z, u, v, w]).reshape(-1, 6))
    # Update the colors of the quiver plot
    Q.set_array(colors)

    # Calculate the average direction and magnitude
    avg_direction = np.arctan2(v.mean(), u.mean())
    avg_magnitude = np.sqrt(u.mean()**2 + v.mean()**2)

    # Update the line in the average direction plot
    L.set_data([avg_direction, avg_direction], [0, avg_magnitude])

    # Update the image in the heatmap plot
    I.set_data(np.sqrt(u**2 + v**2 + w**2))

    return Q, L, I,

ani = FuncAnimation(fig, update, frames=itertools.count(), interval=100, blit=True)

# Start the tkinter main loop
tk.mainloop()