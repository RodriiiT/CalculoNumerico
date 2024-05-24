import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Evaluación 1"

    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()
        page.views.append(
            ft.View(
                '/',
                [
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
                    "/Conversor",
                    [
                        ft.AppBar(title=ft.Text("Conversor"), bgcolor='blue'),
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
                    "/Seidel",
                    [
                        ft.AppBar(title=ft.Text("Seidel"), bgcolor='blue'),
                        ft.ElevatedButton("Ir al menú", on_click=lambda _: page.go("/")),
                    ],
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
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


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
