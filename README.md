# InstaRamen

An Interactive Front-end Web Development Project - Code Institute
<br>
By Linda Hsu

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/index.png)

<br>

[InstaRamen](https://linda-instaramen.herokuapp.com) is a website created for ramen lovers to view a collection of instant noodles from all around the world. One could search for by a ramen flavour, add a new ramen to the collection if it is not available, edit all ramens in the collection and even delete them. A feature of this website is that users could rate and leave their reviews on the ramen for the benefit of future visitors.

The deployed website can be found in
[**Heroku**](https://linda-instaramen.herokuapp.com)

### Project Purpose

The objective of InstaRamen is to enable users to search for information of ramens of their choice. If it couldn't be found, users could provide new entries to the collection and view them after they've filled in the 'add ramen' form. Users could also edit a ramen of their choice and even delete any one they choose.

### User Stories

- #### As a user, I'd like to see:
    - A professional, modern and clean looking website to attract me to continue clicking on the other features 
    - Easy to understand and clear selections which would point me to the correct pages
    - Buttons which are straightforward in their purpose that allow me to view more information or do an action.
    - Options to have full control on adding, viewing, editing and deleting any ramen in the collection 

## UX / UI

### User Experience

- Users are welcomed with a refreshing orange color and a large noodles picture when they first visit the site. This sets the tone that this website is all about ramen. 

- There is an eyecatching icon of a bowl of ramen on the navbar and also as the favicon to further enhance the website's purpose. 

- On larger screens, there are options on top of the navigation page for easy navigation on this website. On smaller screens, a hamburger on the left hand side of the navigation bar provides a menu of options when it is clicked on. 

- A search function is provided on the main page that enable users to search for ramen flavours

- If the user gives an input that is not found, a sad faced kitty cat's face will be shown on the search result page. The user could input a new search to search for other flavours. 

- An introductory message is given on the main page to explain the functions and purpose of the website. 

- The 3 latest ramen additions are shown below the introductory message in the form of cards and a 'more' button suggests a call-for-action from the users if they'd like to view more information. 

- The user could view the entire ramen collections or view them by continents. The display ramen cards in the ramen collection page is sorted by the latest added ramen for users to see the newest entry. The display ramen cards in each of the continents options are sorted by countries for easy reference. 

- A form is provided when the user would like to add a new entry to the ramen collection. The asterisks (*) imply that the fields are required to be filled before form submission. 

- A drop down selection of ramen brands is provided and if the user don't find the one he/she is looking for, a new brand could be added by clicking on the "add brand" button. The user would be brought to a new page to add a new brand. 

- After a new brand is added, the user is brought back to the the "add ramen" page where the newly added brand could be found in the drop down list. 

- After the user fills in all fields and selects a picture to upload, upon clicking on the "submit" button,  he/she is brought to the "ramen collection" page where the latest ramen would be shown on the top left. This way they could verify that their form submission is successful. 

- To see the full information of the recently added ramen, the user could click on the "more" button. 

- Should the user want to edit the form, they could be brought to the form by clicking on "edit" at the display ramen page. 

- The edit form is pre-filled with the original entries of the user for easy reference. After the user make changes, the form can be saved by clicking on the "save changes" button. 

- Once the user choose to delete a ramen entry, they would be brought back to the ramen collection page. 

- If there are any errors along the way, the user would be brought to an error 404 page where a shocked cat picture would hopefully shock the users into inputing or clicking on the right things. 

### Design Ideas

The website was designed with an orange theme color as it is refreshing and close to the colours of food and noodles, with a clean white background to ensure all the texts, cards, images and other elements to 'pop up' to the user.

- #### Fonts

    - The font **'Poppin'** was chosen as the primary font as it's rounded edges creates a warm and comforting feeling to the user.
    - The font **'Montserrat'** was chosen as the font for all titles  ```<h4>Titles</h4>``` to give a distint but subtle feel that it's different to make the texts look more interesting to the user.

- #### Colours

    - **Main Heading and Footer -** An orange theme colour was chosen for the navigation bar and footer for all pages to set a refreshing and subtle warm  connection to ramen because most noodles are yellowish, orangish in colour by nature. Black for the fonts on the bars are chosen to contrast against the bright orange for ease of reading.
    
    - **Cards -** A white background was chosen for each card and any lines in the original design of the card was taken out to give a smooth flow feeling from the image to the information underneath. Black was chosen for the fonts to contrast against the background for easy reading.
    
    - **Add, Edit, Search & More Buttons -** 'Add' buttons (for ramen and brand), 'edit,' 'search' and the 'more' buttons are in the theme orange color indication a call-to-action for the users for these important features.

    - **Cancel & Delete Buttons -** The 'cancel' button is in green to give a contrast against the orange theme button indicating a different function from the rest. The 'delete' button is in bright red because it indicates danger of not being able to retrieve the ramen once it is deleted. 
    
    - **Forms -** A ligtened yellow background was chosen for the 'add ramen' and 'edit ramen' forms to give it a pop-up look on the page. All the labels are in the orange colour to keep the theme consistent across all pages.
    
    - **Active Input fields -** When an input field is active, the materialized icons & bottom border transforms to orange, keeping the primary orange color theme consistent.
    
- #### Styling

    To achieve a warm, comforting feel for the user experience as well as keeping the website looking clean and modern, I used a CSS framework
    [Materialize!](https://materializecss.com/) to achieve this objective.
    
    **Special styles include:**
    
    - **Input fields -** When the user clicks on the field to input text, a simple but efficient animation provided by Materialize moves the placeholder to the top of the field while changing the bottom of the border to the theme orange colour. 

    - **Buttons -** Materialize also provides a neat animation in a class called 'waves' for buttons which gives an interesting effect when they are clicked on. Also, when all the buttons are hovered over, a shadow appears on the buttons to make them look 3D and pop-up, which indicates a call-to-action is possible.
    
    
## Features

### Existing Features

1. #### Home Page

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/index.png)
    
- When the user first arrives at the page, he/she is welcomed with a large background picture of ramen, or noodles, with a search function for ramen flavours. On top of the page is an orange navigational bar with an icon of a bowl of ramen and chopsticks and links to the other pages. For the mobile devices, the links are presented when the user clicks on the 'hamburger' icon of 3 horizontal lines.

-  If the user scrolls down the main page, there is a few paragraphs of text describing the purpose and intent of the website. Further down, there are 3 recently added ramens shown in the form of cards with pictures and a short but important description of the ramen brand and flavour, with a 'more' button should the user would like to view more information.

- At the bottom of the page, there is a footer in the orange color with the ramen icon which points the user to the top of the page and a short summary of the website. In the 'keep in touch' section, there are links to my personal social media. Github repository and LinkedIn sites for anyone who wishes to contact me. There is also a disclaimer that this website is meant for educational purposes only.

    
2. #### Search Ramen Page

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/ramen-search.png)
    <br>
    
- When the user has inputted a ramen flavour in the search box on the main page, he/she is brought to this search results page where on top of the page is a line that says 'Search Results for "whatever the user has input into the box."' If there is at least one possible result, the ramen is displayed in a card with an image along with the brand and flavour. There is a vertical scroll button for the user to scroll down in case the lines are too long for the card display section. A 'more' button is available for the user to click on it to view more information on the ramen on the display page.

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/no-results.png)

