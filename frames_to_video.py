import cv2
import numpy as np
import glob
import re

path = 'C:/Users/as20052058/Desktop/goturn_data/data_fixed/frames_dir/5/'

img_array = []
for filename in glob.glob(path+'*.png'):
    img_array.append(filename)

nums = [] #here the file number names will be stored
for each in img_array:
    img = each.split('\\')
    img = img[1].split('.')
    img = img[0].split('_')
    nums.append(int(img[1]))

nums.sort()

sorted_nums =[]
for each in nums:
    img_file = path+'frame_'+str(each)+'.png'
    # print(img_file)
    img = cv2.imread(img_file)
    # print("the image is read",img)
    height,width,layers = img.shape
    size = (width,height)
    # print(size)
    sorted_nums.append(img)
out = cv2.VideoWriter(path+'frame_video1.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
 
for i in range(len(img_array)):
    out.write(sorted_nums[i])
print("The video is created from the frames")
out.release()