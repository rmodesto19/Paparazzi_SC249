# SC-249: Simulação de Drones e Aplicações
# Lab 02: Paparazzi Mobility Model 'Eight'
# Prof. Dr. Vitor Curtis
# Solution by Rafael Modesto and Atila Diniz

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
# Our drone will start from a random posi-  #
# tion within the canvas and will execute   # 
# the desired 'StayAt' path accordingly.    #
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* #
import path, drone, find

def mouseClicked():
    ''' Define the initial point with a mouseclick (optional)
    '''
    background(200)
    p0.set(mouseX,mouseY)
    
# Define the center position
# 1) StayAt
c1 = PVector(600,300)

# Define the parameters of the movement
rd = 100.0 # Radius of the circle
mass = 1.0 # Drone mass in kilograms
max_f = 1.0 # Maximum force -> Defined by structural limits of the aircraft
max_a = (max_f/mass) # Maximum acceleration
max_v = sqrt(rd*max_a/2)  # Maximum linear velocity -> Defined by structural limits of the aircraft
clockwise = False # True for clockwise, False for counterclockwise
t = 0 # Timestamp

def setup():
    frameRate(60)
    size(1200,600)
    global p0, vl, ac, t
    
    # Define the initial parameters for the drone
    p0 = PVector(random(1200),random(600)) # Initial position
    vl = PVector(0.0,0.0) # Initial velocity
    ac = PVector(0.0,0.0) # Initial acceleration
    background(200)

def draw():
    global p0, vl, ac, t, clockwise, rd, c1, t
    
    # Cleaning the canvas
    # background(200)
    noStroke()
    fill(200,5)
    rect(0,0,width,height)
    
    # Setting the acceleration to zero
    ac.set(0.0,0.0)
    
    # Drawing the centers and desired path
    path.drawPath(c1,rd)
    
    # Wind
    w_force = 0.3
    k = random(-PI,PI)
    w = PVector(cos(k),sin(k)).mult(w_force/mass)
    ac.add(w)
    
    translate(p0.x,p0.y)
    rotate(vl.heading())
    
    # Update the parameters for the next iteration
    go = find.center(p0,c1)
    ac.add(find.tangent(go,rd,clockwise).mult(-1).limit(max_a))
    vl.add(ac)    
    vl.limit(max_v)
    p0.add(vl)
    
    # Drawing the drone and the camera
    if t%1 == 0:
        drone.drawDrone(clockwise)
    t+=1
