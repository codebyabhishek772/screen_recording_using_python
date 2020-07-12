import cv2
import numpy as np 
from PIL import ImageGrab

def screenRecorder():
    fourcc = cv2.VideoWritter_fourcc(*'XVID')
    out = cv2.VideoWritter("output.avi", fourcc, (1366, 768))

    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtcolor(img_np, cv2.COLOR_BGRGB)
        cv2.imshow("Screen Recorder", frame)
        cv2.write(frame)

        if cv2.waitKey(1) == 27:
            break
    
    out.release()
    cv2.destroyAllWindow()

screenRecorder()
