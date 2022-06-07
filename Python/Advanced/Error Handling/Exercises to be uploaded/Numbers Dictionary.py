class NextInput(Exception):
    pass

numbers_dictionary={}

line=input()

while line!="Search":
    number_as_string=line
    try:
        try:
            number=int(input())
            numbers_dictionary[number_as_string]=number
            if number!="Search":
                raise NextInput
        except ValueError:
            print("The variable number must be an integer")
            raise NextInput
    except NextInput:
        line=input()


line=input()

while line!="Remove":
    searched=line
    try:
        try:
            print(numbers_dictionary[searched])
            if line!="Remove":
                raise NextInput
        except KeyError:
            print("Number does not exist in dictionary")
            raise NextInput
    except NextInput:
        line=input()

line=input()

while line!="End":
    searched=line
    try:
        try:
            del numbers_dictionary[searched]
            if line!="End":
                raise NextInput
        except KeyError:
            print("Number does not exist in dictionary")
            raise NextInput
    except NextInput:
        line=input()

print(numbers_dictionary)