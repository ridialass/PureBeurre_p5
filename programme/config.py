#! /usr/bin/env python3
# coding: utf-8
# Config file
DB_USER = 'root'
DB_PASS = 'VQW9xu2NJbTM3NYq'
DB_NAME = 'off_db'
CATEGORIES_TO_USE = {
    "Poissons": "%poisson%",
    "Laits": "%lait%",
    "Confitures": "%confiture%",
    "Pizzas": "%pizza%",
    "Pâtisseries": "%patisserie%",
    "Compotes": "%compote%",
    "Infusions": "%infusion%",
    "Glaces": "%glace%",
    "Sandwichs": "%sandwich%",
    "Soupes": "%soupe%"
}
GRADES = ["a", "b", "c", "d", "e"]
HEALTHY_GRADES = ["a", "b"]
LESSHEALTHY_GRADES = ["c", "d", "e"]
LIMIT_PRODUCTS = 500
LIMIT_BAD_PRODUCTS = 20
LIMIT_SUBSTITUDE_FOOD = 5

DATABASE_URL = "mysql+mysqlconnector://root:VQW9xu2NJbTM3NYq@localhost/off_db?charset=utf8mb4"
#DATABASE_NAME = "pureBeure_db"
