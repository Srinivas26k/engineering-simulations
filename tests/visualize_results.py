import matplotlib.pyplot as plt
from src.beam_analysis import calculate_shear_force, calculate_bending_moment

# Beam Parameters
beam_length = 12  # Beam length in meters
load_intensity = 500  # Uniformly distributed load in N/m

# Calculate Shear Force and Bending Moment
x_shear, V = calculate_shear_force(beam_length, load_intensity)
x_moment, M = calculate_bending_moment(beam_length, load_intensity)

# Plot Shear Force Distribution
plt.figure(figsize=(8, 6))
plt.plot(x_shear, V, label='Shear Force', color='red')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Zero reference line
plt.title('Shear Force Distribution')
plt.xlabel('Distance along the beam (m)')
plt.ylabel('Shear Force (N)')
plt.grid(True)
plt.legend()
plt.annotate('Max Shear Force', xy=(0, V[0]), xytext=(2, V[0] + 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate('Zero Shear', xy=(beam_length / 2, 0), xytext=(beam_length / 2 + 1, 500),
             arrowprops=dict(facecolor='blue', arrowstyle='->'))
plt.savefig('shear_force_distribution.png')  # Save the plot
plt.show()

# Plot Bending Moment Distribution
plt.figure(figsize=(8, 6))
plt.plot(x_moment, M, label='Bending Moment', color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Zero reference line
plt.title('Bending Moment Distribution')
plt.xlabel('Distance along the beam (m)')
plt.ylabel('Bending Moment (Nm)')
plt.grid(True)
plt.legend()
plt.annotate('Max Bending Moment', xy=(beam_length / 2, max(M)), 
             xytext=(beam_length / 2 + 2, max(M) - 1000),
             arrowprops=dict(facecolor='green', arrowstyle='->'))
plt.savefig('bending_moment_distribution.png')  # Save the plot
plt.show()
