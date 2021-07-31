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
## Existing Features
## Features Left to Implement
# Information Architecture
## Database Choice
## Data Modeling
# Technologies Used
## Languages
## Libraries and Frameworks
## Tools
## Databases

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


# Testing
# Deployment
## Local Deployment
## Heroku Deployment
# Credits
## Code
## Content and Media
## Acknowledgements
# Disclaimer