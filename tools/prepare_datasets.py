#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : prepare_datasets.py
# @Author   : jade
# @Date     : 2023/6/5 9:39
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
import os
import shutil

from jade import *


def select_person(count,root_dir,new_dir):
    new_dir = new_dir + "_" + str(count)
    CreateSavePath(new_dir)
    CreateSavePath(os.path.join(new_dir,"images"))
    with open(os.path.join(new_dir,"label.txt"),"wb") as f1:
        with open(os.path.join(root_dir,"label.txt")) as f:
            content_list = f.readlines()
            for content in content_list:
                image_path = os.path.join(root_dir,content.split("\t")[0])
                person_id = int(content.split("\t")[1].strip())
                if person_id < count:
                    f1.write("{}\t{}\n".format(image_path,person_id).encode("utf-8"))
                    shutil.copy(image_path,os.path.join(new_dir,"images"))
                else:
                    break


#
# if __name__ == '__main__':
#     select_person(1000,r"F:\MS1M_v2","F:\数据集\人脸识别数据集/face_datasets")