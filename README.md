# Tinder Trails



## Concept
We would like to create a Hiking Trail App for hikers. The users can login or visit as a guest to our web server and filter their preference about trails such as the level of the trails, the proximity, and hiking equipment, etc. Then, we'll provide the best trails for user according to their decisions.

## Team Members
Chris Hernandez, Claudia Caceres, Joseph Gorfinkle, Wan-Fang Chou

## Instructions to Edit the Files in Your Own Machine
1. Clone the folders and the files on GitHub.

    `$ git clone https://github.com/wanfangchou/tindertrails-project.git`

2. Create Virtual Environment

    Install virtual environment:

    `$ pip3 install virtualenv`

    Create virtual environment named "myvenv":

    `$ virtualenv myvenv`
    or
    `$ virtualenv --python=python3 myvenv`

    Activate the virtual environment:

    `$ source myvenv/bin/activate`

3. Install the packages you need

    `(myvenv)$ pip install -r requirements.txt`

4. Run the server on your machine

    `(myvenv)$ python manage.py runserver`

    The website can be accessed at `http://127.0.0.1:8000`

## Running Tests

Activate your virtualenv as shown above and type `pytest` to run tests.

## Tinder Trails admin

username: tindertrails

password: ist303tindertrails

## User Stories and requirements

1.  As a user I want to __log in__ so that I can save my records or favorite trails. (estimate of completion time: __4 days__)

    TASK TO BE COMPLETED IN MILESTONE #1 - ITERATION #1

    a) Using django create a log in authentication template and page which can be linked to from our home page

    b) Using django return the logged in user back to the home page with 'logged-in' flag

2.	As a Hiker I want to __find trails near me__ so that I can quickly begin my hike (estimation of completion time: __4 days__)

    TASKS TO BE COMPLETED IN MILESTONE #1 - ITERATION #1

    a)	On the Home page Create a __find trails near me__ button which links to geolocation code

    b)  The geolocation code returns the user's location

    TASKS TO BE COMPLETED IN MILESTONE #1 - ITERATION #2

    c)	Use the current location to query the ArcGIS database to find local trails

    d)	Ensure the trail information has been loaded to ArcGIS: http://agis.maps.arcgis.com/apps/webappviewer/index.html?id=38dfd1e1f2f14d87a06671e88e4f1ab6

    e)	Pass information from ArcGIS to web server application

    f)	Web server calls the Map API and displays the local trail

    g)	The web application then provides the user the ability to choose a trail or go back to the main page

 ALLOCATED TASKS PER MEMBER:

    Wan-Fang:    Task 2a, 2g

    Claudia:    Task 2d, 2e

    Chris:      Task 2b, 2c

    Joe:        Task 1a, 1b, 2f

  MEETINGS 2X / WEEK - SUNDAY 1PM and WEDNESDAY 9:45PM
  TEST ENVIRONMENT BEING DEVELOPED ALONGSIDE CODE

  MILESTONE 2 - USER STORIES

3.	As a Hiker I want to __find an easy trail__ so that I can enjoy my hike (estimate of completion time: __4 days__)

4.	As a Hiker I want to __find a challenging trail__ so that I can start my hike (estimate of completion time: __3 days__)

5.	As a Hiker I want to __know the elevation profile of a trail__ so that I can be prepared before I go hiking (estimate of completion time: __3 days__)

6.	As a Hiker I want to __find dog/kids friendly trails__ so that I can hike with my dog/kids (estimate of completion time: __3 days__)

6.5	As a Hiker I want to __find ADA accessible trails__ so that I can hike with disabled fellows (estimate of completion time: __2 days__)

7.	As a Hiker I want to __view operation of a trail__ so that I can hike when the trail is available (estimate of completion time: __2 days__)

8. As a Hiker I want to __find trails with wildlife__ so that I can view wildlife while I hike (estimate of completion time: __2 days__)

9.	As a Hiker I want to __find trails with restrooms__ so that I can use it before I hike (estimate of completion time: __2 day__)

10.	As a Hiker I want to __know the length of a trail__ so that I can hike within my allotted time (estimate of completion time: __2 days__)

11.	As a Hiker I want to __find all trails__ so that I can see which trails are available (estimate of completion time: __1 day__)

12. As a Hiker I want to __add a trail__ so that I can give other user's the ability to find trails I enjoy.
    TASKS

    a) Only the users who logged in could see the add a trail button

    b) Users could have two choices for adding a trail

    c) 1. Add the trail on the website directly

    d) Users could click the button to connect to Tinder Trails of ArcGIS app section

    e) Let users add a trail directly on the map

    f) 2. Upload a file and we will help users add a trail on the map

    g) File types users could upload: shapefile, .csv, .gpx, .xml, GeoJSON

    h) File is stored in Django

    g) We could check the uploaded file and use the information inside to add a trail on our ArcGIS server


Milestone #1 Burn_Down Chart and .PPT
url: https://github.com/wanfangchou/tindertrails-project/blob/master/Burn_Chart_4_3_2019.PNG
url: https://github.com/wanfangchou/tindertrails-project/blob/master/Hiking%20Trail%20App%20Milestone1.pptx
