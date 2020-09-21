from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator

"""
    Написать программу «успеваемость». Пользователь вводит 10 оценоĸ студента.
    Оценĸи от 1 до 12. Реализовать меню для пользователя:

    -Вывод оценоĸ (вывод содержимого списĸа);
    -Пересдача эĸзамена (пользователь вводит номер элемента списĸа и новую оценĸу);
    -Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7);
    -Вывод отсортированного списĸа оценоĸ !по убыванию!. (переделать
     любой из алгоритмов с ĸлассной работы и использовать его)
"""

root = Tk()  # -> создание окна

# -> Постоянные виджеты окна
top_label = Label(root, height=2)  # -> Label "Успеваемость" вверху окна
title_entry = Label(root)  # -> текстовый Label 'Введите 10 оценок:'
entry_marks = Entry(root)  # -> поле для ввода оценок

button_output_marks = Button(root)  # -> кнопка "Вывод оценоĸ"
button_retake_an_exam = Button(root)  # -> кнопка "Пересдача эĸзамена"
button_scholarship = Button(root)  # -> кнопка "Выходит ли стипендия"
button_descending_sort = Button(root)  # -> кнопка "Сортировка оценок (по убыванию)"

Separator(root, orient='horizontal').place(x=0, y=55, relwidth=20)  # -> верхний разделитель
Separator(root, orient='horizontal').place(x=0, y=415, relwidth=20)  # -> нижний разделитель

# -> глобальная переменная
marks = []  # -> список оценок


# -> Параметры окна root и его постоянных виджетов
def root_and_widget_config():
    root.geometry('550x500+200+100')
    root.title('Успеваемость')
    root.config(bg='LightGreen')

    top_label.config(bg='MediumSeaGreen', text='Успеваемость', font=('Comic Sans Ms', 13), fg='white', width=55)
    top_label.place(x=0, y=0)

    title_entry.config(bg='LightGreen', font='Arial 13', text='Введите 10 оценок:', fg='SeaGreen')
    title_entry.place(x=40, y=110)

    entry_marks.config(font='Arial 13', relief=RIDGE, bd=3, width=30, justify=CENTER, fg='SeaGreen')
    entry_marks.place(x=235, y=110)

    button_output_marks.config(bg='MediumSeaGreen', text='Вывод оценоĸ', width=20, font='Arial 10', pady=4, fg='white',
                               command=output_of_marks)
    button_output_marks.place(x=30, y=180)

    button_retake_an_exam.config(bg='MediumSeaGreen', text='Пересдача эĸзамена', width=20, font='Arial 10', pady=4,
                                 fg='white', command=retake_an_exam)
    button_retake_an_exam.place(x=30, y=230)

    button_scholarship.config(bg='MediumSeaGreen', text='Выходит ли стипендия', width=20, font='Arial 10', pady=4,
                              fg='white', command=is_a_scholarship_awarded)
    button_scholarship.place(x=30, y=280)

    button_descending_sort.config(bg='MediumSeaGreen', text='Сортировка оценок (по убыванию)', width=20, pady=4,
                                  font='Arial 10', wraplength=120, fg='white', command=descending_sort)
    button_descending_sort.place(x=30, y=330)


def messagebox_error():
    messagebox.showerror('Ошибка', 'Вводите только целые числа от 1 до 12!')


def messagebox_warning():
    messagebox.showwarning('Ошибка', 'Введены неверные оценки!\nВводите оценки от 1 до 12.')


def messagebox_warning_less_than_10():
    messagebox.showwarning('Внимание!', 'Введено менее или более 10 оценок.')


def messagebox_error_number():
    messagebox.showerror('Ошибка!', 'Несуществующий номер оценки.\nВводите номер от1 до 10.')


