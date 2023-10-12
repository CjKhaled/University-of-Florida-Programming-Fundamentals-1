db = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9} #Database of values to be converted

def decoding_menu():
    print("Decoding Menu")
    print("-" * 13)
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit \n")

#Looks messy for just a character, but just reused my code for a whole string decode
def hex_char_decode(hex):
    hex_input = list(hex)
    new_list = []
    translated_list = []
    answer_list = []
    for item in hex_input:
        if item == 'x':
            continue
        new = item.lower()
        new_list.append(new)
    new_list.reverse()
    for value in new_list:
        for key, item in db.items():
            if value == key:
                value = item
                translated_list.append(value)

    count = 0
    for integer in translated_list:
        product = integer * 16**count
        count += 1
        answer_list.append(product)

    decoded = sum(answer_list)

    return decoded

def hex_string_decode(hex):
    hex_input = list(hex) #Turning the string into a list of values
    new_list = []
    translated_list = []
    answer_list = []
    for item in hex_input:
        if item == 'x':
            continue
        new = item.lower()
        new_list.append(new) #Filling a new list with lowered values
    new_list.reverse()
    for value in new_list:
        for key, item in db.items():
            if value == key:
                value = item
                translated_list.append(value) #Converting the values into hexadecimal

    count = 0
    for integer in translated_list:
        product = integer * 16**count #Multiplying and adding it out. I reversed the list so I could increment exponents correctly
        count += 1
        answer_list.append(product)

    decoded = sum(answer_list)

    return decoded

def binary_string_decode(binary):
    binary_input = list(binary)
    new_list = []
    translated_list = []
    for item in binary_input:
        if item == 'b': #Essentially the same process as our other decodes
            continue
        new = item.lower()
        new_list.append(new)
    new_list.reverse()

    count = 0
    for integer in new_list:
        if integer == '0':
            count += 1
            continue
        product = 2 ** count
        translated_list.append(product)
        count += 1

    decoded = sum(translated_list)
    decoded = int(decoded)

    return decoded


def main(): #Our main function controlling the program. Made sure to account for various bugs
    repeat = True
    while repeat is True:
        decoding_menu()
        try:
            answer = int(input("Please enter an option: "))
            if answer > 4 or answer < 0:
                print("You need to input a number 1-4!")
            elif answer == 1:
                conversion = input("Please enter the numeric string to convert: ")
                if len(conversion) > 1:
                    result = hex_string_decode(conversion)
                else:
                    result = hex_char_decode(conversion)
                print(f"Result: {result}")
            elif answer == 2:
                conversion = input("Please enter the numeric string to convert: ")
                result = binary_string_decode(conversion)
                print(f"Result: {result}")
            elif answer == 4:
                print("Goodbye!")
                repeat = False
        except ValueError:
            print("You need to input a number 1-4!")

if __name__ == "__main__":
    main()