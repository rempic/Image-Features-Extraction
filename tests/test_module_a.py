####################################
#
#  Test:
#  1. move to the folder image_features_extraction or tests
#  2.  run  pytest  on the terminel
#
####################################
import numpy as np
import image_features_extraction.Images as fe
import os.path


def test_images():
    sdir = os.path.dirname(__file__)
    sdir_images = os.path.join( sdir, 'images')
    imgs = fe.Images(sdir_images)
    assert imgs is not None
    assert imgs.count() == 4


def test_regions():
    imgs = fe.Images('./images/')
    img = imgs.item(1)
    assert img is not None
    regs = img.regions()
    assert regs is not None
    assert regs.count() == 5384
    areas = regs.prop_values('area')
    assert np.mean(areas) > 54
    reg = regs.item(1)
    assert reg is not None
    per = reg.prop_value('perimeter')
    assert per>29


def test_features():
    imgs = fe.Images('./images/')
    img = imgs.item(1)
    assert img is not None
    regs = img.regions()
    assert regs is not None
    features = regs.get_features(['area', 'centroid'])
    assert features is not None
    assert features.save('temp_file', do_append=False) == 1
