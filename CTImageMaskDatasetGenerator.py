# Copyright 2024 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# CTImageMaskDatasetGenerator.py

import os
import cv2
import sys
import shutil
import numpy as np
import glob
import pydicom
from PIL import Image, ImageOps
import traceback

class CTImageMaskDatasetGenerator:
  def __init__(self, input_dir="./CT", output_dir ="./Liver-master/"):
    self.input_dir = input_dir

    self.output_dir = output_dir
    if os.path.exists(self.output_dir):
      shutil.rmtree(self.output_dir)
    if not os.path.exists(self.output_dir):
      os.makedirs(self.output_dir)

    self.output_images_dir = self.output_dir + "/images"
    self.output_masks_dir  = self.output_dir + "/masks"
    
    os.makedirs(self.output_images_dir)
    os.makedirs(self.output_masks_dir)
  
    # normalization parameter
    self.normalize  = 28

    # sharpening parameters
    self.brightness = 1.4
    self.contrast   = 4.0

  def generate(self):
    subdirs = os.listdir(self.input_dir)
    subdir_index = 100
    for subdir in subdirs:
      subdir_path = os.path.join(self.input_dir, subdir)
      subdir_index += 1
      self.create_image_files(subdir_index, input_dir=subdir_path, output_dir=self.output_images_dir )
      self.create_mask_files(subdir_index, input_dir=subdir_path, output_dir=self.output_masks_dir)

  def create_image_files(self, subdir_index, input_dir="./CT/1", output_dir="./Liver-master/images/"):
    pattern   = input_dir + "/DICOM_anon/*.dcm"
    dcm_files = glob.glob(pattern)
    dcm_files = sorted(dcm_files)
    index = 1000
    for dcm_file in dcm_files:
      file = pydicom.dcmread(dcm_file)
      img = file.pixel_array / self.normalize
      img = self.sharpen(img)
 
      image = Image.fromarray(img)
      image = image.convert("RGB")
      index += 1
      filename = str(subdir_index) + "_" + str(index) + ".jpg"
      output_filepath = os.path.join(output_dir, filename)
      image.save(output_filepath)
      print("--- Saved {}".format(output_filepath))

  def create_mask_files(self, subdir_index, input_dir="./CT/1", output_dir="./Liver-master/masks/"):
    pattern = input_dir + "/Ground/*.png"
    mask_files = glob.glob(pattern)
    mask_files = sorted(mask_files)
    index = 1000
    for mask_file in mask_files:
      image = Image.open(mask_file)
      image = image.convert("L")
      index += 1
      filename = str(subdir_index) + "_" + str(index) + ".jpg"
      output_filepath = os.path.join(output_dir, filename)
      image.save(output_filepath)
      print("--- Saved {}".format(output_filepath))

  def sharpen(self, image):
    base  = np.zeros(image.shape, image.dtype)
    image = cv2.addWeighted(image, self.contrast, base, 0, self.brightness) 
    return image


if __name__ == "__main__":
  try:
    input_dir  = "./Train_Sets/CT"
    output_dir = "./CT-Liver-master"

    generator = CTImageMaskDatasetGenerator(input_dir=input_dir, output_dir=output_dir)
    generator.generate()

  except:
    traceback.print_exc()
