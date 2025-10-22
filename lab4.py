import numpy as np
def throw_rock(m, v0, theta):
    g = 9.81 # in m/s^2
    theta_rad = theta * np.pi / 180 # in radians
    tf = 2 * v0 * np.sin(theta_rad) / g # in sec
    R = v0**2 * np.sin(2 * theta_rad) / g #in m
    hm = v0**2 * np.sin(theta_rad)**2 / (2 * g) # in m
    vh = v0 * np.cos(theta_rad) # in m/s
    Kh = 0.5 * m * vh * hm**2 # in J   

    print("For a rock with %5.3f kg mass thrown with %5.3f m/s at an angle of %6.2f degrees:\n"
          "Time of flight is %10.1e s\n"
          "The range in x-direction is %10.1e m\n"
          "Maximum height is %10.1e m\n"
          "The speed at maximum height is %10.1e m/s\n"
          "Kinetic energy at the maximum height is %8.2e J\n"
          % (m, v0, theta, tf, R, hm, vh, Kh))

    return tf, R, hm, vh, Kh

myresult = throw_rock(1.5, 0.3, 35.20)
