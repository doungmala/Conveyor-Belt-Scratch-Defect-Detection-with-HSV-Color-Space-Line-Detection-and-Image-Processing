import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    # Save image in set directory 
    # Read RGB image 
    img = frame
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for x in range(5):
        name_temp = str(x) + '.png'
        template = cv2.imread(name_temp,0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.95
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

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
