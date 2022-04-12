def drawPath(c1,c2,rd,theta):
    ''' Drawing the 'Eight' path in a black stroke
    '''
    
    stroke(50)
    strokeWeight(3)
    noFill()
    circle(c1.x,c1.y,2*rd) # Center 1
    point(c1.x,c1.y)
    circle(c2.x,c2.y,2*rd) # Center 2
    point(c2.x,c2.y)
      
    stroke(50)
    strokeWeight(3)
    line(c1.x+sin(theta)*rd,c1.y+cos(theta)*rd,c2.x-sin(theta)*rd,c2.y-cos(theta)*rd)
    line(c1.x+sin(theta)*rd,c1.y-cos(theta)*rd,c2.x-sin(theta)*rd,c2.y+cos(theta)*rd)
    
    
