import os

def ensure_models_dir():
    if not os.path.isdir('models'):
        os.makedirs('models')
        print("Created 'models' directory. Please add your model files (haarcascade and yolov5 weights).")