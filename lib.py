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


# -> Параметры постоянных виджетов
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
    messagebox.showwarning('Внимание!', 'Введено менее 10 оценок.')


# -> Выводит результат работы функции и делает проверку
def decorator_output_result(func):
    def wrapper():
        frame_result = Frame()
        frame_result.config(width=280, height=200, bg='PaleGreen')
        frame_result.place(x=235, y=180)

        line_comment = Label(root)
        line_comment.place(x=0, y=440)
        line_comment.config(width=40, bg='LightGreen', font=('Comic Sans Ms', 17),
                            fg='SeaGreen', justify=CENTER)

        if func.__name__ == 'output_of_marks':
            line_comment.config(text='Вывод  оценок')
        elif func.__name__ == 'descending_sort':
            line_comment.config(text='Сортировка  оценок  (по убыванию)')
        elif func.__name__ == 'is_a_scholarship_awarded':
            line_comment.config(text='Выходит  ли  стипендия')

        try:
            func()
        except ValueError:
            messagebox_error()
            error_label = Label(frame_result)
            error_label.config(text='Повнимательнее!))\n\nВведите оценки заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=45, y=52)
            return
        except TypeError:
            messagebox_warning()
            error_label = Label(frame_result)
            error_label.config(text='Неверно введены оценки!\n\nВведите оценки заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=30, y=52)
            return

        else:
            title_output_label = Label(frame_result)
            title_output_label.config(width=28, font=('Comic Sans Ms', 13), bg='PaleGreen', fg='MediumSeaGreen',
                                      justify=CENTER)
            title_output_label.place(x=0, y=55)

            if func() is None:
                messagebox_warning()
                title_output_label.config(text='Неверно введены оценки!\n\nВведите оценки заново.')

            elif func() is Warning:
                messagebox_warning_less_than_10()
                title_output_label.config(text='Неверное количество оценок!\n\nВведите оценки заново.')

            elif func() is True:
                title_output_label.config(text='Поздравляем!))\nСтипендия Ваша!')

            elif func() is False:
                title_output_label.config(text='Увы...\nПока без стипендии.')

            else:
                title_output_label.config(text='Ваши оценки:')
                result_output_label = Label(frame_result)
                result_output_label.config(text=func(), width=30, font='Arial 13', bg='PaleGreen', fg='SeaGreen')
                result_output_label.place(x=2, y=90)

    return wrapper


def decorator_retake_an_exam(func):
    def wrapper():
        frame_result = Frame()
        frame_result.config(width=280, height=200, bg='PaleGreen')
        frame_result.place(x=235, y=180)

        line_comment = Label(root)
        line_comment.place(x=0, y=440)
        line_comment.config(width=40, bg='LightGreen', font=('Comic Sans Ms', 17),
                            fg='SeaGreen', justify=CENTER)
        try:
            result = func()
        except ValueError:
            messagebox_error()
            error_label = Label(frame_result)
            error_label.config(text='Повнимательнее!))\nВведите оценки заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=45, y=130)
            return
        except TypeError:
            messagebox_warning()
            error_label = Label(frame_result)
            error_label.config(text='Неверно введены оценки!\nВведите оценки заново.', font=('Comic Sans Ms', 13),
                               bg='PaleGreen', fg='MediumSeaGreen')
            error_label.place(x=30, y=135)
            return
        else:
            title_output_label = Label(frame_result)
            title_output_label.config(width=28, font=('Comic Sans Ms', 13), bg='PaleGreen', fg='MediumSeaGreen',
                                      justify=CENTER)
            title_output_label.place(x=0, y=135)

            if result is None:
                messagebox_warning()
                title_output_label.config(text='Неверно введены оценки!\nВведите оценки заново.')
            elif result is Warning:
                messagebox_warning_less_than_10()
                title_output_label.config(text='Неверное количество оценок!\nВведите оценки заново.')
                title_output_label.place(x=0, y=75)
            else:
                title_output_label.config(text='Ваши оценки:')
                result_output_label = Label(frame_result)
                result_output_label.config(text=result, width=30, font='Arial 13', bg='PaleGreen', fg='SeaGreen')
                result_output_label.place(x=2, y=90)

    return wrapper


# -> Получает данные из entry и переводит в int при (0 < данные < 13)
def list_marks():
    global marks
    marks = entry_marks.get().split()
    int_marks = []
    for el in marks:
        if 0 < int(el) < 13:
            int_marks.append(int(el))
        else:
            return None
    if len(int_marks) != 10:
        return Warning
    return int_marks


@decorator_output_result
def output_of_marks():  # -> Выводит оценки
    return list_marks()


@decorator_retake_an_exam
def retake_an_exam():
    global marks
    marks = list_marks()
    if marks == Warning:
        return Warning
    entry_number_of_new_mark = Entry(root)
    entry_number_of_new_mark.config(font='Arial 13', relief=RIDGE, bd=3, width=5, justify=CENTER, fg='SeaGreen')
    entry_number_of_new_mark.place(x=455, y=190)

    entry_new_mark = Entry(root)
    entry_new_mark.config(font='Arial 13', relief=RIDGE, bd=3, width=5, justify=CENTER, fg='SeaGreen')
    entry_new_mark.place(x=455, y=230)

    button_replace = Button(root)
    button_replace.config(bg='MediumSeaGreen', text='Заменить', width=20, font='Arial 8', fg='white')
    button_replace.place(x=380, y=270)

    def mark_replacement():
        num_of_new_mark = int(entry_number_of_new_mark.get().split())
        new_mark = int(entry_new_mark.get().split())
        for num, mark in enumerate(marks):
            if num == num_of_new_mark:
                marks.pop(num)
                marks.insert(num, new_mark)
            else:
                return None
        return marks

    return mark_replacement()


@decorator_output_result
def is_a_scholarship_awarded():
    global marks
    marks = list_marks()
    if marks == Warning:
        return Warning
    average_mark = round(sum(marks) / len(marks), 1)
    if average_mark >= 10.7:
        return True
    else:
        return False


@decorator_output_result
def descending_sort():  # -> Сортирует оценки по убыванию
    global marks
    marks = list_marks()
    if marks == Warning:
        return Warning
    for mark in range(len(marks)):
        changes = False
        for el in range(len(marks) - 1 - mark):
            print(el, end=', ')
            if marks[el] < marks[el + 1]:
                marks[el], marks[el + 1] = marks[el + 1], marks[el]
                changes = True
            elif marks[el] >= marks[el + 1]:
                continue
        print('<-')
        print(marks)
        if not changes:
            break
    return marks
