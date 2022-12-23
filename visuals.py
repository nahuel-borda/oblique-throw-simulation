from vpython import * 
from projectile_motion import calculate_velocity

def display_throw(height, speed, angle, max_reach, flight_time, max_height):
    scene = canvas(center=vector(0,5+max_reach[1],0))

    # styling
    scene.align = "left"

    scene.append_to_caption(f'alcance: {max_reach[0]} <br>')
    scene.append_to_caption(f'tiempo de vuelo: {flight_time} <br>')
    scene.append_to_caption(f'elevacion maxima: {max_height[1]} <br>')

    ball_init_position = (-5.5,0.2+height,0)
    
    xmax=text(pos=vector(*ball_init_position)+vector(max_reach[0], max_reach[1], 0), billboard=True, text=f'Xmax', visible=False) #, vector(*max_height,0)], radus=0.01)
    ymax=text(pos=vector(*ball_init_position)+vector(max_height[0], max_height[1], 0), billboard=True, text=f'Ymax', visible=False)
    ground=box(pos=vector(0,0,0), size=vector(6+(height+speed)+round(max_reach[0]),0.2,3), color=color.green)
    
    ball=sphere(pos=vector(*ball_init_position), radius=0.1, color=color.blue)

    g=vector(0,-9.8,0)
    
    v0=speed
    theta=angle

    def run(ball):
        ball.m=1
        ball.v=vector(v0*cos(theta), v0*sin(theta),0)
        ball.velocity_y = vector(0,0,0)
        ball.velocity_x = vector(0,0,0)
        ball_trail = attach_trail(ball)
        ball_trail.start()
        
        ball_arrow_vy = attach_arrow(ball, "velocity_y", color=color.red, scale=0.5)
        ball_arrow_vx = attach_arrow(ball, "velocity_x", color=color.red, scale=0.5)

        ball_arrow_vy.start()
        ball_arrow_vx.start()

        t=0
        dt=0.01
        while ball.pos.y>=0:
            ball.velocity_y = vector(*(0, calculate_velocity(t, speed, angle)[1], 0))
            ball.velocity_x = vector(*(calculate_velocity(t, speed, angle)[0],0, 0))
            rate(100)
            F=ball.m*g
            ball.v=ball.v+(F/ball.m)*dt
            ball.pos=ball.pos+ball.v*dt/ball.m
            t=t+dt
        
        xmax.visible=True
        ymax.visible=True
        
        ball_trail.stop()
        ball_arrow_vy.stop()
        ball_arrow_vx.stop()
        ball_trail.clear()

    while True:
        event = scene.waitfor('mousedown mouseup')
        if event.event == 'mouseup':
            ball=sphere(pos=vector(*ball_init_position), radius=0.1, color=color.blue)
            xmax.visible=False
            ymax.visible=False
            run(ball)

