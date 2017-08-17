################################
# virtualenv remi_bioimage_package
# source activate remi_insight
# source deactivate
#  python setup.py sdist
# pip install . --upgrade
################################

import image_features_extraction.Images as im

imgs = im.Images('./images')
print('numberf of images:{}'.format(imgs.count()))
img1 = imgs.item(5)

print('file names:')
for img in imgs:
    print(img.file_name())


regs = img1.regions()
print('numberf of regions:{}'.format(regs.count()))

print('features:')
df = regs.get_features(['label', 'area','perimeter', 'centroid'], class_value=1)
print(df)


#for reg in regs:
#    areas.append(reg.perimeter)

#import matplotlib.pyplot as plt
#plt.plot(areas)
#plt.show()
