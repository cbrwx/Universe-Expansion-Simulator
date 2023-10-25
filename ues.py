import matplotlib.pyplot as plt
import numpy as np

# Initialize parameters
num_universes = 10  # Number of universes to simulate
time_points_per_universe = 100  # Time points to simulate for each universe
time_points_in_between = 20  # Time points for the "in-between" phase
graviton_multiplier = 1.1  # Multiplier for the graviton effect

# Function to simulate universe expansion with a scale factor
def simulate_universe_expansion(time_points, matter_multiplier, dark_energy_multiplier):
    return np.sin(np.linspace(0, np.pi, time_points)) * matter_multiplier + np.exp(np.linspace(0, 1, time_points)) * dark_energy_multiplier

# Function to simulate the "conformal geometry" phase
def simulate_conformal_geometry_phase(time_points, last_scale_factor):
    t = np.linspace(0, np.pi, time_points)
    return last_scale_factor * np.sin(t) * np.exp(-0.2 * t)  # Added oscillation and decay

# Function to simulate graviton effect
def simulate_graviton_effect(scale_factor):
    return np.array(scale_factor) * graviton_multiplier

# Initialize lists to store meta-time and scale factor
meta_time = []
scale_factor = []

# For marking transition points
transition_points = []

# Loop to simulate each universe
for i in range(num_universes):
    # Generate random multipliers for matter and dark energy for this universe
    matter_multiplier = np.random.uniform(0.5, 1.5)
    dark_energy_multiplier = np.random.uniform(0.5, 1.5)
    
    # Generate time points and scale factor for this universe
    time_points = np.linspace(0, 1, time_points_per_universe)
    expansion = simulate_universe_expansion(time_points_per_universe, matter_multiplier, dark_energy_multiplier)
    
    # Simulate the "conformal geometry" phase
    if i > 0:
        conformal_time_points = np.linspace(meta_time[-1], meta_time[-1] + 0.1, time_points_in_between)
        conformal_expansion = simulate_conformal_geometry_phase(time_points_in_between, scale_factor[-1])
        
        # Apply the graviton effect
        conformal_expansion = simulate_graviton_effect(conformal_expansion)
        
        # Append the "conformal geometry" phase to meta-time and scale factor
        meta_time.extend(conformal_time_points)
        scale_factor.extend(conformal_expansion)
        
        # Mark the start of the "conformal geometry" phase
        transition_points.append(meta_time[-1])
        
        # Offset time points to start where the "conformal geometry" phase ended
        time_points += meta_time[-1]
        
    # Append to meta-time and scale factor lists
    meta_time.extend(time_points)
    scale_factor.extend(expansion)

    # Mark the start of this universe
    transition_points.append(meta_time[0])

# Plotting
plt.figure(figsize=(15, 6))
plt.plot(meta_time, scale_factor)

# Add vertical lines to mark transitions
for point in transition_points:
    plt.axvline(x=point, color='r', linestyle='--')

plt.title("Hypothetical Expansion of Multiple Universes in Series with Conformal Geometry Phases and Graviton Effects")
plt.xlabel("Meta-Time (Arbitrary Units)")
plt.ylabel("Scale Factor (Arbitrary Units)")
plt.grid(True)
plt.show()

explanation = """
# Hypothetical Scale Factor vs Time for Multiple Universes in Series

## Explanation

This graph is a conceptual visualization of the behavior of the scale factor, denoted as a(t), over "meta-time" for a 
sequence of multiple universes. The x-axis corresponds to an arbitrary unit of "meta-time," while the y-axis measures 
the scale factor, a quantitative measure of the size of each universe. Each continuous curve on the graph represents a 
universe's lifetime, adjusted for both time and scale factor to be shown in sequence.

### Phases

1. **Pre-Big Bang (Hypothetical)**: 
    - This phase is speculative and assumes a state devoid of space-time, matter, or energy.
    - The scale factor is at a minimum, effectively zero, representing a state of non-existence or a singularity.

2. **Conformal Geometry Phase to New Universe Spawning**:
    - When a universe reaches its heat death and becomes void of matter, it enters a "conformal geometry" phase. 
      Here, the structure of space-time changes in a way that distances lose their meaning while angles between any 
      two vectors are preserved. This makes the universe "scale-free."
    - The scale factor in this phase, a(t), follows an oscillatory and decaying function as represented by: 
      a(t) = last_scale_factor * sin(t) * exp(-0.2 * t). Here, "last_scale_factor" is the final scale factor of the 
      previous universe.
    - The "graviton effect" is introduced, which scales the existing scale factor by a constant. The new scale factor 
      becomes: new_a(t) = 1.1 * a(t).
    - The amplified oscillations and decay in the scale factor lead to a destabilization in the conformal structure of
      the universe. When the scale factor crosses certain critical thresholds, the conformal geometry collapses, setting
      the initial conditions for a new singularity and, subsequently, a new Big Bang.

3. **Big Bang to Matter Dominance**: 
    - The universe originates from a singularity, expanding rapidly due to a mix of matter and dark energy.
    - The scale factor a(t) increases linearly, represented by: a(t) = sin(time_points) * matter_multiplier + 
      exp(time_points) * dark_energy_multiplier.

4. **Matter to Dark Energy Dominance**: 
    - As the universe continues to expand, matter clusters to form galaxies and other cosmic structures. However, dark 
      energy starts to take over.
    - The rate of increase of the scale factor a(t) starts to decline due to the growing influence of dark energy.

5. **Dark Energy Dominance to Heat Death (Hypothetical)**: 
    - Dark energy becomes the primary component, causing an accelerated expansion of the universe.
    - The scale factor a(t) starts to increase exponentially, which can be represented by: a(t) = exp(time_points).

### Note

- The time axis is stretched linearly for better visualization.
- The model is a simplified abstraction and does not take into account the many intricacies and unknown variables in 
  cosmology like tits and ass, cbrwx.

"""

print(explanation)
