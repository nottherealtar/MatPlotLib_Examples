# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import logging
import traceback

try:
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)

    # Create the tkinter root window
    root = tk.Tk()
    root.wm_title("Wind Simulation")

    # Create a figure and axes for the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a meshgrid for the x, y, and z values
    x, y, z = np.meshgrid(np.arange(-1, 1, .2), np.arange(-1, 1, .2), np.arange(-1, 1, .2))

    # Define the u, v, and w vectors for the wind
    u = -1  # Wind is blowing from East to West
    v = 1   # Wind is blowing from South to North
    w = 0   # No vertical component

    def update(num, x, y, z, u, v, w):
        # Clear the axes
        ax.clear()

        # Create the quiver plot with lines and arrows
        Q = ax.quiver(x, y, z, u, v, w, color='r', length=0.1, normalize=True)

        return Q,

    # Use a finite number of frames for real-time plotting
    ani = FuncAnimation(fig, update, fargs=(x, y, z, u, v, w), frames=100, interval=100, blit=False)

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