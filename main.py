def get_message():
    val = input("Enter your message: ")
    return val

def get_shift():
    shift = int(input("Enter the number of shifts: "))
    return shift

def encode_message(message, shifts):
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            encoded_message += chr(ord(letter) + shifts)
        else:
            encoded_message += letter

    return encoded_message

def main():
    message = get_message()
    shifts = get_shift()
    encrypted = encode_message(message, shifts)
    print(encrypted)
   
if __name__ == "__main__":
    main()