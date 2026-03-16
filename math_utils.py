# sample_math_utils.py

import math
from typing import List


def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): A list of numeric values.

    Returns:
        float: The average value of the numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return sum(numbers) / len(numbers)


def normalize_scores(scores: List[float]) -> List[float]:
    """
    Normalize a list of scores to a 0–1 range.

    Args:
        scores (List[float]): List of numeric scores.

    Returns:
        List[float]: Normalized scores between 0 and 1.
    """
    min_score = min(scores)
    max_score = max(scores)

    if max_score == min_score:
        return [0.0 for _ in scores]

    return [(s - min_score) / (max_score - min_score) for s in scores]


class Circle:
    """
    Represents a geometric circle and provides methods
    to compute its properties.
    """

    def __init__(self, radius: float):
        """
        Initialize a Circle instance.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: Area of the circle.
        """
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        """
        Calculate the circumference of the circle.

        Returns:
            float: Circumference of the circle.
        """
        return 2 * math.pi * self.radius


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filter even numbers from a list.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        List[int]: A list containing only even numbers.
    """
    return [num for num in numbers if num % 2 == 0]
