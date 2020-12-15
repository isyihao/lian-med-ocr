统计当前目录下文件的个数（不包括目录）
$ ls -l | grep "^-" | wc -l
统计当前目录下文件的个数（包括子目录）
$ ls -lR| grep "^-" | wc -l
查看某目录下文件夹(目录)的个数（包括子目录）
$ ls -lR | grep "^d" | wc -l


# 训练
rm -rf /data/PaddleOCR/train_log/1209_1000.log
python3 tools/train.py \
-c configs/rec/rec_chinese_lite_train_v1.1.yml \
-o Global.character_dict_path=./ppocr/utils/dict.txt \
Global.save_model_dir=./output/1215_1830/ \
>/data/PaddleOCR/train_log/1215_1830.log 2>&1 &

tail -n 20 /data/PaddleOCR/train_log/1215_1830.log

Global.pretrain_weights=./pretrain_models/ch_ppocr_mobile_v1.1_rec_pre/best_accuracy \

# 杀死所有python3进程
pkill -9f python3


# 模型转换
python3 tools/export_model.py \
-c configs/rec/rec_chinese_lite_train_v1.1.yml \
-o Global.checkpoints=./output/1208_1700/best_accuracy \
Global.save_inference_dir=./inference/1208_1700

# 超轻量手机端识别预训练模型
wget https://paddleocr.bj.bcebos.com/20-09-22/cls/ch_ppocr_mobile_v1.1_cls_train.tar && tar xf ch_ppocr_mobile_v1.1_cls_train.tar
wget https://paddleocr.bj.bcebos.com/20-09-22/mobile/det/ch_ppocr_mobile_v1.1_det_train.tar && tar xf ch_ppocr_mobile_v1.1_det_train.tar
wget https://paddleocr.bj.bcebos.com/20-09-22/mobile/rec/ch_ppocr_mobile_v1.1_rec_pre.tar && tar xf ch_ppocr_mobile_v1.1_rec_pre.tar


wget https://paddleocr.bj.bcebos.com/20-09-22/server/det/ch_ppocr_server_v1.1_det_train.tar && tar xf ch_ppocr_server_v1.1_det_train.tar

wget https://paddleocr.bj.bcebos.com/20-09-22/server/rec/ch_ppocr_server_v1.1_rec_pre.tar && tar xf ch_ppocr_server_v1.1_rec_pre.tar

# 预测image_dir指定的单张图像
python3 tools/infer/predict_system.py \
--image_dir="./doc/med/raw_1.1.jpeg" \
--det_model_dir="./inference/ch_ppocr_server_v1.1_det_infer/"  \
--rec_model_dir="./inference/ch_ppocr_server_v1.1_rec_infer/" \
--cls_model_dir="./inference/ch_ppocr_server_v1.1_cls_infer/" \
--rec_char_dict_path="ppocr/utils/dict.txt" \
--use_angle_cls=False \
--use_space_char=True

