# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 读取label文件
    labelList = []
    labelFile = open("./train.txt")
    line = labelFile.readline()
    i = 0
    while line:
        line = line.replace('.png ', '.png\t')
        line = line.replace('.jpg ', '.jpg\t')
        line = line.replace('.jpeg ', '.jpeg\t')
        labelList.append(line)
        line = labelFile.readline()
    labelFile.close()

    fileName = './train_new.txt'
    with open(fileName, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for item in labelList:
            f.write(item)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
