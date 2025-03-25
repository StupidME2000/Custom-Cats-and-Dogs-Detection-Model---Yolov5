# Custom Object Detection with YOLOv5 and Novel Bounding Box Similarity Metric

## Overview
This repository contains a custom object detection pipeline based on YOLOv5, incorporating a novel bounding box similarity metric. The project includes dataset creation, training, evaluation, and a script for custom testing.

## Project Structure
```
├── colab - Notebook/               # Contains Colab notebook and necessary files to run on Google Colab
│   ├── Custom_Object_Detection_YoloV5.ipynb
│   ├── train_val_split.py
│   └── data.zip
│
├── Model/               # Exported model and testing scripts
│   ├── model            # Trained YOLOv5 model
│   ├── model.pt 
│   ├── yolo_detect.py   # Custom script to test on new images
│   ├── test.jpg/        # Sample inference images
│
├── dataset/             # Custom dataset (unlabeled and labeled)
│   ├── Dataset - Unlabled/      # Unlabeled dataset
│   ├── Dataset - labled/    # Dataset labeled using Label Studio
│ 
│
└── README.md            # Project documentation
```

## Getting Started

### Train the Model
Run the Colab notebook to train the model.
1. Open [Custom_Object_Detection_YoloV5.ipynb](https://github.com/StupidME2000/Custom-Cats-and-Dogs-Detection-Model---Yolov5/blob/main/Colab%20-%20Notebook/Custom_Object_Detection_YoloV5.ipynb) in Google Colab.
2. Follow the instructions to train YOLOv5 on the labeled dataset.
3. The best-trained model will be saved as `model.pt`.

## Custom Testing

### 1. Clone the Repository
```bash
git clone https://github.com/StupidME2000/Custom-Cats-and-Dogs-Detection-Model---Yolov5.git
cd Custom-Cats-and-Dogs-Detection-Model---Yolov5
```

### 2. Install Dependencies  

#### For Local Environment:  

1. First, create a Conda environment:  
   ```bash
   conda create --name Yolov5-env1
   conda activate Yolov5-env1
   ```  

2. Navigate to the model folder:  
   ```bash
   cd <path_to_model_folder>
   ```  

3. Install the Ultralytics library:  
   ```bash
   pip install ultralytics
   ```  

4. To test the model:  
   ```bash
   python yolo_detect.py --mode model.pt --source test.jpg
   ```  
   The `yolo_detect.py` script supports various input sources, including:  
   - Live camera feed  
   - Video files  
   - A folder of images  

   You can modify the `--source` parameter accordingly to test different inputs.


## Dataset Preparation
- The dataset consists of manually collected images stored in `dataset/Dataset - Unlabled/`.
- Labels were created using Label Studio and stored in `Dataset - labled/`.

## Novel Bounding Box Similarity Metric
This project introduces a novel similarity metric that enhances traditional IoU by incorporating:
- Geometric factors
- Aspect ratio adjustments
- Distance-based penalties

The metric is implemented within the model evaluation step.

## Results
The trained YOLOv5 model achieves [add performance metrics here] on the custom dataset. Performance is evaluated using:
- mAP (Mean Average Precision)
- Custom bounding box similarity metric

## Future Work
- Improve dataset diversity
- Optimize hyperparameters for better accuracy
- Integrate with real-time inference applications
