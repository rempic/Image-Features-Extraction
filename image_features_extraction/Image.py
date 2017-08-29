
import pandas as pd
import scipy.misc as sm
from skimage.measure import label

from skimage.segmentation import clear_border
from skimage.color import label2rgb
from skimage.measure import label, regionprops
from skimage import filters, io

from image_features_extraction import Regions
from image_features_extraction import MyException
from image_features_extraction import Features
from image_features_extraction import Utils

import Voronoi_Features.Voronoi as VF


class Image(object):
    """
    This class instantiate an object Image through the :class:`Images` and refers to a specific file image

    :example:
    >>> import image_features_extraction as fe
    >>> imgs = fe.Images(folder_name)
    >>> img = imgs.item(1)
    """
    def __init__(self, full_name):
        self.__full_file_name = full_name
        self.__regions = None
        self.__regionsprops = None
        self.__image_intensity = None
        self.__image = None
        self.__image_semented = None
        try:
            # load  image and  segment
            self.__image = io.imread(self.__full_file_name)
            self.__image_semented  = self.__get_regions()
            self.__regionsprops = self.__get_regionsprop()
            self.__centroids = self.prop_values('centroid')
        except MyException.MyException as e:
            print(e.args)


    def Voronoi(self):
        """
        Image Voronoi diagram (refer to documentaiton of my package Voronoi_Features in my github )

        :return: Voronoi object for the current image
        :rtype: Voronoi object
        """
        return VF.Voronoi(self.__centroids, self.__image.shape[1], self.__image.shape[0])


    def width(self):
        return self.__image.shape[1]


    def height(self):
        return self.__image.shape[0]


    def file_name(self):
        """
        full file name of the image

        :returns: file name
        :rtype: string
        """
        return self.__full_file_name


    def set_image_intensity(self, image_intensity):
            """
            Sets the image to measurs  image's region intensity properties (e.g, mean_intensity)

            : param image_intensity:  Image object for intensity measurement
            : type image_intensity: Object Image
            :returns:  the set Image object for intensity measurement
            :rtype:  Object Image
            >>> import image_features_extraction as fe
            >>> imgs = fe.Images(folder_name)
            >>> img = imgs.item(1) # this is the binary image used for segmentation
            >>> img_intensity = imgs.item(0) # this is the original image on which to measure intensities
            >>> img.set_image_intensity(img_intensity)
            >>> features = IMG.features(['label', 'area','perimeter', 'centroid','major_axis_length', 'moments','mean_intensity'], class_value=5)

            """
            self.__image_intensity = image_intensity.__image
            self.__regionsprops = self.__get_regionsprop()

    def regions(self):
        """
        regions(...) returns the Object Regions

        :returns:  :class:`Regions`
        :rtype: string
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> regs = img.Regions()
        """
        try:
            return Regions.Regions(self.__image_semented) # (self.__get_regions())
        except MyException.MyException as e:
            print(e.args)
            return None


    def __get_regions(self):
        # apply thresholding
        val = filters.threshold_otsu(self.__image)
        # segmentation
        image_thresh = self.__image > val
        # returns the single segmented elements of the image
        image_segment = label(image_thresh)
        # removes the image elements at the borde
        return  clear_border(image_segment)


    #def __get_mask(self, redo=False):
    #    if redo == False:
    #        return self.__mask
    #    # ithresholding to build the map
    #    val = filters.threshold_otsu(self.__image)
    #    # cretes the mask
    #    return self.__image > val

    def __get_regionsprop(self):
        return regionprops(self.__get_regions(), intensity_image=self.__image_intensity)


    def get_image_segmentation(self):
        """
        Builds the image with mask overlay to show the segmentation

        :returns: The image in RGB format, in a 3-D array of shape (.., .., 3).
        :rtype: ndarray
        """
        try:
            return  label2rgb(self.__get_regions(), image=self.__image)
        except MyException.MyException as e:
            print(e.args)
            return None

    def features(self, features_list, prefix='', suffix=''):
        """
        Returns a table with all  values for the property names given in input, and supplies an
        additional parameter for feature classification

        :param features_list: list of property/measure names (e.g, 'area', 'centroid', etc )
        :type features_list: List
        :param prefix: prefix for features name
        :type prefix:  string
        :param suffix: prefix for features name
        :type suffix: string
        :returns: Features Object
        :rtype: Features Object
        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> feature = img.get_features(['label', 'area','perimeter', 'centroid'])
        """
        df = pd.DataFrame()
        try:
            #self.__regionsprops = self.__get_regionsprop()
            n = len(self.__regionsprops)
            df['id'] = range(0,n)
            for feature_name in features_list:
                values = self.prop_values(feature_name)
                Utils.insert_values(prefix + feature_name + suffix, df, values)

            return Features.Features(df)
        except Exception as e:
            print("one or more input labels might be wrong:{}".format(e))
            return None


    def prop_values(self, prop_name):
        """
        Measure the values of the specified  property/measure name (e.g., 'area') for all
        elements contained in the object Regions.

        :param prop_name: name of the property to measure (e.g, 'area')
        :type prop_name: string
        :returns:  property name  values
        :rtype: List

        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> regs = img.Regions()
        >>> areas = regs.prop_values('area')

        The following properties can be accessed as attributes or keys:

        **area** : int
            Number of pixels of region.
        **bbox** : tuple
            Bounding box ``(min_row, min_col, max_row, max_col)``.
            Pixels belonging to the bounding box are in the half-open interval
            ``[min_row; max_row)`` and ``[min_col; max_col)``.
        **bbox_area** : int
            Number of pixels of bounding box.
        **centroid** : array
            Centroid coordinate tuple ``(row, col)``.
        **convex_area** : int
            Number of pixels of convex hull image.
        **convex_image** : (H, J) ndarray
            Binary convex hull image which has the same size as bounding box.
        **coords** : (N, 2) ndarray
            Coordinate list ``(row, col)`` of the region.
        **eccentricity** : float
            Eccentricity of the ellipse that has the same second-moments as the
            region. The eccentricity is the ratio of the focal distance
            (distance between focal points) over the major axis length.
            The value is in the interval [0, 1).
            When it is 0, the ellipse becomes a circle.
        **equivalent_diameter** : float
            The diameter of a circle with the same area as the region.
        **euler_number** : int
            Euler characteristic of region. Computed as number of objects (= 1)
            subtracted by number of holes (8-connectivity).
        **extent** : float
            Ratio of pixels in the region to pixels in the total bounding box.
            Computed as ``area / (rows * cols)``
        **filled_area** : int
            Number of pixels of filled region.
        **filled_image** : (H, J) ndarray
            Binary region image with filled holes which has the same size as
            bounding box.
        **image** : (H, J) ndarray
            Sliced binary region image which has the same size as bounding box.
        **inertia_tensor** : (2, 2) ndarray
            Inertia tensor of the region for the rotation around its mass.
        **inertia_tensor_eigvals** : tuple
            The two eigen values of the inertia tensor in decreasing order.
        **intensity_image** : ndarray
            Image inside region bounding box.
        **label** : int
            The label in the labeled input image.
        **local_centroid** : array
            Centroid coordinate tuple ``(row, col)``, relative to region bounding
            box.
        **major_axis_length** : float
            The length of the major axis of the ellipse that has the same
            normalized second central moments as the region.
        **max_intensity** : float
            Value with the greatest intensity in the region.
        **mean_intensity** : float
            Value with the mean intensity in the region.
        **min_intensity** : float
            Value with the least intensity in the region.
        **minor_axis_length** : float
            The length of the minor axis of the ellipse that has the same
            normalized second central moments as the region.
        **moments** : (3, 3) ndarray
            Spatial moments up to 3rd order::
                m_ji = sum{ array(x, y) * x^j * y^i }
            where the sum is over the `x`, `y` coordinates of the region.
        **moments_central** : (3, 3) ndarray
            Central moments (translation invariant) up to 3rd order::
                mu_ji = sum{ array(x, y) * (x - x_c)^j * (y - y_c)^i }
            where the sum is over the `x`, `y` coordinates of the region,
            and `x_c` and `y_c` are the coordinates of the region's centroid.
        **moments_hu** : tuple
            Hu moments (translation, scale and rotation invariant).
        **moments_normalized** : (3, 3) ndarray
            Normalized moments (translation and scale invariant) up to 3rd order::
                nu_ji = mu_ji / m_00^[(i+j)/2 + 1]
            where `m_00` is the zeroth spatial moment.
        **orientation** : float
            Angle between the X-axis and the major axis of the ellipse that has
            the same second-moments as the region. Ranging from `-pi/2` to
            `pi/2` in counter-clockwise direction.
        **perimeter** : float
            Perimeter of object which approximates the contour as a line
            through the centers of border pixels using a 4-connectivity.
        **solidity** : float
            Ratio of pixels in the region to pixels of the convex hull image.
        **weighted_centroid** : array
            Centroid coordinate tuple ``(row, col)`` weighted with intensity
            image.
        **weighted_local_centroid** : array
            Centroid coordinate tuple ``(row, col)``, relative to region bounding
            box, weighted with intensity image.
        **weighted_moments** : (3, 3) ndarray
            Spatial moments of intensity image up to 3rd order::
                wm_ji = sum{ array(x, y) * x^j * y^i }
            where the sum is over the `x`, `y` coordinates of the region.
        **weighted_moments_central** : (3, 3) ndarray
            Central moments (translation invariant) of intensity image up to
            3rd order::
                wmu_ji = sum{ array(x, y) * (x - x_c)^j * (y - y_c)^i }
            where the sum is over the `x`, `y` coordinates of the region,
            and `x_c` and `y_c` are the coordinates of the region's weighted
            centroid.
        **weighted_moments_hu** : tuple
            Hu moments (translation, scale and rotation invariant) of intensity
            image.
        **weighted_moments_normalized** : (3, 3) ndarray
            Normalized moments (translation and scale invariant) of intensity
            image up to 3rd order::
                wnu_ji = wmu_ji / wm_00^[(i+j)/2 + 1]
            where ``wm_00`` is the zeroth spatial moment (intensity-weighted area).


        .. [1] http://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops
        """
        try:
            vals = []
            for i in self.__regionsprops:
                vals.append(getattr(i, prop_name))
            return vals
        except Exception as e:
            print(e.args)
            return None
