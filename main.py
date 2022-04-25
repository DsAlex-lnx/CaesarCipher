def caesar_cipher_encode(text, key):
    cipher = ''
    
    for letter in range(len(text)):
        char = text[letter]
        
        cipher += chr((ord(char) + key - 64) % 26 + 65)  
    
    return cipher

def caesar_cipher_decode(cipher):
    alphabetic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for letter in range(len(alphabetic)):
        decode = '' 
        for character in cipher:
            if character in alphabetic:
                search = alphabetic.find(character)
                search -= letter 
                if search < 0:
                    search += len(alphabetic)
                decode += alphabetic[search]
            else:
                decode += character
    
        print('Decode #%s: %s' % (letter+1, decode))  


def main():
    clear_text = input('Enter your text here:\n').upper()

    print('Chose option by number:\n')
    option = int(input('(1) Code | (2) Decode\n'))

    if option == 1:
        shift_pattern = int(input('Chose a shift pattern:\n'))

        result = caesar_cipher_encode(clear_text, shift_pattern)
        print(result)    

    elif option == 2:
        caesar_cipher_decode(clear_text)

    else: 
        print('Chose a valid option!')

if __name__ == '__main__':
    main()

