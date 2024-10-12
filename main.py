import flet as ft
import sqlite3 as sq
from simpledt import SQLDataTable


def main(page: ft.Page):

    def step_first(e):

        page.controls.clear()
        #строка ввода длины
        textfield_1 = ft.TextField(
            label='Длина крыши',
            hint_text='Введите длину крыши в метрах',
            keyboard_type=ft.KeyboardType.NUMBER,
            # input_filter = ft.NumbersOnlyInputFilter()
            )
        #строка ввода ширины

        textfield_2 = ft.TextField(
            label='Ширина крыши',
            hint_text='Введите ширину крыши в метрах',
            keyboard_type=ft.KeyboardType.NUMBER,
            # input_filter = ft.NumbersOnlyInputFilter()

        )

        # def change_checkbox(e):
        #     textfield_3.disabled = f"{c.value}"
        #     textfield_3.update()


        # c = ft.Checkbox(label='Выступ отсутствует', on_change=change_checkbox)
        #
        # textfield_3 = ft.TextField(label='Длина выступа',
        #                            hint_text='Введите длину вуступа в метрах',
        #                            keyboard_type=ft.KeyboardType.NUMBER
        #                           )
        # Выбор материала
        conn = sq.connect('material_table.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Номер, Название, Длина, Ширина, Производитель FROM material")
        material_list = cursor.fetchall()

        page.controls.clear()


        def calculeted_material(e):
            num = list_material.value[1]

            conn = sq.connect('material_table.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Длина, Ширина FROM material WHERE Номер = ?", (f'{num}'))
            hight, wight = cursor.fetchone()
            conn.commit()
            conn.close()
        list_material = ft.Dropdown(label='Выберите материал',hint_text='Материал', on_change=calculeted_material)
        for el in material_list:
            list_material.options.append(ft.dropdown.Option(el))
            page.update()

        conn.commit()
        conn.close()



        def calculeted_1(e):
            num = list_material.value[1]

            conn = sq.connect('material_table.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Длина, Ширина FROM material WHERE Номер = ?", (f'{num}'))

            hight, wight = cursor.fetchone()

            conn.commit()
            conn.close()

            ploshad_krishi = float(textfield_1.value) * float(textfield_2.value)
            ploshad_lista = float(hight) * float(wight)
            kolichestv_listov = ploshad_krishi / ploshad_lista
            kolichestv_listov = int(round(kolichestv_listov, 1))
            final_text.value = f"Вым понадобится {kolichestv_listov} листов"
            page.update()
        calculeted_btn = ft.ElevatedButton(text='Расчитать', on_click=calculeted_1)

        final_text = ft.Text()
        page.add(drop_list,
                 textfield_1,
                 textfield_2,
                 list_material,
                 ft.Row(controls=[calculeted_btn], alignment=ft.MainAxisAlignment.CENTER),
                 final_text
                 )

    def step_second(e):
        page.controls.clear()
        # строка ввода длины
        textfield_1 = ft.TextField(
            label='Длина первого ската',
            hint_text='Введите длину первого ската в метрах',
            keyboard_type=ft.KeyboardType.NUMBER,
            # input_filter = ft.NumbersOnlyInputFilter()
        )
        # строка ввода ширины

        textfield_2 = ft.TextField(
            label='Ширина первого ската',
            hint_text='Введите ширину первого ската в метрах',
            keyboard_type=ft.KeyboardType.NUMBER,
            # input_filter = ft.NumbersOnlyInputFilter()

        )
        # строка ввода длины
        textfield_3 = ft.TextField(
            label='Длина второго ската',
            hint_text='Введите длину второго ската в метрах',
            keyboard_type=ft.KeyboardType.NUMBER,
            # input_filter = ft.NumbersOnlyInputFilter()
        )
        # строка ввода ширины

        textfield_4 = ft.TextField(
            label='Ширина второго ската',
            hint_text='Введите ширину второго ската в метрах',
            keyboard_type=ft.KeyboardType.NUMBER,
            # input_filter = ft.NumbersOnlyInputFilter()

        )
        conn = sq.connect('material_table.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Номер, Название, Длина, Ширина, Производитель FROM material")
        material_list = cursor.fetchall()
        def calculeted_material(e):
            num = list_material.value[1]

            conn = sq.connect('material_table.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Длина, Ширина FROM material WHERE Номер = ?", (f'{num}'))
            hight, wight = cursor.fetchone()
            conn.commit()
            conn.close()
        list_material = ft.Dropdown(label='Выберите материал', hint_text='Материал', on_change=calculeted_material)
        for el in material_list:
            list_material.options.append(ft.dropdown.Option(el))
            page.update()
        def calculeted_1(e):
            num = list_material.value[1]

            conn = sq.connect('material_table.db')
            cursor = conn.cursor()
            cursor.execute("SELECT Длина, Ширина FROM material WHERE Номер = ?", (f'{num}'))

            hight, wight = cursor.fetchone()

            conn.commit()
            conn.close()

            ploshad_krishi = (float(textfield_1.value) * float(textfield_2.value)) + (float(textfield_3.value) * float(textfield_4.value))
            ploshad_lista = float(hight) * float(wight)
            kolichestv_listov = ploshad_krishi / ploshad_lista
            kolichestv_listov = int(round(kolichestv_listov, 1))
            final_text.value = f"Вым понадобится {kolichestv_listov} листов"
            page.update()
        calculeted_btn = ft.ElevatedButton(text='Расчитать', on_click=calculeted_1)
        conn.commit()
        conn.close()
        final_text = ft.Text()
        page.add(drop_list, textfield_1, textfield_2, textfield_3, textfield_4, list_material, calculeted_btn, final_text)

    drop_list = ft.Dropdown(
        label='Тип',
        hint_text='Выберите тип крыши',
        options=[
            ft.dropdown.Option(text='Односкатная', on_click=step_first),
            ft.dropdown.Option(text='Двускатая', on_click=step_second)
        ]
    )

    def bar_change(e):
        page.controls.clear()
        nav_dest = e.control.selected_index

        if nav_dest == 0:  #при выборе кнопки "калькулятор" открывается страница калькулятора
            page.add(ft.Row(controls=[lider_text], alignment=ft.MainAxisAlignment.CENTER), drop_list)

        elif nav_dest == 1:  #при выборе кнопки "склад" открывается страница склада
            def delete_material(e):
                page.controls.clear()
                textfiled_delete = ft.TextField(label='Номер материала', hint_text='Введите номер материала для удаления')
                def delete_material_2(e):
                    conn = sq.connect('material_table.db')
                    cursor = conn.cursor()
                    cursor.execute(f"DELETE from material where Номер = '{textfiled_delete.value}'")
                    conn.commit()
                    conn.close()

                    page.controls.clear()

                    page.add(dt,ft.Row(controls=[delete_btn], alignment=ft.MainAxisAlignment.CENTER))
                    page.controls.clear()
                    page.add(dt,ft.Row(controls=[delete_btn], alignment=ft.MainAxisAlignment.CENTER))

                delete_btn_2 = ft.ElevatedButton(text='Удалить материал',on_click=delete_material_2)

                page.add(textfiled_delete,ft.Row(controls=[delete_btn_2], alignment=ft.MainAxisAlignment.CENTER))

            try:
                sql = SQLDataTable('sqlite', 'material_table.db', 'material')
                dt = sql.datatable

                delete_btn = ft.ElevatedButton(
                    text='Удалить материал',
                    on_click = delete_material
                )
                page.add(dt,
                         ft.Row(controls=[delete_btn], alignment=ft.MainAxisAlignment.CENTER)
                         )
            except ValueError:
                page.add(
                    ft.Row(controls=[ft.Text('Здесь пока ничего нет. Добавтве материал, чтобы увидеть таблицу')],alignment=ft.MainAxisAlignment.CENTER))



        elif nav_dest == 2:#добавление материала

            def get_material(e):
                conn = sq.connect('material_table.db')
                cursor = conn.cursor()


                cursor.execute('CREATE TABLE IF NOT EXISTS material(Номер INTEGER PRIMARY KEY, Название TEXT, Длина REAL, Ширина REAL, Производитель TEXT)')# values = [f({material_input.value},{hight_input.value},{wight_input.value},{autor_input.value})]
                cursor.execute(f"INSERT INTO material VALUES (NULL, '{material_input.value}', '{float(hight_input.value)}','{float(wight_input.value)}','{autor_input.value}')")

                # cursor.execute(f"SELECT * FROM material WHERE name = '{material_input.value}' AND height = '{hight_input.value}' AND wight = '{wight_input.value}' AND manufacturer = '{autor_input.value}'")
                print(cursor.fetchone())
                conn.commit()
                conn.close()
                page.controls.clear()
                page.add(material_input,
                    hight_input,
                    wight_input,
                    autor_input,
                    ft.Row(controls=[button_get_material], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[ft.Text('Материал добавлен')], alignment=ft.MainAxisAlignment.CENTER)

                )
            def disabled(e):
                if all([material_input.value, hight_input.value, wight_input.value, autor_input.value]):
                    button_get_material.disabled = False
                else:
                    button_get_material.disabled = True
                page.update()


            material_input = ft.TextField(
                label = 'Название материала',
                hint_text='Введите название материала',
                on_change= disabled
            )
            hight_input = ft.TextField(
                label='Длина',#длина листа
                hint_text='Введите длину материала в метрах',
                on_change= disabled,
                # input_filter = ft.NumbersOnlyInputFilter()
            )
            wight_input = ft.TextField(
                label='Ширина',#ширина листа
                hint_text='Введите ширину материала в метрах',
                on_change= disabled,
                # input_filter = ft.NumbersOnlyInputFilter()
            )
            worked_wight = ft.TextField(
                label='Ширина',  # ширина листа
                hint_text='Введите рабочую ширину материала в метрах',
                on_change=disabled,
                # input_filter = ft.NumbersOnlyInputFilter()
            )
            autor_input = ft.TextField(
                label='Производитель',#производитель
                hint_text='Введите производителя',
                on_change= disabled
            )
            button_get_material = ft.ElevatedButton(
                text='Добавить материал',
                on_click=get_material,
                disabled=True
            )

            page.add(
                material_input,
                hight_input,
                wight_input,
                autor_input,
                ft.Row(controls=[button_get_material], alignment=ft.MainAxisAlignment.CENTER)
            )



    page.navigation_bar = ft.NavigationBar(
        destinations=[ft.NavigationBarDestination(icon=ft.icons.CALCULATE, label='Калькулятор'),
                      ft.NavigationBarDestination(icon=ft.icons.WAREHOUSE, label='Склад'),
                      ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label='Добавление материала')
                      ], on_change=bar_change

    )
    page.window.height = 700
    page.window.width = 570
    page.window.top = 300
    page.window.left = 300

    lider_text = ft.Text("СторйСчёт", size=70, weight=ft.FontWeight.W_900, text_align=ft.TextAlign.CENTER)

    page.update()

    page.add(ft.Row(controls=[lider_text], alignment=ft.MainAxisAlignment.CENTER), drop_list)
    page.theme_mode = 'green'
    # cursor.close()
ft.app(target=main)
