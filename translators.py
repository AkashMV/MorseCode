from dictionaries import string_to_morse, morse_to_string


def morse_to_text(morse):
    morse_char = ''
    morse_word = [None]

    try:
        for char in morse:
            index = len(morse_word) - 1
            if char == ' ':
                morse_word.append(None)
                morse_char = ''
                continue
            morse_char += char
            morse_word[index] = morse_to_string[morse_char]
        translated_string = ''.join(morse_word)
        return translated_string
    except KeyError:
        print("Please make sure that you have entered morse code.")
        print('Please make sure you have entered "/" for space\n')
        print('Note- This translator does not support special characters \n')

        return False


def text_to_morse(text):
    try:
        morse = ''
        for letter in text:
            morse += string_to_morse[letter.upper()]
            morse += ' '
        return morse
    except KeyError:
        print("Please make sure that you have entered a text.")
        print('Please make sure you have entered "/" for space\n')
        print('Note- This translator does not support special characters \n')

        return False


def translator(user_input, mode):

    if mode:
        result = text_to_morse(user_input)
        if result:
            print(f"Your input: {user_input}\n"
                  f"Your input in morse: {result}"
                  )
            return result
        else:
            print('Translation failed')
            return False

    elif not mode:
        result = morse_to_text(user_input)
        if result:
            print(f"Your input: {user_input}\n"
                  f"Your input in text: {result}"
                  )
            return result
        else:
            print('Translation failed')
            return False
