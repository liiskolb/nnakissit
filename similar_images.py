from scipy import misc
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine
import numpy as np
import glob

base_images = []
for i in range(10):
    base_images.append([None, None, np.inf, misc.imread("/gpfs/hpchome/liiskolb/nnakissit/generated/gen_img%s.png" % str(i))])
    all_distances.append([])
j = 0
for image_path in glob.glob("/gpfs/hpchome/liiskolb/nnakissit/data/train/classroom/*.png"):
    image = misc.imread(image_path)
    for i in range(10):
        dist = euclidean(base_images[i][3].flatten(), image.flatten())
        all_distances[i].append((image_path, dist))
        if dist < base_images[i][2]:
            base_images[i] = (image, image_path, dist, base_images[i][3])
    if j % 10000 == 0:
        for i in range(10):
            print(i, base_images[i][1], base_images[i][2])
    j += 1

for i in range(10):
    print(i, base_images[i][1], base_images[i][2])
    print(sorted(all_distances[i], key=lambda x:x[1])[:5])
