#!/usr/bin/env python3
"""
module app:
Flask public API
"""
from api.v1 import app_bp
from flask import abort, jsonify, request
import requests


@app_bp.route('/classify-number', methods=['GET'], strict_slashes=False)
def classify_number():
    """ Returns interesting mathematical properties about a number,
    including a fun fact.
    """
    number = request.args.get('number')
    try:
        number = int(number)
    except ValueError:
        abort(400)

    response = {
        'number': number,
        'is_prime': is_prime(number),
        'is_perfect': '',
        'properties': [],
        'digit_sum': get_digit_sum(number),
        'fun_fact': get_fun_fact(number)
    }

    return jsonify(response), 200


def get_digit_sum(number):
    """ Returns the sum of the digits of the given number
    """
    sum = 0
    while number > 0:
        sum += number % 10
        number = int(number / 10)

    return sum


def get_fun_fact(number):
    """ Returns an interesting fact about the given number from numbersapi.com
    """
    url = f'http://numbersapi.com/{number}'
    response = requests.get(url)
    return response.text

def is_prime(number):
    """ Checks and returns whether the given number is a prime number or not
    """
    if number < 2:
        return False

    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return False
    return True