import cv2
import numpy as np
import imutils

def process():
    while True:
        video = cv2.VideoCapture(0)

        while True:
            ret, frame = video.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            x = cv2.Sobel(frame, cv2.CV_16S, 1, 0)
            y = cv2.Sobel(frame, cv2.CV_16S, 0, 1)

            absX = cv2.convertScaleAbs(x)
            absY = cv2.convertScaleAbs(y)

            dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


            cv2.imshow("Video", dst)
            key = cv2.waitKey(25)
            if key == 27:
                break


    video.release()
    cv2.destroyAllWindows()


#process()

def nothing(x):
    pass

def videoplay():
    cap = cv2.VideoCapture("/home/mp913/Desktop/Louis/Project 101/2018-11-08-151649.webm")

    cv2.namedWindow("frame")
    cv2.createTrackbar("Gray", "frame", 0, 1, nothing)
    cv2.createTrackbar("Threshold", "frame", 0, 1, nothing)
    cv2.createTrackbar("Min Value", "frame", 0, 254, nothing)
    cv2.createTrackbar("Max Value", "frame", 1, 255, nothing)

    while True:
        ret, frame = cap.read()
        font = cv2.FONT_HERSHEY_COMPLEX


        gray = cv2.getTrackbarPos("Gray", "frame")

        if gray == 0:
            cv2.putText(txt, str("Grayscale: Off"), (10, 15), font, 0.5, (0, 0, 255))
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.putText(txt, str("Grayscale: On"), (10, 15), font, 0.5, (0, 0, 255))

        thresh_btn = cv2.getTrackbarPos("Threshold", "frame")
        if thresh_btn == 0 :
            cv2.putText(frame, str("Threshold: Off"), (10, 30), font, 0.5, (0, 0, 255))
        else:
            t = cv2.getTrackbarPos("Min Value", "frame")
            m = cv2.getTrackbarPos("Max Value", "frame")


            frame = cv2.threshold(frame, t, m, cv2.THRESH_BINARY)[1]
            cv2.putText(frame, str("Threshold: On"), (10, 30), font, 0.5, (0, 0, 255))
            cv2.putText(frame, 'Min value: ' + str(t), (10, 45), font, 0.5, (0, 0, 255))
            cv2.putText(frame, 'Min value: ' + str(t), (10, 45), font, 0.5, (0, 0, 255))


        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def cam():
    cap = cv2.VideoCapture(0)


    cv2.namedWindow("frame")
    cv2.createTrackbar("Gray", "frame", 0, 1, nothing)
    cv2.createTrackbar("Threshold", "frame", 0, 1, nothing)
    cv2.createTrackbar("Min Value", "frame", 0, 254, nothing)
    cv2.createTrackbar("Max Value", "frame", 1, 255, nothing)

    cv2.createTrackbar("Gaussian", "frame", 0, 20, nothing)
    cv2.createTrackbar("Canny", "frame", 0, 1, nothing)
    cv2.createTrackbar("Sobel", "frame", 0, 1, nothing)
    cv2.createTrackbar("Opening", "frame", 0, 1, nothing)
    cv2.createTrackbar("Closing", "frame", 0, 1, nothing)
    cv2.createTrackbar("Contours", "frame", 0, 1, nothing)
    #cv2.createTrackbar("OTSU", "frame", 0,1, nothing)
    cv2.createTrackbar("Show Text", "frame", 0, 1, nothing)


    while True:
        ret, frame = cap.read()

        font = cv2.FONT_HERSHEY_COMPLEX

        #cv2.rectangle(frame,(0,0),(150,200),(0,255,0),-1)
        ##############################################################################################################
        reset = cv2.waitKey(1) & 0xFF

        if reset == ord('r'):
            cv2.setTrackbarPos("Gray", "frame",0)
            cv2.setTrackbarPos("Threshold", "frame", 0)
            cv2.setTrackbarPos("Min Value", "frame", 0)
            cv2.setTrackbarPos("Max Value", "frame", 1)

            cv2.setTrackbarPos("Gaussian", "frame", 0)
            cv2.setTrackbarPos("Canny", "frame", 0)
            cv2.setTrackbarPos("Sobel", "frame", 0)
            cv2.setTrackbarPos("Opening", "frame", 0)
            cv2.setTrackbarPos("Closing", "frame", 0)
            cv2.setTrackbarPos("Contours", "frame", 0)
            cv2.setTrackbarPos("Show Text", "frame", 0)

        ##############################################################################################################
        gray = cv2.getTrackbarPos("Gray", "frame")
        gray_x = 10
        gray_y = 15

        if gray == 0:
            gray_text = "Grayscale: Off"
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_text = "Grayscale: On"


        ##############################################################################################################
        gaus = cv2.getTrackbarPos("Gaussian", "frame")
        if gaus == 0:
            cv2.putText(frame, str("Gaussian: Off"), (10, 75), font, 0.5, (0, 0, 255))
        else:
            count = gaus % 2

            if (count == 0):
                gaus += 1
                cv2.putText(frame, 'Blur value: ' + str(gaus), (10, 75), font, 0.5, (0, 0, 255))
                frame = cv2.GaussianBlur(frame, (gaus, gaus), 0)

            else:
                cv2.putText(frame, 'Blur value: ' + str(gaus), (10, 75), font, 0.5, (0, 0, 255))
                frame = cv2.GaussianBlur(frame, (gaus, gaus), 0)

            output = frame.copy()
        ##############################################################################################################
        thresh_btn = cv2.getTrackbarPos("Threshold", "frame")
        t = cv2.getTrackbarPos("Min Value", "frame")
        m = cv2.getTrackbarPos("Max Value", "frame")

        if thresh_btn == 0:
            cv2.putText(frame, str("Threshold: Off"), (10, 30), font, 0.5, (0, 0, 255))
        else:
            if gaus == 0:
                frame = cv2.threshold(frame, t, m, cv2.THRESH_BINARY)[1]
            else:
                frame = cv2.threshold(output, t, m, cv2.THRESH_BINARY)[1]

            cv2.putText(frame, str("Threshold: On"), (10, 30), font, 0.5, (0, 0, 255))
            cv2.putText(frame, 'Min value: ' + str(t), (10, 45), font, 0.5, (0, 0, 255))
            cv2.putText(frame, 'Max value: ' + str(m), (10, 60), font, 0.5, (0, 0, 255))

        ##############################################################################################################
        #note: canny value depends on min&max value
        canny = cv2.getTrackbarPos("Canny", "frame")

        if canny == 0:
            cv2.putText(frame, str("Canny: Off"), (10, 90), font, 0.5, (0, 0, 255))
        else:
            if gaus == 0:
                frame = cv2.Canny(frame, t, m)
            else:
                frame = cv2.Canny(frame, t, m)
            cv2.putText(frame, str("Canny: On"), (10, 90), font, 0.5, (0, 0, 255))



        ##############################################################################################################

        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.getTrackbarPos("Opening", "frame")

        if opening == 0:
            cv2.putText(frame, str("Opening: Off"), (10, 90), font, 0.5, (0, 0, 255))
        else:
            #cv2.putText(frame, str("Opening: On"), (10, 90), font, 0.5, (0, 0, 255))
            frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)


        ##############################################################################################################

        closing = cv2.getTrackbarPos("Closing", "frame")

        if closing == 0:
            cv2.putText(frame, str("Opening: Off"), (10, 90), font, 0.5, (0, 0, 255))
        else:
            #cv2.putText(frame, str("Opening: On"), (10, 90), font, 0.5, (0, 0, 255))
            frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)


        ##############################################################################################################

        sobel = cv2.getTrackbarPos("Sobel", "frame")
        if sobel == 0:
            cv2.putText(frame, str("Sobel: Off"), (10, 105), font, 0.5, (0, 0, 255))
        else:
            x = cv2.Sobel(frame, cv2.CV_16S, 1, 0)
            y = cv2.Sobel(frame, cv2.CV_16S, 0, 1)

            absX = cv2.convertScaleAbs(x)
            absY = cv2.convertScaleAbs(y)

            dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
            cv2.putText(frame, str("Sobel: On"), (10, 105), font, 0.5, (0, 0, 255))
            frame = dst.copy()

        ##############################################################################################################
        cnt = cv2.getTrackbarPos("Contours", "frame")
        if cnt == 0:
            cv2.putText(frame, str("Contours: Off"), (10, 120), font, 0.5, (0, 0, 255))
        else:
            cv2.putText(frame, str("Contours: On"), (10, 120), font, 0.5, (0, 0, 255))
            cnts = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            output = frame.copy()
            output = cv2.cvtColor(frame,cv2.COLOR_GRAY2RGB)
            for c in cnts:
                cv2.drawContours(output, [c], -1, (255, 0, 255), 3)

            text = "I found {} objects!".format(len(cnts))
            cv2.putText(output, text, (10, 175), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                        (0,0,255), 2)

            frame = output.copy()


        ##############################################################################################################
        #shows in RGB format

        rgb = cv2.getTrackbarPos("Show Text", "frame")
        if rgb == 0:
            cv2.putText(frame, str("RGB Mode: Off"), (10, 135), font, 0.5, (0, 0, 255))
        else:
            cv2.putText(frame, str(gray_text), (gray_x, gray_y), font, 0.6, (0, 0, 255), 2)


       #not working
        '''
        otsu = cv2.getTrackbarPos("OTSU", "frame")

        if otsu == 0:
            cv2.putText(frame, str("OTSU: Off"), (10, 135), font, 0.5, (0, 0, 255))
        else:
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
            ret,th = cv2.threshold(frame, 0, 0, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            frame = th.copy()
            cv2.putText(frame, str("OTSU: On"), (10, 135), font, 0.5, (0, 0, 255))

        '''
        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break


    cap.release()
    cv2.destroyAllWindows()


#videoplay()
#process()
cam()