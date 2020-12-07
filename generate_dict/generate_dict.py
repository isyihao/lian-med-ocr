# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 读取label文件
    dictMap = {}
    labelFile = open("./train.txt")
    line = labelFile.readline()
    i = 0
    while line:
        line = line.replace('.png ', '.png\t')
        line = line.replace('.jpg ', '.jpg\t')
        line = line.replace('.jpeg ', '.jpeg\t')
        strs = str.split(line, '\t')
        if len(strs) > 1:
            for char in strs[1]:
                if not (char in dictMap):
                    dictMap[char] = True
            i = i + 1
        line = labelFile.readline()
    labelFile.close()

    # 读取lian-med-dict
    labelFile = open("./lian-med-dict.txt")
    line = labelFile.readline()
    while line:
        line = line.replace('\n', '')
        if not (line in dictMap):
            dictMap[line] = True
        line = labelFile.readline()
    labelFile.close()

    fileName = 'dict.txt'
    with open(fileName, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        dictMapSorted = sorted(dictMap.keys())
        for item in dictMapSorted:
            content = item + '\n'
            f.write(content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
