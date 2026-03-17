
def calculate_average(numbers: List[float]) -> float:
    
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return sum(numbers) / len(numbers)
