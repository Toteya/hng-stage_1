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

    if not number:
        abort(400)
    try:
        number = int(number)
    except ValueError:
        abort(400)

    response = {
        'number': number,
        'is_prime': is_prime(number),
        'is_perfect': is_perfect(number),
        'properties': get_properties(number),
        'digit_sum': get_digit_sum(number),
        'fun_fact': get_fun_fact(number)
    }

    return jsonify(response), 200


def get_digit_sum(number):
    """ Returns the sum of the digits of the given number
    """
    number = abs(number)
    sum = 0
    while number > 0:
        sum += number % 10
        number = int(number / 10)

    return sum


def get_fun_fact(number):
    """ Returns an interesting fact about the given number from numbersapi.com
    """
    url = f'http://numbersapi.com/{number}/math'
    response = requests.get(url)
    return response.text


def is_prime(number):
    """ Checks and returns whether the given number is a prime number or not
    """
    if number < 2:
        return False

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True


def is_perfect(number):
    """ Checks and returns whether the given number is a Perfect Number:
    i.e. A positive integer that equals the sum of its proper factors (all its
    divisors except itself)
    """
    # find the list of factors of the number
    factors = [i for i in range(1, int(number / 2) + 1) if number % i == 0]

    if sum(factors) == number:
        return True
    return False


def get_properties(number):
    """ Returns the properties of a number - whether it's odd or even, whether
    or not it's an Armstrong number.
    """
    properties = []
    if number % 2 == 0:
        properties.append('even')
    else:
        properties.append('odd')
    # properties.append('even') if number % 2 == 0 else properties.append('odd')

    num = number
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = int(num / 10)

    pow = len(digits)
    narcissistic_sum = 0
    for digit in digits:
        narcissistic_sum += digit ** pow

    if narcissistic_sum == number:
        properties.append('armstrong')

    return properties
