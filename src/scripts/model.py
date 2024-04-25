import pandas as pd
import tensorflow as tf


# Load the text files containing image names for training/validation and testing
with open('../../documentation/train_val_list.txt', 'r', encoding='utf-8') as file:
    train_val_images = file.read().splitlines()

with open('../../documentation/test_list.txt', 'r', encoding='utf-8') as file:
    test_images = file.read().splitlines()

# Load df_labels DataFrame containing image file names and metadata
df_labels = pd.read_csv('../../data/df_labels.csv')

# Filter df_labels based on the images in train_val_images and test_images
train_val_df = df_labels[df_labels['index'].isin(train_val_images)]
test_df = df_labels[df_labels['index'].isin(test_images)]

# Define image file paths for training/validation and testing sets
train_val_image_paths = ['../../data//images/' +
                            filename for filename in train_val_df['index'].tolist()]

test_image_paths = ['../../data/images/' + filename for filename in test_df['index'].tolist()]

# Define metadata features for training/validation and testing sets
train_val_metadata = train_val_df[['gender', 'view-position']]
test_metadata = test_df[['gender', 'view-position']]

# Create TensorFlow datasets for metadata
train_val_metadata_dataset = tf.data.Dataset.from_tensor_slices(
                                train_val_metadata.to_dict(orient='records'))

test_metadata_dataset = tf.data.Dataset.from_tensor_slices(test_metadata.to_dict(orient='records'))

# Create TensorFlow datasets for training/validation and testing sets
train_val_dataset = tf.data.Dataset.zip((train_val_image_paths, train_val_metadata_dataset))
test_dataset = tf.data.Dataset.zip((test_image_paths, test_metadata_dataset))
