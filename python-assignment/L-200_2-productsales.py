#!/usr/bin/env python3

#########################################################################################################
######################## This script will perfom product sales calculations ###########################
#####################################    Author : Arun Reddy       ######################################
#########################################################################################################

def calculate_sales_fun(salesdata_list):
    product_sales={}
    for sale in salesdata_list:
        product_id = sale['product_id']
        quantity_sold = int(sale['quantity_sold'])
        price_per_unit = int(sale['price_per_unit'])
        revenue = quantity_sold * price_per_unit
        if product_id in product_sales:
            product_sales[product_id]['quantity_sold'] += quantity_sold
            product_sales[product_id]['revenue'] += revenue
        else:
            product_sales[product_id] = {'product_name': sale['product_name'], 'quantity_sold': quantity_sold, 'revenue': revenue}
    return product_sales

def print_total_sales(product_sales):
    for product_id, sales_info in product_sales.items():
        print(f"Product ID: {product_id}, Product Name: {sales_info['product_name']}, Total Sales: {sales_info['revenue']}")

def main():

    salesdata_list=[

    {'product_id':'p001', 'product_name':'pname1', 'quantity_sold':'5', 'price_per_unit':'40'},
    {'product_id':'p002', 'product_name':'pname2', 'quantity_sold':'15', 'price_per_unit' : '20'},
    {'product_id':'p003', 'product_name' : 'pname3', 'quantity_sold':'25', 'price_per_unit' : '10'},
    {'product_id' : 'p002', 'product_name' : 'pname2', 'quantity_sold': 53, 'price_per_unit':'20'}

    ]
    product_sales=calculate_sales_fun(salesdata_list)

    print_total_sales(product_sales)

main()