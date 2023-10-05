# Bangrad - Share the music

Bangrad is a music sharing site where users can recommend music and connect with other users. A user can create a unique
profile and find all other users on the site. The site has a forum where most of the activity is going on.
The site is also wired up to the Spotify library from the home page so its possible to search for a track directly
on the site, making it easy to copy the link from a track directly and paste in the forum. This is the whole idea
of the forum, that users should share the music. The forum works so that to make a post you also has to post a link to
some music. 

![Bangrad Home page](https://res.cloudinary.com/djunroohl/image/upload/v1696541151/pfnlefttcxkyao51avfu.png)

# Features

### Track Search

The spotify search field was from the start a feature intended to be used for users to use when posting in the forum. 
From the spotify search results the users can then copy the link for a particular track they want to share in the forum. 
(if they press ... on the track a link will appear).
The songs can be played from the site and opened in the spotify app if the user wants to get more info. 

### Profile Page
Here the user can enter after succesfully registering. The user can upload profile image and write a short bio. They can also
add links to personal social media and various other accounts and 2 websites. These links will also display under the
forum author in the forums. 

### The Forum

The forum is where users can meet and exchange artists and music they've discovered and share links and create posts.
All registered users can also comment in the forums. 

### CKEDITOR

In the forum the users have a many choices for how they like their posts to look. With ckeditor in the form the user can insert
images from img links and a whole lot of styling to make the post and the forum more interesting and engaging.

### Memberlist

If the user is registered the members tab is visible in the navbar. If the user navigates to members, all registered users on the site
will be listed and the user can then access any users profilepage to learn more about them by clicking on each member.


# DEBUGGING AND TECHNICAL ISSUES

I had some difficulty getting ckeditor to work after deployment to heroku. In development it worked just fine
when making forum posts but when deployed it would not show up in the body field of the forum form.
I believe the source to this was that ckeditor somehow ended up in STATICFILES storage instead of the ordinary STATIC
storage after deployment.
## Solution:
I installed whitenoise and did the recommended changes in setting.py together with a script for ckeditor in the addinlodge 
template to solve this issue (I found this script from reading the ckeditor docs )
https://ckeditor.com/docs/ckeditor5/latest/installation/getting-started/quick-start-other.html#running-the-editor-2



## Code Sources
I started building the user registraion from the start using this guide.
https://www.devhandbook.com/django/user-registration/






A frequent error also I had was when I logged in and tried entering the profile page I received
this error message.

The lodge is where users can meet and exchange artists they've discovered and share links to music.
The user has to register in order to access the forum. 


# THE SPOTIPY API

I managed to have the spotipy api working on the site. The user will be prompted when entering the site to authorize
his/her spotify account, this will happen each time the users navigates to the home page. The credentials and secret keys 
are stored in the env.py.
So when having been authorized the user can search in the round search field and hit enter. The results will be collected in
rows beneath. The idea was that the user could then copy the links directly in the results and add in forums to recommend 
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
- After Deploy is clicked it will install various files


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
- As a user I can create a profile and edit it
- As an admin I can create, edit and delete user from the admin panel
- As an admin I can delete comments in the forum
- As an admin I can delete threads in the forum
- As an admin I can see information about the users in the admin panel


# FUTURE IMPROVEMENTS

## Profile Collections

The profile page could have more features such as a folder system where the user could save
lists of music in different categories or collections. The users could then grant access to these folders or 
share them with other user in the forum.

## Advanced Search
Add advanced search query functionality to the spotipy endpoint. The endpoint in script.js
can be changed to search for more specific information for music such as tempo, musical keys, danceabilty, popularity, language, 
locations and much more. Using spotify credentials as tokens for longer periods is also possible.


# Special thanks

To tutor support for helping out daily to try and solve the issues. I wouldnt have come as far as I did without it.







