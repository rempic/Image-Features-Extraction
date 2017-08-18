import pandas as pd
import os.path


class Features(object):
    """
    contain the dataframe
    """
    def __init__(self, data_frame):
        self.__data_frame = data_frame


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
        the existing storage. It just tris to append the date and might fail or not depending on the type of storage
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
        load the data from the local directory with name indicated
        """
        if do_append==True:
            add_header = True
            if os.path.isfile(file_name) == False:
                add_header = False
            with open(file_name, 'a') as f: # it appends or creates a new file
                self.__data_frame.to_csv(f, header=add_header)
        else:
            with open(file_name, 'w') as f: # it creates a new file
                self.__data_frame.to_csv(f, header=True)
        return 1


    def get_dataframe(self):
        """
        returns  the data frame contining the feature values
        """
        return self.__data_frame
