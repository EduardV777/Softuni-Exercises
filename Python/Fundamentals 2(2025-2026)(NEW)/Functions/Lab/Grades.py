# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"


def grade(val = float(input())):

    if 2.00 <= val <= 2.99:
        print("Fail")

    elif 3.00 <= val <= 3.49:
        print("Poor")

    elif 3.50 <= val <= 4.49:
        print("Good")

    elif 4.50 <= val <= 5.49:
        print("Very Good")

    elif 5.50 <= val <= 6.00:
        print("Excellent")


grade()