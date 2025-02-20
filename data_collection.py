import cv2, os


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 26
dataset_size = 150

cap = cv2.VideoCapture(0)

for i in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR,str(i))):
        os.makedirs(os.path.join(DATA_DIR,str(i)))
    print("Collecting Image for Sign: ",chr(i+65))
    finished = False
    while True:
        ret,frame = cap.read()
        cv2.putText(frame,"Press S to collect image data.",(100,50),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,34),2,cv2.LINE_AA)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(25)==ord('s'):
            break 
    count = 0
    while count < dataset_size:
        ret,frame = cap.read()
        cv2.imshow("Frame",frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR,str(i),f"{count}.jpg"),frame)
        count+=1

cap.release()
cv2.destroyAllWindows()






