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
    
<img src='assets/images/rtd-title.png' height='200px' width='500px'>

- __The Game Area__

  - The game area allows the user to interact with the main functions of the website and play the game. The user will has the options to roll either their dice or the computers dce by using the two dice buttons.

<img src='assets/images/Roll the Dice! - Google Chrome 12_03_2022 12_32_51.png' width='750px' height='400px'>

- __The Dice Value section__

  - The dice values are placed directly below both the player dice and the computer dice. When the game commences both the players dice value and the computers dice value are 0, because no one has rolled.
  - When the user rolls the first set of dice the value of 'Your roll:' changes to the combnation of the two randomised values and the same happens to the 'Computers Roll:' when the user rolls the computer dice.  

<img src='assets/images/rtd-value.png' height='150px' width='300px'>

- __The Command Area__

  - The command section is an ever looping paragraph which guids the user of what to do. To begin with it instructs the user to roll the players dice and then follows by instructing the user to roll the computers dice.

  - Aswell as directing the users decsions the command area also outputs the results of the fucntions to the user. For example it outputs the players first and second dice, and then the same for the computers role, and finally who won that game.

  - Finally the command section displays the the user who is the winner when the desired score limit has been reached.

<img src='assets/images/rtd-command.png' height='200px' width='350px'> 

__The Scores area__

  - The scores area has two components, the players score and the computers score. Once both sets od dice are rolled the script calculates the winner of that game and increments either the players score or the computers score by 1. Once this desired score limit has been reached the scores both reset back to 0.

<img src='assets/images/rtd-score.png' height='200px' width='350px'> 

__The Tab Area__

  - The tab area has 3 selectors to choose from; 3,5 and 7. The defualt value whne the game is loaded is 5 however should the user want to change the score limit of the game, they can do this by selecting either 3 or 7.


### Features Left to Implement

- I wanted to add some sort of visual animation for high and low dice rolls. For example if the combined dice roll was above 10 then the roll value of the player roll would have a gold backgorund and if the roll was below 6 then the roll value would have a red background.

## Testing 

In this section, you need to convince the assessorn the future: that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Felliswitten.github.io%2Fproject-2-roll-the-dice%2F)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-maths%252F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
    - No errors were found when passing through the official [Jshint validator](https://jshint.com/)
      - The following metrics were returned: 
      - There are 11 functions in this file.
      - Function with the largest signature takes 2 arguments, while the median is 0.
      - Largest function has 10 statements in it, while the median is 3.
      - The most complex function has a cyclomatic complexity value of 4 while the median is 2.

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-maths/


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 