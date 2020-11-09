import cv2

img = cv2.imread("cr7.jpg",0) #okuma 0 gri renge çeviri
# print(img)
cv2.namedWindow("deneme",cv2.WINDOW_NORMAL) #pencere isimlendirmesi ve özellgi

cv2.imshow("deneme",img) #pencere isimlendirmesi
cv2.imwrite("cr7degisken.jpg",img) # kayıt islemi
cv2.waitKey(0) # ekran kalma süresi
cv2.destroyAllWindows()
