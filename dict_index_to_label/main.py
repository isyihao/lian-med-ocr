# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 读取字典文件
    dictStrList = []
    dictFile = open("dict.txt")
    line = dictFile.readline()
    while line:
        line = line.replace("\n", '')
        dictStrList.append(line)
        line = dictFile.readline()
    dictFile.close()

    # 读取label文件
    labelStrList = []
    labelFile = open("data_train.txt")
    line = labelFile.readline()
    while line:
        strs = str.split(line, ' ')
        if len(strs) > 1:
            resultStr = strs[0] + '\t'
            for i in range(1, len(strs) - 1):
                resultStr = resultStr + dictStrList[int(strs[i])]
            labelStrList.append(resultStr)
        line = labelFile.readline()
    dictFile.close()

    fileName = 'train.txt'
    with open(fileName, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for item in labelStrList:
            item = item + '\n'
            f.write(item)
            print('writing %s ' % item)
    f.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
