# Custom Object Detection with YOLOv5 and Novel Bounding Box Similarity Metric

## Overview
This repository contains a custom object detection pipeline based on YOLOv5, incorporating a novel bounding box similarity metric. The project includes dataset creation, training, evaluation, and a script for custom testing.

## Project Structure
```
├── colab - Notebook/               # Contains Colab notebook and necessary files to run on Google Colab
│   ├── Assesment_YoloV5.ipynb
│   ├── train_val_split.py
│   └── data.zip
│
├── model/               # Exported model and testing scripts
│   ├── model            # Trained YOLOv5 model
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

### 1. Train the Model
Run the Colab notebook to train the model.
1. Open `colab/object_detection_notebook.ipynb` in Google Colab.
2. Follow the instructions to train YOLOv5 on the labeled dataset.
3. The best-trained model will be saved as `best_model.pt`.






### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies
For Colab:
```bash
pip install -r colab/requirements.txt
```
For Local Environment:
```bash
pip install torch torchvision numpy opencv-python label-studio
```

### 3. Train the Model
Run the Colab notebook to train the model.
1. Open `colab/object_detection_notebook.ipynb` in Google Colab.
2. Follow the instructions to train YOLOv5 on the labeled dataset.
3. The best-trained model will be saved as `best_model.pt`.

### 4. Custom Testing
Use the provided script to test the model on new images:
```bash
python model/test_script.py --image path/to/image.jpg
```
Results will be saved in the `inference/` folder.

## Dataset Preparation
- The dataset consists of manually collected images stored in `dataset/raw_images/`.
- Labels were created using Label Studio and stored in `dataset/labeled_data/`.
- Annotations are converted into YOLO format and stored in `dataset/annotations/`.

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

## Contributing
Feel free to fork this repository and submit pull requests for improvements or fixes.

## License
This project is licensed under the MIT License.

---

### Contact
For any questions or collaboration inquiries, reach out via [your email or GitHub profile].

