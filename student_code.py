"""Learning Outcome: Functions"""
import statistics
from collections import Counter
def sum_of_squares(n: int):
    """
    Calculate the sum of the squares of all integers from 1 to n.

    Parameters:
    n (int): A non-negative integer up to which the squares will be summed.

    Returns:
    int: The sum of the squares of all integers from 1 to n.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n >= 0:
        return sum(map(lambda n: n*n,[num for num in range(1,n+1)])) 
    else:
        raise ValueError

def evaluate_performance(grades: list, min_pass: int):
    """
    Evaluate the performance based on a list of grades and a minimum passing grade.

    Parameters:
    grades (list): A list of integers representing student grades.
    min_pass (int): The minimum average grade required to pass.

    Returns:
    str: "Pass" if the average grade is greater than or equal to min_pass, otherwise "Fail".
    """
    return 'Pass' if (sum(grades)/len(grades)) >= min_pass else 'Fail'
    

def calculate_cumulative_performance(scores: dict):
    """
    Calculate the cumulative performance based on student scores.

    Parameters:
    scores (dict): A dictionary where keys are subject names and values are the corresponding scores.

    Returns:
    dict: A dictionary containing the average score and a list of subjects where the score is below average.
    """
    allnum = []
    for k,v in scores.items():
        allnum.append(v)
    ava = round(sum(allnum)/len(allnum),2)
    return {"average":ava, "below_average":[sjb for sjb,v in scores.items() if v < ava]}


def analyze_improvement(scores: list):
    """
    Analyze the improvement trend based on a list of scores.

    Parameters:
    scores (list): A list of integers representing scores over time.

    Returns:
    dict: A dictionary containing the trend of improvement ("positive", "negative", or "neutral") 
          and a boolean indicating whether there has been an improvement.
    """
    trend = ''
    if scores[0]>scores[1]:
        trend = "positive" 
    elif scores[0]==scores[1]:
        trend = "neutral"
    else:
        trend =  "negative"

    
    return {
        "trend":  trend,
        "improved": True
    }

def rank_students(students: list[tuple[str, int]]):
    """
    Rank students based on their scores.

    Parameters:
    students (list): A list of tuples where each tuple contains a student's name and their score.

    Returns:
    list: A sorted list of tuples in descending order based on scores.
    """
    pass

"""Learning Outcome: Basic Loops"""
def even_numbers(n: int):
    """
    Generate a list of even numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating even numbers.

    Returns:
    list: A list of even integers from 1 to n.
    """
    return [n for n in range(1,n+1) if n % 2 == 0]

def odd_numbers(n: int):
    """
    Generate a list of odd numbers from 1 to n.

    Parameters:
    n (int): The upper limit for generating odd numbers.

    Returns:
    list: A list of odd integers from 1 to n.
    """
    return [n for n in range(1,n+1) if n % 2 != 0]

def sum_multiples_of_num(num: int, length: int):
    
    """
    Calculate the sum of multiples of a given number up to a specified length.

    Parameters:
    num (int): The number whose multiples are to be summed.
    length (int): The upper limit for the range of multiples.

    Returns:
    int: The sum of multiples of num from 1 to length.
    """
    # return sum([n for n in range(1,length) if n % num == 0])

def skip_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping a specific number.

    Parameters:
    n (int): The number to skip.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n.
    """
    pass

def break_test(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, stopping when a specific number is encountered.

    Parameters:
    n (int): The number at which to stop adding to the list.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding n and stopping before it.
    """
    pass

def sum_numbers_until_zero(nums: list):
    """
    Calculate the sum of numbers in a list until a zero is encountered.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The sum of integers in the list up to (but not including) the first zero.
    """
    joined = "".join(str(item) for item in nums)
    splied = joined.split('0')    
    return sum([int(item) for item in list(splied[0])])

def count_positive_numbers(nums: list):
    """
    Count the number of positive integers in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    return len([i for i in nums if i > 0])

def sum_dictionary_values(dictionary: dict):
    """
    Calculate the sum of all values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    """
    return sum(dictionary.values())

def sum_unique_elements(elements: list):
    """
    Calculate the sum of unique elements in a list.

    Parameters:
    elements (list): A list of integers.

    Returns:
    int: The sum of unique integers in the list.
    """
    return sum(set(elements))

def skip_divisible_by_num(n: int, length: int):
    """
    Generate a list of numbers from 1 to length, skipping those that are divisible by a specific number.

    Parameters:
    n (int): The number to skip multiples of.
    length (int): The upper limit for generating numbers.

    Returns:
    list: A list of integers from 1 to length, excluding those divisible by n.
    """
    return [num for num in range(1, length+1) if num % n != 0]

"""Learning Outcome: Processing Data"""

def square_numbers(nums: list):
    """
    Calculate the square of each number in a list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    """
    return list(map(lambda n: n**2,nums))

def transform_string(input: str, transform: str):
    """
    Transform a string based on the specified transformation type.

    Parameters:
    input (str): The string to be transformed.
    transform (str): The type of transformation ('capitalize', 'upper', 'lower').

    Returns:
    str: The transformed string.

    Raises:
    ValueError: If the transformation type is unknown.
    """
    return input.capitalize() if transform == 'Capitalize' else input.upper() if transform == 'Uppercase' else input.lower()
def sum_and_average(nums: list[int]):
    """
    Calculate the sum and average of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    tuple: A tuple containing the sum and average of the numbers.
    """
    return (sum(nums),sum(nums)/len(nums))

def word_frequency_count(words: list[str]):
    """
    Count the frequency of each word in a list.

    Parameters:
    words (list[str]): A list of words.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    return Counter(words)

def filter_even_numbers(nums: list[int]):
    """
    Filter out even numbers from a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    return [n for n in nums if n % 2 == 0]

"""Learning Outcome: Simple Algorithms(Problem Solving)"""

def find_median(nums: list[int]):
    """
    Find the median of a list of numbers.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    float: The median value of the list.

    Raises:
    ValueError: If the list is empty.
    """
    if len(nums) > 0 :
        return statistics.median(nums)
    else:
        raise ValueError

def reverse_string(input: str):
    """
    Reverse the given string.

    Parameters:
    input (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return input[::-1]

def largest_number(nums: list[int]):
    """
    Find the largest number in a list.

    Parameters:
    nums (list[int]): A list of integers.

    Returns:
    int or None: The largest number in the list, or None if the list is empty.
    """
    return max(nums) if len(nums) != 0 else None

def is_prime(n: int):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    return True if len([num for num in range(1,n+1) if n % num == 0] )== 2 else False

def count_character_occurrences(word_sentence: str, char_count: str):
    """
    Count the occurrences of a character in a given sentence.

    Parameters:
    word_sentence (str): The sentence in which to count occurrences.
    char_count (str): The character to count.

    Returns:
    int: The number of occurrences of the character in the sentence.
    """
    return word_sentence.count(char_count)