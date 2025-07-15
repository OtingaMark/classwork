# --- BASIC DATA TYPES AND EXAMPLES ---

num: int = 10
name: str = "John Doe"
avg: float = 19.95
names: list = ["carl", "mary"]
cars: tuple = ("volvo", "CX-5")  # Changed square brackets to parentheses for tuple
marks: set = {1, 2, 3}  # Changed list to set using curly braces

# --- DICTIONARY ---

std: dict = {"Name": "Alice", "Age": 21}

students: list = [
    {"Name": "Alice", "Marks": [70, 69, 68]},
    {"Name": "Mark", "Marks": [71, 63, 64]},
    {"Name": "John", "Marks": [79, 86, 45]}
]

# --- AVERAGE FUNCTION ---

def average(marks: list[int]) -> float:
    return sum(marks) / len(marks)  # Use len(marks),

# --- TESTING THE AVERAGE FUNCTION ---

for student in students:
    name = student["Name"]
    avg_score = average(student["Marks"])
    print(f"{name}'s average score is {avg_score:.2f}")
