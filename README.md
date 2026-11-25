# 🐍 Python Basics — Solved Problems

My solutions to the practice tasks from a Python basics course (modules 15–27).
The collection goes from the very first programs written in an IDE all the way to
object-oriented programming, iterators and generators.

**114 tasks · 13 modules · 107 solved ✅ · 7 in progress ⏳**

> The task statements (in each `README.md`) are in Russian, as in the original course.
> Each task below has an English title alongside the original one.

## 📁 Project structure

Each module is a folder, and each task inside it is its own folder:

```
python-ds/
├── 16_Lists/                  ← module (number + topic)
│   ├── 01_list_gen/           ← task (number + short name)
│   │   ├── README.md          ← task statement
│   │   └── main.py            ← my solution
│   └── ...
└── ...
```

Some tasks also include input data files (`.txt`, `.zip`, `.log`) that the program reads.

## ▶️ How to run a solution

You only need **Python 3.6+** — no external libraries.

```bash
git clone https://github.com/erzhansu12/python-ds.git
cd python-ds/16_Lists/01_list_gen
python main.py
```

Run tasks that work with files **from inside their own folder**, so the program can find its data files.

## 📚 Modules & tasks

### Module 15 — Working in an IDE

Basic programs written in PyCharm: input/output, loops, arithmetic. → [`15_IDE/`](15_IDE/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [System info](15_IDE/01_os_info/) | Информация о системе | ✅ |
| 02 | [Session](15_IDE/02_session/) | Сессия | ✅ |
| 03 | [Sum and difference](15_IDE/03_sum_and_dif/) | Сумма и разность | ✅ |
| 04 | [Reverse number 3](15_IDE/04_reverse_num/) | Число наоборот 3 | ✅ |
| 05 | [Smallest divisor](15_IDE/05_least_divisor/) | Наименьший делитель | ✅ |
| 06 | [Coin 2](15_IDE/06_coin2/) | Монетка 2 | ✅ |
| 07 | [Years](15_IDE/07_years/) | Года | ✅ |

### Module 16 — Lists

Creating, indexing and iterating over lists. → [`16_Lists/`](16_Lists/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [List generation](16_Lists/01_list_gen/) | Генерация списка | ✅ |
| 02 | [Tournament](16_Lists/02_tournament/) | Турнир | ✅ |
| 03 | [Cells](16_Lists/03_cells/) | Клетки | ✅ |
| 04 | [Video cards](16_Lists/04_videocards/) | Видеокарты | ✅ |
| 05 | [Movies](16_Lists/05_movie/) | Кино | ✅ |
| 06 | [Word analysis](16_Lists/06_word_analysis/) | Анализ слова | ✅ |
| 07 | [Containers](16_Lists/07_containers/) | Контейнеры | ✅ |
| 08 | [Running digits](16_Lists/08_running_nums/) | Бегущие цифры | ✅ |
| 09 | [Word analysis 2](16_Lists/09_word_analysis_2/) | Анализ слова 2 | ✅ |
| 10 | [Sorting](16_Lists/10_sort/) | Сортировка | ⏳ |

### Module 17 — List methods

append, insert, remove, pop, count, index, sort and friends. → [`17_List_methods/`](17_List_methods/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Scary code](17_List_methods/01_scary_code/) | Страшный код | ✅ |
| 02 | [Line-up](17_List_methods/02_line/) | Шеренга | ✅ |
| 03 | [Parts](17_List_methods/03_details/) | Детали | ✅ |
| 04 | [Party](17_List_methods/04_party/) | Вечеринка | ✅ |
| 05 | [Songs](17_List_methods/05_songs/) | Песни | ✅ |
| 06 | [Unique elements](17_List_methods/06_unique_elems/) | Уникальные элементы | ✅ |
| 07 | [Roller skates](17_List_methods/07_roller_skates/) | Ролики | ✅ |
| 08 | [Counting rhyme](17_List_methods/08_rhyme_cnt/) | Считалка | ✅ |
| 09 | [Friends](17_List_methods/09_friends/) | Друзья | ✅ |
| 10 | [Symmetric sequence](17_List_methods/10_simmetrical_seq/) | Симметричная последовательность | ✅ |

### Module 18 — List comprehensions & slices

Building lists in one line, slicing, 2D lists. → [`18_List_comprehensions/`](18_List_comprehensions/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Vowels](18_List_comprehensions/01_vowels/) | Гласные буквы | ✅ |
| 02 | [Generation](18_List_comprehensions/02_generation/) | Генерация | ✅ |
| 03 | [Random competition](18_List_comprehensions/03_random_competition/) | Случайные соревнования | ✅ |
| 04 | [Practicing slices](18_List_comprehensions/04_slices/) | Тренируемся со срезами | ✅ |
| 05 | [Reversal](18_List_comprehensions/05_reversal/) | Разворот | ✅ |
| 06 | [List compression](18_List_comprehensions/06_list_compression/) | Сжатие списка | ✅ |
| 07 | [2D list](18_List_comprehensions/07_two_dimensional_list/) | Двумерный список | ✅ |
| 08 | [Entertainment](18_List_comprehensions/08_entertainment/) | Развлечение | ✅ |
| 09 | [List of lists 2](18_List_comprehensions/09_list_of_lists_2/) | Список списков 2 | ✅ |
| 10 | [Caesar cipher](18_List_comprehensions/10_caesar_cipher/) | Шифр Цезаря | ✅ |

### Module 19 — Strings

String methods, formatting, splitting and joining. → [`19_Strings/`](19_Strings/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Restaurant menu](19_Strings/01_restaurant_menu/) | Меню ресторана | ✅ |
| 02 | [Longest word](19_Strings/02_longest_word/) | Самое длинное слово | ✅ |
| 03 | [Files](19_Strings/03_files/) | Файлы | ✅ |
| 04 | [Capital letters](19_Strings/04_capital_letters/) | Заглавные буквы | ✅ |
| 05 | [Password](19_Strings/05_password/) | Пароль | ✅ |
| 06 | [Compression](19_Strings/06_compression/) | Сжатие | ✅ |
| 07 | [IP address 2](19_Strings/07_ip_adress_2/) | IP - адрес 2 | ✅ |
| 08 | [Ticker](19_Strings/08_ticker/) | Бегущая строка | ✅ |
| 09 | [Message](19_Strings/09_message/) | Сообщение | ✅ |
| 10 | [The truth](19_Strings/10_the_truth/) | Истина | ✅ |

### Module 20 — Dictionaries & sets

Key-value storage, counting, set operations. → [`20_Dictionaries_and_sets/`](20_Dictionaries_and_sets/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Songs 2](20_Dictionaries_and_sets/01_songs_2/) | Песни 2 | ✅ |
| 02 | [Geography](20_Dictionaries_and_sets/02_geography/) | География | ✅ |
| 03 | [Cryptocurrency](20_Dictionaries_and_sets/03_cryptocurrency/) | Криптовалюта | ✅ |
| 04 | [Goods](20_Dictionaries_and_sets/04_goods/) | Товары | ✅ |
| 05 | [Frequency histogram 2](20_Dictionaries_and_sets/05_frequency_hist_2/) | Гистограмма частоты 2 | ✅ |
| 06 | [Synonym dictionary](20_Dictionaries_and_sets/06_synonym_dict/) | Словарь синонимов | ✅ |
| 07 | [Pizza](20_Dictionaries_and_sets/07_pizza/) | Пицца | ✅ |
| 08 | [Guess the number](20_Dictionaries_and_sets/08_guess_number/) | Угадай число | ✅ |
| 09 | [Pedigree](20_Dictionaries_and_sets/09_pedigree/) | Родословная | ✅ |
| 10 | [Palindrome again](20_Dictionaries_and_sets/10_palindrome_again/) | Снова палиндром | ⏳ |

### Module 21 — Tuples

Immutable sequences, unpacking, zip, sorting with keys. → [`21_Tuples/`](21_Tuples/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Code review](21_Tuples/01_code_review/) | Ревью кода | ✅ |
| 02 | [Universal program 2](21_Tuples/02_universal_prog_2/) | Универсальная программа 2 | ✅ |
| 03 | [Function](21_Tuples/03_function/) | Функция | ✅ |
| 04 | [Players](21_Tuples/04_players/) | Игроки | ✅ |
| 05 | [One family](21_Tuples/05_one_family/) | Одна семья | ✅ |
| 06 | [Pairs](21_Tuples/06_pairs/) | По парам | ✅ |
| 07 | [Sort function](21_Tuples/07_sort_function/) | Функция сортировки | ✅ |
| 08 | [Contacts 3](21_Tuples/08_contacts_3/) | Контакты 3 | ✅ |
| 09 | [Competition protocol](21_Tuples/09_competition_protocol/) | Протокол соревнований | ✅ |
| 10 | [Custom zip](21_Tuples/10_my_zip/) | Свой zip | ✅ |

### Module 22 — Functions

Recursion, *args/**kwargs, default arguments, deep copy. → [`22_Functions/`](22_Functions/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Challenge 2](22_Functions/01_challenge_2/) | Challenge 2 | ✅ |
| 02 | [Custom zip 2](22_Functions/02_my_zip_2/) | Свой zip 2 | ✅ |
| 03 | [Fibonacci sequence](22_Functions/03_fibonacci/) | Ряд Фибоначчи | ✅ |
| 04 | [Element search 2](22_Functions/04_search_element_2/) | Поиск элемента 2 | ✅ |
| 05 | [Speeding up a function](22_Functions/05_make_function_faster/) | Ускоряем работу функции | ✅ |
| 06 | [Deep copy](22_Functions/06_deep_copy/) | Глубокое копирование | ✅ |
| 07 | [Advanced sum function](22_Functions/07_advanced_sum/) | Продвинутая функция sum | ✅ |
| 08 | [List of lists 2](22_Functions/08_list_of_lists_2/) | Список списков 2 | ✅ |
| 09 | [Towers of Hanoi](22_Functions/09_hanoi_towers/) | Ханойские башни | ✅ |

### Module 23 — Files

Reading and writing text files, walking directories, zip archives. → [`23_Files/`](23_Files/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Sum of numbers 2](23_Files/01_nums_sum_2/) | Сумма чисел 2 | ✅ |
| 02 | [Zen of Python](23_Files/02_zen_of_python/) | Дзен Пайтона | ✅ |
| 03 | [Zen of Python 2](23_Files/03_zen_of_python_2/) | Дзен Пайтона 2 | ✅ |
| 04 | [Files and folders](23_Files/04_files_and_folders/) | Файлы и папки | ✅ |
| 05 | [Saving](23_Files/05_save/) | Сохранение | ✅ |
| 06 | [Paranoia](23_Files/06_paranoia/) | Паранойя | ✅ |
| 07 | [Tournament](23_Files/07_tournament/) | Турнир | ✅ |
| 08 | [Frequency analysis](23_Files/08_frequency_analysis/) | Частотный анализ | ✅ |
| 09 | [War and Peace](23_Files/09_war_and_peace/) | Война и мир | ✅ |

### Module 24 — Exceptions

try/except/finally, raising and handling custom errors. → [`24_Exceptions/`](24_Exceptions/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Names 2](24_Exceptions/01_names_2/) | Имена 2 | ✅ |
| 02 | [Coordinates](24_Exceptions/02_coordinates/) | Координаты | ✅ |
| 03 | [Lucky number](24_Exceptions/03_lucky_number/) | Счастливое число | ✅ |
| 04 | [Registration](24_Exceptions/04_registration/) | Регистрация | ✅ |
| 05 | [Text calculator](24_Exceptions/05_text_calc/) | Текстовый калькулятор | ✅ |
| 06 | [Chat](24_Exceptions/06_chat/) | Чат | ✅ |
| 07 | [Text calculator 2](24_Exceptions/07_text_calc_2/) | Текстовый калькулятор 2 | ⏳ |

### Module 25 — Object-oriented programming

Classes, objects, methods; small games and simulations. → [`25_OOP/`](25_OOP/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Fight](25_OOP/01_fight/) | Драка | ✅ |
| 02 | [Students](25_OOP/02_students/) | Студенты | ✅ |
| 03 | [Circle](25_OOP/03_circle/) | Окружность | ✅ |
| 04 | [Fathers, mothers and kids](25_OOP/04_fathers_mothers_kids/) | Отцы, матери и дети | ✅ |
| 05 | [Happy farm 2](25_OOP/05_happy_farm_2/) | Веселая ферма 2 | ✅ |
| 06 | [Magic](25_OOP/06_magic/) | Магия | ✅ |
| 07 | [Cohabitation](25_OOP/07_cohabitation/) | Совместное проживание | ✅ |
| 08 | [Blackjack](25_OOP/08_blackjack/) | Блэкджек | ✅ |
| 09 | [Tic-tac-toe](25_OOP/09_tic-tac-toe/) | Крестики-нолики | ⏳ |

### Module 26 — OOP principles

Encapsulation, inheritance, polymorphism, magic methods. → [`26_OOP_principles/`](26_OOP_principles/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Taxes](26_OOP_principles/01_taxes/) | Налоги | ✅ |
| 02 | [Karma](26_OOP_principles/02_karma/) | Карма | ✅ |
| 03 | [Custom dict](26_OOP_principles/03_my_dict/) | Свой словарь | ✅ |
| 04 | [Company](26_OOP_principles/04_company/) | Компания | ✅ |
| 05 | [Car!](26_OOP_principles/05_auto/) | А-а-автомобиль! | ✅ |
| 06 | [Cohabitation 2](26_OOP_principles/06_cohabitation_2/) | Совместное проживание 2 | ⏳ |
| 07 | [Stack](26_OOP_principles/07_stack/) | Стек | ✅ |

### Module 27 — Iterators & generators

Custom iterators, yield, lazy sequences, linked list. → [`27_Iterators_and_generators/`](27_Iterators_and_generators/)

| # | Task | Задача | Status |
|---|---|---|---|
| 01 | [Squares of numbers](27_Iterators_and_generators/01_num_squares/) | Квадраты чисел | ✅ |
| 02 | [Refactoring](27_Iterators_and_generators/02_refactoring/) | Рефакторинг | ✅ |
| 03 | [File paths](27_Iterators_and_generators/03_files_path/) | Пути файлов | ✅ |
| 04 | [Hofstadter sequence](27_Iterators_and_generators/04_hof_seq/) | Последовательность Хофштадтера | ✅ |
| 05 | [Line count](27_Iterators_and_generators/05_str_count/) | Количество строк | ⏳ |
| 06 | [Singly linked list](27_Iterators_and_generators/06_linked_list/) | Односвязный список | ⏳ |
## 🛠 Topics covered

`lists` · `list comprehensions` · `slices` · `strings` · `dicts` · `sets` · `tuples` · `zip` ·
`functions` · `recursion` · `file I/O` · `os` · `exceptions` · `classes` · `inheritance` ·
`magic methods` · `iterators` · `generators`
