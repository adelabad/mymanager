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


def operator(self, op, *args):


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
            file_search_all.file_search_all(args[0],args[1])
        except:
            print "unable to operate"


    if op == "file_search_exact":
        try:
            file_search_exact.file_search_exact(args[0],args[1])
        except:
            print "unable to operate"


    if op == "folder_search_all":
        try:
            folder_search_all.folder_search_all(args[0],args[1])
        except:
            print "unable to operate"


    if op == "folder_search_exact":
        try:
            folder_search_exact.folder_search_exact(args[0],args[1])
        except:
            print "unable to operate"

