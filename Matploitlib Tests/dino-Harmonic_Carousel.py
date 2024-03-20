# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import itertools
import logging
import traceback

try:
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)

    # Create the tkinter root window
    root = tk.Tk()
    root.wm_title("Harmonic Carousel Visualization")

    # Create a figure and axes for the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a meshgrid for the x, y, and z values
    x, y, z = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))

    def update(num, x, y, z):
        # Clear the axes
        ax.clear()

        # Update the u, v, and w vectors for the new frame
        u = np.sin(2 * x * np.pi / 20 * (x + num))
        v = np.cos(2 * y * np.pi / 25  * (x + num))
        w = np.sin(2 * z * np.pi / 30 * (z + num))

        # Create the quiver plot with lines and arrows
        Q = ax.quiver(x, y, z, u, v, w, color='r', length=0.1, normalize=True)

        return Q,

    ani = FuncAnimation(fig, update, fargs=(x, y, z), frames=itertools.count(), interval=100, blit=False)

    # Create a canvas for the plot and add it to the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Start the tkinter main loop
    tk.mainloop()

except Exception as e:
    # Print the error message
    print("An error occurred:")
    print(traceback.format_exc())

# Wait for user input before closing the console
input("Press Enter to close the console...")