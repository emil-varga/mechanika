import numpy as np
import matplotlib.pyplot as plt

def draw_circle(ax, center, radius, color='green', alpha=0.5):
    circle = plt.Circle(center, radius, color=color, alpha=alpha, fill=False)
    ax.add_patch(circle)