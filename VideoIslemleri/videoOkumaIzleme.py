import cv2

cap = cv2.VideoCapture("video.mp4") # 0 webcam kullanma yada yol verme

while True:
    ret,frame =cap.read(); # 2değer okuyor true/false - kare
    if ret ==0: #video bittiginde kapatsın
        break
    frame = cv2.flip(frame,1) # aldığımız görüntüyü istenilen eksende yön değiştirir yansıtır y eksenine göre tersini aldık aynada tersi gibi
    cv2.imshow("video",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"): #her frame 30ms gösterilecek q'ye basınca kaapatıcak
        break
cap.release()
cv2.destroyAllWindows()