## Price Calculator ##
### Python Project ##
![Responsive-price](https://user-images.githubusercontent.com/88729876/149689889-ff1e8aa4-be35-4d07-9f05-17096a2fdc19.jpg)

1. Description
2. Purpose
3. Technologies used
4. Validator Testing
5. Deployment
6. Resources
7. Acknowledgements


# 1.Description #
![price-calculator](https://user-images.githubusercontent.com/88729876/149684593-2882e80d-a0b7-4ff1-acf2-41a1cf68493e.png)

Price Calculator aims to be a helpful program for both user and owner. Both can use it to update and check data and both parties can use its quotes for a more efficient way of receiving information.

# 2.Purpose #

This programe is meant to be a simple tool to find out as soon as possible how much a simple light/socket change can cost. Once the spreadsheet is updated with current prices, accurate quotes can be created and one can have an idea as to how affordable or not a DYI project is.

# 3. Technologies used #

## Language ##
Python3 - This project is written only with Python as a the programming language.

### Other programmes: ###
Google sheets - To get my google sheet document (gspread) to store/modify or delete the user added information
Gspread - The API to connect my to my programme.
GitHub - Making my repository and push my commited code.
Gitpod - Save and commit my workspace.
Heroku - To deploy my programme and get a livelink.
Am I responsive - For the print screen of my deployed programme for this readme.
Draw.io - For make my flowchart.
PEP8 - To validate python code

### Validator Testing ###

![PEP8Validator](https://user-images.githubusercontent.com/88729876/149689369-1052871c-cf6e-4be7-8dfd-83f5dca6af96.jpg)


### 5. Deployment ###
To build this program, I have used the Code Institutes template to be able to deploy it on Heroku and to be able to use the program on a web server. Using Gitpod IDE. In order to save my work I always git add, git commit with a message and then git push it to my Github repository.

Project Deployment:
For deploy this project in Heroku I followed these steps:

Log in to my account at Heroku
Select "new" and "Create new app" from the dashboard.
Create a unique name for the project
Navigate from the deploy tab at the top and select the setting tab.
Because I use Code Institute template, I need to add a config var for creating this app. (Not necessary if you do not use the template)
Select Reveal config vars button. In KEY field, input PORT with capital letters. In VALUE field, input 8000 and then select add button.
Then add buildpacks below the config var section.
Select Python as yout first bulid pack in buildpacks window and save that.
Add another buildpack and add node.JS and save. The order of the buildpacks is importent to be Python at the top and node.JS at the bottom.
Select the deploy tab again and go to the deployment method section.
Select GitHub - connect to GitHub button and follow the steps to connect to your GitHub account.
Select your account and enter the name of yout repository and then select search.
When Heroku has find your repository select connect to connect the repository to the app within Heroku.
Below App connected section, I choose to manual deployments options further down.
When that is done correctly this will provide me the live link for this programe.
Then I choose Automatic Deploys button that will automatically rebuild the app everytime you add, commit and push from GitPod.

# Here is the final deployed link: #
![image](https://user-images.githubusercontent.com/88729876/149689741-e56bba00-c5c5-4e06-b6df-26739a7ae0ab.png)


# 6. Resources #

List slicing
1. https://stackoverflow.com/questions/53049296/python-slicing-lists-to-get-the-first-item-in-the-list-slicing-lists-of-lists

Tabular Data
2.https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

Tabulate
3. https://pypi.org/project/tabulate/

Gspread
4. https://docs.gspread.org/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column

Tables creating
5.https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd

Math error Stack Overflow
6. https://stackoverflow.com/questions/25573298/math-error-when-multiplying-float-by-integer-in-python

Python Operator
7.https://www.w3schools.com/python/python_operators.asp

Soil and plant
8.https://soil-and-plant-area-calculator.herokuapp.com/

Contactbook
9.https://github.com/StinaAxelsson/contactbook-project3

Draw.io for the diagram

## 7.Acnkowledgments ##

Although not an extremely complicated project, I must say it has taken me more than I thought to begin to grasp the basics of Python. I am fortunate to have a briliant mentor, Richard Wells who I can confidently rely on to explain what I don't fully understand and to help whenever needed.Thank you Richard.

I am also greatful that CI adopted slack and the people on there are always helpful and eager to assist in any way.

