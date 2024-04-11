import random

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
correct_answer = random.choice(lis)
counter = 0
number_not_found = True

while number_not_found:
    for i, number in enumerate(lis):
        print("Suggest a number between 1 and 10")
        answer = int(input())
        counter += 1

        if answer == correct_answer:
            print(f"Congratulations! {correct_answer} is the correct answer")
            print(f"You get the number with the {counter} try.")
            number_not_found = False
            break
        elif answer < correct_answer and counter <= 2:
            print(f"{answer} is not the correct answer. Do not give up. Try once again with bigger number.")
        elif answer > correct_answer and counter <= 2:
            print(f"{answer} is not the correct answer. Do not give up. Try once again with smaller number.")
        elif answer != correct_answer and counter == 3:
            print(f"{answer} is not the correct answer. Unfortunately, you failed.")
            print(f"The correct answer was {correct_answer}")
