# dictionary = {
#
#     "Name" : "Mostak",
#     "Age"  : 21,
#     "Phone Number" : "12345678"
# }
#
# print(dictionary.get("Name", "You have entered an invalid value"))

number = {

    '0' : "Zero",
    '1' : "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
}

user_number = input(">")

for i in user_number:
    print(number.get(i, "(!)"), end=" " )