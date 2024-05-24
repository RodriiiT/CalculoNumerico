import flet as ft

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
                    ft.ElevatedButton("Conversor", on_click=lambda _: page.go("/Conversor")),
                    ft.ElevatedButton("Seidel", on_click=lambda _: page.go("/Seidel")),
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
            page.views.append(
                ft.View(
                    route="/Seidel",
                    controls=[
                        ft.AppBar(title=ft.Text("Gauss-Seidel"), bgcolor='blue'),
                        ft.Dropdown(
                            label="Seleccione el tamaño de la matriz",
                            hint_text="Tamaño matriz",
                            width=page.width*0.5,
                            options=[
                                ft.dropdown.Option("3x3"),
                                ft.dropdown.Option("4x4"),
                                ft.dropdown.Option("5x5"),
                                ft.dropdown.Option("6x6"),
                                ft.dropdown.Option("7x7"),
                                ft.dropdown.Option("8x8"),
                                ft.dropdown.Option("9x9"),
                            ],
                        ),
                        ft.Text(
                            value="Ingrese los valores de la matriz A",
                            size=20
                        ),
                        ft.Text(
                            value="Ingrese los valores del vector B",
                            size=20
                        ),
                        ft.Text(
                            value="Vector X resultados",
                            size=20
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton("Operar"),
                                ft.ElevatedButton("Limpiar"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        ),
                        ft.ElevatedButton("Ir al menú", on_click=lambda _: page.go("/")),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
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
