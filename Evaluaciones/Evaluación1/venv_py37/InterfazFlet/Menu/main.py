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
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/Store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
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
