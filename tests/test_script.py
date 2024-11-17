from beam_analysis import calculate_bending_moment, calculate_shear_force, calculate_bending_stress


# Test Running
beam_lenght = 12        # lenght of beam
load_intensity = 50     # Uniformly distributed load in N/m
l = 0.2                 # lenght of the beam in meters
b = 0.2                 # Height of the beam in meters
h = 0.4                 # Height of the beam in meters
y = h/2                 # Distance from neutral axis to extreme fiber (half the height)

# Moment of interia (for rectangular beam)
I = (b*h**3)/12
print(f"Moment of interia (I): {I:.6f} m^4")

# Calculate shear force
x_shear,V = calculate_shear_force(beam_lenght,load_intensity)
print(f"shear force at start (x=0): {V[0]:.2f} N")
print(f"shear force at midpoint (x={beam_lenght/2}):{V[len(V)//2]:.2f} N")
print(f"shear force at end (x={beam_lenght/2}): {V[-1]:.2f} N")

#calculate bending moment
x_moment, M=calculate_bending_moment(beam_lenght,load_intensity)
print(f"Bending Moment at start (x=0): {M[0]:.2f} Nm")
print(f"Bending Moment at midpoint (x={beam_lenght/2}): {M[len(M)//2]:.2f} Nm")
print(f"Bending Moment at end (x={beam_lenght}): {M[-1]:.2f} Nm")

# Calculate bending stress at midpoint
bending_stress = calculate_bending_stress(M[len(M)//2], y, I)
print(f"Bending Stress at midpoint: {bending_stress:.2f} Pa")

