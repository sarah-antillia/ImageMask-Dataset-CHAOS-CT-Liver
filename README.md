<h2>ImageMask-Dataset-CHAOS-CT-Liver (2024/05/16) </h2>
This is a simple ImageMask Dataset for CHAOS-CT-Liver Image Segmentation.<br>
The original dataset used here has been taken from the following web-site.
<br>
<a href="https://chaos.grand-challenge.org/Download/">
Combined<br>
Healthy<br>
Abdominal<br>
Organ<br>
Segmentation
</a>
<br>
<br>
<b>Image and mask sample</b><br>
<hr>
<table>
<tr>
<th>
Image 
</th>
<th>
Mask
</th>
<th>
Image+Mask
</th>

</tr>

<td>
<img src="./samples/images/101_1012.jpg" width="320" height="auto">
</td>
<td>
<img src="./samples/masks/101_1012.jpg" width="320" height="auto">

</td>
<td>
<img src="./samples/blended/101_1012.jpg" width="320" height="auto">

</td>

</table>
<hr>

<br>
<b>Download CHAOS-CT-Liver-ImageMaskDataset</b><br>
You can download our 512x512 jpg CHAOS-CT-Liver dataset generated here from the google drive 
<a href="https://drive.google.com/file/d/1etFEBSESEUhDIXOroyjSnqK4yGjdaMNU/view?usp=sharing">CT-Liver-ImageMaskDataset-V1.zip</a>.
<br>
<br>
<h3>1. Dataset Citation</h3>
The original dataset used here has been taken from the following web-site.<br>

<b>
<a href="https://chaos.grand-challenge.org/Download/">
 Combined<br> Healthy<br> Abdominal<br> Organ<br> Segmentation<br>
</a>
</b>
<br>

CHAOS dataset can be downloaded via the link below. <br>
<br>
https://doi.org/10.5281/zenodo.3362844<br>
<br>
All participants are considered to have read and accepted the Rules.<br> 
The data is licensed under Attribution-NonCommercial-ShareAlike 4.0 International.<br>  
The data can be downloaded via the link below:<br>
<br>
https://doi.org/10.5281/zenodo.3362844<br>
<br>
In your works, please give appropriate credit, provide 
<a href="https://chaos.grand-challenge.org/Publications/">a link</a> 
to the license, and indicate if changes were made. 
<br>
The citation information can be found in the 
<a href="https://chaos.grand-challenge.org/Publications/"><b>Publications and Citation</b> </a>page.
<br>

<h3>2. Download CHAOS dataset </h3>
If you would like to generate your own dataset by yourself, please download the original CHAOS dataset from 
the following <a href="https://zenodo.org/records/3431873">
CHAOS - Combined (CT-MR) Healthy Abdominal Organ Segmentation Challenge Data
</a>
<br>
Please download 
<a href="https://zenodo.org/records/3431873/files/CHAOS_Train_Sets.zip?download=1">
CHAOS_Train_Sets.zip
</a>
, and expand the downloaded Train_Sets file in your working folder.<br>
 It contains CT and MR datasets as shown below.<br>
<pre>
./Train_Sets
├─CT
└─MR
</pre>
The folder structure of <b>Train_Sets/CT</b> is the following. 
<pre>
./Train_Sets/CT
├─1
│  ├─DICOM_anon
│  └─Ground
├─2
│  ├─DICOM_anon
│  └─Ground
 ...
└─30
    ├─DICOM_anon
    └─Ground
</pre>
Each DICOM_anon of the numbered folder contains a lot of DICOM dcm files files, and Ground corresponding mask png files as shown below.
<pre>
,/DICOM_anon
├─i0000,0000b.dcm
├─i0001,0000b.dcm
├─i0002,0000b.dcm
...
└─i0095,0000b.dcm
</pre>
<pre>
,/Ground
├─liver_GT_000.png
├─liver_GT_001.png
├─liver_GT_002.png
...
└─liver_GT_095.png
</pre>

<h3>3. Generate master dataset </h3>
Please move to <b>ImageMask-Dataset-CHAOS-CT-Liver</b> direcotory, and run the following commnad for Python 
script <a href="./CTImageMaskDatasetGenerator.py">CTImageMaskDatasetGenetator.py</a> to generate
images and masks jgp files.<br>
<pre>
>python CTImageMaskDatasetGenerator.py 
</pre>
, by which <b>CT-Liver-master</b> datatset will be created.<br>
<pre>
./CT-Liver-master
  ├─images
  └─masks
</pre>

<h3>4. Split master dataset </h3>
Please run the following command for Python script <a href="./split_master.py">split_master.py</a>.
<pre>
>python split_master.py
</pre>
, by wich test, train, and valid subdatasets will be created.<br>

<pre>
./CT-Liver-ImageMaskDataset-V1
├─test
│  ├─images
│  └─masks
├─train
│  ├─images
│  └─masks
└─valid
    ├─images
    └─masks
</pre>


<hr>
Train images sample<br>
<img src="./asset/train_images_sample.png" width="1024" height="auto"><br>
Train masks sample<br>
<img src="./asset/train_masks_sample.png" width="1024" height="auto"><br>

<hr>
Validation (Image + Mask)<br>

<img src="./asset/validation.png" width="1024" height="auto"><br>
<br>
Dataset Statistics <br>
<img src ="./CT-Liver-ImageMaskDataset-V1_Statistics.png" width="512" height="auto">
<br>


