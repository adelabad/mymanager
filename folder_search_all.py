import os


def check_with_pattern(name, my_list):
    result = []
    for item in my_list:
        if name in item:
            result.append(item)
    return result


def folder_search_all(directory, name):
    result = []
    for root, folders, files in os.walk(directory):
        matches = check_with_pattern(name, folders)
        for item in matches:
            
            result.append(os.path.join(root, item))
    return result

#print folder_search_all("d:\\", 'New')
