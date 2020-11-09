import cv2
import numpy as np

# canvs oluşturuyoruz. belirli bir alanı siyah canvas oluşturuyor Çizim yapıldığında kullanılan veri tipi uint8'dir
canvas = np.zeros((512,512,3), dtype=np.uint8) +255
        # cizgi  başlangıc,bitis,renk, kalınlık
cv2.line(canvas,(50,50),(206,206),(255,0,0),thickness=5)
        #dikdörtgen
cv2.rectangle(canvas,(20,20),(50,50),(255,0,0),thickness=-1)  #-1 içi dolu veriri
        #cember            yarıçap
cv2.circle(canvas, (200,200),100,(0,0,255),thickness=5 )
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

