# Projet 5 : Utilisez les donnees publiques de l'OpenFoodFacts

Develop with python3/Ubuntu

### Installation Guide

#### 1. Create a virtualenv with python3
```
virtualenv --python=python3 env
```
#### 2. Install requirements
```
pip install -r requirements.txt
```
#### 3. Authorize access to the database
```
GRANT ALL PRIVILEGES ON * . * TO 'yourusername'@'localhost' IDENTIFIED BY 'yourpassword';
```
#### 4. Edit config.py file
```
DB_USER = 'yourusername'
DB_PASS = 'yourpassword'
DB_NAME = 'yourdatabasename'
```
#### 5. Choose categories
add or delete categories. Max 10. You can unselect a categories with a '#' in front of the name.
```
#Pizzas -> unselect pizza
Pizzas -> select pizza
```
#### 6. Add contents to the database
```
python db_creation.py
```
#### 7. Install Fonts

#### 8. Start app
```
python open_food_facts.py
```
