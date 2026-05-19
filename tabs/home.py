import flet as ft
asset_url = "https://raw.githubusercontent.com/vish4life/my_assets/main/portfolio_assets/assets/"

def home_view(on_nav_change):
    return ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            # alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    scroll=ft.ScrollMode.AUTO,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        # Left Section: Avatar, Title, and vertical separator
                        ft.Row(
                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                ft.CircleAvatar(
                                    foreground_image_src= asset_url + "shashank.jpeg",
                                    content=ft.Text("LS", color="white", weight=ft.FontWeight.W_200, font_family="Titillium Web Black", size=50),
                                    radius=50,
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            "LAKSHMI SHASHANK CH", 
                                            size=45,  # Adjusted slightly for cleaner side-by-side fit
                                            weight=ft.FontWeight.W_900, 
                                            color="white",
                                            font_family="Titillium Web Black"
                                        ),
                                        ft.Text(
                                            "TECHNOLOGY ENTHUSIAST", 
                                            size=20, 
                                            weight=ft.FontWeight.BOLD, 
                                            color="#e10600",
                                            # color="white",
                                            font_family="Titillium Web",
                                            italic=True,
                                        ),
                                    ]
                                ),
                                
                                # Vertical Separator between profile and cards (Use VerticalDivider)
                                ft.VerticalDivider(width=40, color="white10", thickness=2),
                            ],
                        ),
                        # Right Section: Quick Stats Box
                        ft.Container(
                            width=500, # Defined fixed width for neat layout alignment
                            border=ft.Border(left=ft.BorderSide(5, "#e10600")),
                            padding=20,
                            bgcolor="#1e1e2c",
                            border_radius=8,
                            content=ft.Column([
                                ft.Text("QUICK STATS", size=18, color="#e10600", font_family="Titillium Web Bold"),
                                # Horizontal separator inside the stats box
                                ft.Divider(height=10, thickness=1, color="white10"),
                                ft.Row([ft.Text("Location:", color="white54", width=100), ft.Text("Mississauga, Canada", color="white", weight=ft.FontWeight.BOLD)]),
                                ft.Row([ft.Text("Experience:", color="white54", width=100), ft.Text("16+ Years", color="white", weight=ft.FontWeight.BOLD)]),
                                ft.Row([ft.Text("Focus:", color="white54", width=100), ft.Text("Banking, Payments, AI, Fullstack", color="white", weight=ft.FontWeight.BOLD)]),
                                ft.Row([ft.Text("Status:", color="white54", width=100), ft.Text("Open to Work", color="#00ff00", weight=ft.FontWeight.BOLD)]),
                            ], spacing=10)
                        )
                    ]
                ),
                ft.Container(height=40),
                ft.Text(
                    "Welcome to my digital space! I am Lakshmi Shashank, a technology professional dedicated to building innovative, user-centric solutions. With a deep foundation in banking and a passion for modern development, I bridge the gap between complex financial systems and intuitive digital experiences.", 
                    size=20, 
                    color="white",
                    font_family="Titillium Web",
                    style=ft.TextStyle(letter_spacing=2),
                    italic=True,
                ),
                ft.Container(height=20),
                ft.Text(
                    "Explore my journey, projects, and the technologies that I'm passionate about.➙", 
                    size=20, 
                    color="white",
                    font_family="Titillium Web",
                    style=ft.TextStyle(letter_spacing=2),
                    italic=True,
                ),
                ft.Text("Enjoy the music while on the website, till it lasts ...! 🎧ྀི♪⋆.✮",
                    size=10, 
                    color="white",
                    # align=ft.Alignment.CENTER_RIGHT,
                    font_family="Titillium Web",
                    style=ft.TextStyle(letter_spacing=2),
                    italic=True,
                ),
                ft.Container(height=40),
                ft.Row(
                    controls=[
                        ft.Button(
                            content=ft.Text("ABOUT ME", color="white", weight=ft.FontWeight.W_900), 
                            bgcolor="#e10600",
                            on_click=lambda _: on_nav_change(4),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=4),
                                padding=20,
                            ),
                        ),
                        ft.OutlinedButton(
                            content=ft.Text("VIEW ALL PROJECTS", color="white", weight=ft.FontWeight.W_900),
                            on_click=lambda _: on_nav_change(3),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=4),
                                padding=20,
                                side=ft.BorderSide(2, "white")
                            ),
                        )
                    ]
                ),
                ft.Column(
                    controls=[

                    ]
                ),#next
            ]
        )
    )
