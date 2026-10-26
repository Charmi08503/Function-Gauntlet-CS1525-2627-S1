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
    if celsius < 15:
        return "cold"
    elif celsius <= 25:
        return "comfortable"
    else:
        return "hot"

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    pass

