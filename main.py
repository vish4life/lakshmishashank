import flet as ft

def main(page: ft.Page):
    page.title="Lakshmi Shashank"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Text("HELLO MY APP LAKSHMI SHASHANK")
    )


if __name__ == "__main__":
    ft.run(main, assets_dir="src/assets")
