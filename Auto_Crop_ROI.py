import cv2


    cap = cv2.VideoCapture(0)

    auto = False
    retry = False
    delay = 1
    img_count = 0     ##
    wait_time = 60  #default =40 (3 sec)

    save_file = "/home/mp913/Desktop/bOTTLe/TRY/"
    save_name = "TRY{}.jpg"
    save_size =(1200,1200)

    while True:
        ret, frame = cap.read()
        frame_txt =frame.copy() #first video
        output = frame.copy()

        if auto == False:

            output = frame.copy()
            cv2.putText(frame_txt, "Please Set ROI", (9, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.putText(frame_txt, "Press Space to start", (9, 60), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.putText(frame_txt, "{} image taken".format(img_count), (9, 90), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.imshow("Video", frame_txt)  #showing video

            k = cv2.waitKey(1) & 0xFF

            if k == 32:  #space to start ROI cropping

                while retry == False:

                    r = cv2.selectROI(output)
                    img = output[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]    #coordinates
                    cv2.imshow("ROI", img)

                    k = cv2.waitKey(0) & 0xFF
                    if k == ord("r"):   #r to retry
                        retry = False
                        cv2.destroyWindow("ROI")

                    if k == 32:  #space to proceed
                        break

                auto = True  #convert to auto mode

                y1 = int(r[1])
                x1 = int(r[1] + r[3])
                y2 = int(r[0])
                x2 = int(r[0] + r[2])

                cv2.waitKey(0)  #wait to proceed auto mode

                cv2.destroyAllWindows()

        start = time.time()

        if auto == True:

            output = frame.copy()
            output_txt = frame.copy()
            cv2.rectangle(output_txt,(y2,y1),(x2,x1),(0,255,0),3)   #draw box of ROI
            cv2.putText(output_txt, "Auto crop in 2s", (9, 60), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.putText(output_txt, "Press r to Reset ROI", (9, 90), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.putText(output_txt, "Press Space to Pause", (9, 120), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.putText(output_txt, "{} image taken".format(img_count), (9, 150), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.putText(output_txt, "Press Esc to Exit", (9, 180), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 100, 0), 2)
            cv2.imshow("Video", output_txt)

            k = cv2.waitKey(1) & 0xFF   #video plays continously

            # end = time.time()
            # end += 0.5
            # print("S: ", start)
            # print("E: ", end)
            # duration = end - start
            # # print ("Duration: ",  duration)

            delay +=1   #wait time, increase, stop while 40
            print(delay)

            if k == ord("r"):   #reset ROI
                print("Reset")
                auto = False
                cv2.destroyAllWindows()

            if k == 32: #space to Pause cropping
                cv2.waitKey(0)

            while delay == wait_time:   #proceed while wait time reached (40)
                img_count += 1  #img value
                save_img = output[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]    #coordinates
                save_img2 = save_img.copy()

                # save_img2 = cv2.resize(save_img2, save_size)  #set save size

                cv2.imshow("Saved Img", save_img2)
                cv2.waitKey(500)
                cv2.imwrite(save_file + save_name.format(img_count), save_img2)     #save image to file
                delay = 1   #convert back to 1
                break

        if k == 27: #esc
            print("End")
            break

auto_crop()
