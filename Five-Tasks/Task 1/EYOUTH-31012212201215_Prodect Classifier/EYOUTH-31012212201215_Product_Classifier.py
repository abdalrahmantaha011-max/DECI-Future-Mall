# =====================================================================
# Future Mall - Product Classifier
# Task 1, Sub-task 3
#
# The grocery store in Future Mall wants product photos sorted
# automatically into categories.
#
# Before you start:
#   1. Train your classifier in Google Teachable Machine (Image Project)
#      with one class for each product category you chose.
#   2. Export the model as "Tensorflow -> Keras". You get two files:
#      keras_model.h5 and labels.txt
#   3. Open this file in Google Colab, then upload next to it:
#      keras_model.h5, labels.txt, and your test images.
#   4. labels.txt shows your classes in the order the model uses them.
#      You will need that order in TODO 1.
#   5. Save your finished file with the project naming convention.
#
# Complete every section marked TODO. Do not change the other lines.
# =====================================================================

from keras.models import load_model
from keras.layers import DepthwiseConv2D
from PIL import Image, ImageOps
import numpy as np


# ---------------------------------------------------------------------
# 1. Your categories
# ---------------------------------------------------------------------
# TODO 1: write your category names inside this list, in the SAME order
#         they appear in labels.txt.
#         Example:  categories = ["Fruits", "Vegetables", "Dairy"]

categories = ["Fruits", "Vegetables", "Dairy"]

# ---------------------------------------------------------------------
# 2. Load the model you trained  (given - do not change)
#
#    Teachable Machine saves the model in an older format, so this part
#    tells the newer library how to read it.
# ---------------------------------------------------------------------
class TeachableMachineLayer(DepthwiseConv2D):
    def __init__(self, *args, groups=1, **kwargs):
        super().__init__(*args, **kwargs)


model = load_model(
    "keras_model.h5",
    compile=False,
    custom_objects={"DepthwiseConv2D": TeachableMachineLayer},
)


# ---------------------------------------------------------------------
# 3. Prepare one image for the model  (given - do not change)
# ---------------------------------------------------------------------
def prepare(image_path):
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, (224, 224))
    data = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    return (data / 127.5) - 1


# ---------------------------------------------------------------------
# 4. Classify one image
# ---------------------------------------------------------------------
def classify(image_path):
    scores = model.predict(prepare(image_path), verbose=0)[0]

    # TODO 2: find the POSITION of the highest score in the list `scores`.
    #         Start with position 0 and loop over the rest, keeping the
    #         position of the biggest value you have seen so far.
    best_position = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_position]:
            best_position = i

    # TODO 3: use best_position to pick the matching name from `categories`,
    #         and turn its score into a percentage (score * 100).
    category = categories[best_position]
    confidence = scores[best_position] * 100

    return category, confidence


# ---------------------------------------------------------------------
# 5. Test your classifier
# ---------------------------------------------------------------------
# TODO 4: write the file names of your test images inside this list.
#         Use images that were NOT used in training.
#         Example:  test_images = ["test1.jpg", "test2.jpg", "test3.jpg"]

test_images = ["test01.jpg", "test02.jpg", "test03.jpg"]

# TODO 5: loop over test_images, classify each one, and print a line like:
#         test1.jpg  ->  Fruits  (96%)
for image in test_images:
    category, confidence = classify(image)
    print(f"{image} -> {category} ({confidence:.0f}%)")