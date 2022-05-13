# WAREHOUSE_USER_SYSTEM

WAREHOUSE_USER_SYSTEM is an application to be used in a warehouse wokr environment. This application is meant to enable admin users to provide staff with instructions on how to pick and put away items in the warehouse. Using a system like this rather than using a paper confirmation system prevents incorrect shipments and confirms stock in deliveries. The line for picking is complete to show you how systems like this can be used. In order to test this application you will have to be able to see a version of the spreadsheet the data is stored in, this will allow you to know check_codes(which are digits that corrospong to a location to confirm the location, like a unique identifier) and item_id (to confirm the correct item was in that location), after following the steps of the system the user would then place the item on their pallet and complete the pick of validated stock.

This is the link to the spreadsheet:
https://docs.google.com/spreadsheets/d/1vRrT2R0GUOfYxbyP5Tqs-ovCJ4AYRg7y7H4NXXTuq1c/edit?usp=sharing

## Functions

### Existing Features
- __Greeting the user__
    - The first lines of text the user sees is a greeting. It welcomes them to the program and confirms that the code is commencing.
    
    <img src='images/Screenshot (49).png' width="350px" height="200px">

- __Requesting username and password__
    - This section of the program requests the username and password from the user. For the purposes of you using the application the username: 1 and the password: 1, will allow you access to the program.

    - The username and the password are then seperately vaidated. The prgoram accesses the 'login information' sheet and iterates of the items to check to see if the user name matches any of the usernames in the sheet. The program then queries weather the passowrd entered matches the password saved to the spead sheet.

    - If either the username of password is incorrect the program returns a error statment stating which value is wrong and then starts the process again.

    <img src='images/Screenshot (49).png' width="350px" height="200px">

- __Request system functoin__
    - This function first greets the user and appens the sentence with the user ID in which was entered previously.

    - The request user funtion simply displays some options to the user of which would all carry out seperate functions if fully developed. For now the only function that works is '1) Picking'.

    - It then prints a statment and stores the variable, depending on what variable is answered it executes the corrosponding code.

-__Request shipment number__
    - This feature prints a statment asking the user to input the shipment number for the picklist they want to pick

    - The program the iterates through the code to find items with the shipment number that matches the user entry and appends them to a list.

    - The program also checks to see if the items in the picklist that match the user input have the pick status of picked, if so then it wont allow the user to pick the items again.

   <img src='images/Screenshot (53).png' width="350px" height="200px">

-__Display picks to user__
    - The program then procedes to display each inidvidual pick to the user. It displays the inforation of the pick and request the check code and the item id.

    - Following this the program validates both inputs and checks them agianst the data abse and if it is correct it moves onto the next item until the list is empty.
    
<img src='images/Screenshot (55).png' width="350px" height="200px">

-__Update the pick list sheet__
    - The program the retieves the list with the shipment number that matches the one of the user input. It then replaces all the unpicked, items with picked and updates the spread sheet.
<img src='images/Screenshot (57).png' width="350px" height="200px">


### Unfixed Bugs

    - Although the program does complete the fucntion inteded it does have some bugs. One of the bugs is that once the code is complete it does not restart correctly, i believe this is due to the shipment number input however i ahvent been able to fix it yet.

## Deployment

    - The deployment was a little bit tricky. Heroku had updated their application which meant i had to upload it using the terminal. This was tricky because i had to read through material that wasnt writen with the purpose of uploading a github site to heroku with the pakcages that i had installed. However once the information was pieced together it was fairly simple.

## Credits 
 
    - 'Ger' from code insitute was someone i connected with on two occasions on the Tutor Me section of the code institute website. He helped me fix some structure issues in my code.