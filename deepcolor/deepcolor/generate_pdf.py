import glob
import os
from pathlib import Path

import PIL
import numpy as np

from deepcolor.deepcolor import colorize_image, colornet
from deepcolor.deepcolor.settings import RESOURCES_PATH
from deepcolor.deepcolor.utils import load_image


print("%s/1Mio/*.pkl" % RESOURCES_PATH)
for folder in ["complete/alt_02_model", "complete/alt_03_model", "complete/alt_04_model", "complete/alt_model", "complete/model"]:
    for model in glob.glob("%s/%s/*.pkl" % (RESOURCES_PATH, folder)):
        model_name = os.path.splitext(os.path.basename(model))[0]
        path = Path("../out_data/%s/%s" % (folder, model_name))
        if path.exists():
            print("Skipping: %s" % path.name)
            continue

        for ext in ["jpg", "png", "jpeg"]:
            for filename in glob.glob('../data/*.%s' % ext):
                path.mkdir(parents=True, exist_ok=True)
                model_path = Path(RESOURCES_PATH, model)
                basename = os.path.basename(filename)
                original_image = load_image(filename).convert("RGB")
                colorized_image = colorize_image(original_image, method=colornet.colorize_image, args={"model": model_path})
                img = PIL.Image.fromarray(np.uint8(colorized_image*255))
                converter = PIL.ImageEnhance.Color(img)
                img = converter.enhance(1.5)
                img.save("../out_data/%s/%s/%s.jpg" % (folder, model_name, os.path.splitext(basename)[0]))
