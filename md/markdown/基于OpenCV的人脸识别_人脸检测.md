1：==简介==
**人脸检测**指从现实环境中识别出人脸的**位置**；

**人脸识别**基于**人脸检测**，下一步才能辨析人脸的属性，从而判别这个人是谁。

2：==图像基本概念==
**帧**：一张图
**帧数**：一秒钟刷新多少张图片
**分辨率**：单位大小所能承载的像素，能力为正相关
**图像插值**：提高图像分辨率
OpenCV提供了5种插值方法：**最邻近**、**双线性**、基于像素区域、立方插值及兰索斯插值（加粗的两个时间复杂度低）
介绍：引用 [图像插值](https://blog.csdn.net/spw_1201/article/details/53544014)
**灰度图**：**二值图像**的拓展，在黑白两种颜色中取得灰色，黑，白，灰
**人脸ROI**
3：==应用==
用**Haar级联**来做人脸检测。 Haar级联通过在多个尺度上从图像中提取大量的简单特征来实现。
简单特征主要指边、线、矩形特征等，这些特征都非常易于计算，
然后通过创建一系列简单的分类器来做训练。
这里需要一个cascade_files去训练model。

先去我的Github取到需要的模型训练的.xml文件即cascade_file，下载到python脚本的文件夹下，下面的人脸检测及五官检测代码就直接可以运行了。
如果想看其他方面的人脸识别源码，请移步我的Github。

==https://github.com/shaojintian/Face_detection/tree/master==

```python 
#face_nose&eyes_detection.py
import cv2
import numpy as np

#import Haar files to train face detection model 

face_cascade=cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')
nose_cascade=cv2.CascadeClassifier('cascade_files/haarcascade_mcs_nose.xml')
eye_cascade=cv2.CascadeClassifier('cascade_files/haarcascade_eye.xml')
# check whether haar is done 
if face_cascade.empty():
	raise IOError('Unable to load haarcascade_frontalface_alt')
if nose_cascade.empty():
	raise IOError('Unable to load haarcascade_mcs_nose.xml')
if eye_cascade.empty():
	raise IOError('Unable to load haarcascade_eye.xml')	
# initialize camera from PC camera 
# parameter 0 -> PC camera
camera=cv2.VideoCapture(0)

#image clearity scale 

scale_image=0.6


# infinite circle to capture images 

while True:
	#capture current image
	#frame->帧
	ret,frame=camera.read()
	#每次都调整一下帧的大小
	#interpolation（插值法）：最近邻时间复杂度最小
	frame=cv2.resize(frame,None,fx=scale_image,fy=scale_image,
					interpolation=cv2.INTER_NEAREST)
	#将图像转为灰度图
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	#灰度图像上运行人脸检测器->人脸矩形框
		#1.5->乘积系数，5->最小紧邻数量	
	face_rects=face_cascade.detectMultiScale(gray,1.5,5)
	


	#画出人脸矩形框 
	#nose ,eyes in face_rects
	#3->框的厚度
	for(x,y,w,h) in face_rects:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,128,0),2)
		#require face ROI information
		roi_gray=gray[y:y+h,x:x+w]
		roi_color=frame[y:y+h,x:x+w]

		eye_rects=eye_cascade.detectMultiScale(roi_gray)
		nose_rects=nose_cascade.detectMultiScale(roi_gray)
		#draw eye  and nose rectangle
		for(x_eye,y_eye,w_eye,h_eye) in eye_rects:
			center=(int(x_eye+0.5*w_eye),int(y_eye+0.5*h_eye))
			radius=int(0.3*(w_eye+h_eye))
			color=(0,255,255)
			thickness=2
			cv2.circle(roi_color,center,radius,color,thickness)
		for(x_nose,y_nose,w_nose,h_nose) in nose_rects:
			center=(int(x_nose+0.5*w_nose),int(y_nose+0.5*h_nose))
			radius=int(0.3*(w_nose+h_nose))
			color=(0,255,255)
			thickness=2
			cv2.circle(roi_color,center,radius,color,thickness)
			break


	#显示帧
	cv2.namedWindow('SJT_cam',0)#0->auto size window
	cv2.imshow('SJT_cam',frame)

	# 通过esc退出
	#wait 1ms to check key response
	key=cv2.waitKey(1)
	if key==27:#27==ESC
		break;
#释放摄像头
camera.release()
#关闭所有窗体
cv2.destroyAllWindows()



```









![在这里插入图片描述](https://img-blog.csdnimg.cn/20181128022321986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
