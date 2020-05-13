#The python script for capturing the screenshot and the corresponding mouse pointer coordinates
#This code can be functionalised and the no of lines can be decreased

#Reference https://docs.microsoft.com/en-us/windows/win32/uxguide/inter-mouse
import pyautogui, sys
from PIL import ImageGrab
from PIL import Image
import os
import cv2
import random
import win32gui
import ctypes
ctypes.windll.user32.SetProcessDPIAware() # for DPI scaling
print('Press Ctrl-C to quit.')
import time

try:
    print("Ready....3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    
    count = 0
    t = time.localtime()
    current_time = 400#time.strftime("%Y-%m-%d-%H-%M-%S", t)***********************change here for the directory
    os.mkdir('./data_fixed/frames_dir/'+str(current_time))#creating the directory
    os.chdir('./data_fixed/frames_dir/'+str(current_time))#changingh the directory
    # file1 = open("activeRegion.txt",'w')
    file1 = open(str(current_time)+".txt",'w')
    selectCursor = Image.open('../../../icons/select_text.png')#open png file
    pointerCursor = Image.open('../../../icons/pointer.png')#open png file
    fingerCursor = Image.open('../../../icons/clicker - Copy.png').convert('RGBA')#open png file
    while True:
        count = count+1#the name of the image will be the count
        flags, hcursor, (x,y) = win32gui.GetCursorInfo()

        if(hcursor == 65539):#for the case of pointercursor
            print("the infos are:",flags,hcursor,(x,y))
            curX,curY = pyautogui.position()#get the cursor x,y position
            im = pyautogui.screenshot(region=(0,66,1366,662))#take the screenshot
            file1.write(str(curX)+','+str(curY)+','+str(20)+','+str(20)+'\n')#write into coordinates to the file
            im.paste(pointerCursor,box=(curX,curY-66),mask=pointerCursor)#paste the mask onto the screenshot
            im.save('frame_'+str(count)+'.png')#save the screenshot

            # img = cv2.imread('frame_'+str(count)+'.png')
            # cv2.rectangle(img,(curX,curY-66),(curX+20,curY+20-66),(255,0,0),2)
            # cv2.imwrite('frame_'+str(count)+'.png',img)
        elif(hcursor == 65541):#for the case of selectcursor
            print("the infos are:",flags,hcursor,(x,y))
            curX,curY = pyautogui.position()#get the cursor x,y position
            im = pyautogui.screenshot(region=(0,66,1366,662))#take the screenshot
            file1.write(str(curX)+','+str(curY)+','+str(20)+','+str(20)+'\n')#write into coordinates to the file
            im.paste(selectCursor,box=(curX,curY-66),mask=selectCursor)#paste the mask onto the screenshot
            im.save('frame_'+str(count)+'.png')#save the screenshot

            # img = cv2.imread('frame_'+str(count)+'.png')
            # cv2.rectangle(img,(curX,curY-66),(curX+20,curY+20-66),(255,0,0),2)
            # cv2.imwrite('frame_'+str(count)+'.png',img)
        elif(hcursor == 65567):
            print("the infos are:",flags,hcursor,(x,y))
            curX,curY = pyautogui.position()#get the cursor x,y position
            im = pyautogui.screenshot(region=(0,66,1366,662))#take the screenshot
            file1.write(str(curX)+','+str(curY)+','+str(20)+','+str(20)+'\n')#write into coordinates to the file
            im.paste(fingerCursor,box=(curX,curY-66),mask=fingerCursor)#paste the mask onto the screenshot
            im.save('frame_'+str(count)+'.png')#save the screenshot

            # img = cv2.imread('frame_'+str(count)+'.png')
            # cv2.rectangle(img,(curX,curY-66),(curX+20,curY+20-66),(255,0,0),2)
            # cv2.imwrite('frame_'+str(count)+'.png',img)
except KeyboardInterrupt:
    print('keyboard interrupted and the file is closed and the screenshot is also saved and the final count is!!',count)
    im.save('frame_'+str(count)+'.png')#save the screenshot
    file1.close()

