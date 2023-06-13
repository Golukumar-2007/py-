import cv2
img=cv2.imread("C:/Users/goluk/Desktop/python classes/class116-img-related/solar-system.jpg")
print(img)
cv2.putText(img,
            "sun",(20,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
            "Mercury",(100,250), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
            "Vinus",(190,260), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
            "Earth",(280,270), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
            "Mars",(380,260), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
            "Jupiter",(570,380), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255))
cv2.putText(img,
            "Saturn",(780,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
            "Urinus",(970,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
            "Naptune",(1100,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)
