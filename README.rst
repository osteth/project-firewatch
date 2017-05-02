project-firewatch
======

Team Members:
Dutch
Seth Wahle
Thuy Pham
Nick Hershey
Jason Cuneo

.. image:: https://travis-ci.org/osteth/project-firewatch.svg
   :target: https://travis-ci.org/osteth/project-firewatch

.. image:: https://coveralls.io/repos/mapbox/project-firewatch/badge.png
   :target: https://coveralls.io/r/mapbox/project-firewatch

NASA Space Apps Challenge Submission for the `And YOU can Help Fight Fires! <https://2017.spaceappschallenge.org/challenges/warning-danger-ahead/and-you-can-help-fight-fires/details>`_ challenge.

Project-Firewatch integrates crowd sourced low cost hardware fire monitors with `Fire Information for Resource Management System (FIRMS) <https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms>`_ from the MODIS satelite to 
provide users with granularly accurate yet highly encompasing wildfire information that is easily accessable.
   
.. image:: http://i.imgur.com/7tC5Ea5.png

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/89fEaPE4wlw?rel=0&amp;showinfo=0" frameborder="0"      allowfullscreen></iframe>
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

Finally, give the command line program a try.

.. code-block:: console

    project-firewatch --help
    project-firewatch 4

Sensors
-------------------
We put together prototype hardware sensors for the competeition that anyone can build and contribute their crowdsource Fire data back to our database via the Project-Firewatch API.

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
