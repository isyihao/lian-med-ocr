import os

# 标签文件所在路径
label_files_path = "./labels"
# 字典文件所在路径
dict_files_path = "./dicts"

if __name__ == '__main__':

    dictMap = {}
    dictList = []

    dict_file_names = os.listdir(dict_files_path)
    for dict_file_name in dict_file_names:
        if not os.path.isdir(dict_file_name):
            dict_file = open(dict_files_path + "/" + dict_file_name)
            line = dict_file.readline()
            while line:
                line = line.replace('\n', '')
                dictList.append(line)
                if not (line in dictMap):
                    dictMap[line] = True
                line = dict_file.readline()
            dict_file.close()
            print(dict_file_name + ' is ok!')

    label_file_names = os.listdir(label_files_path)
    for label_file_name in label_file_names:
        if not os.path.isdir(label_file_name):
            label_file = open(label_files_path + "/" + label_file_name)
            line = label_file.readline()
            i = 0
            while line:
                strings = str.split(line, '\t')
                if len(strings) > 1:
                    for char in strings[1]:
                        if not (char in dictMap):
                            dictList.append(char)
                            dictMap[char] = True
                    i = i + 1
                line = label_file.readline()
            label_file.close()
            print(label_file_name + ' is ok!')

    fileName = 'dict.txt'
    with open(fileName, 'w') as f:
        # dictMapSorted = sorted(dictMap.keys())
        for item in dictList:
            content = item + '\n'
            f.write(content)
