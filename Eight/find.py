circdef = 1 # 'circdef' defines which center should be faced

def center(drone,center1,center2):
    ''' Find the nearest center position and return
    the distance vector to the chosen point
    '''
    
    global circdef
    dif1 = PVector.sub(drone,center1)
    dif2 = PVector.sub(drone,center2)
    if (dif1.mag() - dif2.mag()) < 0.1:
        circdef = 1
        return dif1
    else:
        circdef = 2
        return dif2

def tangent(dir,p,clockwise):
    ''' Find the shorter way to the perimeter 
    of the given circular path
    '''
    
    R = dir.mag()
    r = p
    if R>r: # When the drone is out of the circunference, go for the tangent
        alfa = asin(r/R)
    else: # When the drone is in the circunference, follow the path
        alfa = PI/2
    if clockwise:
        dir.rotate(alfa)
    else:
        dir.rotate(-alfa)
    return dir
