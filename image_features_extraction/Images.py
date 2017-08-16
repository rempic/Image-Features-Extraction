#!/usr/bin/env python3

import os
from image_features_extraction import Image
from image_features_extraction import my_iterator
from image_features_extraction import MyException


class Images(my_iterator.my_iterator):
    """
    This class is used as collection of images which will be loaded from a given folder name
    """
    def __init__(self, folder_name, image_file_ext=['tif', 'tiff']):
        self.__iterator_init__()  # initialize my iterator

        self.__folder_name = folder_name
        self.__image_file_ext = image_file_ext
        self.__dicfiles = []
        try:
            self.__load()
        except MyException.MyException as e:
            print(e.args)


    def __load(self):
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
        # check the extension of the file
        ext0 = file_name.split(".")[-1]
        for ext1 in self.__image_file_ext:
            if ext1 == ext0:
                return True
        return False


    def item(self, i):
        """
        image item
        """
        try:
            if i >= self.count():
                raise MyException.MyException("error: index out of bound")
            return Image.Image(os.path.join(self.__folder_name, self.__dicfiles[i]))
        except MyException.MyException as e:
            print(e.args)
