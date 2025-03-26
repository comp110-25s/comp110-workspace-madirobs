"""Exercise 03 Dictionary Tests"""

__author__ = "730673399"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len
import pytest


# tests for invert
def test_invert_():
    """Tests invert with a simple dictionary."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair():
    """Tests invert with a single key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_key_error():
    """Tests invert raising KeyError when duplicat values exist."""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "micheal": "jordan"}
        invert(my_dictionary)


# Tests for count
def test_count_basic_case():
    """Tests count with a list of words."""
    assert count(["apple", "banana", "apple", "cherry", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "cherry": 1,
    }


def test_count_empty_list():
    """Tests count with an empty list."""
    assert count([]) == {}


def tests_count_single_occurrences():
    """Tests count when all elements are unique."""
    assert count(["red", "blue", "green"]) == {"red": 1, "blue": 1, "green": 1}


# Tests for favorite_color


def test_favorite_color_basic_case():
    """Tests favorite_color with a mix of colors."""
    assert favorite_color({"audrey": "blue", "morgan": "red", "madi": "blue"}) == "blue"


def test_favorite_color_tie():
    """Tests favorite_color when two colors have the same occurrence."""
    assert (
        favorite_color(
            {"audrey": "blue", "madi": "pink", "morgan": "pink", "shannon": "blue"}
        )
        == "blue"
    )


def test_favorite_color_single_entry():
    """Tests favorite_color with a single entry."""
    assert favorite_color({"madi": "pink"}) == "pink"


# Tests for bin_len


def test_bin_len_basic_case():
    """Tests bin_len with different length words"""
    assert bin_len(["the", "bad", "friend"]) == {3: {"the", "bad"}, 6: {"friend"}}


def test_bin_len_duplicates():
    """Tests bin_len to ensure duplicates aren't added twice."""
    assert bin_len(["the", "the", "bad"]) == {3: {"the", "bad"}}


def test_bin_len_empty_list():
    """Tests bin_len with an empty list."""
    assert bin_len([]) == {}
