def isRightangled(a,b,c):
    """determines if a triangle with 3 sides a,b and c is a right triangle"""
    if a>b and a>c:        
        if abs((c**2)+(b**2)-(a**2))<0.001:
            return True
        else:
            return False
    elif b>a and b>c:
        if abs((c**2)+(a**2)-(b**2))<0.001:
            return True
        else:
            return False
    elif c>a and c>a:
        if abs((a**2)+(b**2)-(c**2))<0.001:
            return True
        else:
            return False
print("it is ", isRightangled(4.4,5.5,3.3), "that your triangle is right angled")
        