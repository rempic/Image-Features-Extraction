import pandas as pd
from image_features_extraction import my_iterator
from image_features_extraction import Region
from image_features_extraction import MyException
from skimage.measure import label, regionprops


class Regions(my_iterator.my_iterator):
    """
    This class represent a collection of regions: segmented image elements
    It cannot be instanced directly. It is returned from the object :class:`Image` through the function
    Regions(...)

    :example:
    >>> import image_features_extraction as fe
    >>> imgs = fe.Images(folder_name)
    >>> img = imgs.item(1)
    >>> regs = img.Regions()
    """

    def __init__(self, obj_regions):
        try:
             self.__iterator_init__()
             self.__obj_regions_org = obj_regions
             self.__obj_regions = regionprops(obj_regions) # used regionprops from skimage
             self.count_update(len(self.__obj_regions))
        except MyException.MyException as e:
            print(e.args)


    def __regions_obj(self):
        """
        This function returns the Internal object regions. it is used only for debugging
        """
        return self.__obj_regions_org


    def item(self, i):
        """
        Item(..) returns the i-th image element  of the regions.

        :param i: the i-th element of the collection region
        :type i: int
        :returns: Region
        :rtype: object
        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> regs = img.Regions()
        >>> reg = regs.item(1)
        """
        try:
            if i >= self.count():
                raise MyException.MyException("error: index out of bound")

            return Region.Region(self.__obj_regions[i])
        except MyException.MyException as e:
            print(e.args)
            return None


    def prop_values(self, prop_name):
        """
        prop_values(...) returns the values of the specified  property/measure name (e.g., 'area') for all image
        elements contained in the object Regions. For a list of property names refer to "regionprops  <http://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops>"_.

        :param prop_name: name of the property to measure (e.g, 'area')
        :type prop_name: string
        :returns: values of the property name in input
        :rtype: List

        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> regs = img.Regions()
        >>> areas = regs.prop_values('area')
        """
        try:

            vals = []
            for i in self.__obj_regions:
                vals.append(getattr(i, prop_name))
            return vals

        except Exception as e:
            print(e.args)
            return None


    def get_features(self, features, class_value=None, class_name='class_name'):
        """
        get_features(...)  returns a table with all  values for the property names given in input, and supplies an
        additional parameter for feature classification

        :param features: list of property/measure names (e.g, 'area', 'centroid', etc )
        :type features: List
        :param class_value: classification label
        :type class_value: int, string (default=None)
        :returns: table cointaining all property values (columns) for all elements in the regions object  (rows)
        :rtype: Pandas.DataFrame
        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> regs = img.Regions()
        >>> df = regs.get_features(['label', 'area','perimeter', 'centroid'], class_value=1)

        """
        df = pd.DataFrame()
        try:
            for f in features:
                df[f] = self.prop_values(f)
            if class_value is not None:
                df[class_name] = class_value
            return df
        except Exception as e:
            print("one or more input labels might be wrong:{}".format(e))
            return None
