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
    print("Setting up logging...")
    logging.basicConfig(level=logging.DEBUG)

    # Create the tkinter root window
    print("Creating tkinter root window...")
    root = tk.Tk()
    root.wm_title("Wind Simulation")

    print("Creating figure and axes...")
    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')

    # Create the main 3D plot for the wind simulation
    ax1 = fig.add_subplot(121, projection='3d')

    # Create a subplot for the 3D compass
    ax2 = fig.add_subplot(122, projection='3d')

    # Create a meshgrid for the x, y, and z values with larger step size for fewer arrows
    print("Creating meshgrid...")
    x, y, z = np.meshgrid(np.arange(-1, 1, .8), np.arange(-1, 1, .8), np.arange(-1, 1, .8))

    # Define the initial u, v, and w vectors for the wind
    print("Defining initial wind vectors...")
    u = -1  # Wind is blowing from East to West
    v = 1  # Wind is blowing from South to North
    w = np.zeros_like(x)  # No vertical component

    # Create the compass directions
    print("Creating compass directions...")
    directions = ['N', 'E', 'S', 'W']
    for i, direction in enumerate(directions):
        ax2.text(1.2 * np.cos(i * np.pi / 2), 1.2 * np.sin(i * np.pi / 2), 0, direction, ha='center')
        
    def update(num, x, y, z, w):
        # Clear the axes
        ax1.clear()
        ax2.clear()

        # Update the u and v components to simulate wind shifts
        u = -1 + 0.1 * np.sin(num / 10) + 0.1 * np.random.randn(*x.shape)  # Wind shifts from East to West with a slight wiggle
        v = 1 - 0.1 * np.cos(num / 10) + 0.1 * np.random.randn(*x.shape)  # Wind shifts from South to North with a slight wiggle

        # Calculate the magnitude of the wind force
        magnitude = np.sqrt(u**2 + v**2 + w**2)

        # Create the quiver plot with smaller arrow heads, longer arrows for stronger winds, and color representing the wind force
        # Calculate the mean magnitude
        mean_magnitude = np.mean(magnitude)

        # Generate a color based on the mean magnitude
        color = plt.cm.viridis(mean_magnitude)

        # Define the length of the arrows
        length = 1.0

        # Use the length in the quiver plot
        Q = ax1.quiver(x, y, z, u, v, w, color=color, length=length, normalize=True, headlength=4, headwidth=2)

        # Create a topographical heatmap for the wind temperature
        temperature = np.random.uniform(low=0, high=1, size=x.shape)  # Replace with your temperature data
        contour = ax1.contourf(x[:,:,0], y[:,:,0], temperature[:,:,0], cmap='coolwarm', alpha=0.5, levels=20)

        # Add labels to the contour levels
        ax1.clabel(contour, inline=True, fontsize=8)

        # Create the 3D compass
        compass = ax2.quiver(0, 0, 0, u, v, w, color='r', length=1.0)
        ax2.set_xlim([-1.5, 1.5])
        ax2.set_ylim([-1.5, 1.5])
        ax2.set_zlim([-1, 1])
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')

        # Add the compass directions
        print("Creating compass directions...")
        directions = ['N', 'E', 'S', 'W']
        for i, direction in enumerate(directions):
            ax2.text(1.2 * np.cos(i * np.pi / 2), 1.2 * np.sin(i * np.pi / 2), 0, direction, ha='center')
        
    # Use a finite number of frames for real-time plotting
    print("Creating FuncAnimation...")
    ani = FuncAnimation(fig, update, fargs=(x, y, z, w), frames=100, interval=100, blit=False)

    print("Creating tkinter canvas...")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    print("Creating stop button...")
    stop_button = tk.Button(master=root, text='Stop', command=root.quit)
    stop_button.pack(side=tk.BOTTOM)

    # Start the tkinter main loop
    print("Starting tkinter main loop...")
    tk.mainloop()

except Exception as e:
    # Print the error message
    print("An error occurred:")
    print(traceback.format_exc())

# Wait for user input before closing the console
input("Press Enter to close the console...")