- If there isn't any results from the user's search, a big picture of a sad kitty cat is shown saying no results have been found. With the search function available on top of the page, the user can perform another search without having to go back to the main page to do this.  

3. #### Ramen Display Page

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/display-ramen.png)
    <br>
    
- This page displays all the information of the ramen which includes a picture, brand, flavour, stars, country of origin and even reviews.

- From there, there are 2 buttons underneath the information which allows the user to edit the information or to delete this ramen.

- If the user clicks on the edit button, he/she is brought to the edit page.

- If the user clicks on the delete button, he/she is brought back to the ramen collection page which displays all the ramen in the collection.

3. #### Ramen Edit Page

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/edit-ramen.png)
    <br>
    
- At this edit page, the form is pre-filled with entries from the original information. All the fields are available for the user to change if he/she wishes to. 

- On the click of the 'save changes' button, the user is brought back to the ramen collection page to view all the ramens

- If the user changes his/her mind and clicks on the 'cancel' button, the user is diverted to the ramen collection page.
    
4. #### Add Ramen Page 

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/add-ramen.png)
    <br>
    
- On this page, the user is presented with a form with the top line saying that all fields are required. Here the user could fill in the different fields and even upload a ramen picture. On clicking the 'add ramen' button, the user is brought to the ramen collection page where the newest added ramen is shown on the top left hand side. This newly added ramen is also shown on the main page along with 2 other newly added ramens.

- If the user clicks on the 'cancel' button, he/she will be brought to the ramen collection page 

4. #### Ramen Collection Page 

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/ramen-collection.png)

4. #### Ramen Continents Page 

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/ramen-continents.png)
    
7. #### Error 404 Page

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/error404.png)
    <br>
    
- If the user has inputted an invalid entry on the URL, he/she would be brought to this page which shows that there is an error with a picture of a shocked kitty cat.

- When the user scrolls down, there is a 'home' button which allows them to be brought back to the main page with a click of the button.

### Features Left to Implement

1. #### User log in

    - A user log in feature is essential to allow edit and delete functions only to the user who created the ramen. This is to ensure no one deletes the whole collection by accident or tamper with other users' ramen entries.

2. #### Pagination

    - Pagination on the ramen pages would be helpful with organizing the collection as it grows. It also looks neater and helps with loading time.
    
## Database

### MongoDB

- A noSQL database [MongoDB](https://www.mongodb.com/) was chosen for this project for the developer to gain experience in learning to work with a document based database in this cloud era.

### Data types

- These are the types of data that are used in this project:
    - ObjectId
    - String
    - Int32(Integer)
    
### Ramens Database

- A database called 'ramen_database' which contains a main collection called 'ramens' which is where the attributes of each ramen is stored. The data structure is as follows:

| Name of field | field key | field value | type |
--- | --- | --- | --- 
Ramen ID | _id | `<Creates ID automatically>` | ObjectId 
Ramen Brand | brand | `<Name of ramen brand>` | string
Ramen Flavour | flavour | `<Name of ramen flavour>` | string
Ramen Style | style | `<Packaging style of ramen>` | string
Ramen Country of Export | country | `<Country where Ramen is exported from>` | string
Continent of Country | continent | `<Continent of Country>` | string
Ramen Stars | stars | `<Rating of Ramen>` | string
Ramen Reviews | reviews | `<Reviews of Ramen>` | int32
Ramen Image | imageURL | `<Name of image file uploaded>` | string

- In addition to the above 'ramens' collection, there is also the 'countries' collection where all the countries of the world is specificed to a particular continent. The data structure is as follows:

| Name of field | field key | field value | type |
--- | --- | --- | --- 
Ramen ID | _id | `<Creates ID automatically>` | ObjectId 
Country | country | `<Name of country>` | string
Continent of Country | continent | `<Name of continent>` | string

- There is also the 'brands' collection where all the brands of existing ramens are stored and future additions by users from the 'add brand' form submission will also be store. The data structure is as follows:

| Name of field | field key | field value | type |
--- | --- | --- | --- 
Ramen ID | _id | `<Creates ID automatically>` | ObjectId 
Ramen brand | brand | `<Brand of ramen>` | string