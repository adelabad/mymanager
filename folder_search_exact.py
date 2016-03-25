import os


def check_with_pattern(name, my_list):
    result = []
    for item in my_list:
        if name == item:
            result.append(item)
    return result


def folder_search_exact(directory, name):
    result = []
    for root, folders, files in os.walk(directory):
        matches = check_with_pattern(name, folders)
        for item in matches:
            result.append(os.path.join(root, item))
    return result

#print folder_search_exact("e:\\", 'aso')
