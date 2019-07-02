import cv2

capture =cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret,frame = capture.read()
    # 将图像转化为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示图片
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) == ord('q'):
        break