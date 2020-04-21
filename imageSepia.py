import image

img = image.Image("profile tutor.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
print(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        
        red = (p.getRed()*0.393+p.getGreen()*0.769+p.getBlue()*.131)
        green = (p.getRed()*0.349+p.getGreen()*0.686+p.getBlue()*.168)
        blue = (p.getRed()*0.272+p.getGreen()*0.534+p.getBlue()*.131)
        
        newpixel = image.Pixel(red, green, blue)
    
        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()