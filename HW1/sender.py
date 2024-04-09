
def encode_message(filename, message):
    with open(filename, 'wb') as file:
        for char in message:
            binary_char = bin(ord(char))[2:].zfill(8)
            file.write(binary_char.encode())


while True:
    message = input('Type your message: ')
    filename = "covert_channel.txt"
    encode_message(filename, message)
    print("Message encoded and written to file:", filename)
