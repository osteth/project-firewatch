project-firewatch
======

Team Members:
Dutch, Seth Wahle, Thuy Pham, Nick Hershey, Jason Cuneo

.. image:: https://travis-ci.org/osteth/project-firewatch.svg
   :target: https://travis-ci.org/osteth/project-firewatch

.. image:: https://coveralls.io/repos/mapbox/project-firewatch/badge.png
   :target: https://coveralls.io/r/mapbox/project-firewatch

NASA Space Apps Challenge Submission for the `And YOU can Help Fight Fires! <https://2017.spaceappschallenge.org/challenges/warning-danger-ahead/and-you-can-help-fight-fires/details>`_ challenge.

Project-Firewatch integrates crowdsourced low-cost hardware fire monitors with `Fire Information for Resource Management System (FIRMS) <https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms>`_ from the MODIS satellite to 
provide users with granularly accurate yet highly encompassing wildfire information that is easily accessible.
   
.. image:: http://i.imgur.com/7tC5Ea5.png

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="//www.youtube.com/embed/89fEaPE4wlw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

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
	#tests arent yet written and will fail.

Finally, give the command line program a try.

.. code-block:: console

    projectfirewatch --help
    projectfirewatch update
	projectfirewatch start
	
API
==========================

Data Explanation
--------------------------
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Attribute |Short Description                  |Long Description                                                                    |
+==========+===================================+====================================================================================+
|Latitude  |Latitude                           |Center of 1km fire pixel but not necessarily the actual location of                 | 
|          |                                   |the fire as one or more fires can be detected within the 1km pixel.                 |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Longitude |Longitude                          |Center of 1km fire pixel but not necessarily the actual location of                 |
|          |                                   |the fire as one or more fires can be detected within the 1km pixel.                 |
+----------------------------------------------+------------------------------------------------------------------------------------+
|Brightness|Brightness temperature 21          |(Kelvin) |Channel 21/22 brightness temperature of the fire pixel measured in Kelvin.|
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Scan	   |Along Scan pixel size              |The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge  |
|          |                                   |of scan. Scan and track reflect actual pixel size.                                  |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Track     |Along Track pixel size             |The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge  |
|          |                                   |of scan. Scan and track reflect actual pixel size.                                  |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Acq_Date  |Acquisition Date                   |Date of MODIS acquisition.                                                          |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Acq_Time  |Acquisition Time                   |Time of acquisition/overpass of the satellite (in UTC).                             |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Satellite |Satellite                          |A = Aqua and T = Terra.                                                             |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Confidence|Confidence (0-100%)                |This value is based on a collection of intermediate algorithm quantities used in    |
|          |                                   |the detection process. It is intended to help users gauge the quality of individual |
|          |                                   |hotspot/fire pixels. Confidence estimates range between 0 and 100% and are assigned |
|          |                                   |one of the three fire classes (low-confidence fire, nominal-confidence fire, or     |
|          |                                   |high-confidence fire).                                                              |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Version   |Version (Collection and source)    |Version identifies the collection (e.g. MODIS Collection 6) and source of data      |
|          |                                   |processing: Near Real-Time (NRT suffix added to collection) or Standard Processing  |
|          |                                   |(collection only). "6.0NRT" - Collection 6 NRT processing. "6.0" - Collection 6     |
|          |                                   |Standard processing. Find out more on collections and on the differences between    |
|          |                                   |FIRMS data sourced from LANCE FIRMS and University of Maryland.                     |
+----------|-----------------------------------+------------------------------------------------------------------------------------+
|Bright_T31|Brightness temperature 31 (Kelvin) |Channel 31 brightness temperature of the fire pixel measured in Kelvin.             |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|FRP       |Fire Radiative Power               |Depicts the pixel-integrated fire radiative power in MW (megawatts).                |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|DayNight  |Day / Night                        | D = Daytime, N = Nighttime                                                         |
+----------+-----------------------------------+------------------------------------------------------------------------------------+

Requests
---------------------------


Sensors
-------------------
We put together prototype hardware sensors for the competition that anyone can build and contribute crowdsourced Fire data back to our database via the Project-Firewatch API.

.. image:: http://i.imgur.com/L6rXVhw.jpg

.. image:: http://i.imgur.com/JxMAmRT.jpg

.. image:: http://i.imgur.com/35RY8X0.jpg

`Orange pi zero <https://www.aliexpress.com/store/product/New-Orange-Pi-Zero-H2-Quad-Core-Open-source-development-board-beyond-Raspberry-Pi/1553371_32760774493.html?spm=2114.12010108.0.0.RDPr6Z>`_ - $6.99

`4GB SD Card (class 10 speeds are needed for OS operability) <https://www.newegg.com/Product/Product.aspx?Item=9SIA6NC5CC2119&ignorebbr=1&nm_mc=KNC-GoogleMKP-PC&cm_mmc=KNC-GoogleMKP-PC-_-pla-_-Memory+%28Flash+Memory%29-_-9SIA6NC5CC2119&gclid=Cj0KEQjw0IvIBRDF0Yzq4qGE4IwBEiQATMQlMQhSEr8pf6-Yb8otvqncwqoa5_r9YIP59DElH3ynFrAaAtl58P8HAQ&gclsrc=aw.ds>`_ - $2.49

`AC-DC converter/ Power Regulator <http://www.hlktech.net/product_detail.php?ProId=60>`_ - $3.00

`Plug-in Enclosure <https://www.polycase.com/gs-2415>`_ - $5.17

`Keyes Flame Detection Sensor Module for Arduino <http://www.dx.com/p/arduino-flame-detection-sensor-module-135038#.WQQEg9LythE>`_ - $2.66

`KEYES DHT11 Digital Temperature Humidity Sensor Module for Arduino <http://www.gearbest.com/sensors/pp_218522.html>`_ - $1.59

Total prototype parts cost: $21.90
