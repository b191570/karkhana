import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

class MobiusStrip:
    def __init__(self, R, w, n):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _generate_mesh(self):
        U, V = self.U, self.V
        R = self.R

        X = (R + V * np.cos(U / 2)) * np.cos(U)
        Y = (R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)

        return X, Y, Z

    def surface_area(self):
        dX_du = np.gradient(self.X, axis=1)
        dY_du = np.gradient(self.Y, axis=1)
        dZ_du = np.gradient(self.Z, axis=1)

        dX_dv = np.gradient(self.X, axis=0)
        dY_dv = np.gradient(self.Y, axis=0)
        dZ_dv = np.gradient(self.Z, axis=0)

        cross_X = dY_du * dZ_dv - dZ_du * dY_dv
        cross_Y = dZ_du * dX_dv - dX_du * dZ_dv
        cross_Z = dX_du * dY_dv - dY_du * dX_dv
        area_density = np.sqrt(cross_X**2 + cross_Y**2 + cross_Z**2)
        area = simpson(simpson(area_density, self.v, axis=0), self.u, axis=0)
        return area

    def edge_length(self):
        x_top = self.X[-1]
        y_top = self.Y[-1]
        z_top = self.Z[-1]

        x_bot = self.X[0]
        y_bot = self.Y[0]
        z_bot = self.Z[0]

        def arc_length(x, y, z):
            dx = np.diff(x)
            dy = np.diff(y)
            dz = np.diff(z)
            return np.sum(np.sqrt(dx**2 + dy**2 + dz**2))

        return arc_length(x_top, y_top, z_top) + arc_length(x_bot, y_bot, z_bot)

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set_title('Möbius Strip')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    strip = MobiusStrip(R=1, w=0.4, n=200)
    print("Surface Area:", strip.surface_area())
    print("Edge Length:", strip.edge_length())
    strip.plot()
