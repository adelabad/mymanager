##############################
#this py is for operating and#
#what we need from os and    #
#shutil (copy move paste     #
#rename remove search engine #
##############################
import os
import shutil
import file_search_all
import file_search_exact
import folder_search_all
import folder_search_exact


def operator(op, *args):


    if op == "rename":
        try:
            os.rename(args[0], args[1])
        except:
            print "couldn't find the file"


    if op == "getcwd":
        try:
            return os.getcwd()
        except:
            print "unable to operate"


    if op == "change_dir":
        try:
            os.chdir(args[0])
        except:
            print "unable to operate"


    if op == "remove_fd":
        try:
            os.removedirs(args[0])
        except:
            print "please check address"


    if op == "remove_file":
        try:
            os.remove(args[0])
        except:
            print "can't remove . please check the file"


    if op == "new_fd":
        try:
            if not os.path.exists(args[0]):
                os.makedirs(args[0])
            else:
                print "please change folder's name"
        except:
            print "cannot create folder"



    if op == "new_folder":
        try:
            if not os.path.exists(args[0]):
                os.mkdir(args[0])
            else:
                print "please change folder's name"
        except:
            print "cannot create folder"


    if op == "run":
        try:
            os.startfile(args[0])
        except:
            print "couldn't run the file"


    if op == "copy_file":
        try:
            shutil.copy(args[0], args[1])
        except:
            print "couldn't copy the file"


    if op == "copy_folder":
        try:
            shutil.copytree(args[0], args[1])
        except:
            print "couldn't copy the folder"


    if op == "remove_folder":
        try:
            shutil.rmtree(args[0])
        except:
            print "couldn't remove the folder"


    if op == "move":
       try:
            shutil.move(args[0], args[1])
       except:
           print "couldn't move the file"


    if op == "check_dir":
        try:
            return os.path.isdir(args[0])
        except:
            print "unable to operate"


    if op == "check_path":
        try:
            return os.path.exists(args[0])
        except:
            print "unable to operate"


    if op == "check_file":
        try:
            return os.path.isfile(args[0])
        except:
            print "unable to operate"


    if op == "file_search_all":
        try:
            return file_search_all.file_search_all(args[0],args[1])
        except:
            print "unable to operate"


    if op == "file_search_exact":
        try:
            return file_search_exact.file_search_exact(args[0],args[1])
        except:
            print "unable to operate"


    if op == "folder_search_all":
        try:
            return folder_search_all.folder_search_all(args[0],args[1])
        except:
            print "unable to operate"


    if op == "folder_search_exact":
        try:
            return folder_search_exact.folder_search_exact(args[0],args[1])
        except:
            print "unable to operate"


    if op == "file_size":
        try:
            return str(os.path.getsize(args[0]))
        except:
            print "couldn't find the file"


    if op == "folder_size":
        try:
            return str(len(os.listdir(args[0])))
        except:
            print "couldn't find such directory"


    if op == "drive_name":
        try:
            return os.path.splitdrive(args[0])[0]
        except:
            print "couldn't operate"


    if op == "address_split":
        try:
            return os.path.split(args[0])
        except:
            print "couldn't operate"


    if op == "file_format":
        try:
            return os.path.splitext(args[0])[1]
        except:
            print "couldn't operate"


    if op == "cmd":
        try:
            if args[0] == "":
                os.chdir("c:\\")
                os.system('start')
            else:
                os.chdir(args[0])
                os.system('start')
        except:
            os.chdir("c:\\")
            os.system('start')


    if op == "control_panel":
        try:
            os.system("control panel")
        except:
            print "couldn't operate"


    if op == "desktop_adr":
        try:
            return os.path.expanduser("~")+"\Desktop"
        except:
            print "couldn't"



    #this will be updated
