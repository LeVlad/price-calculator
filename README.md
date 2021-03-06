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

### Project Deployment: ###

To deploy this project in Heroku I followed these steps:

1. Log in to my account at Heroku
2. Select "new" and "Create new app" from the dashboard.
3. Create a unique name for the project
4. Navigate from the deploy tab at the top and select the setting tab.
Because I use Code Institute template, I need to add a config var for creating this app. (Not necessary if you do not use the template)
5. Select Reveal config vars button. 
6. Firstly I had to add the creds.json file that had all the required information to link the app to the worksheet. In KEY I added "CREDS" and in VALUE I added the creds.json content.
7. A second config is required, the KEY field, needs PORT with capital letters. The VALUE field, input 8000 and then select add button.
8. Then add buildpacks below the config var section.
9. Select Python as yout first bulid pack in buildpacks window and save that.
10. Add another buildpack and add node.JS and save. The order of the buildpacks is importent to be Python at the top and node.JS at the bottom.
11. Select the deploy tab again and go to the deployment method section.
12. Select GitHub - connect to GitHub button and follow the steps to connect to your GitHub account.
13. Select your account and enter the name of yout repository and then select search.
14. When Heroku has found your repository select connect to connect the repository to the app within Heroku.
15. Below App connected section, I chose to manually deploy the app.
16. After the app was build I received the link and enabled automatic deployment so that every time I commit and push to github, the app updates itself automatically.


# Here is the final deployed link: #
https://price-calculator1388.herokuapp.com/

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

