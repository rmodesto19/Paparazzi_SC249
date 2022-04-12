def center(drone,center1):
    ''' Find the nearest center position and return
    the distance vector to the chosen point
    '''
    
    return PVector.sub(drone,center1)

def tangent(dir,p,clockwise):
    ''' Find the shorter way to the perimeter 
    of the given circular path
    '''
    
    R = dir.mag()
    r = p
    if R>r: # When the drone is out of the circunference, go for the tangent
        alfa = asin(r/R)
    else: #When the drone is in the circunference, follow the path
        alfa = PI/2
    if clockwise:
        dir.rotate(alfa)
    else:
        dir.rotate(-alfa)
    return dir
