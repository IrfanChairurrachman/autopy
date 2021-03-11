from PIL import Image
import os

def edit_image(source, dest, rotate=-90, x=128, y=128):
    for image in os.listdir(source):
        
        f = "{}/{}".format(source, image)
        # f = os.path.join(source, image)
        print(f)
        try:
            img = Image.open(f).convert('RGB')
            file_dest = "{}/{}.jpeg".format(dest, image)
            img.rotate(rotate).resize((x, y)).save(file_dest)
            print('success edited {} and move to {}'.format(f, file_dest))
        except IOError as e:
            print("Can't edit {} because {}".format(f, e))

if __name__ == '__main__':
    source = 'images'
    dest = '/opt/icons'
    edit_image(source, dest)

        