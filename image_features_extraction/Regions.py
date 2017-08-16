import pandas as pd
from image_features_extraction import my_iterator
from image_features_extraction import Region
from image_features_extraction import MyException
from skimage.measure import label, regionprops


class Regions(my_iterator.my_iterator):

    def __init__(self, obj_regions):
        try:
             self.__iterator_init__()
             self.__obj_regions_org = obj_regions
             self.__obj_regions = regionprops(obj_regions)
             self.count_update(len(self.__obj_regions))
        except MyException.MyException as e:
            print(e.args)

    def regions_obj(self):
        return self.__obj_regions_org


    def item(self, i):
        try:
            if i >= self.count():
                raise MyException.MyException("error: index out of bound")

            return Region.Region(self.__obj_regions[i])
        except MyException.MyException as e:
            print(e.args)
            return None

    def prop_values(self, prop_name):
        try:

            vals = []
            for i in self.__obj_regions:
                vals.append(getattr(i, prop_name))
            return vals

        except Exception as e:
            print(e.args)
            return None


    def get_features(self, features, class_value=None, class_name='class_name'):
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
