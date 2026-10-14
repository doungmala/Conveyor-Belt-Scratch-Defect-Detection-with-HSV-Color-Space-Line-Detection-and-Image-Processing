import cv2 
import numpy as np

# Save image in set directory 
# Read RGB image 
img = cv2.imread('test.png')  
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('1.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    x=pt[0]
    y=pt[1]
    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX     
    # org 
    org = (100,100) 
    # fontScale 
    fontScale = 0.5 
    # Blue color in BGR 
    color = (255, 0, 0) 
    # Line thickness of 2 px 
    thickness = 1
    # Using cv2.putText() method
    srtt = 'x : ' + str(x) + ', ' + 'y : ' + str(y)
    cv2.putText(img, srtt, org, font,
                fontScale, color, thickness, cv2.LINE_AA) 

# Output img with window name as 'image' 
cv2.imshow('image', img)  
  
# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)         
  
# Destroying present windows on screen 
cv2.destroyAllWindows()  
