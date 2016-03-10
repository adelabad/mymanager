import os

def check_folder(my_dir):

    directory = os.listdir(my_dir)
    result = []
    for i in range (len(directory)):
        if os.path.isdir(os.path.join(my_dir, directory[i])) and directory[i] != "$RECYCLE.BIN" and directory[i] != "System Volume Information":
            result += [directory[i]]
    return result

def finder(my_dir , name):

    temp = check_folder(my_dir)
    folder = temp
    result = []
    for i in range(len(folder)):
        if name in folder[i]:
            result += [os.path.join(my_dir,folder[i])]
    return "<".join(result)


def search_fd(my_dir, name):
    temp = check_folder(my_dir)
    folder = temp
    if len(folder) == 0:
        return finder(my_dir, name)
    else:
        return finder(my_dir, name) + "<".join([search_fd(os.path.join(my_dir,fold), name) for fold in folder])

def blank_remover(string):
    while "" in string:
        string.remove("")
    return string


#my_dir = raw_input("enter address : ")
#name = raw_input("enter name : ")


def folder_search_all(my_dir, name):
    try:
        temp_result = search_fd(my_dir , name)
        temp_result = temp_result.split("<")
        return blank_remover(temp_result)
    except:
        print "check admin's options in control panel maybe access is denied \nor check your input \nor wrong directory"
