# ecoding=utf-8
ifn = r"medical_words_18000+.txt"
ofn = r"medical_words_18000.txt"

infile = open(ifn, 'r', encoding="utf-8")
outfile = open(ofn, 'a', encoding="utf-8")

for eachline in infile.readlines():
    # 去掉文本行里面的空格、\t、数字（其他有要去除的也可以放到' \t1234567890'里面）
    lines = filter(lambda ch: ch not in ' \t1234567890', eachline)
    outfile.write(''.join(lines))  # 写入train_output.txt(此处是一股脑的全写进去，并没有做任何的分行处理)

infile.close
outfile.close
