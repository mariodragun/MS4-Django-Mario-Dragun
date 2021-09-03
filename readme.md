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



- Easy access change database questions

- To add new questions

- To delete users



#### As user I want to:



- Easy to register

- Easy to login

- To play general knowledge quiz




### Structure:

#### Project has the following sections:


- Home page contains image and navigation bar with access to login, register, admin, 

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

- [Chrome view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/chrome_view.JPG)

- [Firefox view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/firefox_view.JPG)

- [Phone view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/phone_view.JPG)

- [Tab view](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/page%20view/ipad_view.JPG)



####


- Main image was download from [Wallpaper Cave](https://wallpapercave.com/question-mark-wallpapers)




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

- [PEP8 online](http://pep8online.com/) for validation of code

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

- Press Button [New](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heruku_button_new.JPG)

- Select Create a New App, enter the [app name and select region](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heruku_create_new_app.JPG)

- Press Resource / add-ons and search for [Heruku Postgres database](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heruku_postgres_database.JPG)



#### Configuration of connection Github Repository - Heruku


- Click the Deploy tab and select Connect to GitHub

- Enter the repository name and search

- When repository has been found, press the connect button



#### Set environment variables


- Click the Settings tab and then click the [Reveal Config Vars button](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heruku_config_vars.JPG) 


#### Deployment`s final steps


- Select the [Deploy](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heruku_deployment.JPG) tab and click Enable Automation Deployment 

- Install Heroku CLI on PC

- Run PowerShell commands to create super user on Django app: heroku run bash --app mariodragun/MS4-Django-Mario-Dragun, python manage.py migrate, python manage.py createsuperuser

- Register super user [name and password](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/heruku_superuser.JPG)

- Create [quiz](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/quiz_creation.JPG) on Django App

- Create quiz [questions](https://github.com/mariodragun/MS4-Django-Mario-Dragun/blob/main/images/deployment/quiz_questions.JPG)




### Testing:



#### Application was tested on browsers: 


- Chrome

- Firefox




#### Mobile responsive functions:



- phone

- tab



#### Functionality tested:



- That every link is opening right template

- That user registration is functional

- That login is functional

- That quiz is functional

- That admin can delete users

- That admin can add new or to remove old questions




### Conclusion:


- This project was built only for educational purpose and won`t be in commercial use.