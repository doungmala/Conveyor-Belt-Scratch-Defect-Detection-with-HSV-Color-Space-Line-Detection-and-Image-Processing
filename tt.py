import cv2 
import numpy as np

cap = cv2.VideoCapture('Camera_2020-06-13_18_26_defect_at_2_11_Trim.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    img = frame
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for x in range(4):
        name_temp = str(x+1) + '.png'
        #print('name_temp',name_temp)
        template = cv2.imread(name_temp,0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        #print('res',res)
        threshold = 0.95
        loc = np.where( res >= threshold)
        print('loc',loc)
        for pt in zip(*loc[::-1]):
            x=pt[0]
            y=pt[1]
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            # Using cv2.putText() method
            srtt = 'x : ' + str(x) + ', ' + 'y : ' + str(y)
            cv2.putText(img, srtt, (100,100), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 0), 1, cv2.LINE_AA)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
