def drawDrone(clock):
    ''' Drawing the drone with the camera
    facing the desired center
    '''
    
    # The camera rotates to face the center
    if clock:
        h = -40
    else:
        h = 40
        
    # Camera
    stroke(0)
    strokeWeight(1)
    fill(255,0,0)
    c = createShape()
    c.beginShape()
    c.vertex(-4,0)
    c.vertex(4,0)
    c.vertex(1,h)
    c.vertex(-1,h)
    c.endShape()
    shape(c,0,0)
    
    # Drone
    stroke(0)
    fill(255)
    s = createShape()
    s.beginShape()
    s.vertex(-17,15)
    s.vertex(-15,17)
    s.vertex(-5,7)
    s.vertex(5,7)
    s.vertex(15,17)
    s.vertex(17,15)
    s.vertex(7,5)
    s.vertex(7,-5)
    s.vertex(17,-15)
    s.vertex(15,-17)
    s.vertex(5,-7)
    s.vertex(-5,-7)
    s.vertex(-15,-17)
    s.vertex(-17,-15)
    s.vertex(-7,-5)
    s.vertex(-7,5)
    s.endShape()
    shape(s,0,0)
