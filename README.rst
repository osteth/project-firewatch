project-firewatch
======

contributors:
Dutch
Seth
Thuy
Nick
Travis

.. image:: https://travis-ci.org/osteth/project-firewatch.svg
   :target: https://travis-ci.org/osteth/project-firewatch

.. image:: https://coveralls.io/repos/mapbox/project-firewatch/badge.png
   :target: https://coveralls.io/r/mapbox/project-firewatch

NASA Space Apps Challenge Submission for  .. _And YOU can Help Fight Fires!: https://2017.spaceappschallenge.org/challenges/warning-danger-ahead/and-you-can-help-fight-fires/details challenge.

Project-Firewatch integrates crowd sourced low cost hardware fire monitors with .. _Fire Information for Resource Management System (FIRMS): https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms to 
provide users with granularly accurate yet highly encompasing wildfire information that is easily accessable.
   
.. image:: https://raw.github.com/osteth/project-firewatch/blob/master/images/project-firewatch-logo.png

.. contents:: **Table of Contents**
  :backlinks: none

Quick start
-------------------------

To use project-firewatch as the start of a new project, do the following, preferably in
a virtual environment. Clone the repo.

.. code-block:: console

    https://github.com/osteth/project-firewatch.git

Then install in locally editable (``-e``) mode and run the tests.

.. code-block:: console

    pip install -e .[test]
    py.test

Finally, give the command line program a try.

.. code-block:: console

    project-firewatch --help
    project-firewatch 4

Hardware Parts List
-------------------
.. _Orange pi zero - $6.99: https://www.aliexpress.com/store/product/New-Orange-Pi-Zero-H2-Quad-Core-Open-source-development-board-beyond-Raspberry-Pi/1553371_32760774493.html?spm=2114.12010108.0.0.RDPr6Z

.. _4GB SD Card (class 10 speeds are needed for OS operability) $2.49: https://www.newegg.com/Product/Product.aspx?Item=9SIA6NC5CC2119&ignorebbr=1&nm_mc=KNC-GoogleMKP-PC&cm_mmc=KNC-GoogleMKP-PC-_-pla-_-Memory+%28Flash+Memory%29-_-9SIA6NC5CC2119&gclid=Cj0KEQjw0IvIBRDF0Yzq4qGE4IwBEiQATMQlMQhSEr8pf6-Yb8otvqncwqoa5_r9YIP59DElH3ynFrAaAtl58P8HAQ&gclsrc=aw.ds

.. _ AC-DC converter/ Power Regulator $3.00: http://www.hlktech.net/product_detail.php?ProId=60

.. _Plug-in Enclosure $5.17: https://www.polycase.com/gs-2415

.. _Keyes Flame Detection Sensor Module for Arduino $2.66: http://www.dx.com/p/arduino-flame-detection-sensor-module-135038#.WQQEg9LythE

.. _KEYES DHT11 Digital Temperature Humidity Sensor Module for Arduino $1.59: http://www.gearbest.com/sensors/pp_218522.html

Total prototype parts cost: $21.90
