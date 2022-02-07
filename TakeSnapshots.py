import cv2

def takeSnapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()

        #cv2.imwrite()- this method is used to save an image to any storage device
        cv2.imwrite("newPicture1.jpg",frame)
        result = False

    #Release the camera
    videoCaptureObject.release()

    #Close all the window that might have open in the process
    cv2.destroyAllWindows()

takeSnapshot()
