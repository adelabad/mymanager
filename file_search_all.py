import os


def check_with_pattern(name, my_list):
    result = []
    for item in my_list:
        if name in item:
            result.append(item)
    return result


def file_search_all_temp(directory, name):
    result = []
    for root, folders, files in os.walk(directory):
        matches = check_with_pattern(name, files)
        for item in matches:
            result.append(os.path.join(root, item))
            yield result


def file_search_all(directory, name):
    for item in file_search_all_temp(directory, name):
        result = item
    return result



#print file_search_all("d:\\", '123')
