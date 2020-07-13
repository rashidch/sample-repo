import base64
import json
import os
import random
from io import BytesIO
from math import trunc

import numpy as np
import requests
from PIL import Image as PILimage
from PIL import ImageDraw as PILimageDraw


"""
Script to load COCO-2017 dataset from scratch
"""


class COcoDataset:
    def __init__(self, image_dir, annotation_path):

        self.image_dir = image_dir
        self.annotation_path = annotation_path
        self.color = color = [
            "blue",
            "purple",
            "red",
            "green",
            "orange",
            "salmon",
            "pink",
            "gold",
            "orchid",
            "slateblue",
            "limegreen",
            "seagreen",
            "darkgreen",
            "olive",
            "teal",
            "aquamarine",
            "steelblue",
            "powderblue",
            "dodgerblue",
            "navy",
            "magenta",
            "sienna",
            "maroon",
        ]
        json_file = open(self.annotation_path)
        self.coco = json.load(json_file)
        json_file.close()

        self.process_info()
        self.process_licenses()
        self.process_categories()
        self.process_image()
        self.process_segmentations()

    def process_info(self):
        self.info = self.coco["info"]

    def process_licenses(self):
        self.licenses = self.coco["licenses"]

    def process_categories(self):
        self.categories = {}
        self.super_categories = {}
        for category in self.coco["categories"]:
            cat_id = category["id"]
            super_category = category["supercategory"]

            if cat_id not in self.categories:
                self.categories[cat_id] = category  # add category to the category dict
            else:
                print("ERROR: skipping duplicate category id : {}".format(category))

            if super_category not in self.super_categories:

                self.super_categories[super_category] = {cat_id}
            else:
                self.super_categories[super_category] |= {cat_id}

    def process_image(self):
        self.images = {}
        for image in self.coco["images"]:
            image_id = image["id"]
            if image_id not in self.images:
                self.images[image_id] = image
            else:
                print("ERROR: skipping duplicate image id : {}".format(image))

    def process_segmentations(self):
        self.segmentations = {}
        for segmentation in self.coco["annotations"]:
            image_id = segmentation["image_id"]
            if image_id not in self.segmentations:
                self.segmentations[image_id] = []
            self.segmentations[image_id].append(segmentation)

    def display_info(self):
        print("Dataste Info")
        print("============")
        for key, item in self.info.items():
            print("{}: {}".format(key, item))

        requirements = [
            ["description", str],
            ["url", str],
            ["version", str],
            ["year", int],
            ["contributor", str],
            ["date_created", str],
        ]
        for req, req_type in requirements:
            if req not in self.info:
                print("ERROR: {} is missing".format(req))
            elif type(self.info[req]) != req_type:
                print("ERROR: {} should be type {}".format(req, req_type))
        print()

    def display_licenses(self):
        print("Licenses Info")
        print("============")
        for license in self.licenses:
            for key, item in license.items():
                print("{}: {}".format(key, item))
            requirements = [["id", int], ["url", str], ["name", str]]
            for req, req_type in requirements:
                if req not in license:
                    print("ERROR: {} is missing".format(req))
                elif type(license[req]) != req_type:
                    print("ERROR: {} should be type {}".format(req, req_type))
        print()

    def display_categories(self):
        print("Category info")
        print("=============")
        for cat_key, id_val in self.super_categories.items():
            print("Super Category: {}".format(cat_key))
            for cat_id in id_val:
                print("   {} {}".format(cat_id, self.categories[cat_id]["name"]))
            print("")


if __name__ == "__main__":

    image_root = "C:/Users/rashi/Desktop/yolact/data/coco/images"
    annot_file = (
        "C:/Users/rashi/Desktop/yolact/data/coco/annotations/instances_train2017.json"
    )
    cocodataset = COcoDataset(image_dir=image_root, annotation_path=annot_file)
    cocodataset.display_info()
    cocodataset.display_licenses()
    cocodataset.display_categories()
