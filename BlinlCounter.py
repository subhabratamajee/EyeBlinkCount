import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(400, 300,[250,400],invert=True)


idList = [22, 23, 24, 26, 110, 130, 157, 158, 159, 160, 161, 243]
ratioList = []
blinkCounter = 0
counter = 0
color = (255,0,255)
while True:
    ret, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 2, color, cv2.FILLED)

            leftUp = face[159]
            leftDown = face[23]
            leftEyeLeft = face[130]
            leftEyeRight = face[243]
            lengthHor, _ = detector.findDistance(leftUp, leftDown)
            lengthVer, _ = detector.findDistance(leftEyeLeft, leftEyeRight)
            cv2.line(img, leftUp, leftDown, (0, 255, 0), 2)
            cv2.line(img, leftEyeLeft, leftEyeRight, (0, 255, 0), 2)
            ratio = (int((lengthVer/lengthHor)*100))
            ratioList.append(ratio)
            if len(ratioList) >50:
                ratioList.pop(0)
            ratioAvg = sum(ratioList)/len(ratioList)

            if ratioAvg > 350 and counter == 0:
                blinkCounter += 1
                counter = 1
                color = (0,255,0)
            if counter != 0:
                counter += 1
                if counter > 20:
                    counter = 0
                    color = (255,0,255)



            cvzone.putTextRect(img,f'Blink Count : {blinkCounter}',(50,100),colorR=color)
            imgPlot = plotY.update(ratioAvg,color)
            # img = cv2.resize(img, (400, 300))
            # imgStack = cvzone.stackImages([img,imgPlot],2,1)
    else:
        # img = cv2.resize(img, (320, 240))
        imgStack = cvzone.stackImages([img, img], 2, 1)




    # cv2.imshow("image", imgStack)
    cv2.imshow("image", img)
    cv2.imshow("image", imgPlot)
    cv2.waitKey(25)

