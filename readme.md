# The Ultimate Quiz Online

## Milestone 4 Code Institute 





### Summary:


This project is my final project for the Code Institute's Full stack development program.
The main goal of this project is to create online quiz using the Django framework.




### Target Audience:


- General population who enjoy quizzes.

- People who want to expand their general knowledge



### Site Owner Goals:



- Provide the users interesting quizzes

- Make a profit from donations 
  

  

### UX stories:



#### As admin I want to:



- Easy access 

- To add new questions

- To delete users



#### As user I want to:



- Easy to register

- Easy to login

- To play general knowledge quiz




### Structure:

#### Project has the following sections:


- Home page contains image and navigation bar with access to login, register,  

- Login page contains username field, pasword filed and login button

- Register page contains fields: first name, last name, username, email, password, confirm password and register button

- Admin page contains options to add quizzes, questions, users, groups



#### Wireframes:


- [Main page desktop](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/wireframes/desktop_main_wireframe.JPG)

- [Main page tab](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/wireframes/tab_main_wireframe.JPG)

- [Main page phone](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/wireframes/phone_main_wireframe.JPG)

- [Admin page desktop](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/wireframes/admin_desktop_wireframe.JPG)

- [Admin page tab](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/wireframes/Tab_admin_wireframe.JPG)

- [Admin page phone](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/wireframes/phone_admin_wireframe.JPG)


#### Page design:

- [Chrome view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/chrome_view_django.JPG)

- [Firefox view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/firefox_view_django.JPG)

- [Phone view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/mobile_view_django.jpg)

- [Tab view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/tab_view_django.JPG)

#### Fonts:
- I used Roboto from, from Google Fonts

####


- Main image was download from [Wallpaper Cave](https://wallpapercave.com/)

#### Colors:

 Navigation bar:

 - rgb(108, 117, 125)

Quiz: Completed:

- #9ABC66

Quiz list items:

- #DEDEDE

Accounts: Login/Register:

- on card box shadow: #DEDEDE; 

- card button rgb(104, 145, 162)

### Technology used:

- HTML5

- CSS

- Google Fonts

- Bootstrap

- Django [requirements.txt](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/requirements.txt)





### Tools used:



- Visual code studio

- Git pod

- [Github](https://github.com/) for repository hosting service

- [Heroku](https://id.heroku.com/login) to deploy web application

- Heroku Postgres for database

- [Stripe](https://stripe.com/) for payments

- [PEP8 online validator](http://pep8online.com/) for validation of code

- [W3C validator](https://validator.w3.org/)

- [Jigsaw validator](https://jigsaw.w3.org/css-validator/)

- Mockplus for wireframes





### Deployment:



#### Project setup:


- Create a new repository on Git Hub using code institute`s template

- Change repository visibility

- Press green button to open project in git pod

- Create readme.md file and make initial commit

- Make regular commits after project change with quality description using commands: git add -A and git commit -m "message"

- Use git push command in CMD for code commits



#### Deployment to Heroku:


- Navigate to [Heroku](https://id.heroku.com/login)

- Register on Heroku

- Press Button [New](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heroku_button_new.JPG)

- Select Create a New App, enter the [app name and select region](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heroku_create_new_app.JPG)

- Press Resource / add-ons and search for [Heruku Postgres database](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heroku_postgres_database.JPG)



#### Configuration of connection Github Repository - Heruku


- Click the Deploy tab and select Connect to GitHub

- Enter the repository name and search

- When repository has been found, press the connect button



#### Set environment variables


- Click the Settings tab and then click the Reveal Config Vars button

#### Deployment`s final steps


- Select the [Deploy](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heroku_deployment.JPG) tab and click Enable Automation Deployment 

- Install Heroku CLI on PC

- Run PowerShell commands to create super user on Django app: heroku run bash --app mariodragun/MS4-Django-Mario-Dragun, python manage.py migrate, python manage.py createsuperuser

- Register super user [name and password](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heroku_superuser.JPG)

- Create [quiz](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/quiz_creation.JPG) on Django App

- Create quiz [questions](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/quiz_questions.JPG))

- Create [Stripe](https://stripe.com/ie?utm_campaign=paid_brand-IE_en_Search_Brand_Stripe-1615558792&utm_medium=cpc&utm_source=google&ad_content=307395195086&utm_term=kwd-308032378313&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=CjwKCAjwzOqKBhAWEiwArQGwaF7NrJCrJFTgyPVNuW475XepIbMZDUXt1BMI_iCGKfReupMZ3km9qxoCHHUQAvD_BwE) account

- Set Stripe [product/price](https://stripe.com/docs/payments/checkout/client#create-products)

- Set Stripe [donations](https://support.stripe.com/questions/how-to-accept-donations-through-stripe)



### Testing:



#### Application was tested on browsers: 


- Chrome

- Firefox

- Safari



#### Mobile responsive functions:



- Phone

- Tab

Throughout the development of the project, I carried out testing. I used the Chrome Developer Tools consistently. The application structure and mobile-first layout was tested on Google Chrome, Firefox and Safari. The application was tested on the following smartphone devices: iPhone11, Google Pixel 3,



#### Functionality tested:



- That every link is opening right template

- That user registration is functional

- That login is functional

- That quiz is functional

- That admin can delete users

- That admin can add new or to remove old questions

- That donation is functional

Validation tests:

HTML:

- [Home page](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/test_w3c/home_page_w3c.JPG)

- [Quiz page](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/test_w3c/quiz_page_w3c.JPG)

- [Donate page](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/test_w3c/donate_page_w3c.JPG)

- [Login page](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/test_w3c/login_page.JPG)

- [Register page](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/test_w3c/register_page_w3c.JPG)

- [Settings page](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/test_w3c/setings_page_w3c.JPG)


CSS 

- [files/static/accounts/css/index.css](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/css_validator/files-static-account-css-index.JPG)

- [files/statis/accounts/css/style.css](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/css_validator/files-static-account-css-style.JPG)

- [files/static/account/authentication/css/login.css](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/css_validator/files-static-authentication-css-login.JPG)

- [files/static/common/css/style.css](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/css_validator/files-static-common-css-style.JPG)

- [files/static/common/error/style.css](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/css_validator/files-static-common-error-style.JPG)

- [files/static/game/css/style.css](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/css_validator/files-static-game-css-style.JPG)

- [files/static/payment/css/style.css](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/css_validator/files-static-payments-css-style.JPG)

PEP8 

- All of the files were tested, no issues found. Some of the files on Pep8 validator are getting error E501 (length more than 79).This is not issue, according [Django documentation](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) length of 119 is allowed.

Donation 

- [Stripe payment](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/payment_stripe/stripe_payment_1.JPG)

- [Stripe payment confirmation](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/payment_stripe/stripe_payment_2.JPG)

- [Stripe customers](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/payment_stripe/stripe_payment_4.JPG)

- [Stripe payments](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/payment_stripe/stripe_payment_3.JPG)





### Conclusion:


- This project was built only for educational purpose and won`t be in commercial use.