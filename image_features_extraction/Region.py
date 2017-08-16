from image_features_extraction import MyException

class Region(object):
    def __init__(self, obj_region):
        if obj_region is None:
            raise MyException.MyException
        self.__obj_region = obj_region

        self.area = self.__obj_region.area
        self.centroid = self.__obj_region.centroid
        self.eccentricity = self.__obj_region.eccentricity
        self.label = self.__obj_region.label                            #The label in the labeled input image
        self.major_axis_length = self.__obj_region.major_axis_length
        self.perimeter = self.__obj_region.perimeter            #Perimeter of object which approximates the contour as a line through the centers of border pixels using a 4-connectivity.
        self.image = self.__obj_region.image
        self.roi = self.__obj_region.coords
        self.bbox = self.__obj_region.bbox

    def area(self):
        return self.__obj_region.area
