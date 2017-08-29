.. image features extraction documentation master file, created by
   sphinx-quickstart on Mon Aug 14 17:04:45 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Image Features Extraction
============================

This package allows the fast extraction and classification of features  from a set of images.  The resulting
table can be used as training set for a machine learning classifier


.. image:: _static/1.png
   :width: 600px
   :alt: alternate text


The package was originally developed to extract measurements of single cell nuclei from microscopy images (see figure above).
The package can be used to extract features from any set of images for a variety of applications.
Below it is shown a map of Boston used for city density and demographic models.


.. image:: _static/8.png
   :width: 600px
   :alt: alternate text


The image below shows a possible workflow for image feature extraction: two sets of images
with different classification labels are used to produce two data sets for training and testing a classifier


.. image:: _static/2b.png
  :width: 600px
  :alt: alternate text


The image features extraction package  was developed using  the  document object model architecture shown below

.. image:: _static/3b.png
  :width: 600px
  :alt: alternate text

The object 'Image' includes the function Voronoi(), which returns the object Voronoi of my package Voronoi_Features.
The Voronoi object can be used to measure the voronoi tassels of each image regions. It includes >30 measurements.
Below an example of voronoi diagrams from the image shown above

.. image:: _static/09.png
  :width: 600px
  :alt: alternate text

.. image:: _static/10.png
  :width: 600px
  :alt: alternate text

.. image:: _static/voro3.png
  :width: 600px
  :alt: alternate text

.. image:: _static/voro4.png
  :width: 600px
  :alt: alternate text


.. image:: _static/12.png
  :width: 600px
  :alt: alternate text

.. image:: _static/13.png
  :width: 600px
  :alt: alternate text

.. image:: _static/14.png
  :width: 600px
  :alt: alternate text


See classes/modules documentation for more details about the use of the package



Contents:
============

.. toctree::
   :maxdepth: 2

   tutorial.rst
   code.rst
