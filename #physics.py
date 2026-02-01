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
scene.userspan=True
step=20 


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

#Blackhole but now just a star


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
    shininess=0)

my_bh=blackhole(mass=pow(10,7),pos=vec(0,0,0),r_s=2*pow(10,3))
my_bh.velocity=vec(20,45,0)

scene.center=my_bh.visual.pos
#planets

class planets:
    def __init__(self,pos,mass,color):
        self.pos=pos
        self.mass=mass
        self.color=color
        
        self.visual=sphere(pos=pos,color=color,radius=100,shininess=0,emissive=True,mass=mass,make_trail=True)
    

#making planets
p1=planets(pos=vec(5500,0,0),mass=100,color=color.yellow)
p2=planets(pos=vec(6000,500,0),mass=100,color=color.blue)
p1.velocity=vec(0,45,50)
p2.velocity=vec(0,45,40.75)

p3=planets(pos=vec(7500,0,0),mass=100,color=vec(0.4,0.2,0))
p4=planets(pos=vec(8000,500,0),mass=100,color=color.blue)
p4.velocity=vec(0,45,36.515)
p3.velocity=vec(0,45,35.355)

p5=planets(pos=vec(8500,0,0),mass=100,color=vec(0.4,0.2,0))
p6=planets(pos=vec(10000,500,0),mass=100,color=color.blue)
p5.velocity=vec(0,45,34.299)
p6.velocity=vec(0,45,31.622)

# asteroid belt
class asteroids:
    def __init__(self,pos,color):
        self.pos=pos
        
        self.color=color
        self.visual=sphere(pos=pos,color=self.color,radius=10,shininess=0,emissive=True,make_trail=True)

#making asteroids using for looop
asteroid_values=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320]
asteroid=[]
for i in range(1,32):
    asteroid1 = asteroids(pos=vec(6500, 0, random.choice(asteroid_values)), color=vec(0.5, 0.5, 0.5))
    asteroid1.velocity=vec(0,45,45)
    asteroid.append(asteroid1)
#time
dt=0.01

#camera position have to zoom out a lot

scene.camera.pos = vector(30, 10, 0)
scene.camera.follow(my_bh.visual)

scene.camera.axis = vector(-30, -10, 0)
target_cam_pos = vec(-30, 5, 0)

scene.userpan = False
scene.userzoom = True 



#major code work
while True:
    rate(2000)
    my_bh.visual.pos+=my_bh.velocity*dt
    #constant decleration
    G=1
    m_1=pow(10,7)
    m_2=1000
    m_3=1000
    m_4=pow(10,9)
    m_5=10000
    m_6=100000
    
 #force of gravity for mass_1
    r=my_bh.visual.pos-p1.visual.pos
    r_norm=mag(r)
    a=(G*m_1)/r_norm**2
    cute_a=r.norm()*a

#velocity
    p1.velocity=p1.velocity + cute_a*dt
    p1.visual.pos += p1.velocity * dt

#Work of  gravity for Mass 1 and mass 3
    r2=my_bh.visual.pos-p2.visual.pos
    r_norm2=mag(r2)
    a2=(G*m_1)/r_norm2**2
    cute_a2=r2.norm()*a2
    
#velocity
    p2.velocity=p2.velocity + cute_a2*dt
    p2.visual.pos += p2.velocity * dt

#Asteroid Belt
    m=100
    for asteroid1 in asteroid:
        r3=my_bh.visual.pos-asteroid1.visual.pos
       
        r_norm3=mag(r3)
       
        a_asteroid=(G*m_1)/r_norm3**2
       
        norm_a=r3.norm()*a_asteroid
       
        asteroid1.velocity=asteroid1.velocity + (norm_a)*dt
        asteroid1.visual.pos += asteroid1.velocity * dt

    #Outer Planets_1
    r4=my_bh.visual.pos-p3.visual.pos
    r_norm4=mag(r4)
    a4=(G*m_1)/r_norm4**2
    cute_a4=r4.norm()*a4
    p3.velocity=p3.velocity + cute_a4*dt
    p3.visual.pos += p3.velocity * dt

    #Outer Planets_2
    r5=my_bh.visual.pos-p4.visual.pos
    r_norm5=mag(r5)
    a5=(G*m_1)/r_norm5**2
    cute_a5=r5.norm()*a5
    p4.velocity=p4.velocity + cute_a5*dt
    p4.visual.pos += p4.velocity * dt

    #Outer Planets_3
    r6=my_bh.visual.pos-p5.visual.pos
    r_norm6=mag(r6)
    a6=(G*m_1)/r_norm6**2
    cute_a6=r6.norm()*a6
    p5.velocity=p4.velocity + cute_a6*dt
    p5.visual.pos += p4.velocity * dt

    #Outer Planets_4
    r7=my_bh.visual.pos-p6.visual.pos
    r_norm7=mag(r7)
    a7=(G*m_1)/r_norm7**2
    cute_a7=r7.norm()*a7
    p6.velocity=p6.velocity + cute_a7*dt
    p6.visual.pos += p6.velocity * dt