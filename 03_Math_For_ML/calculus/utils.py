import numpy as np
import matplotlib.pyplot as plt

def create_line(x, m, b):
    """
    Calculates the y values for a simple line equation (y = mx + b).
    
    Args:
        x: Input value(s). Can be a single number or a numpy array of numbers.
        m: Slope of the line.
        b: Y-intercept (where the line crosses the y-axis).
        
    Returns:
        The computed y value(s).
    """
    return m * x + b

def plot_simple_line(m, b, x_range=(-10, 10)):
    """
    Plots a simple line y = mx + b.
    """
    x = np.linspace(x_range[0], x_range[1], 100)
    y = m * x + b
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {m}x + {b}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.title("Simple Line Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
