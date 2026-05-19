from math import exp
import flet as ft

edu_prof = [
    {
        'insti':'University of Central Missouri',
        'level':'Master of Science',
        'place':'Missouri, USA',
        'cours':'CIS & IT',
        'years':'2015 - 2016',
        'imgsr':'edu/ucm.png',
        'descr':'Graduated with honors\n- Bigdata (Hadoop)\n- Fullstack (JS & .net)\n- Databases (Oracle, MongoDb)'
    },
    {
        'insti':'Manipal Academy of Higher Education',
        'level':'Post Graduate Diploma',
        'place':'Bengaluru, India',
        'cours':'Banking & Finance',
        'years':'2010 - 2011',
        'imgsr':'edu/mahe4.png',
        'descr':'PG Diploma\n- Economics\n- Banking & Finance\n- Banking technologies'
    },
    {
        'insti':'JN Technological University',
        'level':'Bachelor of Technology',
        'place':'Hyderabad,India',
        'cours':'Aeronautical Engineering',
        'years':'2004 - 2008',
        'imgsr':'edu/jntuh.png',
        'descr':'Engineering\n- Aerospace\n- CATIA / CAD designing\n- Computational Fluid Dynamics'
    },
    {
        'insti':'Sri Chaitanya Junior Kalasala',
        'level':'Secondary Education',
        'place':'Hyderabad,India',
        'cours':'MPC',
        'years':'2002 - 2004',
        'imgsr':'edu/bie.png',
        'descr':'Secondary Education\n- Maths\n- Physics\n- Chemistry'
    },
    
]
import flet as ft

def education_view():
    return ft.Container(
        padding=20,
        content=
        ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
ft.ResponsiveRow(
            spacing=20,
            run_spacing=20,
            controls=[
                ft.Row(
                    [
                        ft.Icon(ft.Icons.SCHOOL, color="#e10600", size=40),
                        ft.Text(
                            "EDUCATION", 
                            size=40, 
                            weight=ft.FontWeight.W_900, 
                            color="white",
                            font_family="Titillium Web Black"
                        ),
                    ],
                    # alignment=ft.MainAxisAlignment.CENTER,
                ),
                *[
                    ft.Container(
                        # 4 items per row on large screens (col=3)
                        # 2 items per row on tablets (col=6)
                        # 1 item per row on mobile (col=12)
                        col={"xs": 12, "sm": 6, "lg": 3}, 
                        padding=20,
                        bgcolor="#1e1e2c",
                        border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                        border_radius=8,
                        # Set a height to keep them uniform and "neat"
                        height=520, 
                        content=ft.Column([
                            ft.Text(
                                study['level'], 
                                size=20, 
                                weight="bold", 
                                color="white",
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS
                            ),
                            ft.Text(
                                study['cours'], 
                                size=20, 
                                weight="bold", 
                                color=ft.Colors.WHITE_38,
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS
                            ),
                            ft.Text(
                                study['insti'], 
                                size=16, 
                                color="#e10600",
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS
                            ),
                            ft.Text(study['years'], size=13, color="white54"),
                            ft.Text(study['place'], size=13, color="white54"),
                            ft.Container(height=5),
                            ft.Text(
                                study['descr'], 
                                color="white70", 
                                size=15,
                                max_lines=6, # Keeps the box height consistent
                                # overflow=ft.TextOverflow.
                            ),
                            ft.Divider(color="white10", height=20),
                            ft.Container(
                                expand=True,
                                border_radius=8,
                                bgcolor=ft.Colors.WHITE,
                                alignment=ft.Alignment.CENTER,
                                content=ft.Image(src=study['imgsr'],width=150,height=200)
                            ),
                            # ft.Image(src=study['imgsr'],width=100,height=100)
                        ], spacing=5)
                    )
                    for study in edu_prof
                ],
            ]
        )
            ]
        ),
        
    )
