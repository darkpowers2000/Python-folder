import math

# Constants from the equation h = -4.9t^2 + 24.5t + 2
a = -4.9
b = 24.5
c = 2

# (a) Velocity function: v = 2at + b
def get_velocity(t):
    return (2 * a * t) + b

print(f"(a) Velocity at 2s: {get_velocity(2)} m/s")
print(f"    Velocity at 4s: {get_velocity(4)} m/s")

# (b) Max height occurs when v = 0 -> t = -b / (2a)
t_max = -b / (2 * a)
print(f"(b) Max height reached at: {t_max} s")

# (c) Max height: plug t_max into h(t)
h_max = (a * t_max**2) + (b * t_max) + c
print(f"(c) Max height: {h_max} m")

# (d) Hits ground when h = 0 (Quadratic Formula)
# t = [-b - sqrt(b^2 - 4ac)] / 2a
discriminant = b**2 - (4 * a * c)
t_impact = (-b - math.sqrt(discriminant)) / (2 * a)
print(f"(d) Hits ground at: {round(t_impact, 3)} s")

# (e) Velocity at impact
v_impact = get_velocity(t_impact)
print(f"(e) Impact velocity: {round(v_impact, 3)} m/s")