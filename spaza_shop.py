#!/usr/bin/python2.7

import csv

def read_sales_history(filename="Nelisa Sales History.csv"):

    history = []

    with open(filename, "rU") as sales_history:
        for row in  csv.reader(sales_history):
            line = row[0].split(";")
	    if line[0] != "Day":
                history.append({"day" : line[0], "date" : line[1], "stock_item" : line[2], "no_sold" : int(line[3]), "sales_price" : line[4]})
    return history

def product_sales(sales_history):
	sales = {}

	for line in sales_history:
		if line["stock_item"] not in sales:
			sales[line["stock_item"]] = 0
		sales[line["stock_item"]] += line["no_sold"]

	return sales

def sales_to_array(sales):
	array = []

	for item in sales:
		array.append({item : sales[item]})

	return array

def most_popular(sales):

	sales_arr = sales_to_array(sales)
	most_pop = {}
	most_pop["name"] = ""
	most_pop["value"] = 0

	for item in sales_arr:

		if most_pop["value"] < item.items()[0][1]:
			most_pop["value"] = item.items()[0][1]
			most_pop["name"] = item.items()[0][0]

	final = {}
	final[most_pop["name"]] = most_pop["value"]
	return final


def most_popular_category(sales):
	product_sales = sales_to_array(sales)

	junk_food = 0
	veg_and_carbs = 0
	fruit = 0
	dairy = 0
	not_edible = 0

	for item in product_sales:
		this_is = item.items()[0][0]
		if this_is == "Mixed Sweets 5s" or this_is == "Fanta 500ml" or this_is == "Cream Soda 500ml" or this_is == "Heart Chocolates" or this_is == "Coke 500ml":
			junk_food += item.items()[0][1]

		elif this_is == "Chakalaka Can" or this_is == "Gold Dish Vegetable Curry Can" or this_is == "Iwisa Pap 5kg" or this_is == "Top Class Soy Mince" or this_is == "Bread":
			veg_and_carbs += item.items()[0][1]
		
		elif this_is == "Bananas - loose" or this_is == "Apples - loose":
				fruit += item.items()[0][1]
		
		elif this_is == "Milk 1l" or this_is == "Imasi":
				dairy += item.items()[0][1]
		
		elif this_is == "Soap Bar" or this_is == "Shampoo 1 litre" or this_is == "Rose (Plastic)" or this_is == "Valentines Cards":
				not_edible += item.items()[0][1]

	cat_sales = [{"junk_food" : junk_food}, {"veg_and_carbs" : veg_and_carbs}, {"fruit" : fruit}, {"dairy" : dairy}, {"not_edible" : not_edible}]

	most = {"name" : "", "value" : 0}
	for i in range(len(cat_sales)):
		if most["value"] < cat_sales[i].values()[0]:
			most["value"] = cat_sales[i].values()[0]
			most["name"] = cat_sales[i].keys()[0]

	moster = {most["name"] : most["value"]}
	return moster

most_popular_category(product_sales(read_sales_history()))