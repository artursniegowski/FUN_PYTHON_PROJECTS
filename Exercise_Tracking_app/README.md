# Exercise_Tracking_app

This app tracks the exercises that we are doing, and how long we are doing them for, and also figures out how many calories did we burn because of the workout that we did. The data is stored online to a Google spreadsheet where it can be easily accessed and viewed. </br>
1. First, the user is asked about the exercises that will be logged in an Excel spreadsheet. This is done with an English sentence.</br>
Example input: running 10km and cycling 55min</br>
![Screenshot](example_view_02.jpg)</br>
2. Next the program will use the API https://www.nutritionix.com/business/api which uses natural processing to decode our sentence and
get the information it requires. </br>
3. In the last step, the program will use the API https://sheety.co/ and create a new row and update the desired Google spreadsheet.</br>
Example view after updating the row: </br>
![Screenshot](example_view_03.jpg)


The user will end up with a Google spreadsheet that is easy to view online. This way, the user can keep track of the exercises. </br>


In order for the program to work, we need to prepare:</br>


First:</br>
create a Google Excel spreadsheet that looks exactly like this:</br>

![Screenshot](example_view_01.jpg)
</br>


Secondly:</br>
While logged in your Gmail account, you should log into the API https://sheety.co/ 
and create a new project and link it to your spreadsheet that you created above.
And also obtain your own sheety end point for the project as well as the secret token for the authorization.
Thousands of people are using Sheety to turn their spreadsheets into powerful APIs to rapidly develop prototypes, websites, apps and more.</br>


Thirdly:</br>
Register and obtain the free API key and API id from https://www.nutritionix.com/business/api.</br>


Fourthly:</br>
After obtaining the data, we have to change the name of .env.example to .env and define the variables according to our data:</br>
NUTRITIONIX_API_KEY = "YOUR_OWN_API_KEY"</br>
NUTRITIONIX_API_ID = "YOUR_OWN_API_ID"</br>
API_SHEETY_END_POINT = "YOUR_OWN_SHEETY_END_POINT"</br>
API_SHEETY_SECRET_TOKEN = "Bearer YOUR_OWN_TOKEN"</br>


Lastly:</br>
The user can adjust the personal variables in the main.py: </br>
GENDER = "male" </br>
WEIGHT_KG = "70.5" </br>
HEIGHT_CM = "176" </br>
AGE = "33" </br>
They are used by the API https://www.nutritionix.com/business/api.</br>



The program was developed using python 3.10.05, requests, APIs. 

In order to run the program, you have to execute the main.py.