import os
import time

def decode_message(filename):
    decoded_message = ""
    with open(filename, 'rb') as file:
        while True:
            binary_char = file.read(8)
            if not binary_char:
                break
            decoded_char = chr(int(binary_char, 2))
            decoded_message += decoded_char
    return decoded_message


filename = "covert_channel.txt"
final_message = ''
while True:
    if os.path.isfile(filename):
        decoded_message = decode_message(filename)
        if final_message != decoded_message:
            final_message = decoded_message
            print("Decoded message:", decoded_message)
    else:
        print(f'{filename} not found!')
        time.sleep(1)
