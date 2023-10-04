# Bangrad radical music discovery
The intent for creating the Bangrad site was to make a platform to make it easy and fun to share music.
![Bangrad Home page](https://github.com/ThomasSpare/Bangrad/blob/bangrad2/images/home_page_cover.jpg)
![Bangrad Home page](https://github.com/ThomasSpare/Bangrad/blob/bangrad2/images/home_page_cover2.jpg)
## Features

### search queries

The spotify search field was from the start a feature intended to be used for users to use when posting in the forum. 
From the spotify search results the users can copy the link for a particular track they want to share in the forum.
The songs can be played from the site and opened in the spotify app if the user wants to get more info.  

### Profile Page
Here the user can enter after succesfuly registering. The user can upload profile image and write a short bio. They can also
add links to personal social media and various other accounts and 2 websites. These links will also display under the
forum author in the forums. 

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

The lodge is where users can meet and exchange artists they've discovered and share links to music.
The user has to register in order to access the forum. 


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

# Debugging
1. Ckeditor not working after deployment to Heroku
The ability to style the posts in the form is not possible after deployment to Heroku.
Source of this error: Unkown 

## Deployment

###  Creating Database using ElephantSQL

1. To generate a managed PostgreSQL database, please proceed to [ElephantSQL](https://customer.elephantsql.com/) and either sign up or sign in to your account. Once you've logged in, click on the 'Create New Instance' button.

2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'

3. Select your preferred region and create the database instance.
- After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section on the following page, copy the PostgreSQL URL.


### Deploying the website in Heroko
- Before deploying in Heroku following files were created:
  1. env.py : stores confidential data eg. API keys, passwords etc.

  2. Procfile : Very important for deployment and must be added with capital P
  
  3. Requirements.txt: This must be updated for deployment in Heroku. It stores data of libraries used for project


- The website was deployed to Heroko using following steps:

#### Login or create an account at Heroku

- Make an account in Heroko and login

#### Creating an app

- Create new app in the top right of the screen and add an app name.
- Select region
- Then click "create app".

#### Open settings Tab

##### Click on config var

- Store CLOUDINARY_URL file from in key and add the values
- Store DATABASE_URL file from in key and add the values
- Store SECRET_KEY file from in key and add the values
- Store PORT in key and value

NOTE: For initial deployment DISABLE_COLLECTSTATIC was also added

##### Add Buildpacks

- Add python buildpack first
- Add Nodejs buildpack after that

#### Open Deploy Tab

##### Choose deployment method

- Connect GITHUB
- Login if prompted

##### Connect to Github

- Choose repositories you want to connect
- Click "Connect"


##### Automatic and Manual deploy

- Choose a method to deploy
- After Deploy is clicked it will install various file


##### Initial Deployment

- Project was deployed in Heroku without content: Initial Deployment


##### Final Deployment

- A view button will display
- Once clicked the website will open

### Forking the GitHub Repository

1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
4. [GitHub Repository](https://github.com/ThomasSpare/Bangrad)

### Cloning the repository in GitHub

1. Visit the GitHub page of the website's repository
2. Click the “Clone” button on top of the page
3. Click on “HTTPS”
4. Click on the copy button next to the link to copy it
5. Open your IDE
6. Type `git clone <copied URL>` into the terminal

# Technologies and Languages used

- ### Code Anywhere IDE
- ### Django
- ### JQuery
- ### SPOTPY API (python library)
- ### Bootstrap


# Testing
1. see separate TESTING.md 

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







