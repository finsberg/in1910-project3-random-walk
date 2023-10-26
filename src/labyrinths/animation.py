import matplotlib.pyplot as plt
from typing import Protocol
import numpy as np

from matplotlib.animation import FuncAnimation

from .labyrinth import plot


class MazeWalker(Protocol):
    x: np.ndarray
    y: np.ndarray
    maze: np.ndarray

    def plot(self) -> None:
        ...

    def move(self) -> None:
        ...


class Animation:
    """Class for animating maze walkers."""

    def __init__(self, mw: MazeWalker, color: str = "springgreen"):
        self._mw = mw
        self.color = color

    def plot(self, size: int, show: bool = True):
        """Figure containing the labyrinth and the walkers."""
        fig, ax = plt.subplots()
        plot(self._mw.maze)
        self._pos = ax.scatter(
            self._mw.x,
            self._mw.y,
            c=self.color,
            s=size,
            alpha=0.4,
        )
        if show:
            plt.show()
        return fig

    def _update_frame(self, i):
        """Plot new data on Figure object."""
        self._mw.move()
        self._pos.set_offsets(np.array([self._mw.x, self._mw.y]).T)
        return (self._pos,)

    def animate(
        self,
        N: int,
        size: int = 10,
        interval: int = 1,
        filename: str = "",
        show: bool = True,
    ):
        """Animate random walk in maze."""
        fig = self.plot(size, show=False)
        animation = FuncAnimation(
            fig,
            self._update_frame,
            interval=interval,
            repeat=False,
            frames=N,
        )
        if filename != "":
            animation.save(filename)
        if show:
            plt.show()
        return animation
