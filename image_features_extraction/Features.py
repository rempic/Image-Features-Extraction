import pandas as pd
import os.path
from image_features_extraction import MyException

class Features(object):
    """
    contain the dataframe
    """
    def __init__(self, data_frame):
        self.__data_frame = data_frame
        self.__class_name = ''
        self.__class_value=None


    def set_class_name(self, class_name):
        self.__class_name = class_name


    def set_class_value(self, class_value):
        self.__class_value = class_value


    def get_class_name(self):
        return self.__class_name


    def get_class_value(self):
        return self.__class_value


    def merge(self, Features_Obj, how_in='inner'):
        """
        Merges in the current Features object a second Features object (ex. obtained from the Voronoi Object)

        :param Features_Obj: External Features Object
        :type Features_Obj: Features (image_features_extraction package)
        :param how_in: 'inner', 'outer'
        :type how_in: string
        >>> import image_features_extraction.Images as fe
        >>> IMGS = fe.Images('../images/CA/1')
        >>> vor = IMG.Voronoi()
        >>> features1 = IMG.features(['area','perimeter','centroid','bbox', 'eccentricity'])
        >>> features2 = vor.features(['area','perimeter','centroid','bbox', 'eccentricity'])
        >>> features3 = features1.merge(features2, how_in='inner')
        >>> features3.get_dataframe().head()
        """
        df1 = Features_Obj.get_dataframe();
        df2 = pd.merge(self.__data_frame, df1, on='id', how=how_in)
        return Features(df2)


    def save(self, storage_name, type_storage='file', do_append=True):
        """
        save the current dataframe into the type of storage given in input.

        :param storage_name: storage name, (e.g., file name if ' storage type is 'file')
        :type storage_name: string
        :param type_storage:  type of storage (default is 'file') ('db', 'json' will be future implementations)
        :type type_storage: string
        :param do_append: if True it appends to existing storage. If False it creates a new storage
        :type do_append: boolean
        if  'do_append=True': This version of the method does not check whether the new data are consistent with presisitng data into
        the existing storage. It just tries to append the date and might fail or not depending on the type of storage
        
        :returns: 1 if sucessuful otherwise 0
        :rtype: int

        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> reg = img.Regions().item(1)
        >>> features = regs.get_features(['label', 'area','perimeter', 'centroid'], class_value=1)
        >>> features.save('my_file_name')
        """
        try:
            if type_storage == 'file':
                return self.__save_file(storage_name, do_append)
            else:
                raise MyException.MyException("error: storage type no specified or not found")
            return 0
        except Exception as e:
            print("one or more input labels might be wrong:{}".format(e))
            return 0


    def __save_file(self, file_name, do_append):
        """
        load the data from the local directory with the name indicated
        """
        if do_append==True:
            add_header = False
            if os.path.isfile(file_name) == False:
                add_header = True
            with open(file_name, 'a') as f: # it appends or creates a new file
                self.__data_frame.to_csv(f, header=add_header)
        else:
            with open(file_name, 'w') as f: # it creates a new file
                self.__data_frame.to_csv(f, header=True)
        return 1


    def get_dataframe(self, include_class=False):
        """
        creates  a panda data frame contining the feature values

        :param include_class: if True if includes the class name and value as the last column
        :type include_class: Boolean
        """
        try:
            df = self.__data_frame.copy()

            if include_class == True:
                if self.__class_name == '':
                    raise MyException.MyException("error: class name not set")
                if self.__class_value is None:
                    raise MyException.MyException("error: class value not set")
                df[self.__class_name]=self.__class_value

            return df
        except MyException.MyException as e:
            print(e.args)
            return None
