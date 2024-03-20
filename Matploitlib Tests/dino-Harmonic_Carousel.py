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

    # Create a meshgrid for the x, y, and z values with larger step size for fewer arrows
    x, y, z = np.meshgrid(np.arange(-1, 1, .8), np.arange(-1, 1, .8), np.arange(-1, 1, .8))

    # Define the initial u, v, and w vectors for the wind
    u = -1  # Wind is blowing from East to West
    v = 1   # Wind is blowing from South to North
    w = 0   # No vertical component

    def update(num, x, y, z):
        # Clear the axes
        ax.clear()

        # Update the u and v components to simulate wind shifts
        u = -1 + 0.1 * np.sin(num / 10)  # Wind shifts from East to West
        v = 1 - 0.1 * np.cos(num / 10)  # Wind shifts from South to North

        # Calculate the magnitude of the wind force
        magnitude = np.sqrt(u**2 + v**2 + w**2)

        # Create the quiver plot with longer arrows and color representing the wind force
        Q = ax.quiver(x, y, z, u, v, w, color=plt.cm.jet(magnitude), length=0.2, normalize=True)

        return Q,

    # Use a finite number of frames for real-time plotting
    ani = FuncAnimation(fig, update, fargs=(x, y, z), frames=100, interval=100, blit=False)

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