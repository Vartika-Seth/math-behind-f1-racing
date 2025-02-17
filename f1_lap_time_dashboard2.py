import numpy as np
from matplotlib.animation import FuncAnimation

# Animation for Speed vs. Time
fig1, ax1 = plt.subplots()
line1, = ax1.plot([], [], color='#FF5757', marker='o', label='Speed (m/s)')
ax1.set_title('Speed vs. Time', color='white')
ax1.set_xlabel('Time (seconds)', color='white')
ax1.set_ylabel('Speed (m/s)', color='white')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend()
ax1.tick_params(colors='white')
fig1.patch.set_alpha(0)
ax1.set_facecolor('black')

def animate_speed(i):
    ax1.clear()
    ax1.plot(time_points[:i+1], speed_points[:i+1], color='#FF5757', marker='o')
    ax1.set_title('Speed vs. Time', color='white')
    ax1.set_xlabel('Time (seconds)', color='white')
    ax1.set_ylabel('Speed (m/s)', color='white')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.tick_params(colors='white')
    ax1.set_facecolor('black')

ani_speed = FuncAnimation(fig1, animate_speed, frames=len(time_points), interval=500)
st.pyplot(fig1)

# Animation for Distance vs. Time
fig2, ax2 = plt.subplots()
line2, = ax2.plot([], [], color='#FFF700', marker='o', label='Distance (m)')
ax2.set_title('Distance vs. Time', color='white')
ax2.set_xlabel('Time (seconds)', color='white')
ax2.set_ylabel('Distance (m)', color='white')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend()
ax2.tick_params(colors='white')
fig2.patch.set_alpha(0)
ax2.set_facecolor('black')

def animate_distance(i):
    ax2.clear()
    ax2.plot(time_points[:i+1], distance_points[:i+1], color='#FFF700', marker='o')
    ax2.set_title('Distance vs. Time', color='white')
    ax2.set_xlabel('Time (seconds)', color='white')
    ax2.set_ylabel('Distance (m)', color='white')
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.tick_params(colors='white')
    ax2.set_facecolor('black')

ani_distance = FuncAnimation(fig2, animate_distance, frames=len(time_points), interval=500)
st.pyplot(fig2)
