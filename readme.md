# The Croatian Food Shop

Croatians are one of the most displaced people on the planet. Along with the Irish and the Lebanese, Croatians are one of the few people groups where the number of people living outside the country actually outnumber the ones living in the country. Even though Croatians live outside of Croatia, they still like to be reminded of home and what better way to remind someone of their home than through food. Food is the one thing that unites everyone and many friendships, business deals and romances have formed through sharing food. This project aims to reunite expat Croatians with their homeland through food. 

## Why this project

I created this project as part of of the Full Stack Web development course at Code Institute. The scope of the project was to create a full feature e-commerce website incorporating Python, Django and a relational database as the backend and HTML, CSS & Javascript as the front end. There were more frameworks and libraries used in this project which will be discussed further in the readme. I chose to create a Croatian Food Shop as I have, for a long time, wanted to buy Croatian food in Ireland. However, only recently has the number of Croatian people in Ireland increased to the number to make a shop like this viable. 
# UX

On the Croatian Food Shop anyone is welcome and able to buy products which are on offer. 
## Project Goals

The goal of this project is to successfully demonstrate the skills and competence in developing a full stack web application.

### Target Audience

- Croatians who live outside Croatia
- Croatian people who live in Croatia and would like to sell their food (can contact shop)
- Croatian restaurant owners who would like to buy ingredients
- Croatians who are hosting a party and would like to present their guests with food from their home country
- People who would like to try Croatian / Balkan food
- All people who like food

### Visitor / User Goals

- Purchase products from their home country in a safe and secure way
- Find information about Croatian food products

### Business Goals

- Provide users with an easy to navigate e-commerce website
- Make a profit from selling Croatian food to customers in Ireland
- Bring Croatian food closer to people living in Ireland
- Capture the Croatian food market in Ireland
- Bring Croatian

## User Stories

User stories are used to guide the development of the website. Below are the user stories used to guide the development of Croatian Food Shop

### Casual User

A casual user is someone who does not visit the site regularly. They will visit from time to time to either browse or buy a few items

- As a user, I expect to access the website from any device, so that I can use the website anytime and anywhere.
- As a user, I expect to easily navigate the website and know where each link will take me, so that I can easily find what I am looking for. 
- As a user, I expect to have all the information easily accessible, so that I can find out what is on offer.
- As a user, I want to find out information about the company so that I know who I am doing business with. 
- As a user, I want to know when I can place my order and when items will be delivered so that I can plan my purchases. 
- As a user, I want to know if the store has a returns policy so that if I am unsatisfied I can easily return products. 
- As a user, I want to easily find products I am looking for so that I can quickly do my shopping. 
- As a user, I want to see the prices of each items so that I can make an informed purchase.
- As a user, I want to see the product description and manufacturer so that I can easily make informed purchasing decisions. 
- As a user, I want to easily add my products to a shopping cart so that I can keep track of what I have already selected. 
- As a user, I want to be presented with a list of products I have selected so that I can review my order. 
- As a user, I want to be able to securely place my order so that I can pay with confidence.
- As a user, I want to be informed that my purchase has succeeded so that I can expect the products to arrive. 
- As a user, I want to be able to register so that I can track my order history. 

### Logged in user

Casual users have an option to register for an account. The benefit of registering for an account is that all orders are saved and easily retrieved, plus at checkout, the user profile and data are automatically retrieved and the form populated with the correct information. 

- As a logged in user, I want to easily log in so that I can access my profile. 
- As a logged in user, I want to update my profile details so that I can change information if my circumstances change. 
- As a logged in user, I want to be able to follow my order history so that I know when and what I ordered in the past. 

### Site owner or Admin

- As a site owner or admin, I want to be able to log into an admin dashboard so that I can easily find information stored in the database. 
- As a site owner or admin, I want to be able to add products to the database so that I can update inventory. 
- As a site owner or admin, I want to be able to delete products from the database so that I can update the inventory. 
- As a site owner or admin, I want to be able to edit current products so that I can update product information if I need to. 

## Design

### Frameworks

