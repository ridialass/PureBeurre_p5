# Purebeurre
Software for the company "Pur beurre"

## Getting Started

The software will analyse a database in order to compare and  find, some products of substitution healthier than user's habits.

### Prerequisites

- [python 3.6 or more](https://www.python.org/downloads/)
- [mysql under wamp_server](http://www.wampserver.com/)

### Functions:

* Search for food in the Open Food Facts database.
* The program offers substitute, description, store or purchase and a link to the Open Food Facts page.
* The user interacts with the program in the terminal.
* If the user enters a character that is not expected, the program repeats the question.
* The search is done on a MySQL database.

### Installation Guide

#### 1. Create a virtualenv with python3
```
python -m virtualenv env
```
#### 2. Activate virtualenv with python3
```
.\Scripts\activate
```
#### 3. Install requirements
```
pip install -r requirements.txt

#### 4. Edit config.py file
```
DB_USER = 'your_user_name'
DB_PASS = 'your_password'
DB_NAME = 'your_database_name'
```
#### 5. Create database
```
python db_creation.py
```
#### 6. Populate database with data from API
```
python db_populate_tables.py
```
#### 7. Start app
```
python client.py
```

### How to use it:

At the launch of the program, two choices are available to the user:
1. Choice 1:
Choose a food to substitute
2. Choice 2:
View favorite foods

If the user chooses the first category, the program asks him the following questions:
* Select category
* Select a product from category
* The program offers a substitute, its description, a store where to buy it and a link to the Open Food Facts page about this food
* Save the result in the database if wanted.

If the user chooses the second category, it is returned to the database containing the foods he has saved in the favorites.

