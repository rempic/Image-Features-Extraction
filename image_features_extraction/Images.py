#!/usr/bin/env python3

import os
from image_features_extraction import Image
from image_features_extraction import my_iterator
from image_features_extraction import MyException


class Images(my_iterator.my_iterator):
    """
    This class contains a collection of images

    :param  folder_name: folder containing images
    :type folder_name: string
    :param  image_file_ext: images file extensions (default=['tif','tiff'])
    :type folder_name: List of strings
    :returns: an instance of the object Images
    :rtype: object
    :example:
    >>> import image_features_extraction as fe
    >>> imgs = fe.Images('my_folder', image_file_ext=['tif','tiff','jpeg'])
    >>> num_images = imgs.count()
    """

    # to implement the class as a collection this object inherits the abstract class my_iterator
    def __init__(self, folder_name, image_file_ext=['tif', 'tiff']):
        """
        class initializer. to implement the class as a collection this object inherits the abstract class my_iterator
        """
        super().__init__()
        #self.__iterator_init__()  # initializes my_iterator
        self.__folder_name = folder_name
        self.__image_file_ext = image_file_ext
        self.__dicfiles = []
        try:
            # load the files image into a list
            self.__load()
        except MyException.MyException as e:
            print(e.args)


    def __load(self):
        """
        load the files image into a list
        """
        # check that the folder exists
        if os.path.isdir(self.__folder_name) == False:
            raise MyException.MyException("Error: folder name does not exist")
        # store the file names
        self.__dicfiles = []
        files = os.listdir(self.__folder_name)
        for f in files:
            if self.__is_imagefile(f):
                self.__dicfiles.append(f)
        self.count_update(len(self.__dicfiles))


    def __is_imagefile(self,file_name):
        """
        checks that the file is an image
        """
        # check the extension of the file
        ext0 = file_name.split(".")[-1]
        for ext1 in self.__image_file_ext:
            if ext1 == ext0:
                return True
        return False


    def item(self, i):
        """
        returns the i-th image

        :param i: the i-th image
        :type i: int
        :returns: :class:`Image`
        :rtype: object
        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        """
        try:
            if i >= self.count():
                raise MyException.MyException("error: index out of bound")
            return Image.Image(os.path.join(self.__folder_name, self.__dicfiles[i]))
        except MyException.MyException as e:
            print(e.args)


    def save(self, storage_name, type_storage='file', do_append=True):
        """
        save the regions from the set of  images into the type of storage given in input.

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
        >>> imgs..save('my_file_name')
        """
        try:
            if type_storage == 'file':
                n = self.count()
                for i in range(0,n):
                    img  = self.item(i)
                    img.regions().save(storage_name, do_append)
            else:
                raise MyException.MyException("error: storage type no specified or not found")
            return 0
        except Exception as e:
            print("one or more input labels might be wrong:{}".format(e))
            return 0
