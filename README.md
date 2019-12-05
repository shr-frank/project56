# Squirrel Tracker Web App

This is a Squirrel Tracker that used the open source data to establish a database of squirrels in Central Park and show them in the map.
User can add, update, delete information about squirrel sightings. 

## Functions

We provide two management commands:

* Import squirrel data:
  * Import a csv file to the database

* Export squirrel data:
  * Export squirrel data to csv file

## Views

There are six views in the web app:

* Map
  * Located at: */map*
  * Shows the map of central park with squirrel sightings on it

* List Sightings
  * Located at: */sightings*
  * Shows the list of squirrel sightings

* Update Sightings
  * Located at: */sightings/<unique-squirrel-id>*
  * Edit the sightings of the squirrel of the unique squirrel id

* Delete Sightings
  * Located at: */sightings/<unique-squirrel-id>*
  * Delete the sightings of the squirrel of the unique squirrel id

* Creation Settings
  * Located at: */sightings/add*
  * Add new sightings 
  * Fields supported: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, 
Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, 
Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent, Runs from

*  Sightings Stats
  * Located at: */sightings/stats*
  * Shows several stats about the squirrel sightings

### Group name

Project Group 56, Section 2

### UNIs

UNIs:[hs3153, yy3013]

### Link to the server

https://robotic-epoch-255500.appspot.com



