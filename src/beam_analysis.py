import numpy as np

def calculate_shear_force(beam_lenght,load_intensity):      #calculating the shear force 
   """
    Calculate shear force distribution along the beam.
    :param beam_length: Length of the beam (m)
    :param load_intensity: Uniformly distributed load (N/m)
    :return: x (position along the beam), shear force (V)
    """ 
   x = np.linspace(0,beam_lenght,100)
   V = load_intensity*(beam_lenght/2-x)
   return x,V

def calculate_bending_moment(beam_lenght,load_intensity):   # Calculating bending moment from beam_lenght and beam intensity
   """
    Calculate bending moment distribution along the beam.
    :param beam_length: Length of the beam (m)
    :param load_intensity: Uniformly distributed load (N/m)
    :return: x (position along the beam), bending moment (M)
    """
   x = np.linspace(0,beam_lenght,100)
   M = (load_intensity/2) * x * (beam_lenght-x) 
   return x,M

def calculate_bending_stress(M,Y,I):
   """
    Calculate bending stress distribution along the beam.
    :param M: Bending moment (Nm)
    :param Y: Young's modulus (Pa)
    :param I: Moment of inertia (m^4)
    :return: x (position along the beam), bending stress (σ)
    """
   return M*Y/I

