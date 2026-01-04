import numpy as np

def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.
    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """
    
    g = 9.81
    theta = np.radians(incline)
    
    # Energy conservation approach:
    # Initial PE = Final KE_translational + Final KE_rotational + Work_by_friction
    
    # For a uniform disk rolling without slipping:
    # - Moment of inertia: I = (1/2) * m * r^2
    # - Rolling constraint: v = ω * r, so ω = v/r
    # - KE_rotational = (1/2) * I * ω^2 = (1/2) * (1/2) * m * r^2 * (v/r)^2 = (1/4) * m * v^2
    # - Total KE = (1/2) * m * v^2 + (1/4) * m * v^2 = (3/4) * m * v^2
    
    # Work done against friction:
    # Normal force: N = m * g * cos(theta)
    # Friction force: f = friction * N
    # Work by friction: W_f = friction * m * g * cos(theta) * length
    
    # Energy equation:
    # m * g * height = (3/4) * m * v^2 + friction * m * g * cos(theta) * length
    # Simplify:
    # g * height = (3/4) * v^2 + friction * g * cos(theta) * length
    # v^2 = (4/3) * [g * height - friction * g * cos(theta) * length]
    
    energy_available = g * height - friction * g * np.cos(theta) * length
    
    # Check if the disk can actually roll down (friction might be too high)
    if energy_available <= 0:
        return 0.0
    v_squared = (4.0 / 3.0) * energy_available
    velocity = np.sqrt(v_squared)
    return velocity


# Test cases
if __name__ == "__main__":
    print("Test Case 1: Frictionless incline")
    # Expected: v = sqrt((4/3) * g * h) = sqrt((4/3) * 9.81 * 10) ≈ 11.48 m/s
    v1 = final_disk_speed(height=10.0, length=20.0, incline=30.0, mass=5.0, friction=0.0, radius=0.5)
    print(f"Height: 10m, No friction")
    print(f"Result: {v1:.2f} m/s")
    print(f"Expected: ~11.48 m/s\n")
    
    print("Test Case 2: Steep incline with higher friction")
    v3 = final_disk_speed(height=8.0, length=12.0, incline=45.0, mass=3.0, friction=0.3, radius=0.4)
    print(f"Height: 8m, Friction: 0.3, Angle: 45°")
    print(f"Result: {v3:.2f} m/s\n")
    
    print("Test Case 3: Very high friction (should return 0 or very low)")
    v4 = final_disk_speed(height=2.0, length=15.0, incline=20.0, mass=1.0, friction=0.5, radius=0.2)
    print(f"Height: 2m, Friction: 0.5, Length: 15m")
    print(f"Result: {v4:.2f} m/s")
    print(f"Expected: 0 or very low (friction consumes energy)\n")
