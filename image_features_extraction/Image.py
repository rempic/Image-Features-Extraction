
import scipy.misc as sm
from skimage.measure import label
from skimage import filters, io
from skimage.segmentation import clear_border

from image_features_extraction import Regions
from image_features_extraction import MyException


class Image(object):


    def __init__(self, full_name):
        self.__full_file_name = full_name
        self.__regions = None
        self.__mask = None
        try:
            self.__get_regions()
        except MyException.MyException as e:
            print(e.args)


    def file_name(self):
        return self.__full_file_name


    def regions(self):
        try:
            regs = self.__get_regions()
            return Regions.Regions(regs)
        except MyException.MyException as e:
            print(e.args)
            return None


    def __get_regions(self):
        # load the image
        self.image = io.imread(self.file_name())
        # ithresholding to build the map
        val = filters.threshold_otsu(self.image)

        self.__mask = self.image > val
        labels_segment = label(self.__mask)
        self.__regions = clear_border(labels_segment)

        return self.__regions
