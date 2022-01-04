import cv2
import board
import neopixel
import numpy as p
from time import sleep

np = neopixel.NeoPixel(board.D18, 60)
np.brightness = 0.5
    
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = img[y, x]
        colorsRGB=tuple(reversed(colorsBGR))
        
        for i in range(60):     
           np[i]=(colorsRGB)
           sleep(0.01)
           print(colorsRGB)
        
        
image = cv2.imread("/home/pi/rgb.jpg")
img = cv2.resize(image,(640,480))


cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)


while True:
    cv2.imshow('RGB', img)
     
    
           
    
        
         
    if cv2.waitKey(10) & 0xFF == 27:
        break
      
        
for i in range(60):
     np[i]=(0,0,0)
    
cv2.destroyAllWindows()
