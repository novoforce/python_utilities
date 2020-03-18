import cv2,os

def FrameCapture(vid_file):

    vidObj = cv2.VideoCapture(vid_file)

    count = 1
    success = 1

    os.chdir('C:/Users/as20052058/Desktop/goturn_data/data_fixed/frames_dir/test/')
    print("THE DIRECTORY IS CHANGED")
    while success:
        success, image = vidObj.read()
        if not success:
            break
        cv2.imwrite("frame%d.jpg" % count, image) 
        count += 1



if __name__ =='__main__':

    vid_file = 'C:/Users/as20052058/Desktop/goturn_data/data_fixed/frames_dir/5/frame_video1.avi'
    print("THE VIDEO IS FED")

    FrameCapture(vid_file)
    print("THE VIDEO IS CONVERTED TO FRAMES")