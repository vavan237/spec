
import PySimpleGUI as sg
from dbcomands import Sqligther
from  functions import *
from PDFing import *
from invoice import *
import sys
import datetime


sq = Sqligther('spec.db')
lst1 = []
street_list = []
house_list = []
room_list = []

for i in sq.get_all_clients():
    lst1.append(i)

for i in sq.get_all_streets():
    street_list += i

for i in sq.get_all_houses():
    house_list += i

for i in sq.get_all_rooms():
    room_list += i

rows = [lst1[i] for i in range(len(lst1))]
header = ['Лицевой счет', 'ФИО', 'Улица', 'Дом','Квартира','Тариф', 'Оплачено','Сумма','Долг','Оплатить до']

rows4 = []
header4 = ['Лицевой счет', 'ФИО', 'Сумма',  'Файл']

rows5 = []
header5 = ['Дата', 'Адрес', 'Стучит', 'Не звонит', 'Не открывает','Кнопка вызова', 'Мастер', 'Выполнен', 'Коментарий']

rows6 = []
header6 = ['Дата формирования', 'дом']

rows6_2 = []
header6_2 = ['Дата' , 'Период', 'Тариф', 'Сумма', 'Адрес', 'ФЛС', 'ФИО']

rows9 = []
header9 = ['Мастер', 'Имя', 'E-mail']

layout_tab8_l = [[sg.T('ФИО'), sg.I(key=('-FIO-'))],
        [sg.T('Тариф'),sg.I(size=(10, 1), key=('-PRICE-'))],
        [sg.T('Лицевой счет'), sg.I(size=(15, 1), key=('-LS-'))],
        [sg.Text('Баланс, руб', auto_size_text=(True)), sg.I(key=('-BALANCE-'))],
        [sg.B('Провести платеж'), sg.B('Посмотреть последнюю квитанцию'), ],
        [sg.T("Реестр платежей")],
        [sg.LB(values=(1, 2, 3), size=(30, 20))]
            ]
layout_tab8_r = [[sg.T('Отправить наряд на ремонт')],
        [sg.R('Мастер 1', 1, expand_x= True, expand_y=True), sg.R('Мастер 2', 1, expand_x= True, expand_y=True), sg.R('Мастер 3', 1, expand_x= True, expand_y=True)],
        [sg.CBox('Стучит'), sg.CBox('Не звонит'), sg.CBox('Не открывает'), sg.CBox('Кнопка вызова')],
        [sg.T('Комментарий')],
        [sg.Output(size=([30, 20]))],
        [sg.B('Отправить'), sg.B('Отмена')]
            ]
layout_tab4_l = [[sg.Table(headings=header4, values=rows4, justification = 'left', size=(70, 70), key=('-WRONG_LS-'), expand_x = True,  )]
                 ]
layout_tab4_r = [[sg.T('Реестр платежа')],
                 [sg.I(key=('-FPATH-')), sg.FileBrowse()],
                 [sg.OK(), sg.Cancel()],
                 [sg.Output(size=(60, 30), key=('-REESTR-'))]
                 ]
houselst = []
roomlst = []
tab1 =  [

    [sg.T('Улица                                                                                              Дом                          Подъезд                     Квартира')],
    [sg.LB([street_list[i] for i in range(len(street_list))],  key=('-STREET-'), size=(55, 20), enable_events=True),
     sg.LB(house_list, key=('-HOUSE-'), size=(15, 20), enable_events=True),
     sg.LB([],  size=(15, 20)),
     sg.LB(values = (roomlst), key=('-ROOM-'),  size=(15, 20))],
    [sg.B('Найти')],
    [sg.T('ФИО'), sg.I(key=('-N_FIO-'))],
    [sg.T('Улица/микрорайон'), sg.I(key=('-N_STREET-'))],
    [sg.T('Дом №'), sg.I(key = ('-N_HOUSE-'))],
    [sg.T('Квартира'), sg.I(size=(20, 1), key=('-N_ROOM-')), sg.T('Тариф'), sg.I(size=(20, 1), key=('-N_PRICE-'))],
    [sg.B('Добавить нового абонента'), sg.B('Добавить из файла "txt"')],

         ]

tab2 =  [ [sg.Table(headings = header, values=rows, justification = 'left', auto_size_columns= True, expand_x = True,  expand_y=True)],
          [sg.B("Выгрузить в файл 'txt'")]


         ]

tab3 = [[sg.B('Сформировать Должников'), sg.I('Введите сумму долга', key=('-SUMM-')), sg.B("Экспорт в 'txt'", expand_x = True)],
        [sg.Table(headings=header, values = rows, key = ('-OUT-DEB-'), justification = 'left', expand_x=True, expand_y=True)]
        ]
