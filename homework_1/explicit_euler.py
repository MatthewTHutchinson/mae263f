import numpy as np
import matplotlib.pyplot as plt

# ---------- Functions ----------

def gradEs(x, index_matrix, stiffness_matrix, l_k):
    f = np.zeros_like(x)
    for i in range(index_matrix.shape[0]):
        ind = index_matrix[i].astype(int)
        xi = x[ind[0]]
        yi = x[ind[1]]
        xj = x[ind[2]]
        yj = x[ind[3]]
        dx = xj - xi
        dy = yj - yi
        l = np.sqrt(dx**2 + dy**2)
        k = stiffness_matrix[i]
        lk = l_k[i]
        if l == 0:
            continue
        dF = k * (1 - lk / l)
        f[ind[0]] += -dF * dx
        f[ind[1]] += -dF * dy
        f[ind[2]] += dF * dx
        f[ind[3]] += dF * dy
    return f

def plot_springs(x, index_matrix, t):
    plt.figure(figsize=(8, 5))
    for i in range(index_matrix.shape[0]):
        ind = index_matrix[i].astype(int)
        xi, yi = x[ind[0]], x[ind[1]]
        xj, yj = x[ind[2]], x[ind[3]]
        plt.plot([xi, xj], [yi, yj], 'bo-')
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.title(f"Time: {t:.2f} s (Explicit Euler, dt = {dt:.6f}s)")
    # plt.axis("equal")
    plt.axis([-1, 3, -6, 1])
    plt.grid(True)
    plt.savefig(f"Explicit_Euler/explicit_spring_network_t{t:.2f}s.png", dpi = 300)
    # plt.show()
    plt.close()

