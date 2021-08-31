import os
import cv2
from tqdm import tqdm
from glob import glob
from albumentations import Transpose, RandomRotate90, HorizontalFlip, VerticalFlip

class data_augment:
    '''
    A class to augment image and mask using albumentation library.

    [
    Example: base_dir is 'Experiment' for folder structure given below:
    Experiment:
        ->data:
            ->images: img1, img2, img3, ...
            ->masks: mask1, mask2, mask3, ...
    ]
    ...

    Attributes
    ----------
    BASE_DIR : str
        path of the base_dir

    Methods
    -------
    create_dir(aug_folder_name):
        Create directory for images and masks to store augmented data
    load_data(folder_name):
        Load list of paths for images and masks for given folder
    augment_data(images_lst, masks_lst, aug_folder_name, augment=True):
        Augment the images and corresponding masks and then saves the augmented data
    '''

    def __init__(self, BASE_DIR):
        '''
        Constructs all the necessary attributes for the data_augment object.

        Parameters
        ----------
            BASE_DIR : str
                path of the base folder
        '''
        self.BASE_DIR = BASE_DIR

    def create_dir(self, aug_folder_name):
        '''
        Create directory for images and masks to store augmented data.

        [
        Creates folder structure as given below:
        aug_folder_name:
            ->images
            ->masks
        ]

        Parameters
        ----------
        aug_folder_name: str
            Folder name for storing augmented data

        Returns
        -------
        None
        '''

        if not os.path.exists(os.path.join(self.BASE_DIR, aug_folder_name, "images")):
            os.makedirs(os.path.join(self.BASE_DIR, aug_folder_name, "images"))

        if not os.path.exists(os.path.join(self.BASE_DIR, aug_folder_name, "masks")):
            os.makedirs(os.path.join(self.BASE_DIR, aug_folder_name, "masks"))

        return

    def load_data(self, folder_name):
        '''
        Loads list of path of images and masks from given folder structure.

        folder_name:
            ->images
            ->masks

        Parameters
        ----------
        folder_name: str
            Folder name

        Returns
        -------
        images_lst: list
            List of images path
        masks_lst: list
            List of masks path
        '''

        images_lst = sorted(glob(os.path.join(self.BASE_DIR, folder_name, "images/*")))
        masks_lst = sorted(glob(os.path.join(self.BASE_DIR, folder_name, "masks/*")))
        return images_lst, masks_lst

    def augment_data(self, images_lst, masks_lst, aug_folder_name, augment=True):
        '''
        Augment image and mask using albumentation library.

        Parameters
        ----------
        images_lst: str
            List of images path
        masks_lst: str
            List of masks path
        aug_folder_name: str
            Folder name for storing augmented data
        augment: bool, (default=True)
            If False no augmentation is applied, If True augmentation is applied

        Returns
        -------
        None
        '''
        for x, y in tqdm(zip(images_lst, masks_lst), total=len(images_lst)):
            name = x.split("\\")[-1].split(".")
            # Extracting the name and extension of the image and the mask.
            image_name = name[0]
            image_extn = name[1]

            # print(image_name, image_extn)
            name = y.split("\\")[-1].split(".")
            mask_name = name[0]
            mask_extn = name[1]

            # Reading image and mask.
            x = cv2.imread(x, cv2.IMREAD_COLOR)
            y = cv2.imread(y, cv2.IMREAD_GRAYSCALE)

            # Augmentation
            if augment == True:
                aug = Transpose(p=1.0)
                augmented = aug(image=x, mask=y)
                x1 = augmented["image"]
                y1 = augmented["mask"]

                aug = RandomRotate90(p=1.0)
                augmented = aug(image=x, mask=y)
                x2 = augmented['image']
                y2 = augmented['mask']

                aug = HorizontalFlip(p=1.0)
                augmented = aug(image=x, mask=y)
                x3 = augmented['image']
                y3 = augmented['mask']

                aug = VerticalFlip(p=1.0)
                augmented = aug(image=x, mask=y)
                x4 = augmented['image']
                y4 = augmented['mask']

                save_images = [x, x1, x2, x3, x4]
                save_masks =  [y, y1, y2, y3, y4]

            else:
                save_images = [x]
                save_masks = [y]

            # Saving the image and mask.
            idx = 0
            for i, m in zip(save_images, save_masks):
                if len(images_lst) == 1:
                    tmp_img_name = f"{image_name}.{image_extn}"
                    tmp_mask_name = f"{mask_name}.{mask_extn}"
                else:
                    tmp_img_name = f"{image_name}_{idx}.{image_extn}"
                    tmp_mask_name = f"{mask_name}_{idx}.{mask_extn}"

                image_path = os.path.join(self.BASE_DIR, aug_folder_name, "images", tmp_img_name)
                mask_path = os.path.join(self.BASE_DIR, aug_folder_name, "masks", tmp_mask_name)

                cv2.imwrite(image_path, i)
                cv2.imwrite(mask_path, m)

                idx += 1

        return


if __name__ == "__main__":
    base_dir = r"C:\project\Leaf Disease Segmentation\Experiment"
    
    # creating object of data_augment class
    obj = data_augment(base_dir)

    # creating folder structure for saving augmented data
    obj.create_dir(aug_folder_name="aug_data")

    # loading list of image and mask path
    images_lst, masks_lst = obj.load_data(folder_name="data")
    print(f"Total Original Images: {len(images_lst)} - Total Original Masks: {len(masks_lst)}")

    # augmenting image and mask and saving on aug_folder_name
    obj.augment_data(images_lst, masks_lst, aug_folder_name="aug_data", augment=True)
    print("Augmentation done!")

    # loading list of image and mask path
    images_lst, masks_lst = obj.load_data(folder_name="aug_data")
    print(f"Total Augmented Images: {len(images_lst)} - Total Augmented Masks: {len(masks_lst)}")


