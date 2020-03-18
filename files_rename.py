import os
import glob

print("THE CURRENT WORKING DIR IS:",os.getcwd())
cwd = os.getcwd()# current working directory

os.chdir(cwd + '/data_fixed/frames_dir/')

cwd = os.getcwd()+'\\'# current working directory
print('*******************',cwd)
start_file_name = 1 # since file names are the numerical values
end_file_name = 40

while start_file_name <= end_file_name:
    
    os.chdir(cwd +str(start_file_name))# inside the frame folder
    print(os.listdir(os.getcwd())[0])

    os.rename(os.listdir(os.getcwd())[0],'actionRegion.txt')

    start_file_name+=1#INCREMENT THE START
print("RENAME DONE")






