import numpy
import cv2
from scipy import ndimage

#采用高斯模糊的方法，高斯模糊即对每个3*3的像素点矩阵进行求平均值从而达到模糊但不失真的效果#


def blur(image, districts, scale):
	if(len(image.shape)!=3):
		print("error")
		exit(0)
		
	new_image = image.copy()        #对图片进行复制再进行修改#
	
	for district in districts:
		new_image = gauss_blur(new_image, district, scale)
		
	return new_image


def gauss_blur(image, district, scale):
	if(image.shape[0] < district[0] + district[2] or image.shape[1] < district[1] + district[3]):
		print("error district")
		exit(1)
	
        #这是高斯模糊的一个标准矩阵#
	gaussian = numpy.array([[1,2,1],
							[2,4,2],
							[1,2,1]]) * 1.0/16
	
	new_image = image.copy()
	#对图片上每个像素点和高斯矩阵进行卷积，卷积次数越高越模糊#
	for r in range(scale):
		for i in range(3):
			new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i] = ndimage.convolve(new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i], gaussian)
	return new_image
	

def blur_version2(image, districts, scale):
	if(len(image.shape)!=3):
		print("error")
		exit(0)
		
	new_image = image.copy()
	
	for district in districts:
		new_image = gauss_blur_version2(new_image, district, scale)
		
	return new_image


def gauss_blur_version2(image, district, scale):
	if(image.shape[0] < district[0] + district[2] or image.shape[1] < district[1] + district[3]):
		print("error district")
		exit(1)
	
        #这里尝试去修改高斯的矩阵观察效果#
	gaussian = numpy.array([[1,2,1],
							[2,100,2],
							[1,2,1]]) * 1.0/112
	
	new_image = image.copy()
	for r in range(scale):
		for i in range(3):
			new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i] = ndimage.convolve(new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i], gaussian)
	return new_image
