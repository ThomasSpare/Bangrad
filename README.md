# Bangrad radical music discovery
The intent for creating the Bangrad site was to make a platform to make it easy and fun to share music.
![Bangrad Home page](https://github.com/ThomasSpare/Bangrad/blob/bangrad2/images/home_page_cover.jpg)
![Bangrad Home page](https://github.com/ThomasSpare/Bangrad/blob/bangrad2/images/home_page_cover2.jpg)
## Features

### search queries

The search will return a list for the user with the search queries and display the artists, songs that are
matching and if the user clickes on ... the links to the respective spotify tracks will appear and the user can copy
this link directly and paste it in a new forum post.

### Profile Page
Here the user can enter after registering. The user can upload a photo and write a short bio. They can
also create folders with links to songs they want to save. After setting up a profile the user can also
post and comment in the lodge forums. 

### The Lodge Forum

The lodge is where users can meet and exchange artists they've discovered and share links to music.
The user has to register in order to access the forum. 


# THE SPOTIPY API

I managed to have the spotipy api working on the site. The user will be prompted when entering the site to authorize
his/her spotify account. I had the credentials and secret keys stored in the env.py but could not link these up to the API.
So when having been authorized the user can search in the round search field and hit enter. The results will be collected in
rows beneath. The thought was that the user could then copy the links directly in the results and add in forums to recommend 
new finds and favorite artists.

# DEPLOYMENT

# Wireframes



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

## Code Anywhere IDE
## Django
## JQuery
## SPOTPY API (python library)
## Bootstrap


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







