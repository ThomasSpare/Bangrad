# TESTING

## Table of Contents

1. [Device Testing](#device-testing)
2. [Manual Testing](#manual-testing-of-user-stories)
3. [Bugs](#bugs)
4. [Unfixed Bugs](#unfixed-bugs)

### Device testing

- Project was tested in various mobile devices and was running succesfully
- iPhone 12
    - Safari
- Samsung S22 Ultra
    - Chrome
- Macbook Pro 2019 16-inch
    - Chrome
    <details><summary>Screenshot</summary>
  <img src="TESTING/screenshots/home_page_chrome.jpg">
    
  </details>
    - Not tested for Safari

    
  </details>
- Also tested various device sizes using [Dev.tools](https://developer.chrome.com/docs/devtools/)

### Manual testing of user stories

1. As a user I want to create a profile and upload a profile image, save social media links, and write my bio so that other users can learn more about me.

| **Step**                            | **Expected Result**                       | **Actual Result** |
| ----------------------------------- | ----------------------------------------- | ----------------- |
| Open website                        | home page loads                           | Work as expected  |
| User register at home page          | The sign up form is visible               | Work as expected  |
| User fills in the required fields   | If valid user is informed of success      | Works as expected |
| User login after register           | Success message and navmenu access        | Works as expected |


<details><summary>Screenshot</summary>
<img src="TESTING/screenshots/register.jpg" >
<img src="TESTING/screenshots/signup_form.jpg" >
<img src="TESTING/screenshots/after_register_success.jpg" >
<img src="TESTING/screenshots/after_login.jpg" >


</details>

2. As a user I want to view and comment on other users forum posts so that I can learn about new music and connect with other users

| **Step**                                | **Expected Result**                     | **Actual Result** |
| --------------------------------------- | --------------------------------------- | ----------------- |
| Open website                            | home page loads                         | Work as expected  |
| User login                              | Navitem forum access                    | Work as expected  |
| User click on forum                     | user is taken to forum page             | Works as expected |
| User can scroll the forum               | forum posts in order of dateadded       | Work as expected  |

 <details><summary>Screenshot</summary>
<img src="TESTING/screenshots/home_page_chrome.jpg" >
<img src="TESTING/screenshots/after_login_success.jpg" >
<img src="TESTING/screenshots/forum_view.jpg" >
<img src="TESTING/screenshots/forum_scroll.jpg" >


</details>

3. As a Site User I can be able to register, login and logout from the website so that I can have a safe environment to work with

| **Step**                                         | **Expected Result**                  | **Actual Result** |
| ------------------------------------------------ | ------------------------------------ | ----------------- |
| User navigates to a "Register" link in a nav bar | Loads register form                  | Work as expected  |
| User fills the form correctly                    | Home page loads with success message | Work as expected  |
| User navigates to a "Login" link in a nav bar    | Loads Login form                     | Work as expected  |
| User fills the form correctly                    | Home page loads with success message | Work as expected  |
| User navigates to a "Logout" link in a nav bar   | Loads Logout confirm page            | Work as expected  |
| User click on logout button                      | Home page loads with success message | Work as expected  |

 <details><summary>Screenshots</summary>
<img src="documentation/user-stories/register-nav.png" >
<img src="documentation/humanitas-pages/register-page.png" >
<img src="documentation/user-stories/sign-up-message.png" >
<img src="documentation/user-stories/login-nav.png" >
<img src="documentation/humanitas-pages/login-page.png" >
<img src="documentation/user-stories/login-message.png" >
<img src="documentation/user-stories/logout-nav.png" >
<img src="documentation/humanitas-pages/logout-page.png" >
<img src="documentation/user-stories/logout-message.png" >

</details>

4. As a Site User I can be able to send message so that I can communicate with the website owner

| **Step**                                        | **Expected Result**                                      | **Actual Result** |
| ----------------------------------------------- | -------------------------------------------------------- | ----------------- |
| User navigates to a "Contact" link in a nav bar | Loads contact us form                                    | Work as expected  |
| User fills the form correctly                   | If user authorised: home page loads with success message | Work as expected  |
| User fills the form correctly                   | If user is not authorised: login page opens with message | Work as expected  |

 <details><summary>Screenshots</summary>
<img src="documentation/user-stories/contact-nav.png" >
<img src="documentation/humanitas-pages/contact-us-page.png" >
<img src="documentation/user-stories/contact-login.png" >
<img src="documentation/user-stories/contact-confirm.png" >
<img src="documentation/user-stories/contactloggedout.png" >
<img src="documentation/user-stories/contact-warning-message.png" >

</details>

5. As a Site User I can view the stories page so that I can view the stories

| **Step**                                        | **Expected Result**                       | **Actual Result** |
| ----------------------------------------------- | ----------------------------------------- | ----------------- |
| User navigates to a "Stories" link in a nav bar | The nav-bar expands to show "Our Stories" | Work as expected  |
| User navigates to a "Our Stories" link          | The "Our Stories" Page opens              | Work as expected  |

<details><summary>Screenshots</summary>
<img src="documentation/user-stories/nav-bar-our-story.png" >
<img src="documentation/humanitas-pages/our-stories-page.png" >

</details>

6. As a Site User I can click a story so that I can read the full post

| **Step**                                          | **Expected Result**                         | **Actual Result** |
| ------------------------------------------------- | ------------------------------------------- | ----------------- |
| User navigates to a "Stories" link in a nav bar   | The nav-bar expands to show "Our Stories"   | Work as expected  |
| User navigates to a "Our Stories" link            | The "Our Stories" Page opens                | Work as expected  |
| User clicks on "Read More" link in the story card | User is authorised: Story detail page opens | Work as expected  |
| User clicks on "Read More" link in the story card | User is unauthorised: Login page opens      | Work as expected  |

<details><summary>Screenshots</summary>
<img src="documentation/user-stories/nav-bar-our-story.png" >
<img src="documentation/humanitas-pages/our-stories-page.png" >
<img src="documentation/user-stories/readmore-login.png" >
<img src="documentation/humanitas-pages/story-detail-page.png" >
<img src="documentation/user-stories/readmore-loggedout.png" >
<img src="documentation/humanitas-pages/login-page.png" >
</details>

7. As a Site User I can comment on the story so that I can be involved in conversation

| **Step**                                          | **Expected Result**                                          | **Actual Result** |
| ------------------------------------------------- | ------------------------------------------------------------ | ----------------- |
| User navigates to a "Stories" link in a nav bar   | The nav-bar expands to show "Our Stories"                    | Work as expected  |
| User navigates to a "Our Stories" link            | The "Our Stories" Page opens                                 | Work as expected  |
| User clicks on "Read More" link in the story card | User is authorised: Story detail page opens                  | Work as expected  |
| User write a comment and submit                   | The comment is added in comment section with success message | Works as expected |

<details><summary>Screenshot</summary>
<img src="documentation/user-stories/nav-bar-our-story.png" >
<img src="documentation/humanitas-pages/our-stories-page.png" >
<img src="documentation/user-stories/readmore-login.png" >
<img src="documentation/humanitas-pages/story-detail-page.png" >
<img src="documentation/humanitas-pages/comment-section.png" >
<img src="documentation/user-stories/comment-add.png" >

</details>