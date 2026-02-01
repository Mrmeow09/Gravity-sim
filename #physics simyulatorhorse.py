#physics simyulator
from vpython import *
import random
import math
import numpy as np 
import matplotlib.pyplot as plt # type: ignore 

#background setting 
scene.background = color.black
scene.width = 1200
scene.height = 800
scene.userspin=True
step=20 

def geta(p1,p2,M):
    rx=p1-p2
    r_norm=mag(rx)
    a=(G*M)/r_norm**2
    cute_a=rx.norm()*a
    return cute_a
    


class blackhole:
    def __init__ (self,mass,pos,r_s):
        self.mass=mass
        self.pos=pos # type: ignore
        self.r_s=r_s

        self.visual=sphere(
    pos=self.pos, 
    radius=self.r_s, 
    color=color.red,
    emissive=True,   
    shininess=0,
    make_trail=True)

G=6.67e-11
m=1.808001e+30
m2=2.428e+29
R=1.94477e+15
q=2.137e+14
r2=1.7145233e+15
t=0
dt=(1e+8)*5

center_point = sphere(pos=vec(R/2,0,0), radius=1e+10, color=color.white)
#toliman
my_bh=blackhole(mass=pow(10,7),pos=vec(R,0,0),r_s=597675*1e+8)
my_bh.velocity=vec(0,0,91.25)
scene.range=R*2
scene.center=my_bh.visual.pos
#proxima centauri
my_bh2=blackhole(mass=pow(10,7),pos=vec(0,0,0),r_s=107132*1e+8)
my_bh2.velocity=vec(0,0,249.00)

scene.center=my_bh.visual.pos
scene.autoscale = True
def move_camera(evt):
    k = evt.key
    
    
    if k == 'w':
        scene.camera.pos += scene.forward * step
    if k == 's':
        scene.camera.pos -= scene.forward * step
    

    side_vector = cross(scene.forward, scene.up).norm()
    
    if k == 'd':
        scene.camera.pos += side_vector * step
    if k == 'a':
        scene.camera.pos -= side_vector * step
    

scene.bind('keydown', move_camera)
while True:
    rate(200000)
    #force of gravity for m2
    t+=dt
    r=my_bh.visual.pos-my_bh2.visual.pos

    

#force of gravity for m
    e=geta(my_bh2.pos,my_bh2.pos,m)
    kv1 = e * dt
    kp1 = my_bh2.velocity * dt

    e2=geta(my_bh2.pos + kp1/2,my_bh2.pos,m)
    kv2 = e2 * dt
    kp2 = (my_bh2.velocity+kv1/2) * dt

    e3=geta(my_bh.pos + kp2,my_bh2.pos,m)
    kv3 = e3 * dt
    kp3 = (my_bh2.velocity+kv2/2)* dt

    e4=geta(my_bh.pos + kp3,my_bh2.pos,m)
    kv4 = e4 * dt
    kp4 = (my_bh2.velocity+kv3)* dt
    my_bh2.velocity+=(1/6)*(kv1+2*kv2+2*kv3+kv4)
    my_bh2.visual.pos+=(1/6)*(kp1+2*kp2+2*kp3+kp4)

    


    e5=geta(my_bh2.pos,my_bh.pos,m2)
    kv5 = e5 * dt
    kp5 = my_bh.velocity * dt

    e6=geta(my_bh2.pos + kp1/2,my_bh.pos,m2)
    kv6 = e6 * dt
    kp6 = (my_bh.velocity+kv1) * dt

    e7=geta(my_bh2.pos + kp2,my_bh.pos,m2)
    kv7= e7 * dt
    kp7= (my_bh.velocity+kv6)* dt

    e8=geta(my_bh2.pos + kp7,my_bh.pos,m2)
    kv8 = e8 * dt
    kp8 = (my_bh.velocity+kv3)* dt
    my_bh.velocity+=(1/6)*(kv5+2*kv6+2*kv7+kv8)
    my_bh.visual.pos+=(1/6)*(kp5+2*kp6+2*kp7+kp8)

    

#velocity
   
