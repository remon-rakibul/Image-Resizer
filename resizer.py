import cv2
import os

def rename_files(file_dir):
    """ Renames file names in a given directory """
    file_dir = r'{}'.format(file_dir)
    file_list = os.listdir(file_dir)
    saved_path = os.getcwd()
    os.chdir(file_dir)
    i = 1
    for file_name in file_list:
        os.rename(file_name, '{}.jpg'.format(i))
        i += 1
    os.chdir(saved_path)


def resize_images(file_dir, width, height):
    """ 
        Resizes images in a given directory
    """
    file_dir = r'{}'.format(file_dir)
    images = os.listdir(file_dir)
    saved_path = os.getcwd()
    os.chdir(file_dir)
    new_dir = './Resized'
    try:
        os.mkdir(new_dir)
    except:
        pass
    for image in images:
        img = cv2.imread(image)
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
        cv2.imwrite('{}/{}_resized.jpg'.format(new_dir, image[:-4]), img)
    os.chdir(saved_path)