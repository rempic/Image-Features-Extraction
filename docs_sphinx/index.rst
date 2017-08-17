.. image features extraction documentation master file, created by
   sphinx-quickstart on Mon Aug 14 17:04:45 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Image Features Extraction
============================

This package allows the fast extraction and classification of features  from a set of images. Then the resulting
table can be used as training set for a classification machine learning model

The package was originally developed to extract measurements of single cell nuclei from microscopy images
(see figure below), but it can be used to extract features from any set of images.

.. image:: _static/1.png
   :width: 600px
   :alt: alternate text

Below it is shown an example of an image with triangular shapes obtained  from Google, which features were extracted
by using  the  image features extraction package  to build a training set for a machine learning classifier

.. image:: _static/7c.png
  :width: 500px
  :alt: alternate text

The image below show a possible workflow for the image features extraction package where two sets of images
with different labels were  extracted and returned in a table. Then the table can be used as training set to train
a machine learning classifier

.. image:: _static/2b.png
  :width: 600px
  :alt: alternate text

The image features extraction package  has a  document object model architecture (shown below)

.. image:: _static/3b.png
  :width: 600px
  :alt: alternate text

See classes/modules documentation for more details about the package code



Contents:
============

.. toctree::
   :maxdepth: 2

   tutorial.rst
   code.rst
