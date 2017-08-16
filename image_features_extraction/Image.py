
import scipy.misc as sm
from skimage.measure import label
from skimage import filters, io
from skimage.segmentation import clear_border

from image_features_extraction import Regions
from image_features_extraction import MyException


class Image(object):
    """
    Class image containing the single image obtained from the collection :class:`Images`

    :example:
    >>> import image_features_extraction as fe
    >>> imgs = fe.Images(folder_name)
    >>> img = imgs.item(1)
    """

    def __init__(self, full_name):
        self.__full_file_name = full_name
        self.__regions = None
        self.__mask = None
        try:
            self.__get_regions()
        except MyException.MyException as e:
            print(e.args)


    def file_name(self):
        """
        file_name(...) return the full file name of the image
        """
        return self.__full_file_name


    def regions(self):
        """
        regions(...) returns the Object Regions

        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> regs = img.Regions()
        """
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
        # cretes the mask
        self.__mask = self.image > val
        # returns the single segmented elements of the image
        labels_segment = label(self.__mask)
        # removes the image elements at the border
        self.__regions = clear_border(labels_segment)
        return self.__regions
