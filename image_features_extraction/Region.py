from image_features_extraction import MyException


class Region(object):
    """
    Object refering to a single image region
    """
    def __init__(self, obj_region):
        if obj_region is None:
            raise MyException.MyException
        self.__obj_region = obj_region


    def prop_value(self, prop_name):
        """
        Measure  the specified  property name (e.g., 'area')

        :param prop_name: name of the property to measure (e.g, 'area')
        :type prop_name: string
        :returns: value of the property name
        :rtype: int,float,list

        :example:
        >>> import image_features_extraction as fe
        >>> imgs = fe.Images(folder_name)
        >>> img = imgs.item(1)
        >>> regs = img.Regions()
        >>> reg = regs.Region()
        >>> area = reg.prop_value('area')

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
        """
        try:
            return getattr(self.__obj_region, prop_name)
        except Exception as e:
            print(e.args)
            return None
