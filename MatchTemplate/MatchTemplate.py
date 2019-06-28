import cv2
import numpy as np

img_rgb = cv2.imread("./img/photo.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


template = cv2.imread('./img/template.jpg',0)

w, h = template.shape[::-1]

#查看三组图像(图像标签名称，文件名称)
cv2.imshow('rgb',img_rgb)
cv2.imshow('gray',img_gray)
cv2.imshow('template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()


#res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

#使用matchTemplate对原始灰度图像和图像模板进行匹配
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#设定阈值
threshold = 0.7
#res大于70%
loc = np.where( res >= threshold)

#使用灰度图像中的坐标对原始RGB图像进行标记
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
#显示图像    
cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
