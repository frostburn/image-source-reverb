from pylab import *
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from image_source_reverb.shapes import equilateral_triangle


# TODO: Improve
def gaussian_point_source_2D(t, r, tightness=50):
    """
    A somewhat close approximation to the 2D Wave Equation with gaussian initial conditions
    """
    u = exp(-(tightness * (t-r))**2)
    u -= exp(-(tightness * (t-r)-0.5)**2)*0.66
    return u * (r + 0.5)**-0.5

x = linspace(-2.2, 2.2, 256)
x, y = meshgrid(x, x)

inside = vectorize(lambda x, y: equilateral_triangle.contains([x, y]))(x, y)


source_x = 1.0
source_y = 0.2

reflections = equilateral_triangle.reflections([source_x, source_y], 8)

print("Calculating using {} reflected images...".format(len(reflections)))

u = 0*x
fig, ax = plt.subplots()
plots = [ax.imshow(u * inside, vmin=-0.5, vmax=0.5)]
def update(t):
    u = 0*x
    for image_source, sign in reflections:
        if t - 2 < norm(image_source) < t + 2:
            r = sqrt((x-image_source[0])**2 + (y-image_source[1])**2)
            u += gaussian_point_source_2D(t, r) * sign
    plots[0].set_data(u * inside)
    return plots

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 256),
                    init_func=lambda: plots, blit=True, repeat=False, interval=50)
plt.show()
