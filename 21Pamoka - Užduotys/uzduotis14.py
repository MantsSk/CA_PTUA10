class MorseCodeTranslator:
    def __init__(self):
        self.morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
            '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
        }

    def text_to_morse(self, plain_text):
        morse_code = ' '.join(self.morse_code_dict.get(char.upper(), '') for char in plain_text)
        return morse_code

    def morse_to_text(self, morse_code):
        morse_code_dict_reverse = {value: key for key, value in self.morse_code_dict.items()}
        decoded_text = ''.join(morse_code_dict_reverse.get(code, '') for code in morse_code.split(' '))
        return decoded_text


user_input = input("Enter the text for translation to morse code: ")

morse_translator = MorseCodeTranslator()

translated_morse_code = morse_translator.text_to_morse(user_input)
print(f"\nEncoded Morse Code: {translated_morse_code}")


user_input = input("Enter morse code for translation to text: ")
translated_text = morse_translator.morse_to_text(user_input)
print(f"\nDecoded Text: {translated_text}")
