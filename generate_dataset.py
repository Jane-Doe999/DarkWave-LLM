import random

OUTPUT_FILE = "dataset.txt"
TARGET_LINES = 20000

coding_questions = [
    ("what is python", "Python is a programming language used for automation, scripting, data science, and software development."),
    ("what is a variable", "A variable stores a value that can be used by a program."),
    ("what is a function", "A function is a reusable block of code that performs a task."),
    ("what is a loop", "A loop repeats code multiple times."),
    ("what is recursion", "Recursion is when a function calls itself."),
    ("write a python for loop", "for i in range(10):\n    print(i)"),
    ("write a function that adds two numbers", "def add(a, b):\n    return a + b"),
    ("what is a list in python", "A list is a collection of ordered values."),
    ("what is a dictionary in python", "A dictionary stores key value pairs."),
    ("what is an algorithm", "An algorithm is a step by step procedure for solving a problem."),
]

knowledge_questions = [
    ("what is gravity", "Gravity is a force that attracts objects with mass toward each other."),
    ("what is the sun", "The sun is a star at the center of our solar system."),
    ("what is water", "Water is a molecule made of two hydrogen atoms and one oxygen atom."),
    ("what is electricity", "Electricity is the flow of electric charge."),
    ("what is the capital of France", "The capital of France is Paris."),
    ("what is the capital of Japan", "The capital of Japan is Tokyo."),
    ("what is photosynthesis", "Photosynthesis is how plants convert sunlight into energy."),
    ("what is the speed of light", "The speed of light is approximately 299,792,458 meters per second."),
    ("what is an atom", "An atom is the smallest unit of matter."),
    ("what is a planet", "A planet is a large object that orbits a star."),
]

math_questions = [
    ("what is 2 plus 2", "2 plus 2 equals 4."),
    ("what is 10 times 5", "10 times 5 equals 50."),
    ("what is 9 minus 3", "9 minus 3 equals 6."),
    ("what is 12 divided by 4", "12 divided by 4 equals 3."),
]

all_pairs = coding_questions + knowledge_questions + math_questions

lines = []

while len(lines) < TARGET_LINES:
    q, a = random.choice(all_pairs)
    lines.append(f"User: {q}\nAI: {a}\n")

with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Added {TARGET_LINES} lines to dataset.txt")
