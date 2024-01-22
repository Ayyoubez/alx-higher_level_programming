#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except (ValueError, TypeError, ZeroDivisionError):
        result = None
        return result
    finally:
        print("Inside result: {} ".format(result))
