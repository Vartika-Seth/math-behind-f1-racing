import math
import matplotlib.pyplot as plt

# User inputs
track_length = float(input("Enter track length in meters: "))  # Example: 5000m
avg_speed_kmh = float(input("Enter average speed in km/h: "))  # Example: 250 km/h

# Convert km/h to m/s
avg_speed_ms = avg_speed_kmh * (1000 / 3600)

# Acceleration & Braking Assumptions
acceleration = 4  # m/s² (F1 car acceleration)
braking = 6  # m/s² (F1 car braking)

# Time to reach max speed
t_accel = avg_speed_ms / acceleration  
s_accel = 0.5 * acceleration * t_accel**2  

# Braking distance (before a turn)
s_braking = (avg_speed_ms**2) / (2 * braking)  

# Remaining track distance for steady speed
s_constant = track_length - (s_accel + s_braking)  
t_constant = s_constant / avg_speed_ms  

# Time for braking phase
t_braking = avg_speed_ms / braking  

# Total Lap Time
lap_time = t_accel + t_constant + t_braking

# Display the results
print(f"Final Estimated Lap Time: {lap_time:.2f} seconds")

# Visualization Data
time_points = [0, t_accel, t_accel + t_constant, lap_time]
speed_points = [0, avg_speed_ms, avg_speed_ms, 0]
distance_points = [0, s_accel, s_accel + s_constant, track_length]

# Plotting Speed vs. Time
plt.figure(figsize=(10, 6))
plt.plot(time_points, speed_points, label='Speed (m/s)', color='red', marker='o')
plt.title('Speed vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Speed (m/s)')
plt.grid(True)
plt.legend()
plt.show()

# Plotting Distance vs. Time
plt.figure(figsize=(10, 6))
plt.plot(time_points, distance_points, label='Distance (m)', color='blue', marker='o')
plt.title('Distance vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Distance (m)')
plt.grid(True)
plt.legend()
plt.show()
