def distance(x1, y1, x2, y2):
    deltax = x2 - x1
    deltay = y2- y1
    z = (deltax**2 + deltay**2)**.5
    return z
print(distance(1,0,4,0))

def areaofcircle(x3, y3, x4, y4):
    area = 3.14 * distance(x3, y3, x4, y4)**2
    return area
print("the area of your circle with radius", areaofcircle(0,1,0,0))