import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) +255

font2=cv2.FONT_HERSHEY_SIMPLEX


cv2.putText(canvas,"Deneme",(40,80),font2,3,(0,0,0),cv2.LINE_AA)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()