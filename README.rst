project-firewatch
===================

Team Members:
Dutch osbourne, Seth Wahle, Thuy Pham, Nick Hershey, Jason Cuneo

.. image:: https://travis-ci.org/osteth/project-firewatch.svg
   :target: https://travis-ci.org/osteth/project-firewatch

.. image:: https://coveralls.io/repos/mapbox/project-firewatch/badge.png
   :target: https://coveralls.io/r/mapbox/project-firewatch

2017 NASA Space Apps Challenge Submission for the `And YOU can Help Fight Fires! <https://2017.spaceappschallenge.org/challenges/warning-danger-ahead/and-you-can-help-fight-fires/details>`_ challenge.

Project-Firewatch integrates crowdsourced low-cost hardware fire monitors with `Fire Information for Resource Management System (FIRMS) <https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms>`_ from the MODIS satellite to 
provide users with granularly accurate yet highly encompassing wildfire information that is easily accessible.
   
.. image:: http://i.imgur.com/7tC5Ea5.png

.. raw:: html

    <embed>
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="//www.youtube.com/embed/89fEaPE4wlw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; 
        width: 100%; height: 100%;"></iframe>
    </div>
    </embed>



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


Command-line Interface
===========================
Project Firewatch Includes a Command-line Interface(CLI) to ensure easy use for non-technical personell as well as provide powerfull POSIX compliant
features needed by experienced systems administrators and highly techincal persons.

Commands
---------------------------
.. code-block:: console
Format:
projectfirewatch <commads><options><arguments>

	projectfirewatch --help

	projectfirewatch update
	projectfirewatch start	
	
	
CLI Development Roadmap
--------------------------- 
- [x] Build Basic CLI functionality.
- [x] Write fucntion to automaically download MODIS Data.
- [x] Write funtion to re-format MODIS data into a usable JSON format. 
- [x] Combine download and format function and add to CLI as update.
- [x] Improve Error resilience of update function.
- [x] Integrate API with CLI.
- [x] Integrate Map with CLI.
- [ ] Write unit tests.
- [ ] add periodic auto update of MODIS data to server function.
- [ ] Add Daemon functionality to CLI.
- [ ] make GUI extension??

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
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Brightness|Brightness temperature 21(Kelvin)  |Channel 21/22 brightness temperature of the fire pixel measured in Kelvin.          |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Scan	   |Along Scan pixel size              |The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge  |
|          |                                   |of the scan. Scan and track reflect actual pixel size.                              |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Track     |Along Track pixel size             |The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge  |
|          |                                   |of the scan. Scan and track reflect actual pixel size.                              |
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
|          |                                   |FIRMS data sourced from LANCE FIRMS and the University of Maryland.                 |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|Bright_T31|Brightness temperature 31 (Kelvin) |Channel 31 brightness temperature of the fire pixel measured in Kelvin.             |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|FRP       |Fire Radiative Power               |Depicts the pixel-integrated fire radiative power in MW (megawatts).                |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|DayNight  |Day / Night                        | D = Daytime, N = Nighttime                                                         |
+----------+-----------------------------------+------------------------------------------------------------------------------------+



Requests
---------------------------

+----------+-----------------------------------+------------------------------------------------------------------------------------+
|requests  |modifiers                          |Long Description                                                                    |
+==========+===================================+====================================================================================+
|lat       |plus                               |/api/?lat=43.6271&plus=10&minus=10                                                  |
|          |minus                              |results filteres to a latitude plus and minus a given location.                     |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|lon       |plus                               |/api/?lat=43.6271&plus=10&minus=10                                                  |
|          |minus                              |results filteres to a longitude plus and minus a given location.                    |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|scan-min  |                                   |/api/?scan-min=1                                                                    |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|scan-max  |                                   |/api/?scan-max=2                                                                    |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|track-min |                                   |/api/?track-min=1                                                                   |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|track-max |                                   |/api/?track-max=2                                                                   |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|date      |end                                |/api/?date=<julian begin date>&end=<julian end date>                                |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|time      |until                              |/api/?time=0255&until=2250   (in UTC and military time).                            |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|onland    |                                   |/api/?onland=True                                                                   |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|confidence|                                   |/api/?confidence=65    (sets minimum confidence of results)                         |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|frp       |                                   |/api/?frp=16    (sets minimum power of results in megawatts).                       |
+----------+-----------------------------------+------------------------------------------------------------------------------------+
|day       |                                   |/api/?onland=True                                                                   |
+----------+-----------------------------------+------------------------------------------------------------------------------------+

