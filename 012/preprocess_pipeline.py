# import os
import tensorflow as tf
# import prepare_dataframe as pdf
# import matplotlib.pyplot as plt
# from tensorflow.keras.layers.experimental import preprocessing


def preprocess(img_path, mask_path, img_size=(256, 256)):
    """ Preprocess the image and their mask 
    
    Parameters
    ----------
    img_path : str
        path of image

    mask_path : str
        path of mask

    Returns
    -------
    input_image: processed image (img_size=256x256)

    input_mask: processed mask (img_size=256x256)
    """

    input_image = tf.io.read_file(img_path)  # read image
    input_image = tf.image.decode_jpeg(
        input_image, channels=3)  # decode image in 3 channel
    input_image = tf.image.resize(input_image, img_size)  # resize 256x256
    input_image = tf.cast(input_image, tf.float32) / 255.0      #normalize range 0-1

    input_mask = tf.io.read_file(mask_path)  # read mask
    input_mask = tf.image.decode_jpeg(
        input_mask, channels=1)  # decode mask in 1 channel
    input_mask = tf.image.resize(input_mask, img_size)  # resize 256x256
    input_mask = tf.math.sign(input_mask)  # normalize range 0-1

    return input_image, input_mask


def create_dataset(df):
    ds = tf.data.Dataset.from_tensor_slices(
        (sorted(df["img_path"].values), sorted(df["mask_path"].values)))
    ds = ds.map(preprocess, tf.data.AUTOTUNE)
    return ds


def display(display_list):
  plt.figure(figsize=(8, 10))

  title = ['Input Image', 'True Mask', 'Predicted Mask', 'Mask On Image']

  for i in range(len(display_list)):
    plt.subplot(1, len(display_list), i+1)
    plt.title(title[i])
    plt.imshow(tf.keras.preprocessing.image.array_to_img(display_list[i]))
    plt.axis('off')
  plt.show()

def show_img_mask(show = False):
    if show:
        for images, masks in train_batches.take(2):
            sample_image, sample_mask = images[0], masks[0]
            display([sample_image, sample_mask])
    return


# if __name__ == "__main__":
#     BASE_DIR = os.getcwd()

#     img_folder = os.path.join(BASE_DIR, 'aug_data/images')
#     mask_folder = os.path.join(BASE_DIR, 'aug_data/masks')

#     df = pdf.get_df(img_folder, mask_folder)
#     train_df, test_df = pdf.split_df(df)

#     train_images = create_dataset(train_df)
#     test_images = create_dataset(test_df)

#     TRAIN_LENGTH = len(train_df)
#     TEST_LENGTH = len(test_df)
#     BATCH_SIZE = 16
#     BUFFER_SIZE = 500
#     STEPS_PER_EPOCH = TRAIN_LENGTH // BATCH_SIZE
#     VALIDATION_STEPS = TEST_LENGTH // BATCH_SIZE

#     train_batches = (
#         train_images
#         .cache()
#         .shuffle(BUFFER_SIZE)
#         .batch(BATCH_SIZE)
#         .repeat()
#         .prefetch(buffer_size=tf.data.AUTOTUNE))

#     test_batches = test_images.batch(BATCH_SIZE)

#     # display image and corresponding mask
#     show_img_mask(show=False)




