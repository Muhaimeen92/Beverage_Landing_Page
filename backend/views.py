import json
import uuid

import names
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .models import Order


def index(request):
    '''
    This method is the /order API call that generates an order number and stores the incoming order request
    in the database.
    '''
    if request.method == 'POST':
        order_details = json.loads(request.body)
        order_details = check_order_details(order_details)
        order_number = str(generate_order_number())
        generate_order(order_details, order_number)
        order = get_Order(order_number)

        return JsonResponse(order)

def display_order(request, order_number):
    '''
    This is method serves the GET request for retrieving an order with a specific order number from the database.
    '''
    if request.method == 'GET':
        order = get_Order(order_number)
        return JsonResponse(order)

def generate_order(order_details, order_number):
    '''
    Creates a new order and stores in the databse
    '''

    order = Order(orderNumber=order_number, customerName=order_details["customerName"],
                  quantity=int(order_details["quantity"]), city=order_details["city"],
                  province=order_details["province"], country=order_details["country"])
    order.save()
    return

def get_Order(order_number):
    '''
    Fetches an order with a particular order number from the database.
    '''

    order = Order.objects.get(orderNumber=order_number)
    order = model_to_dict(order)
    return order

def generate_order_number():
    '''
    Generates a random UUID4 number for the order number
    '''

    order_number = uuid.uuid4()
    return order_number

def check_order_details(order_details):
    '''
    Checks to see if the incoming order details has a cusotmer name and/or quantity of order proivded. If not,
    generates a random name for customer name and sets quantity to 1.
    '''

    if not order_details["customerName"]:
        order_details["customerName"] = names.get_full_name()
    if not order_details["quantity"]:
        order_details["quantity"] = 1

    return order_details
