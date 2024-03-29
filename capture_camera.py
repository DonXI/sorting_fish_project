### capture camera by video ###

import uuid, cv2, time, os

cam = cv2.VideoCapture(0) # open camera 0 
# set size camera
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
start = time.time()

name_folder = "dataset_img"
if not os.path.isdir(name_folder):
    os.makedirs(name_folder)

while True :
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    unique_file_name = str(uuid.uuid4())

    # auto save image 5 seconds
    '''
    stop = time.time() - start
    if stop >= 5:
        start = time.time()
        cv2.imwrite(f"{unique_file_name}.jpg", frame)
        print(unique_file_name)
    '''

    # manual save image
    if cv2.waitKey(1) & 0xFF == ord('s') :
        cv2.imwrite(f"{name_folder}/{unique_file_name}.jpg", frame)
        print(unique_file_name)

    # typing e for exit
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cam.release()
cv2.destroyAllWindows()