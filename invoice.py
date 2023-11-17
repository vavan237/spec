# -*- coding: utf-8 -*-
import locale
from decimal import Decimal
from pathlib import Path
from borb.pdf import SingleColumnLayout, OrderedList, Paragraph, FlexibleColumnWidthTable, PageLayout, TableCell, \
    Alignment, Image, Barcode, BarcodeType
from borb.pdf.canvas.font.font import Font
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from datetime import datetime
from borb.pdf.pdf import PDF
locale.setlocale(locale.LC_ALL, "ru")
font_path: Path = Path(__file__).parent / "Open_Sans/OpenSans-VariableFont_wdth,wght.ttf"
custom_font: Font = TrueTypeFont.true_type_font_from_file(font_path)



def get_table(qr, fio, adres, ls, tarif, total, credit, total_summ):
    period = datetime.today().strftime('%B')
    current_date = datetime.now().strftime('%d-%m-%Y')
    table: FlexibleColumnWidthTable = (FlexibleColumnWidthTable(number_of_columns=7, number_of_rows=14)
        .add(TableCell(Barcode(data=qr, width=Decimal(90), height=Decimal(90), type=BarcodeType.QR, ), row_span=7))
        .add(TableCell(Paragraph(f"Получатель платежа", font_size=Decimal(8), font=custom_font, horizontal_alignment=Alignment.CENTERED), column_span=6))
        .add(TableCell(Paragraph('Общество с ограниченной ответственностью "СПЕЦ", 358000, Калмыкия Респ, Элиста г, ул.Ю.Клыкова 81Г корп. 3А, каб."6" Расчетный счет 40702810460300003949, в СТАВРОПОЛЬСКОЕ ОТДЕЛЕНИЕ N5230 ПАО СБЕРБАНК, СТАВРОПОЛЬ БИК 040702615, ИНН 0816025962, КПП 081601001, ОРГН 1130816022578',
            horizontal_alignment=Alignment.CENTERED, font_size=Decimal(5), font=custom_font), column_span=6))
        .add(TableCell(Paragraph("Плательщик", horizontal_alignment=Alignment.CENTERED, font=custom_font, font_size=Decimal(8)), column_span=6))
        .add(TableCell(Paragraph(f'ФИО:  {fio}', font=custom_font, font_size=Decimal(8)), column_span=3))
        .add(TableCell(Paragraph(f'Период {period}', font=custom_font, font_size=Decimal(8)), column_span=3))
        .add(TableCell(Paragraph(f'Адрес  {adres}', font=custom_font, font_size=Decimal(8)), column_span=3))
        .add(TableCell(Paragraph(f'ФЛС  {ls}', font=custom_font, font_size=Decimal(8)), column_span=3))
        .add(TableCell(Paragraph(f'Дата заполнения  {current_date}', font=custom_font, font_size=Decimal(8)), column_span=3))
        .add(TableCell(Paragraph('Подпись плательщика', font=custom_font, font_size=Decimal(8)), column_span=3))
        .add(TableCell(Paragraph('Общество с ограниченной ответственностью "СПЕЦ", 358000, Калмыкия Респ, Элиста г, ул.Ю.Клыкова 81Г корп. 3А, каб."6" Расчетный счет 40702810460300003949, в СТАВРОПОЛЬСКОЕ ОТДЕЛЕНИЕ N5230 ПАО СБЕРБАНК, СТАВРОПОЛЬ БИК 040702615, ИНН 0816025962, КПП 081601001, ОРГН 1130816022578',
            font=custom_font, font_size=Decimal(5)), column_span=6))
        .add(TableCell(Image(Path("image/photo_2023-10-28_15-29-24.jpg"), horizontal_alignment=Alignment.CENTERED, vertical_alignment=Alignment.MIDDLE, width=Decimal(80), height=Decimal(80)), row_span=7))
        .add(Paragraph("Вид платежа", font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED))
        .add(Paragraph(f"Тариф  {tarif}", font=custom_font, font_size=Decimal(7),
                       horizontal_alignment=Alignment.CENTERED))
        .add(Paragraph("Объем", font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED))
        .add(Paragraph(f"Нач. 100%", font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED))
        .add(Paragraph(f"Всего", font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED))
        .add(Paragraph(f"ФИО:  {fio}", font=custom_font, font_size=Decimal(7)))
        .add(TableCell(Paragraph("Обслуживание СОД(домофон)", font=custom_font, font_size=Decimal(7),
                                 horizontal_alignment=Alignment.CENTERED), row_span=4))
        .add(TableCell(Paragraph(tarif, font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED), row_span=4))
        .add(TableCell(Paragraph("100%", font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED), row_span=4))
        .add(TableCell(Paragraph(tarif, font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED), row_span=4))
        .add(TableCell(Paragraph(total, font=custom_font, font_size=Decimal(7), horizontal_alignment=Alignment.CENTERED), row_span=4))
        .add(Paragraph(f"Адрес:  {adres}", font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(f"Период:  {period}", font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(f"ФЛС:  {ls}", font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(f"+ Долг / - Аванс на начало:  {credit}", font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(f"Итого:", font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(tarif, font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(tarif, font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(tarif, font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(total, font=custom_font, font_size=Decimal(7)))
        .add(Paragraph(tarif, font=custom_font, font_size=Decimal(7)))
        .add(TableCell(Paragraph('Квитанцию можно оплатить в отделениях Почты,Сбербанка, Сбер-банк Онлайн, в РКЦ: ул.Городовикова, д.7 (старый ЗАГС), 1 микр д.3, 3 микр д.8, 8 микр д. 67 "Б" (Магнит)',
            font=custom_font, font_size=Decimal(5), horizontal_alignment=Alignment.CENTERED), column_span=5))
        .add(Paragraph(f"Итого к оплате:  {total_summ}", font=custom_font, font_size=Decimal(7)))
        .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))

    )
    return table


def get_invoice(val_list):
    doc: Document = Document()
    page: Page = Page()
    doc.add_page(page)
    layout: PageLayout = SingleColumnLayout(page)
    for i in range(len(val_list)):
        tab = get_table(val_list[i][1],
                        val_list[i][1],
                        val_list[i][2] + ' д ' + val_list[i][3] + ' кв ' + val_list[i][4],
                        val_list[i][0],
                        str(val_list[i][5]),
                        str(val_list[i][6]),
                        str(val_list[i][6]),
                        str(abs(int(val_list[i][6]) - int(val_list[i][5])))
                       )
        layout.add(tab)
        layout.add(Paragraph("Тел.: 9-54-58, Билайн-8-961-549-5458, Мегафон-8-937-469-5458. Сайт: 95458.рф, email: 95458@mail.ru, WhatsApp - 8-937-469-5458 Оплачивая данную квитанцию Вы соглашаетесь с условиями публичной оферты расположенной в интернете по адресу: http://specrf.ru/index.php/dogovor График работы мастеров: Пон.-Пят. с 9:00 до 17:00, перерыв с 12:30 до 13:30, Суббота с 9:00 до 14:00, Воскресенье-выходной. График работы офиса: Пон.-Пят. с 9:00 до 16:00, перерыв с 12:30 до 13:30, суббота, воскресенье-выходной.",
            font=custom_font, font_size=Decimal(5), horizontal_alignment=Alignment.CENTERED))
        layout.add(Paragraph(" "))
        layout.add(Paragraph(" "))





    with open("output.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, doc)









