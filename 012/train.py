import os
import random
from glob import glob
import tensorflow as tf
from unet import unet_model
from segmentation_models.metrics import iou_score
from segmentation_models.losses import bce_jaccard_loss, bce_dice_loss

AUTOTUNE = tf.data.AUTOTUNE


class LoadPaths:
    def __init__(self, BASE_DIR, aug_folder_name="aug_data", train_size=0.8, ** kwargs):
        self.BASE_DIR = BASE_DIR
        self.aug_folder_name = aug_folder_name
        self.train_size = train_size
        super().__init__(**kwargs)

    def load_paths(self):
        image_paths = sorted(
            glob(os.path.join(self.BASE_DIR, self.aug_folder_name, "images/*")))
        mask_paths = sorted(
            glob(os.path.join(self.BASE_DIR, self.aug_folder_name, "masks/*")))
        return image_paths, mask_paths

    def train_test_split(self):
        image_paths, mask_paths = self.load_paths()
        count = int(len(image_paths)*self.train_size)

        # split in train and test
        train_images = image_paths[:count]
        train_masks = mask_paths[:count]
        test_images = image_paths[count:]
        test_masks = mask_paths[count:]
        return train_images, train_masks, test_images, test_masks


class DataLoader:
    def __init__(self, image_paths, mask_paths, image_size=(256, 256), channels=(3, 1), **kwargs):
        self.image_paths = image_paths
        self.mask_paths = mask_paths
        self.image_size = image_size
        self.channels = channels
        super().__init__(**kwargs)

    def preprocess(self, img_path, mask_path):
        input_image = tf.io.read_file(img_path)
        input_image = tf.image.decode_jpeg(
            input_image, channels=self.channels[0])
        input_image = tf.image.resize(input_image, self.image_size)
        input_image = tf.cast(input_image, tf.float32) / 255.0

        input_mask = tf.io.read_file(mask_path)
        input_mask = tf.image.decode_jpeg(
            input_mask, channels=self.channels[1])
        input_mask = tf.image.resize(input_mask, self.image_size)
        input_mask = tf.math.sign(input_mask)

        return input_image, input_mask

    def data_batch(self, batch_size, shuffle=False):
        data = tf.data.Dataset.from_tensor_slices(
            (self.image_paths, self.mask_paths))
        data = data.map(self.preprocess, num_parallel_calls=AUTOTUNE)

        if shuffle:
            # Prefetch, shuffle then batch
            data = data.prefetch(AUTOTUNE).shuffle(
                random.randint(0, len(self.image_paths))).batch(batch_size)
        else:
            # Batch and prefetch
            data = data.batch(batch_size).prefetch(AUTOTUNE)
        return data


class train(LoadPaths):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load_data(self):
        loadpath_obj = LoadPaths(self.BASE_DIR)
        train_images, train_masks, test_images, test_masks = loadpath_obj.train_test_split()
        print('Train images count: ', len(train_images), 'Train masks count: ', len(train_masks),
              '\nTest images count: ', len(test_images), 'Test masks count: ', len(test_masks))

        train_length = len(train_images)
        test_length = len(test_images)

        train_dataset = DataLoader(train_images, train_masks)
        test_dataset = DataLoader(test_images, test_masks)

        train_batches = train_dataset.data_batch(batch_size=4)
        test_batches = test_dataset.data_batch(batch_size=4)
        print('batch done')

        return train_length, test_length, train_batches, test_batches

    def model_callbacks(self):
        early_stop = tf.keras.callbacks.EarlyStopping(
            patience=5, monitor='val_iou_score', mode='max', restore_best_weights=True)

        checkpoint = tf.keras.callbacks.ModelCheckpoint(
            filepath='models/model_disease.h5', monitor='val_iou_score',
            verbose=0, save_best_only=True, mode='max')

        reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_iou_score', factor=0.1, patience=5, verbose=0,
            mode='max', min_delta=0.0001, min_lr=0.00002)

        tb_callback = tf.keras.callbacks.TensorBoard('models/logs/logs')

        return [early_stop, checkpoint, reduce_lr, tb_callback]

    def model_train(self, BATCH_SIZE, EPOCH):
        TRAIN_LENGTH, TEST_LENGTH, train_batches, test_batches = self.load_data()
        STEPS_PER_EPOCH = TRAIN_LENGTH // BATCH_SIZE
        VALIDATION_STEPS = TEST_LENGTH // BATCH_SIZE

        # creating object of unet architecture
        model = unet_model()

        # compile model
        model.compile(optimizer='adam', loss=bce_jaccard_loss,
                      metrics=[iou_score])

        # fit model
        callbacks = self.model_callbacks()
        model_history = model.fit(train_batches, epochs=EPOCH, steps_per_epoch=STEPS_PER_EPOCH,
                                  validation_data=test_batches, validation_steps=VALIDATION_STEPS,
                                  callbacks=callbacks)


# Driver Code
if __name__ == '__main__':
    base_dir = r"C:\project\Leaf Disease Segmentation\Experiment"
    tr = train(BASE_DIR=base_dir)
    tr.model_train(BATCH_SIZE=4, EPOCH=2)
