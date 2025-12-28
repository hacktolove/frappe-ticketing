import random
def generate_seat():
    letters = ["A", "B", "C", "D", "E"]
    random_letter = random.choice(letters)

    random_number = random.randint(1,100)

    return f"{random_number}{random_letter}"
