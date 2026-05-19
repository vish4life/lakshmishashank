import flet as ft
import flet_audio as fa

from tabs.home import home_view
from tabs.education import education_view
from tabs.work import experience_view
from tabs.projects import projects_view
from tabs.about import about_view

def main(page: ft.Page):
    page.title = "Lakshmi Shashank"
    page.bgcolor = "#0a0a0f"  # Deep dark background, carbon like
    page.theme_mode = ft.ThemeMode.DARK
    
    # Load F1-like Fonts
    page.fonts = {
        "Titillium Web": "https://raw.githubusercontent.com/google/fonts/main/ofl/titilliumweb/TitilliumWeb-Regular.ttf",
        "Titillium Web Bold": "https://raw.githubusercontent.com/google/fonts/main/ofl/titilliumweb/TitilliumWeb-Bold.ttf",
        "Titillium Web Black": "https://raw.githubusercontent.com/google/fonts/main/ofl/titilliumweb/TitilliumWeb-Black.ttf",
    }
    # Set default theme
    page.theme = ft.Theme(font_family="Titillium Web")
    
    # page audio
    audio_src = fa.Audio(
        src="F1HansZimmer.mp3",
        autoplay=True,
        volume=0.1,
    )
    page.services.append(audio_src)

    content_area = ft.AnimatedSwitcher(
        expand=True,
        content=ft.Container(), # Initial empty content
        transition=ft.AnimatedSwitcherTransition.FADE, # Fade effect
        duration=800, # Duration in milliseconds
        reverse_duration=100, # How fast the old content disappears
        switch_in_curve=ft.AnimationCurve.EASE_IN_OUT, # Smooth movement
    )

    def on_nav_change(index):
        # idx = e.control.selected_index
        page.navigation_bar.selected_index = index
        idx = index
        if idx == 0:
            content_area.content = home_view(on_nav_change)
        elif idx == 1:
            content_area.content = education_view()
        elif idx == 2:
            content_area.content = experience_view()
        elif idx == 3:
            content_area.content = projects_view(page)
        elif idx == 4:
            content_area.content = about_view(page)
        content_area.update()
        page.update()
    
    content_area.content = home_view(on_nav_change)
    # content_area.content = about_view(page)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SCHOOL_OUTLINED, selected_icon=ft.Icons.SCHOOL, label="Education"),
            ft.NavigationBarDestination(icon=ft.Icons.WORK_OUTLINE, selected_icon=ft.Icons.WORK, label="Experience"),
            ft.NavigationBarDestination(icon=ft.Icons.DASHBOARD_OUTLINED, selected_icon=ft.Icons.DASHBOARD, label="Projects"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINE, selected_icon=ft.Icons.PERSON, label="About"),
        ],
        on_change=lambda e: on_nav_change(e.control.selected_index),
        bgcolor="#1e1e2c",
        indicator_color="#e10600",
        selected_index=0,
    )

    # Background image stack
    bg_container = ft.Container(
        image=ft.DecorationImage(
            src="bg.jpg",
            fit=ft.BoxFit.COVER,
            color_filter=ft.ColorFilter(ft.BlendMode.MULTIPLY, "#404040"), # Darken background
            opacity=0.3,
        ),
        expand=True,
    )

    main_stack = ft.Stack(
        controls=[
            bg_container,
            content_area
        ],
        expand=True
    )

    # window size changes
    def on_window_resize(e):
        page.update(page.width, page.height)
    page.on_resize = on_window_resize

    page.add(main_stack)

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")