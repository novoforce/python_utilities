import os,sys
change = '/data_fixed/frames_dir/40/'
os.chdir(os.getcwd()+change)
print("The dir is ",os.getcwd())

file_to_be_modified = open('actionRegion.txt','r') #file is opened in rad/write mode
# file_to_be_modified = file_to_be_modified.read()
file_second = open('activeRegion2.txt','w')


for line in file_to_be_modified:
    print('the line IS',line)
    li = line.split(',')
    li[1] = int(li[1]) - 66
    print(li)
    file_second.write(str(li[0])+',')
    file_second.write(str(li[1])+',')
    file_second.write(str(li[2])+',')
    file_second.write(str(li[3]))

file_to_be_modified.close()
file_second.close()
