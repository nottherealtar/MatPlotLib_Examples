# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
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
    fig = plt.figure(figsize=(10, 5))

    # Create the main 3D plot for the wind simulation
    ax1 = fig.add_subplot(121, projection='3d')

    # Create a subplot for the 3D compass
    ax2 = fig.add_subplot(122, projection='3d')

    # Create a meshgrid for the x, y, and z values with larger step size for fewer arrows
    x, y, z = np.meshgrid(np.arange(-1, 1, .8), np.arange(-1, 1, .8), np.arange(-1, 1, .8))

    # Define the initial u, v, and w vectors for the wind
    u = -1  # Wind is blowing from East to West
    v = 1   # Wind is blowing from South to North
    w = 0   # No vertical component

    # Create the compass directions
    directions = ['N', 'E', 'S', 'W']
    for i, direction in enumerate(directions):
        ax2.text(1.2 * np.cos(i * np.pi / 2), 1.2 * np.sin(i * np.pi / 2), 0, direction, ha='center')

    def update(num, x, y, z):
        # Clear the axes
        ax1.clear()
        ax2.clear()

        # Update the u and v components to simulate wind shifts
        u = -1 + 0.1 * np.sin(num / 10)  # Wind shifts from East to West
        v = 1 - 0.1 * np.cos(num / 10)  # Wind shifts from South to North

        # Calculate the magnitude of the wind force
        magnitude = np.sqrt(u**2 + v**2 + w**2)

        # Create the quiver plot with longer arrows for stronger winds and color representing the wind force
        Q = ax1.quiver(x, y, z, u, v, w, color=plt.cm.viridis(magnitude), length=magnitude, normalize=True)

        # Create a heatmap for the wind temperature
        temperature = np.random.uniform(low=0, high=1, size=x.shape)  # Replace with your temperature data
        ax1.imshow(temperature, cmap='coolwarm', interpolation='bilinear', alpha=0.5, extent=[-1, 1, -1, 1])

        # Create the 3D compass
        compass = ax2.quiver(0, 0, 0, u, v, w, color='r', length=1.0)
        ax2.set_xlim([-1.5, 1.5])
        ax2.set_ylim([-1.5, 1.5])
        ax2.set_zlim([-1, 1])
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')

        # Add the compass directions
        for i, direction in enumerate(directions):
            ax2.text(1.2 * np.cos(i * np.pi / 2), 1.2 * np.sin(i * np.pi / 2), 0, direction, ha='center')

        return Q, compass,

    # Use a finite number of frames for real-time plotting
    ani = FuncAnimation(fig, update, fargs=(x, y, z), frames=100, interval=100, blit=False)

    # Create a canvas for the plot and add it to the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Create a button to stop the animation and end the script
    stop_button = tk.Button(master=root, text='Stop', command=root.quit)
    stop_button.pack(side=tk.BOTTOM)

    # Start the tkinter main loop
    tk.mainloop()

except Exception as e:
    # Print the error message
    print("An error occurred:")
    print(traceback.format_exc())

# Wait for user input before closing the console
input("Press Enter to close the console...")