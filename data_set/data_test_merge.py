# 拆分数据集
import os
import shutil
import random

in_img_path = '/data/PaddleOCR/data_set/after_merge_train/images'    # 图片路径
in_txt_path = '/data/PaddleOCR/data_set/after_merge_train/train.txt'  # train.txt路径
out_path =    '/data/PaddleOCR/data_set/after_merge_test'      #生成的文件夹路径

def create_files(in_img_path,in_txt_path,out_img_Path,out_txt_path):
    i = 0
    k = 100000 #拆分数量
    with open(in_txt_path,'r', encoding="utf-8") as file: # 按行读取全部
        lines = file.read().splitlines()
    random_lines = random.sample(lines, k) # 随机读取
    # 重新写入原文件
    with open(in_txt_path, 'w', encoding="utf-8") as output_train_file:
        output_train_file.writelines(line + "\n"
                                for line in lines if line not in random_lines)
    #写入test文件
    with open(out_txt_path, 'w', encoding="utf-8") as output_test_file:
        output_test_file.writelines(random_line + "\n"
                                for random_line in random_lines)
    # 获取图片名
    in_img_list = os.listdir(in_img_path)
    # 移动
    for random_line in random_lines:
        random_img_name = random_line.split('\t')[0]
        for in_img_name in in_img_list:
            if random_img_name == in_img_name:
                shutil.move(in_img_path + '/' + in_img_name, out_img_Path)
                i = i + 1
                print("当前移动" + str(i) + "个图片")
            else:
                continue

if __name__ == '__main__':
    # 不存在则创建
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    out_img_Path = out_path+'/images'      # 将找到的图片放到该路径里
    out_txt_path = out_path+'/test.txt'  # 将找到的txt文件放到该文件里
    # 不存在则创建目录
    if not os.path.exists(out_img_Path):
        os.mkdir(out_img_Path)
    # 不存在则创建文件
    if not os.path.exists(out_txt_path):
        os.system(r"touch {}".format(out_txt_path))
    create_files(in_img_path,in_txt_path,out_img_Path,out_txt_path)