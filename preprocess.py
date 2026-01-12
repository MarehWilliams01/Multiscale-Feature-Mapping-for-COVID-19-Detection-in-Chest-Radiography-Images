import os
import shutil
import random
from PIL import Image

# Set the path to your dataset and create new folders for train and test
original_dataset_dir = r'E:\all_images'  # Path where original dataset is located
new_base_dir = r'E:\all_images_preprocessed'  # Path where new train/test folders will be created

train_dir = os.path.join(new_base_dir, 'train')
test_dir = os.path.join(new_base_dir, 'test')

# Create train and test directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Set the desired image size
target_size = (224, 224)

# Iterate over each class (assuming you have two classes)
classes = os.listdir(original_dataset_dir)  # The folder names represent class names

for class_name in classes:
    # Paths for class in train and test directories
    train_class_dir = os.path.join(train_dir, class_name)
    test_class_dir = os.path.join(test_dir, class_name)
    
    # Create class subdirectories if they don't exist
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)
    
    # List all images in the class directory
    class_dir = os.path.join(original_dataset_dir, class_name)
    images = os.listdir(class_dir)
    
    # Shuffle the images randomly to split them
    random.shuffle(images)
    
    # Calculate 90% for train and 10% for test
    split_idx = int(0.9 * len(images))
    
    train_images = images[:split_idx]
    test_images = images[split_idx:]
    
    # Copy and resize images for training set
    for image_name in train_images:
        src_path = os.path.join(class_dir, image_name)
        dst_path = os.path.join(train_class_dir, image_name)
        
        # Open and resize the image
        with Image.open(src_path) as img:
            img = img.resize(target_size)
            img.save(dst_path)  # Save resized image to the train folder
    
    # Copy and resize images for testing set
    for image_name in test_images:
        src_path = os.path.join(class_dir, image_name)
        dst_path = os.path.join(test_class_dir, image_name)
        
        # Open and resize the image
        with Image.open(src_path) as img:
            img = img.resize(target_size)
            img.save(dst_path)  # Save resized image to the test folder

print(f"Images processed and saved in '{train_dir}' and '{test_dir}'")
