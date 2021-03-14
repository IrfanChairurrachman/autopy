from PIL import Image
import os

def edit_image(source, x=600, y=400):
    dest = source
    for image in os.listdir(source):
        if '.tiff' in image:
            f = "{}/{}".format(source, image)
            print(f)
            try:
                img = Image.open(f).convert('RGB')
                file_dest = "{}/{}".format(dest, image.replace('.tiff', '.jpeg'))
                img.resize((x, y)).save(file_dest)
                print('success convert {} to {}'.format(f, file_dest))
            except IOError as e:
                print("Can't edit {} because {}".format(f, e))

if __name__ == '__main__':
    source = 'images'
    edit_image(source)

        