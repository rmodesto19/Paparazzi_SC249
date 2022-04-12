def drawPath(c1,rd):
    ''' Drawing the 'StayAt' path in a black stroke
    '''
    
    stroke(50)
    strokeWeight(3)
    noFill()
    circle(c1.x,c1.y,2*rd) # Center 1
    point(c1.x,c1.y)
