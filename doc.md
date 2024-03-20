# Text to Morse Code Converter

**Text to Morse Code Converter** - это простое приложение, которое предоставляет возможность преобразования текста в морзянку и обратно. Программа написана на Python с использованием библиотеки Tkinter для создания графического интерфейса.

## Функциональность

- **Преобразование текста в морзянку:** Введите текст в соответствующее поле ввода, выберите язык и нажмите кнопку "Convert Text to Morse". Результат будет отображен в окне вывода.
  
- **Преобразование морзянки в текст:** Введите последовательность символов морзянки в поле ввода "Enter Morse Code", выберите язык и нажмите кнопку "Convert Morse to Text". Результат будет отображен в окне вывода.

- **Выбор языка:** Программа поддерживает два языка: английский и русский. Вы можете выбрать язык, с которым будет работать преобразование.

- **Копирование результатов:** Результаты преобразования можно скопировать в буфер обмена, нажав на кнопку "Copy".

## Использование

1. Введите текст в соответствующее поле ввода.
2. Выберите язык (по умолчанию - английский).
3. Нажмите кнопку "Convert Text to Morse", чтобы преобразовать текст в морзянку.
4. Результат преобразования отобразится в окне вывода.
5. Для преобразования морзянки в текст введите последовательность символов морзянки в поле ввода "Enter Morse Code".
6. Повторите шаги 2-4, нажав кнопку "Convert Morse to Text".

## Технические детали

- **Язык программирования:** Python
- **Используемые библиотеки:** tkinter, tkinter.scrolledtext, pyperclip
- **Алгоритм преобразования:** Программа использует словари для представления символов алфавита и цифр в морзянке для английского и русского языков. Алгоритм проходит по введенному тексту или морзянке, заменяя символы соответствующими значениями из словарей.

Этот проект создан для удобного преобразования текста в морзянку и обратно, а также для изучения возможностей графического интерфейса Tkinter.