# PaddleFace

## 训练人脸识别模型

```bash
python tools/train.py -c ./ppcls/configs/GeneralRecognitionV2/GeneralRecognitionV2_PPLCNetV2_base.yaml
```

## 模型导出

```bash
python tools/export_model.py -c ./ppcls/configs/GeneralRecognitionV2/GeneralRecognitionV2_PPLCNetV2_base.yaml -o Global.pretrained_model="output/RecModel/best_model"
```

## 获取特征向量

```bash
cd deploy
python python/predict_rec.py  -c configs/inference_rec.yaml  -o Global.rec_inference_model_dir="../inference"
```

## 生成特征库

```bash
cd deploy
python python/build_gallery.py -c configs/inference_rec.yaml

```

## 预测人脸

```bash
python python/predict_system.py  -c configs/inference_rec.yaml  -o Global.rec_inference_model_dir="../inference" -o Global.rec_nms_thresold=0.2
```