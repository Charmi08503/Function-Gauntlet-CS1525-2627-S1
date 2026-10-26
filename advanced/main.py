def temperature_in_safe_range(
    celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """Checks whether a temperature is within a safe range.
    Minimum_f and maximum_f are the range limits in Fahrenheit.
    Returns True if the temperature is within the range.
    """
    fahrenheit = celsius_to_fahrenheit(celsius)
    return minimum_f <= fahrenheit <= maximum_f

def can_afford_with_tip(
    balance: float, cost: float, tip_percent: float
) -> bool:
    """Checks whether someone can afford an item and its tip.
    Balance is the available money, cost is the price,
    and tip_percent is the tip percentage.
    Returns True if there is enough money for both.
    """
    tip = calculate_tip(cost, tip_percent)
    total_cost = cost + tip
    return balance >= total_cost

def meets_average(
    score1: float, score2: float, score3: float, required_average: float
) -> bool:
    """Checks whether three scores meet an average: score1, score2 and score3.
    Required_average is the minimum average needed.
    Returns True if the average is high enough.
    """
    average = average_three(score1, score2, score3)
    return average >= required_average

def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """Checks whether someone's initials match the expected initials.
    First_name and last_name are the person's names.
    Expected_initials are the initials being checked.
    Returns True if they match, otherwise False.
    """
    initials = make_initials(first_name, last_name)
    return initials.lower() == expected_initials.lower()