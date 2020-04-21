import image

def smooth(oldimage):
    """Smooths out the quality of the image"""
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    print("your resolution is: ", oldw, oldh)
    # newim = image.EmptyImage(int(oldw), int(oldh))
    
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
            oldimage.setPixel(col, row, newpixel)
            oldimage.setPixel(col+1, row, newpixel)
            oldimage.setPixel(col, row+1, newpixel)
            oldimage.setPixel(col+1, row+1, newpixel)
            
            
            
    print("here")
    return oldimage
            
            
            
            
            
 
img = image.Image("tiger.jpg")
smoothed = smooth(img)
print(smoothed)
win = image.ImageWin(smoothed.getWidth(), smoothed.getHeight())

smoothed.draw(win)
win.exitonclick()
# img.setDelay(1,15)   # setDelay(0) turns off animation


