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

# Create a figure and axes for the plot
fig, ax = plt.subplots()

# Create a second figure and axes for the average direction plot
fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})

# Create a meshgrid for the x and y values
x, y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))

# Initialize the u and v vectors
u = np.sin(2 * x * np.pi / 20 * x)
v = np.cos(2 * y * np.pi / 25  * x)

# Flatten the colors array
colors = np.sqrt(u**2 + v**2).flatten()

# Create the quiver plot with lines and arrows
Q = ax.quiver(x, y, u, v, colors, pivot='mid', units='inches')

# Create a line for the average direction plot
L, = ax2.plot([], [])

# Create a canvas for the plot and add it to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a second canvas for the average direction plot and add it to the second tkinter window
canvas2 = FigureCanvasTkAgg(fig2, master=root2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def update(num):
    # Update the u and v vectors for the new frame
    u = np.sin(2 * x * np.pi / 20 * (x + num))
    v = np.cos(2 * y * np.pi / 25  * (x + num))
    # Update and flatten the color array for the new frame
    colors = np.sqrt(u**2 + v**2).flatten()
    # Update the u and v components of the quiver plot
    Q.set_UVC(u, v)
    # Update the colors of the quiver plot
    Q.set_array(colors)

    # Calculate the average direction and magnitude
    avg_direction = np.arctan2(v.mean(), u.mean())
    avg_magnitude = np.sqrt(u.mean()**2 + v.mean()**2)

    # Update the line in the average direction plot
    L.set_data([avg_direction, avg_direction], [0, avg_magnitude])

    return Q, L,

ani = FuncAnimation(fig, update, frames=itertools.count(), interval=100, blit=True)

# Start the tkinter main loop
tk.mainloop()