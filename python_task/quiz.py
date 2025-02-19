# Python task- Clothing Brands Quiz
print("\033[32mWelcome to the Clothing Brand Quiz!\033[0m")
print("\033[32mTest your knowledge about popular clothing brands and their logos.\033[0m")
print("\033[32mChoose the correct answer and have fun!\033[0m")
print("\033[32mLet’s get started! 🌟\033[0m")
questions = [
    ("Which brand is known for its iconic 'swoosh' logo and athletic wear?", ["A. Nike", "B. Adidas", "C. Puma", "D. Reebok"], "A"),
    ("Which brand's logo is a red and white 'C' and is known for high-end denim and apparel?", ["A. Levi's", "B. Calvin Klein", "C. Tommy Hilfiger", "D. Wrangler"], "A"),
    ("Which luxury brand has a logo featuring a horse and rider?", ["A. Ralph Lauren", "B. Hugo Boss", "C. Lacoste", "D. Burberry"], "A"),
    ("Which brand is known for its 'three stripes' logo and is a major sportswear brand?", ["A. Nike", "B. Adidas", "C. Under Armour", "D. Puma"], "B"),
    ("Which clothing brand is associated with the logo of a crocodile?", ["A. Lacoste", "B. Fred Perry", "C. Polo Ralph Lauren", "D. Nautica"], "A")
]

score = 0

# Loop through each question, options, and answer
for question, options, correct_answer in questions:
    print("----------------------")
    print(question)
    for option in options:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()

    if guess == correct_answer:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {correct_answer}")

# Display final results
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print(f"Your score is: {score}/{len(questions)}")
print(f"Your score is: {int((score / len(questions)) * 100)}%")

