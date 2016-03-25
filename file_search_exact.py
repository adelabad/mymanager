import os


def check_with_pattern(name, my_list):
    result = []
    for item in my_list:
        if name == item:
            result.append(item)
    return result


def file_search_exact(directory, name):
    result = []
    for root, folders, files in os.walk(directory):
        matches = check_with_pattern(name, files)
        for item in matches:
            result.append(os.path.join(root, item))
    return result

#print file_search_exact("d:\\", '123.txt')
