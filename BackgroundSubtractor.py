import cv2
import numpy as np

capture =cv2.VideoCapture(0)
# 将图像转化为灰度图
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 显示图片

fgbg = cv2.createBackgroundSubtractorMOG2() # 利用BackgroundSubtractorMOG2算法消除背景
# fgbg.setHistory(20)


while(True):
    # 获取一帧
    ret,frame = capture.read()

    # fgmask = bgModel.apply(frame)
    fgmask = fgbg.apply(frame)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    cv2.imshow('frame', frame)
    cv2.imshow('frame2', res)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()