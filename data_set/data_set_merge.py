# 合并数据集
import os
import shutil

in_path = 'F:/OCR/PaddleOCR/before_merge'  #需要复制的文件夹路径
out_path = 'F:/OCR/PaddleOCR/after_merge'      #生成的文件夹路径

def get_files(inPath,out_img_Path,out_txt_path):
    i = 0
    for filepath,dirnames,filenames in os.walk(inPath):   #在多级目录下找文件
        for filename in filenames:
            #str1 = filename.split('.')[0]
            str1_1 = filename.split('.')[1]
            if filename == "train.txt":
                f = open(filepath + '/' + filename, "r", encoding="utf-8")
                g = open(out_txt_path, "a", encoding="utf-8")
                for line in f.readlines():
                    g.write(line)
                #g.write("\n")
                g.close()
            elif str1_1 == "jpg" or str1_1 == "jpeg" or str1_1 == "JPG" or str1_1 == "JPEG" or str1_1 == "png" or str1_1 == "PNG":
                shutil.copy(filepath + '/' + filename, out_img_Path)
                i = i + 1
                print("当前完成" + str(i) + "个图片")
            else:
                continue
if __name__ == '__main__':
    # 不存在则创建
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    out_img_Path = out_path+'/images'      # 将找到的图片放到该路径里
    out_txt_path = out_path+'/train.txt'  # 将找到的txt文件放到该文件里
    # 不存在则创建目录
    if not os.path.exists(out_img_Path):
        os.mkdir(out_img_Path)
    # 不存在则创建文件
    if not os.path.exists(out_txt_path):
        os.system(r"touch {}".format(out_txt_path))
    get_files(in_path,out_img_Path,out_txt_path)