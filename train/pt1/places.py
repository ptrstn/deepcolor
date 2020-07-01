import argparse
import os

image_location = "Images"
label_location = "Labels"

parser = argparse.ArgumentParser(description='Process Images from LabelMe')
parser.add_argument('--path', metavar='-p', help='path to images')

args = parser.parse_args()

places205_location = "data/vision/torralba/deeplearning/images256"
full_image_location = "{}/{}".format(args.path, places205_location)

lut = dict()
lut_counter = 0


# TODO: Subfolder!
def create_tag_list(tag_name, image_full_path, tag_prefix=""):
    full_tag = "_".join([tag_prefix, tag_name]) if tag_prefix != "" else tag_name
    dir_name = "/".join([image_full_path, tag_name])
    print(dir_name)
    tags = []
    for name in os.listdir(dir_name):
        if os.path.isfile("/".join([dir_name, name])):
            tags.append(("/".join([dir_name, name]), full_tag))
        else:
            tags += create_tag_list(name, dir_name, full_tag)
    return tags


tag_list = []

for name in [name for name in os.listdir(full_image_location)]:
    image_full_path = "{}/{}".format(full_image_location, name)

    if not os.path.isdir(full_image_location):
        continue

    for tag in os.listdir(image_full_path):
        tag_list += create_tag_list(tag, image_full_path)

with open('train.txt', 'w') as f:
    for item in tag_list:
        if not item[1] in lut:
            lut[item[1]] = lut_counter
            lut_counter += 1
        f.write("{} {}\n".format(item[0], lut[item[1]]))