API Development Roadmap
--------------------------
- [x] Get basic FlaskAPI functionality working.
- [x] Get pretty FlaskAPI markdown displayer working.
- [x] Figure out how to get MODIS data and.
- [x] Pull in MODIS data from flat file.	
- [x] Allow user to dump all MODIS data at request. 
- [ ] Write Unit Tests
- [ ] Switch over to DB from flat file.
- [ ] Create specfication for MODIS data queries. 
- [ ] Expand API to allow for data filtering.
- [ ] Create Specification for Sensor Data.
- [ ] Expand API to allow writing of sensor data to DB.
- [ ] Expand API to allow querying of sensor data.


Map
==========================
The map displays all known satellite discovered wildfires as well as the location and status of all active sensors. 

.. image:: https://i.imgur.com/RQYuLHp.png
.. image:: https://i.imgur.com/1v6zC9t.png

Map Development Roadmap
--------------------------
- [x] Basic Map Functionality.
- [x] Display a pin and circle.
- [x] figure out radius expansion algorithm to accuratly display MODIS satellite data.
- [x] Display mock sensor data. 
- [x] Integrate with CLI. 
- [ ] Get Map to display all MODIS fire Data .
- [ ] Migrate from flat file to DB.
- [ ] Display all live sensor data. 
- [ ] Allow user to specify a focus location.
- [ ] Attempt to pull cell phone GPS location and use it as users locaion.


Sensors
==========================
We put together prototype hardware sensors for the competition that anyone can build and contribute crowdsourced Fire data back to our database via the Project-Firewatch API.

.. image:: http://i.imgur.com/L6rXVhw.jpg

.. image:: http://i.imgur.com/JxMAmRT.jpg

.. image:: http://i.imgur.com/35RY8X0.jpg

Bill of Materials
-------------------------

`Orange pi zero <https://www.aliexpress.com/store/product/New-Orange-Pi-Zero-H2-Quad-Core-Open-source-development-board-beyond-Raspberry-Pi/1553371_32760774493.html?spm=2114.12010108.0.0.RDPr6Z>`_ - $6.99

`4GB SD Card (class 10 speeds are needed for OS operability) <https://www.newegg.com/Product/Product.aspx?Item=9SIA6NC5CC2119&ignorebbr=1&nm_mc=KNC-GoogleMKP-PC&cm_mmc=KNC-GoogleMKP-PC-_-pla-_-Memory+%28Flash+Memory%29-_-9SIA6NC5CC2119&gclid=Cj0KEQjw0IvIBRDF0Yzq4qGE4IwBEiQATMQlMQhSEr8pf6-Yb8otvqncwqoa5_r9YIP59DElH3ynFrAaAtl58P8HAQ&gclsrc=aw.ds>`_ - $2.49

`AC-DC converter/ Power Regulator <http://www.hlktech.net/product_detail.php?ProId=60>`_ - $3.00

`Plug-in Enclosure <https://www.polycase.com/gs-2415>`_ - $5.17

`Keyes Flame Detection Sensor Module for Arduino <http://www.dx.com/p/arduino-flame-detection-sensor-module-135038#.WQQEg9LythE>`_ - $2.66

`KEYES DHT11 Digital Temperature Humidity Sensor Module for Arduino <http://www.gearbest.com/sensors/pp_218522.html>`_ - $1.59

Total prototype parts cost: $21.90

Operating System
--------------------------
for the prototype sensors we utilized the ARMBIAN Orange Pi Zero build available `Here`<https://dl.armbian.com/orangepizero/Ubuntu_xenial_default.7z>
