import image

def double(oldimage):
    """Doubles the size of the image"""
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    
    newim = image.EmptyImage(oldw * 2, oldh*2)
    
    for row in range(oldh):
        for col in range(oldw):
            oldpixel = oldimage.getPixel(col, row)
            
            newim.setPixel(2*col, 2*row, oldpixel)
            newim.setPixel(2*col+1, 2*row, oldpixel)
            newim.setPixel(2*col, 2*row+1, oldpixel)
            newim.setPixel(2*col+1, 2*row+1, oldpixel)
    
    return newim
            
            
            
            
            
    
img = image.Image("profile tutor.jpg")
win = image.ImageWin(2*img.getWidth(), 2*img.getHeight())
print("old resolution:",img.getWidth(), img.getHeight())
print("new resolution:",2*img.getWidth(), 2*img.getHeight())
# img.setDelay(1,15)   # setDelay(0) turns off animation

bigimg = double(img)

bigimg.draw(win)
win.exitonclick()