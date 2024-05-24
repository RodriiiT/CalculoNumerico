import flet as ft
import numpy as np
from gaussseidel import gauss_seidel

def main(page: ft.Page) -> None:
    page.title = "Evaluación 1"

    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(
            ft.View(
                route='/',
                controls=[
                    ft.AppBar(title=ft.Text("Inicio"), bgcolor='blue'),
                    ft.Text(value='Menú', size=30,color='black'),
                    ft.Row(
                        [
                            ft.ElevatedButton("Conversor", on_click=lambda _: page.go("/Conversor")),
                            ft.ElevatedButton("Seidel", on_click=lambda _: page.go("/Seidel")),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                ],
                vertical_alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        if page.route == "/Conversor":
            page.views.append(
                ft.View(
                    route="/Conversor",
                    controls=[
                        ft.AppBar(title=ft.Text("Conversor"), bgcolor='blue'),
                        ft.Dropdown(
                            label="Seleccione el sistema de salida",
                            hint_text="Sistema de salida",
                            width=page.width*0.3,
                            options=[
                                ft.dropdown.Option("Binario"),
                                ft.dropdown.Option("Ternario"),
                                ft.dropdown.Option("Cuaternario"),
                                ft.dropdown.Option("Octal"),
                                ft.dropdown.Option("Decimal"),
                                ft.dropdown.Option("Hexadecimal"),
                                ],
                                autofocus=True,
                        ),
                        ft.TextField(
                            label="Ingrese el valor que desea convertir",
                            width=page.width*0.3,
                            ),
                        ft.Dropdown(
                            label="Seleccione el sistema de salida",
                            hint_text="Sistema de salida",
                            width=page.width*0.3,
                            options=[
                                ft.dropdown.Option("Binario"),
                                ft.dropdown.Option("Ternario"),
                                ft.dropdown.Option("Cuaternario"),
                                ft.dropdown.Option("Octal"),
                                ft.dropdown.Option("Decimal"),
                                ft.dropdown.Option("Hexadecimal"),
                                ],
                                autofocus=True,
                        ),
                        ft.TextField(
                            label="Resultado",
                            disabled=True,
                            width=page.width*0.3,
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Convertir"),
                                ft.ElevatedButton("Limpiar"),
                            ],
                            alignment= ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        ),
                        ft.ElevatedButton("Ir al menú", on_click=lambda _: page.go("/")),
                    ],
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    spacing=20
                )
            )
        elif page.route == "/Seidel":
        #Dropdown para seleccionar el tamaño de la matriz
            tam_matriz = ft.Dropdown(
                label="Seleccione el tamaño de la matriz",
                hint_text="Tamaño de la matriz",
                width=page.width * 0.3,
                options=[
                    ft.dropdown.Option("3x3"),
                    ft.dropdown.Option("4x4"),
                    ft.dropdown.Option("5x5"),
                    ft.dropdown.Option("6x6"),
                ],
                autofocus=True,
            )

            page.views.append(
                ft.View(
                    route="/Seidel",
                    controls=[
                        ft.AppBar(title=ft.Text("Gauss-Seidel"), bgcolor='blue'),
                        tam_matriz,
                        ft.ElevatedButton("Generar campos"),
                        ft.ElevatedButton("Ir al menú", on_click=lambda _: page.go("/")),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
