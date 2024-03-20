# Импорт библиотек Tkinter для создания графического интерфейса
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext

# Словари для преобразования символов в морзянку
abc_eng = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
        ':': '---...', ';': '-.-.-.', '-': '-....-', '/': '-..-.', 
        '_': '..--.-', '(': '-.--.', ')': '-.--.-', '"': '.-..-.', 
        '\'': '.----.', '+': '.-.-.', '=': '-...-', '@': '.--.-.'}

abc_rus = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
        'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 
        'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 
        'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 
        'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 
        'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 
        'Ю': '..--', 'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', 
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', 
        ':': '---...', ';': '-.-.-.', '-': '-....-', '/': '-..-.', 
        '_': '..--.-', '(': '-.--.', ')': '-.--.-', '"': '.-..-.', 
        '\'': '.----.', '+': '.-.-.', '=': '-...-', '@': '.--.-.'}

# Функция для преобразования текста в морзянку
def text_to_morse(text, abc):
    morse_code = ''
    for char in text.upper():
        if char in abc:
            morse_code += abc[char] + ' '
        elif char == ' ':
            morse_code += ' '
    return morse_code.strip()

# Функция для преобразования морзянки в текст
def morse_to_text(morse_code, abc):
    text = ''
    morse_code += ' '  # Пробел в конце, чтобы правильно разделить коды
    char = ''
    for symbol in morse_code:
        if symbol != ' ':
            char += symbol
        else:
            if char in abc.values():
                text += [key for key, value in abc.items() if value == char][0]
            elif char == '':
                text += ' '
            char = ''
    return text

# Функция для преобразования текста в морзянку
def convert_text():
    input_text = text_entry.get()
    language = language_var.get()
    # Выбор алфавита в соответствии с выбранным языком
    if language == "English":
        morse = text_to_morse(input_text, abc_eng)
    else:
        morse = text_to_morse(input_text, abc_rus)
    # Очистка окна вывода и добавление результата
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, morse)

# Функция для преобразования морзянки в текст
def convert_morse():
    input_morse = morse_entry.get()
    language = language_var.get()
    # Выбор алфавита в соответствии с выбранным языком
    if language == "English":
        text = morse_to_text(input_morse, abc_eng)
    else:
        text = morse_to_text(input_morse, abc_rus)
    # Очистка окна вывода и добавление результата
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, text)

# Создание графического интерфейса
root = tk.Tk()
root.title("Text to Morse Code Converter")

# Настройка сетки для элементов интерфейса
for i in range(5):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

# Метки и поля ввода
text_label = ttk.Label(root, text="Enter text:")
text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
text_entry = ttk.Entry(root, width=40)
text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

morse_label = ttk.Label(root, text="Enter Morse Code:")
morse_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
morse_entry = ttk.Entry(root, width=40)
morse_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Выбор языка и кнопки для конвертации текста и морзянки
language_var = tk.StringVar()
language_var.set("English")
language_label = ttk.Label(root, text="Select language:")
language_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
language_option = ttk.OptionMenu(root, language_var, "English", "English", "Russian")
language_option.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

text_to_morse_button = ttk.Button(root, text="Convert Text to Morse", command=convert_text)
text_to_morse_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

morse_to_text_button = ttk.Button(root, text="Convert Morse to Text", command=convert_morse)
morse_to_text_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Многострочное поле вывода результата
output_text = scrolledtext.ScrolledText(root, height=6, width=40)
output_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Запуск главного цикла Tkinter для отображения интерфейса
root.mainloop()