tab4 = [[sg.Col(layout_tab4_l, expand_x=True), sg.Col(layout_tab4_r)]

        ]
tab5 = [[sg.Table(headings=header5, values = rows5, justification = 'left',expand_x=True, expand_y=True, key=('-ORDERS-'))],
        [sg.B("Обновить список нарядов", size=(30, 2), key=('-REFRESH-'))]

        ]

tab6 = [[sg.B('Начислить тариф'), sg.B('Сформировать Сбербанк', size=(40, 2), pad=(250, 0), expand_x = True) ],
        [sg.B('Сформировать квитанции')],
        [sg.B('Сформировать квитанции для дома')],
        [sg.LB(values=(street_list), enable_events=True, key=('-STRLST-'),size= (10, 1)), sg.T('Дом'), sg.LB(values=(houselst), key=('-HOUSELST-'), size= (10, 1))],
        [sg.Table(headings=header6, values=rows6, key = ('-INVVAL-'),justification = 'left', auto_size_columns=False, size=(30, 50)), sg.Table(headings=header6_2, values=rows6_2, size=(5, 30), expand_x = True)]

        ]
tab7 = [[sg.B('Проверить почту'), sg.B('Настройки почты')],
        [sg.B('Добавить реестр платежей'), sg.B('Засчитать платежи', pad=(250, 0), size=(20, 2))],
        [sg.LB(values=(1, 2, 3), size=(30, 40)), sg.Output(size=(100,40))]
        ]
tab8 = [[sg.Col(layout_tab8_l), sg.Col(layout_tab8_r)]

        ]
tab9 = [[sg.B('Редактировать', expand_x=True, size=(100, 3) )],
        [sg.Table(headings=header9, values=rows9, expand_x=True, expand_y=True)]

        ]
layout = [ [sg.TabGroup([
            [sg.Tab('Главная', tab1, expand_x = True,  expand_y=True),
             sg.Tab('Лицевые счета', tab2, expand_x = True,  expand_y=True),
             sg.Tab('Долги', tab3,  expand_x = True,  expand_y=True),
             sg.Tab('Ошибки', tab4, expand_x = True,  expand_y=True),
             sg.Tab('Наряды', tab5, expand_x = True,  expand_y=True),
             sg.Tab('Квитанции', tab6, expand_x = True,  expand_y=True),
             sg.Tab('Реестр платежей', tab7, expand_x = True,  expand_y=True),
             sg.Tab('Карточка квартиры', tab8, expand_x = True,  expand_y=True, key=('-TAB8-')),
             sg.Tab('Мастера', tab9, expand_x = True,  expand_y=True)

             ],
                       ], expand_x = True,  expand_y=True)

           ],
         ]
