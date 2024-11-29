import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# Function to compute fractional integral/derivative kernel
def fractional_derivative_kernel(alpha, t, tau):
    """
    Computes the fractional derivative memory kernel.

    Parameters:
    alpha (float): Fractional order (0 < alpha < 1)
    t (float): Current time
    tau (float): Past time
    
    Returns:
    float: Memory kernel weight
    """
    return (t - tau)**(-alpha) / gamma(1 - alpha)

# Function to simulate anomalous diffusion with memory effects
def anomalous_diffusion(time_steps, alpha=0.5):
    """
    Simulates anomalous diffusion using fractional derivatives.

    Parameters:
    time_steps (int): Number of time steps for the simulation
    alpha (float): Fractional order (0 < alpha < 1)
    
    Returns:
    np.ndarray: Position over time with memory effects
    """
    # Initialize variables
    position = np.zeros(time_steps)
    memory = np.zeros(time_steps)
    
    # Loop through each time step
    for t in range(1, time_steps):
        # Calculate fractional memory effects (integral approximation)
        memory_sum = 0
        for tau in range(0, t):
            memory_sum += fractional_derivative_kernel(alpha, t, tau) * position[tau]
        
        # Update position with a random step and memory contribution
        position[t] = position[t-1] + np.random.normal(0, 1) + 0.1 * memory_sum
    
    return position

# Parameters for the simulation
time_steps = 500
alpha_values = [0.2, 0.5, 0.8]

# Plot results for different alpha values
plt.figure(figsize=(10, 6))
for alpha in alpha_values:
    result = anomalous_diffusion(time_steps, alpha=alpha)
    plt.plot(result, label=f"Alpha = {alpha}")

# Plot formatting
plt.title("Anomalous Diffusion with Memory Effects")
plt.xlabel("Time Steps")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.show()
