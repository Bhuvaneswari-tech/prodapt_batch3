import math

def calc_late_fee(days_late):
    return math.ceil(days_late * 2.5)