window = sg.Window('SPEC', layout, size = (1000, 600))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == '-STREET-':
        for i in values['-STREET-']:
            strlst = i
        try:
            houselst = sq.get_street_all_houses(strlst)
            window['-HOUSE-'].update(houselst)
        except:
            sg.popup("Error")

    if event == '-HOUSE-' and values['-STREET-'] :
        for i in values['-HOUSE-']:
            houselst = i
        try:
            roomlst = sq.get_house_all_rooms(strlst, houselst)
            window['-ROOM-'].update(roomlst)
        except:
            sg.popup("Error")



    if event == "Найти" and values['-STREET-'] and values['-HOUSE-'] and values['-ROOM-']:
        try:
            val = values['-STREET-'] + values['-HOUSE-'] + values['-ROOM-']

            window['-TAB8-'].select()
            if window['-TAB8-']:
                values['-FIO-'] = sq.get_name_pr_cli(val[0], val[1], val[2])[0][0]
                window['-FIO-'].update(values['-FIO-'])
                values['-PRICE-'] = sq.get_name_pr_cli(val[0], val[1], val[2])[0][1]
                window['-PRICE-'].update(values['-PRICE-'])
                values['-LS-'] = sq.get_name_pr_cli(val[0], val[1], val[2])[0][2]
                window['-LS-'].update(values['-LS-'])
                values['-BALANCE-'] = sq.get_name_pr_cli(val[0], val[1], val[2])[0][3]
                window['-BALANCE-'].update(values['-BALANCE-'])
                if int(values['-BALANCE-']) < 0:
                    sg.popup('Есть долг',  button_color = 'red', background_color='red', grab_anywhere=True)
        except:
            sg.popup('Несуществующий адрес')
    elif event == "Найти" and values not in (['-STREET-'], ['-HOUSE-'], ['-ROOM-']):
        sg.popup('Убедитесь что выбраны улица, дом и квартира')

    if event == 'Добавить нового абонента' and values['-N_FIO-'] and values['-N_STREET-'] and values['-N_HOUSE-'] and values['-N_ROOM-'] and values['-N_PRICE-']:
        sq.add_new_cli(values['-N_FIO-'], values['-N_STREET-'], values['-N_HOUSE-'], values['-N_ROOM-'], values['-N_PRICE-'])
        sg.popup('Добавлено')
    elif event == 'Добавить нового абонента' and values not in (['-N_FIO-'], ['-N_STREET-'], ['-N_HOUSE-'], ['-N_ROOM-'],['-N_PRICE-']):
        sg.popup('Проверьте все ли поля заполнены')

    if event == 'Добавить из файла "txt"':
        try:
            fpath = sg.popup_get_file('Выберите текстовый документ')
            lov = get_from_txt(fpath)

            for i in lov:
                if i[1]  in street_list and i[2]  in house_list and i[3] in room_list:
                    sg.popup(f'Такой адрес уже существует: {i[1]} {i[2]} {i[3]}')
                    continue

                elif i[1]  not in street_list or i[2]  not in house_list or  i[3] not in room_list:
                    sq.add_new_cli(i[0], i[1], i[2], i[3], i[4])
                sg.popup('Добавлено')
        except :
            sg.popup('Укажите файл')

    if event == 'Сформировать Должников' and values['-SUMM-']:

        try:
            text = []
            values['-OUT-DEB-'] = sq.get_debtors(values['-SUMM-'])
            window['-OUT-DEB-'].update(values['-OUT-DEB-'])
            text += values['-OUT-DEB-']


        except ValueError:
            values['-OUT-DEB-'] = sq.get_debtors('0')
            window['-OUT-DEB-'].update(values['-OUT-DEB-'])
            text += values['-OUT-DEB-']
    if event == "Экспорт в 'txt'":
        try:
            add_to_txt(text)
            sg.popup('Выгружено')
        except:
            sg.popup('Сформируйте должников')

    if event == "Выгрузить в файл 'txt'":
        add_to_txt(sq.get_all_clients(), 'E:/all_clients.txt')
        sg.popup('Выгружено')

    if event == 'OK' and values['-FPATH-']:
        lst2 = []
        for i in reed_ls_txt(values['-FPATH-'])[3:]:
            i.append(values['-FPATH-'])
            lst2.append(i)
        rows4 = [i for i in lst2]
        values['-WRONG_LS-'] = rows4[3:]
        window['-WRONG_LS-'].update(values['-WRONG_LS-'])
        values['-REESTR-'] = values['-FPATH-']
        window['-REESTR-'].update(values['-REESTR-'])
    elif event == 'Cancel':
        values['-FPATH-'] = []
        window['-FPATH-'].update(values['-FPATH-'])

    if "Обновить список нарядов":
        rows5 = [i for i in sq.get_all_orders()]
        values['-ORDERS-']= rows5
        window['-ORDERS-'].update(values['-ORDERS-'])

    if event == 'Сформировать квитанции':
        today = datetime.datetime.today()
        res = []
        for i in sq.get_all_clients():
            res.append([j for j in i])

        try:
            get_invoice(res)
            sg.popup("Операция выполнена, файл находится в корневом каталоге программы")
        except:
            sg.popup("Что-то пошло не так, попробуйте еще раз")

    if values['-STRLST-']:
        for i in values['-STRLST-']:
            strlst = i
        try:
            houselst = sq.get_street_all_houses(strlst)
            window['-HOUSELST-'].update(houselst)

        except:
            sg.Print('Error')

    if event == 'Сформировать квитанции для дома' and values['-HOUSELST-'] and values['-STRLST-']:
        vals = ''
        valh = ''
        hres = []
        for i in values['-STRLST-']:
            vals += i
        for j in values['-HOUSELST-']:
            valh += j
        try:
            hres.append(sq.get_house_clients(vals, valh))
            get_invoice(hres)
            rows6 = [[datetime.date.today(), vals + ' ' + valh]]
            window['-INVVAL-'].update(rows6)
            sg.popup("Операция выполнена, файл находится в корневом каталоге программы")
        except:
            sg.Print('Error')
    if event == 'Начислить тариф':
        sg.popup_yes_no("Начислить тариф всем абонентам ?")
        if 'Yes':
            sq.add_tarif()
            sg.popup("Тариф начислен")
        else:
            pass







window.close()