# -> Выводит результат работы функции и делает проверку
def decorator_output_result(func):
    def wrapper():
        frame_result = Frame()  # -> фрейм вывода результата
        frame_result.config(width=280, height=200, bg='PaleGreen')
        frame_result.place(x=235, y=180)

        line_comment = Label(root)  # -> подсказка результат нажатия какой кнопки выведен на данный момент
        line_comment.place(x=0, y=440)
        line_comment.config(width=40, bg='LightGreen', font=('Comic Sans Ms', 17), fg='SeaGreen', justify=CENTER)

        # -> отображение текста подсказки в зависимости от имени функции, которая вызывалась
        if func.__name__ == 'output_of_marks':
            line_comment.config(text='Вывод  оценок')
        elif func.__name__ == 'descending_sort':
            line_comment.config(text='Сортировка  оценок  (по убыванию)')
        elif func.__name__ == 'is_a_scholarship_awarded':
            line_comment.config(text='Выходит  ли  стипендия')

        try:
            result = func()  # -> вызов функции и присваивание переменной

        except ValueError:
            messagebox_error()  # -> сообщение об ошибке
            error_label = Label(frame_result)  # -> отображает текст об ошибке
            error_label.config(text='Повнимательнее!))\n\nНачните заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=45, y=52)
            return

        except TypeError:
            messagebox_warning()  # -> сообщение об ошибке
            error_label = Label(frame_result)  # -> отображает текст об ошибке
            error_label.config(text='Неверно введены оценки!\n\nНачните заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=30, y=52)
            return

        else:
            # -> отображает текст в зависимости от результата работы функции
            title_output_label = Label(frame_result)
            title_output_label.config(width=28, font=('Comic Sans Ms', 13), bg='PaleGreen', fg='MediumSeaGreen',
                                      justify=CENTER)
            title_output_label.place(x=0, y=55)

            if result is None:
                messagebox_warning()  # -> сообщение об ошибке
                title_output_label.config(text='Неверно введены оценки!\n\nНачните заново.')

            elif result is Warning:
                messagebox_warning_less_than_10()  # -> сообщение об ошибке
                title_output_label.config(text='Неверное количество оценок!\n\nНачните заново.')

            elif result is True:
                title_output_label.config(text='Поздравляем!))\nСтипендия Ваша!')

            elif result is False:
                title_output_label.config(text='Увы...\nПока без стипендии.')

            else:
                title_output_label.config(text='Ваши оценки:')

                # -> отображает результат работы функции
                result_output_label = Label(frame_result)
                result_output_label.config(text=result, width=30, font='Arial 13', bg='PaleGreen', fg='SeaGreen')
                result_output_label.place(x=2, y=90)

    return wrapper


# -> Выводит результат работы функции retake_an_exam и делает проверку
def decorator_retake_an_exam(func):
    def wrapper():
        frame_result = Frame()  # -> фрейм вывода результата
        frame_result.config(width=280, height=200, bg='PaleGreen')
        frame_result.place(x=235, y=180)
        try:
            result = func()  # -> вызов функции и присваивание переменной
        except ValueError:
            messagebox_error()  # -> сообщение об ошибке
            error_label = Label(frame_result)  # -> отображает текст об ошибке
            error_label.config(text='Повнимательнее!))\nНачните заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=45, y=55)
            return
        except TypeError:
            messagebox_warning()  # -> сообщение об ошибке
            error_label = Label(frame_result)  # -> отображает текст об ошибке
            error_label.config(text='Неверно введены оценки!\nНачните заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=30, y=55)
            return
        else:
            # -> отображает текст в зависимости от результата работы функции
            title_output_label = Label(frame_result)
            title_output_label.config(width=28, font=('Comic Sans Ms', 13), bg='PaleGreen', fg='MediumSeaGreen',
                                      justify=CENTER)
            title_output_label.place(x=0, y=45)

            if result is None:
                messagebox_warning()  # -> сообщение об ошибке
                title_output_label.config(text='Неверно введены оценки!\nНачните заново.')

            elif result is False:
                messagebox_error_number()  # -> сообщение об ошибке
                title_output_label.config(text='Неверный номер оценки!\nВведите заново.')
                title_output_label.place(x=0, y=75)

            elif result is Warning:
                messagebox_warning_less_than_10()  # -> сообщение об ошибке
                title_output_label.config(text='Неверное количество оценок!\nВведите оценки заново.')
                title_output_label.place(x=0, y=75)
            else:
                title_output_label.config(text='Ваш новый список оценок:')

                # -> отображает результат работы функции
                result_output_label = Label(frame_result)
                result_output_label.config(text=result, width=30, font='Arial 13', bg='PaleGreen', fg='SeaGreen')
                result_output_label.place(x=2, y=90)

    return wrapper


# -> Получает данные из entry и переводит в int при (0 < данные < 13)
def list_marks():
    global marks

    # -> проверяет формировался ли уже список оценок
    if not marks:                          # -> если нет, то
        marks = entry_marks.get().split()  # -> получает список из entry
    else:                                  # -> если да, то
        marks = marks                      # -> оставляет его

    int_marks = []                         # -> список для элементов типа int
    for el in marks:                       # -> формирует список оценок, переводя их в int
        if 0 < int(el) < 13:               # -> при условии 0 < оценка < 13
            int_marks.append(int(el))
        else:
            return None

    if len(int_marks) != 10:               # -> проверка условия ввода 10 оценок
        return Warning

    return int_marks


@decorator_output_result  # -> применение декоратора к функции
def output_of_marks():  # -> формирует список оценок из entry
    return list_marks()


# -> создаёт поле для ввода новой оценки и заменяет выбранную из списка на новую
def retake_an_exam():
    frame_decor = Frame()  # -> фрейм для поддержания красоты ))
    frame_decor.config(width=280, height=200, bg='PaleGreen')
    frame_decor.place(x=235, y=180)

    label_number_of_new_mark = Label(root)  # -> текст 'Введите номер новой оценки:'
    label_number_of_new_mark.config(font='Arial 11', bg='PaleGreen', text='Введите номер новой оценки:', fg='SeaGreen')
    label_number_of_new_mark.place(x=240, y=185)

    label_new_mark = Label(root)  # -> текст 'Введите новую оценку:'
    label_new_mark.config(font='Arial 11', bg='PaleGreen', text='Введите новую оценку:', fg='SeaGreen')
    label_new_mark.place(x=240, y=225)

    entry_number_of_new_mark = Entry(root)  # -> поле для ввода номера новой оценки
    entry_number_of_new_mark.config(font='Arial 13', relief=RIDGE, bd=3, width=5, justify=CENTER, fg='SeaGreen')
    entry_number_of_new_mark.place(x=455, y=180)

    entry_new_mark = Entry(root)  # -> поле для ввода новой оценки
    entry_new_mark.config(font='Arial 13', relief=RIDGE, bd=3, width=5, justify=CENTER, fg='SeaGreen')
    entry_new_mark.place(x=455, y=220)

    button_replace = Button(root)  # -> кнопка 'Заменить'
    button_replace.config(bg='MediumSeaGreen', text='Заменить', width=20, font='Arial 8', fg='white')
    button_replace.place(x=380, y=270)

    line_comment = Label(root)  # -> подсказка результат нажатия какой кнопки выведен на данный момент
    line_comment.place(x=0, y=440)
    line_comment.config(width=40, bg='LightGreen', font=('Comic Sans Ms', 17), fg='SeaGreen', justify=CENTER,
                        text='Пересдача эĸзамена')

    @decorator_retake_an_exam  # -> применение декоратора к функции
    def mark_replacement():    # -> получает значения из entry и производит замену оценки
        global marks
        marks = list_marks()

        if marks == Warning:  # -> предупреждение на случай ошибки в списке оценок
            return Warning

        num_of_new_mark = int(entry_number_of_new_mark.get())  # -> получает номер оценки из entry
        if num_of_new_mark > 10 or num_of_new_mark < 1:        # -> проверка вхождения номера оценки в нужный диапазон
            return False

        new_mark = int(entry_new_mark.get())                   # -> получает значение новой оценки из entry
        if new_mark > 12 or new_mark < 1:                      # -> проверка вхождения оценки в нужный диапазон
            return None

        marks.pop(num_of_new_mark - 1)                         # -> удаление старой оценки
        marks.insert(num_of_new_mark - 1, new_mark)            # -> добавление новой

        return marks

    button_replace.config(command=mark_replacement)    # -> привязка функции к кнопке


@decorator_output_result  # -> применение декоратора к функции
def is_a_scholarship_awarded():    # -> проверяет получается ли стипендия
    global marks
    marks = list_marks()

    if marks == Warning:  # -> предупреждение на случай ошибки в списке оценок
        return Warning

    average_mark = round(sum(marks) / len(marks), 1)  # -> вычисление среднего балла
    if average_mark >= 10.7:                          # -> сравнение с проходным баллом для стипендии
        return True
    else:
        return False


@decorator_output_result  # -> применение декоратора к функции
def descending_sort():  # -> создаёт новый равноценный список, сортирует его по убыванию (исходный список не меняется)
    global marks
    marks = list_marks()

    if marks == Warning:  # -> предупреждение на случай ошибки в списке оценок
        return Warning

    marks_copy = [i for i in marks]    # -> формирует список аналогичный списку оценок, чтоб не изменять изначальный

    # -> сортировка списка по убыванию
    for mark in range(len(marks_copy)):
        changes = False  # -> переменная хранит информацию об изменениях в списке
        for el in range(len(marks_copy) - 1 - mark):
            if marks_copy[el] < marks_copy[el + 1]:
                marks_copy[el], marks_copy[el + 1] = marks_copy[el + 1], marks_copy[el]  # -> меняются местами
                changes = True  # -> если были изменения
            elif marks_copy[el] >= marks_copy[el + 1]:
                continue
        if not changes:
            break

    return marks_copy
