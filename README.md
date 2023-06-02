# Bangrad radical music discovery
Bangrad is a place for music connoisseurs, hobby musicians and anyone looking to search
the Spotify database for a particular track based on its tempo, musical key, location, language,
popularity, release year and more. The large spotify database, sometimes called the jukebox
of the universe, had in fact in 2023 around 80 million tracks to choose from.

![Bangrad Home page](https://github.com/ThomasSpare/Bangrad/blob/bangrad2/images/bangrad%20home.jpg)
## Features

### search queries

The user can make searches in the database based on only one or several parameters combined.
Which gives the user a powerful tool for doing very specialized searches. The search will
return a list for the user with the search queries and display the artists, songs that are
matching and links to the respective spotify tracks.

### List gallery

After each search the user can choose to save the list in their profile gallery. The user can arrange
the saved list in folders of their choice. The user can for instance create a folder called
dancefloor bangers and inside this folder create more folders with names of their choice.

### Profile Page
Here the user can enter after registering. The user can upload a photo and write a short bio. They can
also create folders with links to songs they want to save. After setting up a profile the user can also
post and comment in the lodge forums. 

### The Lodge

The lodge is where users can meet and exchange artists they've discovered and share their links and saved lists.
All registered users can comment in the forums. 

# DEBUGGING AND TECHNICAL ISSUES

This project had a bad turn in the end as I had to delete my whole user registration folder called 'users'
as this was causing a major conflict and caused errors I could not correct. This error stopped the project
completely and I had to revert to using allauth templates in the last days before submission.
The user could not register, the forum did not work anymore nor did the profile page. 

![Error 1](https://github.com/ThomasSpare/Bangrad/blob/bangrad2/images/save%20%20force%20argument%20probably%20todo%20with%20the%20username%20issue%20in%20users-%20views.jpg)

I also had to reset my databases several times during the build.

![Database reset](https://github.com/ThomasSpare/Bangrad/blob/bangrad2/images/last%20error.jpg)


## Code Sources
I started building the user registraion from the start using this guide.
https://www.devhandbook.com/django/user-registration/






A frequent error also I had was when I logged in and tried entering the profile page I received
this error message.



# THE SPOTIPY API

I managed to have the spotipy api working on the site. The user will be prompted when entering the site to authorize
his/her spotify account. I had the credentials and secret keys stored in the env.py but could not link these up to the API.
So when having been authorized the user can search in the round search field and hit enter. The results will be collected in
rows beneath. The thought was that the user could then copy the links directly in the results and add in forums to recommend 
new finds and favorite artists.

As I wanted to integrate the Spotipy API I followed this simple method to use a sript.js file in the Static folder
to run the API from. 
- https://www.youtube.com/watch?v=d0FFlTeyAY8
- https://github.com/mujibsardar/spotify_jquery_only/blob/master/script.js

### STEPS
- To have the API working I had to first create the app at https://developer.spotify.com/
- Using the address for my homepage https://bangrad.herokuapp.com (without the '/' at the end)
I put this in my redirect URI at my app settings in Spotify for developers.
- then this same address has to be inserted in the script.js file redirect URI as encoded
so using this site to encode it
https://www.url-encode-decode.com/
I get this redirect URI address in my script.js file.
https%3A%2F%2Fbangrad.herokuapp.com

- the script.js is lastly inserted in the base.html as <script>

- The Spotipy API is now linked up 

# DEPLOYMENT

I used Heroku to deploy my site in the following steps:

- In settings.py set DEBUG: False
- Final git Push from Code Anywhere
- delete DISABLE_COOLECTSTATIC in Heroku config Vars
- Deploy branch from Heroku



# Technologies and Languages used

- ### Code Anywhere IDE
- ### Django
- ### JQuery
- ### SPOTPY API (python library)
- ### Bootstrap


# Testing
## As time ran out I did not have much time to write and go through all testing such as lighthouse and PEP8 validation.
I had alot of technical issues as descibed above.

# USER STORIES

- As a user I want to search for music and share my finds with others
- As a user I can Search for music
- As a user I can post links from searches in the forums
- As a user I can posts comments on threads in the forum
- As a user I can create a profile and edit it (does not work)
- As an admin I can create, edit and delete user from the admin panel
- As an admin I can delete comments in the forum
- As an admin I can delete threads in the forum
- As an admin i can see information about the users in the admin panel


# FUTURE IMPROVEMENTS

In the user profile page the user could be able to create more advanced setups. For
instance be able to create folders, name these and fill these with links to music they want to store.
They could then grant access to these fodlers or share them with other user in the forum.

Desgin of forum and overall site could be better. As I didnt have the time to properly go through the layout of the forum.

Add advanced search query functionality to the spotipy endpoint. The endpoint in script.js
can be changed to search for more specific information for music such as tempo, musical keys, danceabilty, popularity, language, 
locations and much more.

The spotify credentials should be linked up so that the user dont need to grant the site permission every time.


# Special thanks

To tutor support for helping out daily to try and solve the issues. I wouldnt have come as far as I did without it.







