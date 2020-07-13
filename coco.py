import torchvision.datasets as data_set
import matplotlib.pyplot as plt

'''
Loading COCO Dataset using pytorch Dataset.CocoDetection class

Editor: Rashid Ali
'''
image_root = 'C:/Users/rashi/Desktop/yolact/data/coco/images'
annot_file = 'C:/Users/rashi/Desktop/yolact/data/coco/annotations/instances_train2017.json'
coco_train = data_set.CocoDetection(root=image_root, annFile=annot_file )
print('Number of Samples:', len(coco_train))

img, target = coco_train.__getitem__(index=1)

print('Target', target)

img.show()

