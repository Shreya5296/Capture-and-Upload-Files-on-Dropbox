import cv2
import time
import random
import dropbox

startTime = time.time()

def takeSnapshot():
    number = random.randint(0,100)

    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()

        #cv2.imwrite()- this method is used to save an image to any storage device
        image_name  = "img" + str (number) + ".png"
        cv2.imwrite(image_name,frame)
        startTime = time.time
        result = False

    #Release the camera
    videoCaptureObject.release()

    #Close all the window that might have open in the process
    cv2.destroyAllWindows()

    print("Snapshot taken")
    return image_name
    
def uploadFile(image_name):
    access_token = 'sqAnqpyuEbEAAAAAAAAAAeq5g1lN-CiRqZXtpVgrcWvVqkN6WuEN3WN-TVd_WFcV'
    
    file = image_name
    file_from = file
    file_to = "/test images/" + (image_name)

    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-startTime) >= 5):
            name = takeSnapshot()
            uploadFile(name)

if __name__ == '__main__':
	main()
