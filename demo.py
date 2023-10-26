# # Quickstart
# Once installed the package you can import the labyrinths package

import labyrinths
import matplotlib.pyplot as plt

# Now we can start by creating a maze

example_maze = labyrinths.example()

# We can also plot it

labyrinths.plot(example_maze)
plt.show()

# There also other types of labyrinths. For example a circular one

circular_maze = labyrinths.circular(R=100, padding=2)
labyrinths.plot(circular_maze)
plt.show()

# and a layered maze

layered_maze = labyrinths.layered_labyrinth(layers=2, width=3, height=5)
labyrinths.plot(layered_maze)
plt.show()
