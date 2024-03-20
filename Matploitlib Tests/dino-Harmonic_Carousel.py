# Import necessary libraries
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting
from matplotlib.animation import FuncAnimation  # For creating animations
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # For embedding plots in tkinter windows
import tkinter as tk  # For creating GUI
import itertools



# Create the tkinter root window
root = tk.Tk()
root.wm_title("Harmonic Carousel Visualization")  # Set the title of the window

# Create a figure and axes for the plot
fig, ax = plt.subplots()

# Create a meshgrid for the x and y values
# np.arange creates a sequence of numbers from 0 to 2*pi with a step of 0.2
x, y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))

# Initialize the u and v vectors
# These vectors are based on the sin and cos functions, creating a harmonic motion
u = np.sin(2 * x * np.pi / 20 * x)
v = np.cos(2 * y * np.pi / 25  * x)

# Flatten the colors array
colors = np.sqrt(u**2 + v**2).flatten()

# Create the quiver plot with lines and arrows
Q = ax.quiver(x, y, u, v, colors, pivot='mid', units='inches')

# Create a canvas for the plot and add it to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)  # Create the canvas with the figure
canvas.draw()  # Draw the plot onto the canvas
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)  # Add the canvas to the tkinter window

# Define an update function for the animation
# This function is called for each frame of the animation
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
    return Q,  # Return the updated quiver plot

# Create the animation
# 'fig' is the figure to animate
# 'update' is the function to call for each frame
# 'frames' is the number of frames in the animation
# 'interval' is the time between frames in milliseconds
# 'blit' is set to True to only redraw the parts of the plot that have changed
ani = FuncAnimation(fig, update, frames=itertools.count(), interval=100, blit=True)

# Start the tkinter main loop
# This starts the GUI and makes the window appear on the screen
tk.mainloop()