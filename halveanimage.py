import image

def halve(oldimage):
    """Halves the size of the image"""
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    
    newim = image.EmptyImage(int(oldw * .5), int(oldh*.5))
    
    for row in range(oldh-1):
        for col in range(oldw-1):
            oldpixel1 = oldimage.getPixel(col, row)
            oldpixel2 = oldimage.getPixel(col+1, row)
            oldpixel3 = oldimage.getPixel(col, row+1)
            oldpixel4 = oldimage.getPixel(col+1, row+1)
            newred = int((oldpixel1.getRed() + oldpixel2.getRed() + oldpixel3.getRed() + oldpixel4.getRed()) / 4)
            newgreen = int((oldpixel1.getGreen() + oldpixel2.getGreen() + oldpixel3.getGreen() + oldpixel4.getGreen()) / 4)
            newblue = int((oldpixel1.getBlue() + oldpixel2.getBlue() + oldpixel3.getBlue() + oldpixel4.getBlue()) / 4)
            
            newpixel = image.Pixel(newred, newgreen, newblue)
            
            newim.setPixel(int(.5*col), int(.5*row), newpixel)
          
    
    return newim
            
            
            
            
            
    
img = image.Image("profile tutor.jpg")
win = image.ImageWin(.5*img.getWidth(), .5*img.getHeight())
print("old resolution:",img.getWidth(), img.getHeight())
print("new resolution:",.5*img.getWidth(), .5*img.getHeight())
# img.setDelay(1,15)   # setDelay(0) turns off animation

halfing = halve(img)

halfing.draw(win)
win.exitonclick()