def getFexternal(m):
  W = np.zeros_like(m)
  for i in range(len(m) // 2 ):
    W[2 * i] = 0.0
    W[2 * i + 1] = m[2 * i + 1] * (-9.8)
  return W

# ---------- Load Node & Spring Data ----------
nodes_file_path = 'nodes.txt'
node_coordinates = []

try:
    with open(nodes_file_path, 'r') as f:
        for line in f:
            # Split each line by comma and remove leading/trailing whitespace
            parts = [part.strip() for part in line.split(',')]
            # Assuming the format is node number, x, y
            # We only need x and y, which are the second and third elements (index 1 and 2)
            if len(parts) == 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    node_coordinates.append([x, y])
                except ValueError:
                    print(f"Skipping line due to non-numeric coordinates: {line.strip()}")
            else:
                print(f"Skipping line due to incorrect format: {line.strip()}")

    # Convert the list of coordinates to a NumPy array
    node_matrix = np.array(node_coordinates)

    print("Node coordinates successfully loaded into a numpy matrix.")
    # display(node_matrix)
    print(node_matrix)

except FileNotFoundError:
    print(f"Error: The file '{nodes_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

springs_file_path = 'springs.txt'
index_info = []
stiffness_info = []

try:
    with open(springs_file_path, 'r') as f:
        for line in f:
            # Split each line by comma and remove leading/trailing whitespace
            parts = [part.strip() for part in line.split(',')]
            # Assuming the format is spring number, first node, second node, stiffness
            if len(parts) == 3:
                try:
                    first_node_index = float(parts[0])
                    second_node_index = float(parts[1])
                    stiffness = float(parts[2])
                    index_info.append([2*first_node_index, 2*first_node_index+1, 2*second_node_index, 2*second_node_index+1])
                    stiffness_info.append(stiffness)
                except ValueError:
                    print(f"Skipping line due to non-numeric coordinates: {line.strip()}")
            else:
                print(f"Skipping line due to incorrect format: {line.strip()}")

    # Convert the list of coordinates to a NumPy array
    index_matrix = np.array(index_info)
    stiffness_matrix = np.array(stiffness_info)

    print("Spring indices successfully loaded into a numpy matrix.")
    #display(index_matrix)
    print(index_matrix)

    print("Spring stiffnesses successfully loaded into a numpy matrix.")
    #display(stiffness_matrix)
    print(stiffness_matrix)

except FileNotFoundError:
    print(f"Error: The file '{springs_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Preparation at t = 0
N = node_matrix.shape[0]       # Number of nodes
ndof = 2 * N                   # Number of degrees of freedom (2 per node)

# Initialize positions, velocities
x_old = np.zeros(ndof)
u_old = np.zeros(ndof)

# Set initial position from node_matrix
for i in range(N):
  x_old[2*i] = node_matrix[i][0]
  x_old[2*i+1] = node_matrix[i][1]

# Rest lengths for each spring
l_k = np.zeros_like(stiffness_matrix)
for i in range(stiffness_matrix.shape[0]):
  ind = index_matrix[i].astype(int)
  xi = x_old[ind[0]]
  yi = x_old[ind[1]]
  xj = x_old[ind[2]]
  yj = x_old[ind[3]]
  l_k[i] = np.sqrt((xj - xi)**2 + (yj - yi)**2)

# Mass
m = np.ones(ndof)  # uniform mass of 1.0 for each DOF

# Weight
W = getFexternal(m)  # gravity force vector


# ---------- Simulation Parameters ----------
dt = 0.001
t_end = 10
t_array = np.arange(0, t_end + dt, dt)
plot_times = [0, 0.1, 1]
free_DOF = np.array([2, 3, 6, 7])  # Node 1 and Node 3 (x and y)
fixed_DOF = np.array([0, 1, 4, 5])

y_node1 = np.zeros(len(t_array))
y_node3 = np.zeros(len(t_array))
x_node1 = np.zeros(len(t_array))
x_node3 = np.zeros(len(t_array))

y_node1[0] = x_old[3]
y_node3[0] = x_old[7]
x_node1[0] = x_old[2]
x_node3[0] = x_old[6]

# ---------- Main Explicit Euler Loop ----------
for k in range(len(t_array) - 1):
    t = t_array[k+1]

    damping_coefficient = 0.5  # velocity-proportional damping
    f_damping = -damping_coefficient * u_old

    f = -gradEs(x_old, index_matrix, stiffness_matrix, l_k) + W + f_damping
    a = np.zeros_like(x_old)
    a[free_DOF] = f[free_DOF] / m[free_DOF]
    a[fixed_DOF] = 0

    # Explicit Euler Update
    u_new = u_old + dt * a
    x_new = x_old + dt * u_old
    u_new[fixed_DOF] = 0

    # Prepare for next iteration
    x_old = x_new
    u_old = u_new

    # Save DOFs
    x_node1[k + 1] = x_new[2]
    y_node1[k + 1] = x_new[3]
    x_node3[k + 1] = x_new[6]
    y_node3[k + 1] = x_new[7]

    # Plot at specified times
    """if any(np.isclose(t, pt, atol=1e-4) for pt in plot_times):
        plot_springs(x_new, index_matrix, t)"""

# ---------- Plot Displacement vs. Time ----------
# Y motion
plt.figure(figsize=(8, 5))
plt.plot(t_array, y_node1, 'r-', label="Node 1")
plt.plot(t_array, y_node3, 'b-', label="Node 3")
plt.title("Y Position of Free Nodes (Explicit Euler, dt = 0.001)")
plt.xlabel("Time (s)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)
plt.savefig("Explicit_Euler/explicit_y_position_vs_time.png", dpi = 300)
# plt.show()

# X motion
plt.figure(figsize=(8, 5))
plt.plot(t_array, x_node1, 'r-', label="Node 1")
plt.plot(t_array, x_node3, 'b-', label="Node 3")
plt.title("X Position of Free Nodes (Explicit Euler, dt = 0.001)")
plt.xlabel("Time (s)")
plt.ylabel("X Position (m)")
plt.legend()
plt.grid(True)
plt.savefig("Explicit_Euler/explicit_x_position_vs_time.png", dpi = 300)
# plt.show()