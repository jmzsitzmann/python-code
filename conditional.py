def grade(percentage):
    if percentage >= 90:
        print("your grade is A")
    elif percentage >= 80 and percentage < 90:
        print("your grade is B")
    elif percentage >= 70 and percentage < 80:
        print("your grade is C")
    elif percentage >= 60 and percentage < 70:
        print("your grade is D")
    elif percentage < 60:
        print("your grade is F")
score = input("what is your percentage?")
grade(score)