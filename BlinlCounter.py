import cv2
import cvzone
from  cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
idList = [22,23,24,26,110,157,158,159,160,161]

while True:
    ret, img= cap.read()
    img , faces = detector.findFaceMesh(img,draw=False)

    if faces :
        face = faces[0]
        for id in idList:
            cv2.circle(img,face[id],2,(255,0,255))

    # img =cv2.resize(img,(480,350))
    cv2.imshow("image",img)
    cv2.waitKey(1)

