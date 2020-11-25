import cv2
import dropbox
import time
import random

start_time = time.time()

def takesnapshot():
    number = random.randint(0, 100)

    print("started")
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videocaptureobject.read()
        img_name = 'image'+str(number)+'.jpg'
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False
        print('snapshot captured')
        return img_name
      
    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'SYF2N-PIwYcAAAAAAAAAAXOZXS7Bdbsappj4umjAyYZ74ghoRf8yukxfuQ9ChF_c'
    file = img_name
    file_from = file
    file_to = '/motionCamera/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        if ((time.time()-start_time) >= 2):
            name = takesnapshot()
            upload_file(name)

main()