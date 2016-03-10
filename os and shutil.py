##############################
#this py is for defining     #
#what we need from os and    #
#shutil (copy move paste     #
#rename remove search engine #
##############################
import os, shutil

#######################
os.rename(src=,dst=)
#######################
os.getcwd()
#######################
os.chdir(path=)
#######################
os.walk(top=)
'''
for (a,b,c) in os.walk("e:\\test"):
    print c
'''
########################
os.removedirs(path=)
########################
os.remove(path=)
########################
os.makedirs(path=)
########################
os.mkdir(path=)
'''def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)'''
########################
os.startfile(filepath=)
########################
shutil.copy(src=,dst=)
########################
shutil.copytree(src=,dst=)
########################
shutil.rmtree(path=)
########################
os.path.join(path=,*path)
########################
shutil.move(src=,dst=)
########################
os.listdir(path=)
########################
os.path.isdir(path=)
########################
os.path.dirname(path=)
########################
os.path.exists(path=)
########################
os.path.isfile(path=)
########################
os.path.split(path=)     #file
########################
os.path.splitext(path=)  #format
#######################
os.path.splitdrive(path=)
#######################