- [Bootstrap](https://getbootstrap.com/) 5 is the front end web framework chosen for this project. The framework offers ease of use and the ability to quickly develop a modern front end design. It was used to create the navigation and structure of the front end. 
- [jQuery](https://jquery.com/) is used to support the functioning of the payment system Stripe as well as add additional functionality to website elements such as links and buttons. 

### Color Scheme

The color palette was taken from the website [Coolors.co](https://coolors.co/). It was chosen for it's gradient of blue tones which represent the Croatian sky, coast and deep sea. As the target audience of the site are Croatian expats, the colors chosen should represent those which would resonate with the target audience.   

![Croatian Food Shop Color Palette](/readme_data/colorpalette/croatian-food-shop-color-palette.png)

## Wireframes

[Balsamiq Wireframe Tools](https://balsamiq.com/) was used to create the wireframes for this project. 

- [Home Page](/readme_data/wireframes/Home_Page_resize.png)
- [Products Page](/readme_data/wireframes/Products_resize.png)
- [Products Details](/readme_data/wireframes/Product_details_resize.png)
- [Purchase View](/readme_data/wireframes/Purchase_view_resize.png)
- [Payment Page](/readme_data/wireframes/CC_Form_View_resize.png)
- [Order Information](/readme_data/wireframes/Order_info_resize.png)

**Note:** The wireframes are a basic representation of the actual look of the site. 
# Features

This section will go through all the features implemented in the Croatian Food Store
## Apps Used
This section will go through all the apps created in the project and their function

### Checkout App

The checkout app functions as a place where users can get an overview of the products they have selected for purchase. It displays this information and gives users the option to either update the quantity of the items they purchased or to delete them all together. 

### Home App

This app displays the **home**, **about**, **delivery & returns** and **FAQ** pages.

### Products App

The products app holds all the information about the products offered on the site. It holds the product models and allows administrators to edit / add / delete products.

### Profiles App

The profiles app stores information about the registered users on the site. 

### Purchase

The purchase app takes care of working with orders and payments. 

## Site Pages

### Features present throughout the site

The following features are added to the base template so they are included in all pages throughout the site

- **Navigation bar** - The navigation bar contains links for the user to navigate around the site. It links to the shop where users can find all the products available for purchase. There is a dropdown link for product categories. This categories list is dynamically generated from the categories model. The user can also navigate to the About Us, Delivery & Returns and FAQ pages. These are static pages which will be explained further in the readme. 

- **Search Bar** - Users can search for products from anywhere on the site. The search looks for key words in the product name, product description and manufacturer name. 
Users can therefore search by name, description and manufacturer. 

- **My Account link** - The my account link changes dynamically based on the logged in status of the user. Non logged in users will be presented with the option to register for an account or to log in with their credentials. 

- **Shopping Cart link** - The shopping cart link is present on all pages as a convenient way for the user to always know the value of the items they have selected for purchase and as a quick way to purchase products. 

- **Site title** - Users can see the site title on all pages and by clicking the title can go back to the home page. The home page is not the main focus of the site and therefore no need to create a special link for it.

- **Site footer** - The site footer is available throughout the site and it clearly displays the shop address, social media links (social media links do not work as this site is for educational purposes only) and links to the static pages. 
### Home Page

![Home Page](/readme_data/site_pages/home_resize.png)

The home page displays a carousel of featured apps. The site administrator can add or remove featured status for any product when editing or creating a new product. This can be done by ticking a "Featured" checkbox on the product form. All featured products are added to the carousel. 

The carousel items contain a product image, product name, description, manufacturer, price and button which links to the product details page. From there the user can add the product to their cart. 

### About US

![About Us page](/readme_data/site_pages/about_us_resize.png)

The about us page is made up of two columns. The left column contains information about the company. The right column contains a map of Croatia. In mobile view, the columns expand so that the text is above the map. 

### Delivery & Returns Page

![Delivery and Returns](/readme_data/site_pages/delivery_returns_resize.png)

The Delivery and Returns Page inform the users on the terms and conditions for delivery as well as what to do if they wish to return any products. 

### FAQ Page

![FAQ](/readme_data/site_pages/faq_resize.png)

The FAQ page has all frequently asked questions from opening hours to how to register on the site. 
The questions are individually packaged into an accordion element from the Bootstrap framework. 

### Shop

![Shop](/readme_data/site_pages/shop_resize.png)

The shop page is the main focus of the site. This is where users can view all the products and it contains important elements:

- **Product Card** - Each product is displayed in its own product card. The card contains a product image, product name, manufacturer and price. At the bottom of the card there is a category link. When a user clicks on the category link the site will filter all products in that category and display on the shop page. 

- **Category side menu** - On the left there is a category site menu. It is dynamically generated based on the categories of products available in the shop. When an admin adds a new category in the administrator panel, a new category will appear in the side menu. If a user clicks on any of the categories, the products will filter by that category and display on the page. 

- **Product title** - Above the products there is a product count which informs the user how many products are in the category they are currently looking at. It also informs the user which category they have selected so that they can easily navigate through the shop. 

- **Sorting dropdown** - Above the products on the right there is a sorting dropdown menu which sorts products by price, manufacturer and alphabetically. 

- **Back to top button** - in the bottom right corner there is a "Back to top" button. If the user scrolls through the store they can press the button to get back to the top of the page. 

### Products Detail

![Products Detail](/readme_data/site_pages/product_details_resize.png)

The product details page gives the user more information about a product. 
On this page the user can see a larger image of the product. If they click on the image, a full size image will open in a new browser window. The user can see the product name, product manufacturer, product price, product description. 

From this page, the user can add this product to their cart by selecting the quantity and pressing "Add to cart". If the user does not want to purchase the product, they can return to the shop by pressing "Keep Shopping". 

### Product Success Message

![Product Success Message](/readme_data/site_pages/success_message_resize.png)

If a user decides to place an item into their cart, they will be presented with a message informing them that the product is now in their cart. From here the user can close the message and keep shopping or click "Go to Secure Checkout" and complete the order. 

### Checkout Page

![Checkout Page](/readme_data/site_pages/checkout_page_resize.png)

If a user decides to see what is in their cart, they will be taken to the checkout page. Here they will see a list of all the products in their cart, the quantity of products they selected, the individual product price and subtotal if they will buy additional quantities. 

If a user wishes to update the quantity, they can change the number in the number field and press "Update" This will update the quantity and recalculate the subtotal, grand total and delivery cost if the total is over €50. 

### Purchase page

![Purchase page](/readme_data/site_pages/purchase_page_zoom_out_resize.png)

The purchase page is separated into two columns. The included photo is zoomed out to 70% and therefore looks different to the other screenshots in this readme. 
The left column contains a form where the user will enter their shipping and billing information. 
Below the form there is an option to register for an account to save information to their profile or login if they already have an account. 
Below these links the user can either go back to the store to continue shopping or complete the purchase. 

The right column contains the details of the order. 

### Order Confirmation

![Order Confirmation](/readme_data/site_pages/order_confirmation_resize.png)

When a user completes the order, they will be presented with the order confirmation page. This page will show the user the products they ordered, the address where the order will be shipped and the total cost of the order. 

The user is also informed that an order will be emailed to their email address in the success message in the top right. 

## Features Left to Implement

- **Stock model** - A model referencing the products and displaying the current stock of items. This was not implemented due to time constraints. 

- **Custom 404 and 500 error pages** - This was not implemented due to time constraints. 


# Information Architecture

## Database Choice

The database used in development is [SQLlite3](https://www.sqlite.org/index.html) as it comes with the dhango package. However, in production, the database was changed to [PostgreSQL](https://www.postgresql.org/)
## Data Modeling

### Products App

#### Categories Model

**Database Key**|**Field Type**|**Validation**
:-----:|:-----:|:-----:
name|CharField|max\_length=254, null=False, blank=False
friendly\_name|CharField|max\_length=254, null=True, blank=True

#### Product Model

**Database Key**|**Field Type**|**Validation**
:-----:|:-----:|:-----:
category|Foreign Key "Category"|null=True, blank=True, on\_delete=models.SET\_NULL
sku|CharField|max\_length=254, null=True, blank=True
name|CharField|max\_length=254
description|TextField| 
manufacturer|Foreign Key "Manufacturer"|null=True, blank=True, on\_delete=models.SET\_NULL
price|DecimalField|max\_digits=6, decimal\_places=2, null=False, blank=False
image\_url|URLField|max\_length=1024, null=True, blank=True
image|ImageField|null=True, blank=True
featured|BooleanField|default=False

#### Manufacturer Model

**Database Key**|**Field Type**|**Validation**
:-----:|:-----:|:-----:
name|CharField|max\_length=254
friendly\_name|CharField|max\_length=254, null=True, blank=True

### Profile App

#### UserProfile Model

**Database Key**|**Field Type**|**Validation**
:-----:|:-----:|:-----:
user|OneToOneField - "User"|on\_delete=models.CASCADE
default\_phone\_number|CharField|max\_length=20, null=True, blank=True
default\_street\_address1|CharField|max\_length=100, null=True, blank=True
default\_street\_address2|CharField|max\_length=100, null=True, blank=True
default\_town\_or\_city|CharField|max\_length=40, null=True, blank=True
default\_eircode|CharField|max\_length=10, null=True, blank=True
default\_county|CharField|max\_length=100, null=True, blank=True
default\_country|CountryField|blank\_label="Country", null=True, blank=True

### Purchase App

#### Order Model

**Database Key**|**Field Type**|**Validation**
:-----:|:-----:|:-----:
order\_number|CharField|max\_length=32, null=False, editable=False
user\_profile|ForeignKey - "UserProfile"|on\_delete=models.SET\_NULL, null=True, blank=True, related\_name='orders'
full\_name|CharField|max\_length=50, null=False, blank=False
email|EmailField|max\_length=254, null=False, blank=False
phone\_number|CharField|max\_length=20, null=False, blank=False
country|CountryField|blank\_label="Country *", null=False, blank=False
eircode|CharField|max\_length=10, null=False, blank=False
town\_or\_city|CharField|max\_length=40, null=False, blank=False
street\_address1|CharField|max\_length=100, null=False, blank=False
street\_address2|CharField|max\_length=100, null=True, blank=True
county|CharField|max\_length=100, null=False, blank=False
date|DateTimefield|auto\_now\_add=True
delivery\_cost|DecimalField|max\_digits=10, decimal\_places=2, null=False, default=0
order\_total|DecimalField|max\_digits=10, decimal\_places=2, null=False, default=0
grand\_total|DecimalField|max\_digits=10, decimal\_places=2, null=False, default=0
original\_cart|TextField|null=False, blank=False, default="none"
stripe\_pid|Charfield|max\_length=254, null=False, blank=False, default="none"

#### OrderLineItem Model

**Database Key**|**Field Type**|**Validation**
:-----:|:-----:|:-----:
order|ForeignKey - "Order"|null=False, blank=False, on\_delete=models.CASCADE, related\_name='lineitems'
product|ForeignKey - "Product"|null=False, blank=False, on\_delete=models.CASCADE
quantity|IntegerField|null=False, blank=False, default=0
lineitem\_total|DecimalField|max\_digits=6, decimal\_places=2, null=False, blank=False, editable=False
# Technologies Used
## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - Used to display back-end data in HTML

## Libraries and Frameworks

- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [jQuery](https://jquery.com/) - to simplify DOM manipulation and to initialize Bootstrap functions.
- [Bootstrap](https://getbootstrap.com/) - as the front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - Used to import fonts for the project
- [Font Awesome](https://fontawesome.com/) - Used to add icons to buttons and as text supplements
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django.
- [Stripe](https://stripe.com/ie) - Service to handle payments in the app
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used to style forms in the app

## Tools

- [VSCode](https://code.visualstudio.com/) - A cross platform code editor used to develop this project
- [GitHub](https://github.com/) - A cloud based code repository used to store all code files for this project
- [Heroku](https://heroku.com) - Used to host this application online
- [PIP](https://pypi.org/project/pip/) - used to install the necessary dependencies for the project
- [Balsamiq Wireframes](https://balsamiq.com/) - Used to make wireframes for the project
- [Paint.net](https://www.getpaint.net/) - Used to resize images.
- [AWS S3 Bucket](https://aws.amazon.com/) - used to store static and media files
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Adds compatibility with AWS S3
- [Travis CI](https://travis-ci.com/) - Continuous integration service
- [Coolors.co](https://coolors.co/) - Color picker service
- [CleanPNG](https://www.cleanpng.com/png-croatia-vector-map-rijeka-2316421/download-png.html) - To download the favicon
- [The Noun Project](https://thenounproject.com/term/croatia-map/350294/) To download a map of Croatia for the about page. 
- [Microsoft Edge](https://www.microsoft.com/en-us/edge?r=1) - Web browser used for testing and page preview
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/) - Web browser user for testing
- [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) - Used to design the tables used in this readme file
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) - Used to create a virtual environment to install project dependencies

## Databases

- [SQLlite3](https://www.sqlite.org/index.html) - Database used in development
- [PostgreSQL](https://www.postgresql.org/) - Database used in production

## Testing

- [W3C Markup Validation Service](https://validator.w3.org/) - Testing that all HTML code is valid
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Testing that all CSS code is valid
- [JS Hint](https://jshint.com/) - Testing that all javascript code is valid
- [PEP8 Online](http://pep8online.com/) - Testing that all python code is valid

# Testing
# Deployment
## Local Deployment

To deploy this project locally please make sure you have the following installed:

- An IDE of your choice. I used VSCode
- Git
- Pip
- Python

The steps to follow are:

1. Download this git repository to your local machine. There are two ways to do this. Navigate to [Croatian Shop repo](https://github.com/bowets/croatianshop) and click on the green button. Download the ZIP file into a folder on your local machine and open with you IDE. 
Alternatively, you could open command prompt and navigate to your development folder. In that folder initialize Git with `git init`. Then go back to the repository, click on the green button and copy the link to the repository. When you copy the link in command prompt type `git clone <link you copied>`. This will download the repository to your local folder. 

2. Set the environmental variables
- Create `.env` file in the projects root directory
- Create `.gitignore` file and add `.env` to gitignore. 
- Set your environmental variables in `.env` as follows:
```
import os

os.environ.setdefault("SECRET_KEY", "< Your Secret Key >")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "< Your Stripe Public Key >")
os.environ.setdefault("STRIPE_SECRET_KEY", "< Your Stripe Secret Key >")
os.environ.setdefault('STRIPE_WH_SECRET', '< Your Stripe Web Handler Key >')
os.environ.setdefault('DEVELOPMENT', 'True')
```

3. Install the project requirements `pip install -r requirements.txt`
4. Perform migrations to initialize the database 
- `py manage.py makemigrations`
- `py manage.py migrate`
5. If you would like to load the data into the database you can use the db.json fixture. Otherwise you can add your own data through the admin panel. 
- To load the data using the fixture `py manage.py loaddata db.json`
6. Create a superuser to access the admin panel
- `py manage.py createsuperuser`
- Follow the prompts to create a super user
7. This should be all and you can start up the server
- `py manage.py runserver`
- Django will fire up the localhost server and you can see what the page looks like
8. If you would like to access the admin panel to modify or add products add `/admin` to the base URL in the browser

## Heroku Deployment

To deploy to Heroku you will need to clone the project as described in the local deployment section above. 
Once the project is cloned and ready on your local machine:

1. Create a new repository in Github and push this project into the new repository.
2. Log in to [Heroku](https://www.heroku.com/home) if you have an account or if you do not have an account, create a new account.
3. when in the Heroku dashboard, click on the "New" button and then select "Create new app"
4. On the next screen enter an app name (must be unique) and select the region closest to you. 
5. When in the app dashboard click on "Resources" and search for "Heroku Postgres". This will be your database for the project. 
6. Go to the settings tab and click on "Reveal config vars". You will see a config variable `DATABASE_URL`. Copy this URL and go back to the project in your IDE.
7. Install dj-database-url `pip install dj-database-url`
8. Open settings.py in your project and find `DATABASES`. 
8. Comment out the original database code and copy the below in. 
 ```
DATABASES = {
        'default': dj_database_url.parse(<DATABASE_URL that you copied from your heroku>)
    }
```
9. Now run migrations
- `py manage.py makemigrations`
- `py manage.py migrate`
- `py manage.py loaddata db.json`
- This will load the data into the postgres database in heroku
10. Delete the database codes from your settings.py and replace with:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.getenv('DATABASE_URL', ''))
    }
else:
    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
11. Go back to Heroku and navigate to settings and select "Reveal Config Vars. Here you will enter the configuration keys and values from your env.py file. They should look similar to this:
```
DATABASE_URL: <your database URL>
SECRET_KEY: <your secret key>
STRIPE_PUBLIC_KEY: <your secret key>
STRIPE_SECRET_KEY: <your secret key>
STRIPE_WH_SECRET: <your secret key>
SECRET_KEY: <your secret key>
AWS_ACCESS_KEY_ID: <your secret key>
AWS_SECRET_ACCESS_KEY: <your secret key>
EMAIL_HOST_PASS: <your email password from Google>
EMAIL_HOST_USER: <your email address>
USE_AWS: True
```
11. In the deploy section, click on "Connect to GitHub".
9. Select your github user account and search for the repository that you want to deploy.
10. If you want, you can enable Automatic Deployment. This will build your application each time you push any changes to GitHub.
11. Now go back to the "Deploy" tab and click on "Deploy Branch"
12. The website should be deployed on ```https://[your_app_name].herokuapp.com/```

# Credits
## Code
- The project's code was developed by following the Code Institute video lessons and based on the understanding of the Boutique Ado Django Mini-Project, but was customized, modified and enhanced to fit the project purposes.
- The Django web documentation provided information on creating additional models
- StackOverflow provided solutions to debugging URLs and view bugs
## Content and Media

- [CleanPNG](https://www.cleanpng.com/png-croatia-vector-map-rijeka-2316421/download-png.html) - Favicon
- [The Noun Project](https://thenounproject.com/term/croatia-map/350294/) Map of Croatia for the about page

## Acknowledgements

The Code Institute staff and lecturers. 
Special thanks to Guido Cecilio Garcia, my Code Institute mentor, for his guidance and advice whilst working on this project.
# Disclaimer

This application is developed for educational purposes only and not for commercial use. 