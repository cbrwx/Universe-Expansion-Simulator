# Universe(s)-Expansion-Simulator
This Python script simulates the hypothetical expansion of multiple universes in a serial configuration. It incorporates different phases like matter-dominance, dark energy-dominance, and a 'conformal geometry' phase that connects one universe to the next. The simulation then visualizes these expansions using Matplotlib.

# Hypothetical Scale Factor vs Time for Multiple Universes in Series

## Explanation

This graph is a conceptual visualization of the behavior of the scale factor, denoted as a(t), over "meta-time" for a sequence of multiple universes. The x-axis corresponds to an arbitrary unit of "meta-time," while the y-axis measures the scale factor, a quantitative measure of the size of each universe. Each continuous curve on the graph represents a universe's lifetime, adjusted for both time and scale factor to be shown in sequence.

### Phases

1. **Pre-Big Bang (Hypothetical)**: 
    - This phase is speculative and assumes a state devoid of space-time, matter, or energy.
    - The scale factor is at a minimum, effectively zero, representing a state of non-existence or a singularity.

2. **Conformal Geometry Phase to New Universe Spawning**:
    - When a universe reaches its heat death and becomes void of matter, it enters a "conformal geometry" phase. Here, the structure of space-time changes in a way that distances lose their meaning while angles between any two vectors are preserved. This makes the universe "scale-free."
    - The scale factor in this phase, a(t), follows an oscillatory and decaying function as represented by: a(t) = last_scale_factor * sin(t) * exp(-0.2 * t). Here, "last_scale_factor" is the final scale factor of the previous universe.
    - The "graviton effect" is introduced, which scales the existing scale factor by a constant. The new scale factor becomes: new_a(t) = 1.1 * a(t).
    - The amplified oscillations and decay in the scale factor lead to a destabilization in the conformal structure of the universe. When the scale factor crosses certain critical thresholds, the conformal geometry collapses, setting the initial conditions for a new singularity and, subsequently, a new Big Bang.

3. **Big Bang to Matter Dominance**: 
    - The universe originates from a singularity, expanding rapidly due to a mix of matter and dark energy.
    - The scale factor a(t) increases linearly, represented by: a(t) = sin(time_points) * matter_multiplier + exp(time_points) * dark_energy_multiplier.

4. **Matter to Dark Energy Dominance**: 
    - As the universe continues to expand, matter clusters to form galaxies and other cosmic structures. However, dark energy starts to take over.
    - The rate of increase of the scale factor a(t) starts to decline due to the growing influence of dark energy.

5. **Dark Energy Dominance to Heat Death (Hypothetical)**: 
    - Dark energy becomes the primary component, causing an accelerated expansion of the universe.
    - The scale factor a(t) starts to increase exponentially, which can be represented by: a(t) = exp(time_points).

### Note

- The time axis is stretched linearly for better visualization.
- The model is a simplified abstraction and does not take into account the many intricacies and unknown variables in cosmology like tits and ass, cbrwx.

A more graphical representation:
![hyp_exp_c](https://github.com/cbrwx/Universe-Expansion-Simulator/assets/81207429/35159f22-f7f4-4607-82a7-5399ef183f69)
![4545](https://github.com/cbrwx/Universe-Expansion-Simulator/assets/81207429/b711aa68-553c-4c12-baee-ecfcf831b49e)
![65656](https://github.com/cbrwx/Universe-Expansion-Simulator/assets/81207429/966ca6e7-64d3-4a42-8d8d-2eb915392670)

Code derived from standing on the shoulders of these sources:

- Before the Big Bang: An Outrageous New Perspective and its Implications for Particle Physics by Roger Penrose
- Roger Penrose - The Cyclic Universe: A Conversation
- The Emperor's New Mind by Roger Penrose
- Cycles of Time: An Extraordinary New View of the Universe by Roger Penrose
- NASA's Universe 101: Big Bang and Expansion of the Universe
- Dark Energy, Dark Matter - NASA Science
- The Distribution of Dark Matter in the Universe - APS Physics
- Conformal Field Theory - Scholarpedia
- Conformal Geometry: A Publication of the Max Planck Institute for Mathematics
- Graviton - CERN
- The Graviton - Scholarpedia
- The Heat Death of the Universe - Physics of the Universe
- The Multiverse - Stanford Encyclopedia of Philosophy
- Multiverse - MIT Technology Review
