import numpy as np
import matplotlib.pyplot as plt
import sys

# Check if a filename is provided
if len(sys.argv) < 2:
    # Read from standard input
    data = np.fromstring(sys.stdin.read(), dtype=np.float32)
else:
    # Read the filename from the command line
    filename = sys.argv[1]
    # Read the data from the file
    data = np.fromfile(filename, dtype=np.float32)

# Reshape the data into pairs
data = data.reshape(-1, 2)

# Create the time array
time = np.arange(data.shape[0]) / 48000.0

# Plot I and Q
plt.figure(figsize=(10, 6))
plt.plot(time, data[:, 0], color='blue', label='I')
plt.plot(time, data[:, 1], color='red',  label='Q')

# Label the axes
plt.xlabel('Time (s)')
plt.ylabel('Signal')

# Enable the grid
plt.grid(True)

# Enable the legend
plt.legend()

# Show the plot with interactive mode on
plt.ioff()
plt.show()

