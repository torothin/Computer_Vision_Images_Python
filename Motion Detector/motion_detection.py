import cv2, time

first_frame=None

video=cv2.VideoCapture(0)
time.sleep(10)

while True:

    check, frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
        #blurs image so that it is easier to calculate differences between frames.
        #Also smooths the lines increasing accuracy between calculations.
        #(21,21) is the bluring setpoint, 0 is the standard distribution.
        #More info in the documentaion

    if first_frame is None:
        first_frame=gray
        continue
            #resets to the beginning of the while loop from here.
            #Wont run the rest of the code in the while loop

    delta_frame=cv2.absdiff(first_frame,gray)

    cv2.imshow("Capturing",gray)
    cv2.imshow("delta",delta_frame)
    #cv2.imshow("first",first_frame)

    key=cv2.waitKey(1)
    #print(first_frame)
    # print(gray)
    # print(delta_frame)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
