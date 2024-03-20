import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Create the tkinter root window
root = tk.Tk()
root.wm_title("Harmonic Carousel Visualization")

# Create a figure and axes for the plot
fig, ax = plt.subplots()

# Create a meshgrid for the x and y values
x, y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))

# Initialize the quiver plot with the u and v vectors
u = np.sin(2 * x * np.pi / 20 * x)
v = np.cos(2 * y * np.pi / 25  * x)
Q = ax.quiver(x, y, u, v, pivot='mid', color='r', units='inches')

# Create a canvas for the plot and add it to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Define an update function for the animation
def update(num):
    u = np.sin(2 * x * np.pi / 20 * (x + num))
    v = np.cos(2 * y * np.pi / 25  * (x + num))
    Q.set_UVC(u, v)
    return Q,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 200), interval=100, blit=True)

# Start the tkinter main loop
tk.mainloop()

#nottherealtar
