import os 
path = "D:\Software files\dg-intern-assign\RESTAPI"
dir_list = os.listdir(path) 
print(dir_list)
for root, subdirectories, files in os.walk(path):
    for subdirectory in subdirectories:
        print(os.path.join(root, subdirectory))
    for file in files:
        print(os.path.join(root, file))