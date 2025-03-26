"""Exercise 03 Dictionary"""

__author__ = "730673399"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary"""
    inverted_dict: dict[str, str] = {}  # initialize empty dictionary
    for key in input_dict:  # iterates over each key in input dictionary
        value = input_dict[key]  # access corresponding value
        if value in inverted_dict:  # Check if value is already in the key
            raise KeyError(
                f"Duplicate value '{value}' found, cannot invert dictionary."
            )
        inverted_dict[value] = (
            key  # Assigns original value as new key and original key as new value
        )
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the # of times each unique string is found in the list."""
    count_dict = {}  # initializes an empty dictionary to store the counts
    for item in input_list:  # iterates over each item in list
        if item in count_dict:  # If items already in dictionary, incremete count by 1
            count_dict[item] += 1
        else:  # if not in dictionary, initialize count to equal 1
            count_dict[item] = 1
    return count_dict  # Returns the dictionary with counted occurences


def favorite_color(name_color_dict: dict[str, str]) -> str:
    """Determines most common favorite color in a dictionary."""
    color_counts = count(
        [name_color_dict[key] for key in name_color_dict]
    )  # counts occurence of each color
    max_count = max(color_counts[color] for color in color_counts)  # find highest count

    for key in name_color_dict:  # iterate over keys to find first max occurence
        color = name_color_dict[key]
        if color_counts[color] == max_count:
            return color  # return first encountered most frequent color
    return ""  # returns an empty string if no color is found


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Bins strings into a dictionary based on length."""
    length_bins = {}
    for string in strings:
        length = len(string)
        if length not in length_bins:
            length_bins[length] = []
        if string not in length_bins[length]:
            length_bins[length].append(string)
    return length_bins
