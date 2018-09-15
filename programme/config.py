#! /usr/bin/env python3
# coding: utf-8
"""Configuration file for the constants."""

DB_USER = 'p5_user'
DB_PASS = 'p5_password'
DB_NAME = 'p5_db'
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
