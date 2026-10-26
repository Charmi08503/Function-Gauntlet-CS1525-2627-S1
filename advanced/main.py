def is_even(number: int) -> bool:
    """Checks whether number is even.
    Returns True if number is even, otherwise False.
    """
    return number % 2 == 0

def count_vowels(text: str) -> int:
    """Counts the vowels in text.
    Returns the number of vowels.
    """
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit.
    Returns the temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

def reverse_text(text: str) -> str:
    """Reverses text.
    Returns the text backwards.
    """
    reversed_text = ""
    for letter in text:
        reversed_text = letter + reversed_text
    return reversed_text

def larger_number(number1: int, number2: int) -> int:
    """Finds the larger of two numbers: number1 and number2.
    Returns the larger number.
    """
    if number1 > number2:
        return number1
    else:
        return number2

def average_two(number1: int, number2: int) -> float:
    """Calculates the average of two numbers: number1 and number2.
    Returns their average.
    """
    return (number1 + number2) / 2

def can_afford(balance: float, cost: float) -> bool:
    """Checks whether someone can afford an item.
    Balance is the money available and cost is the item's price.
    Returns True if there is enough money, otherwise False.
    """
    return balance >= cost

def repeat_text(text: str, times: int) -> str:
    """Repeats a piece of text.
    Times is the number of repetitions.
    Returns the repeated text.
    """
    result = ""
    for count in range(times):
        result = result + text
    return result

def contains_word(sentence: str, word: str) -> bool:
    """Checks whether a sentence contains a certain word.
    Returns True if the word is found, otherwise False.
    """
    return word.lower() in sentence.lower()

def calculate_tip(cost: float, tip_percent: float) -> float:
    """Calculates a tip.
    Cost is the original price and tip_percent is the tip percentage.
    Returns the tip amount.
    """
    return cost * tip_percent / 100

def make_initials(first_name: str, last_name: str) -> str:
    """Makes initials from a first and last name.
    Returns the initials in uppercase.
    """
    return first_name[0].upper() + last_name[0].upper()

def percent_score(score: float, total: float) -> float:
    """Calculates a score as a percentage.
    Score is the points earned and total is the total possible points.
    Returns the percentage, or 0 if total is 0.
    """
    if total == 0:
        return 0.0
    return score / total * 100

def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Checks whether a number is within a range.
    Number is the value checked, minimum is the lowest value,
    and maximum is the highest value.
    Returns True if the number is within the range.
    """
    return minimum <= number <= maximum

def all_different(text1: str, text2: str, text3: str) -> bool:
    """Checks whether three pieces of text are different: text1, text2 and text3.
    Returns True if all three are different.
    """
    return text1 != text2 and text1 != text3 and text2 != text3

def average_three(number1: float, number2: float, number3: float) -> float:
    """Calculates the average of three numbers: number1, number2 and number3.
    Returns their average.
    """
    return (number1 + number2 + number3) / 3

def describe_temperature(celsius: float) -> str:
    """Describes a temperature.
    Returns cold, comfortable, or hot.
    """
    if celsius < 10:
        return "cold"
    elif celsius <= 20:
        return "comfortable"
    else:
        return "hot"


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

# Test calls

print("temperature_in_safe_range:", temperature_in_safe_range(20, 50, 80), "and", temperature_in_safe_range(0, 50, 80))

print("can_afford_with_tip:", can_afford_with_tip(25, 20, 10), "and", can_afford_with_tip(20, 20, 10))

print("meets_average:", meets_average(80, 90, 100, 85), "and", meets_average(50, 60, 70, 80))

print("initials_match:", initials_match("Peter", "Parker", "PP"), "and", initials_match("Tony", "Stark", "ST"))