import flet as ft
about_text ="""Namasthey ..!\n\nI am Lakshmi Shashank a Software Engineer who is passionate about crafting efficient solutions to various business needs and real world problems. I keep myself busy with learning new technologies, art forms and cooking. Beyond work when I’m not at my desk, you’ll likely find me\n\n   - Exploring the world through a lens—capturing landscapes and family moments with my photography.\n   - I’m a nature enthusiast who finds peace on a hiking trail and inspiration through traveling to new cultures.\n   - At home, I enjoy decompressing with video games, movies, and a great soundtrack.\n   - Most importantly, I cherish my time playing with my kids, whether we’re on a 'nature scavenger hunt' or just enjoying a quiet afternoon together."""
connect_text="I’m always open to discussing new opportunities, creative collaborations, or even just sharing a great hiking trail recommendation. Whether you have a specific project in mind or just want to connect, I’d love to hear from you. Let’s build something amazing together!"
attr_text = "Digital design is a collaborative effort. I’d like to attribute the beautiful icons used throughout this site to the talented creators at Flaticon. Thank you for helping bring this portfolio to life!"
abt = [
    {
        'imgsr':'hobby/photo.png',
        'descr':'I love capturing the world through my lens, finding beauty in both grand landscapes and family moments. Check out the Photography Highlights section below to see my work!',
    },
    {
        'imgsr':'hobby/hike.png',
        'descr':'There’s nothing like the peace of a mountain trail to clear the mind and stay connected with nature.\n \n ',
    },
    {
        'imgsr':'hobby/music.png',
        'descr':'A constant companion in my life, music provides the perfect soundtrack for both focus and relaxation.\n ',
    },
    {
        'imgsr':'hobby/cooking.png',
        'descr':'I enjoy experimenting with flavors in the kitchen, turning a meal into a creative and rewarding project.\n ',
    },
    {
        'imgsr':'hobby/playing.png',
        'descr':"My most cherished time is spent with my family, especially engaging in 'nature scavenger hunts' with my kids.\n ",
    },
    {
        'imgsr':'hobby/coding.png',
        'descr':'Even in my downtime, building small apps and solving puzzles through code remains a favorite creative outlet.\n ',
    },
    {
        'imgsr':'hobby/stock.png',
        'descr':'I enjoy analyzing market trends and applying data-driven strategies to navigate the financial world.\n ',
    },
    {
        'imgsr':'hobby/gamepad.png',
        'descr':'Whether for the storytelling or the competitive challenge, gaming is my go-to for decompressing and having fun.\n ',
    },
    
]
hob_pix = [
    {
        'imgsr':'hobby/mycaptures/sea.jpg',
        'detls':"Fisherman's pride\n Vancouver"
    },
    {
        'imgsr':'hobby/mycaptures/horizon.jpg',
        'detls':"Urban Divide\n Muskoka"
    },
    {
        'imgsr':'hobby/mycaptures/tanjavur.jpg',
        'detls':"Chola's Marvel\n Tanjavur"
    },
    {
        'imgsr':'hobby/mycaptures/nortedam.jpg',
        'detls':"Nortedam Cathedral\n Montreal"
    },
    {
        'imgsr':'hobby/mycaptures/food.jpg',
        'detls':"Thai Delicacy\n Pad Thai"
    },
    {
        'imgsr':'hobby/mycaptures/owl.jpg',
        'detls':"Halloween Hoot\n Mississauga"
    },
    {
        'imgsr':'hobby/mycaptures/stories.jpg',
        'detls':"Wall Arts\n Mississauga"
    },
    {
        'imgsr':'hobby/mycaptures/natraja.jpg',
        'detls':"Ether of Consciousness\n Chidambaram"
    },
]

connect_icon=[
    {
        'imgsr':'connect/mail.png',
        'detls':"Gmail",
        'url':"mailto:chlakshmishashank@gmail.com"
    },
    {
        'imgsr':'connect/linkedin.png',
        'detls':"LinkedIn",
        'url':"https://www.linkedin.com/in/lakshmishashankch/"
    },
    {
        'imgsr':'connect/github.png',
        'detls':"Github",
        'url':"https://github.com/vish4life"
    },
]

def about_view(page:ft.Page):
    async def handle_click(e):
        print('came into the handle click: ',e)
        url = e.control.data
        if url:
            await page.launch_url(url,web_popup_window_name="_blank")
    return ft.Container(
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    [
                        ft.Icon(ft.Icons.PERSON, color="#e10600", size=40),
                        ft.Text(
                            "ABOUT ME", 
                            size=40, 
                            weight=ft.FontWeight.W_900, 
                            color="white",
                            font_family="Titillium Web Black"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(height=20,color="white10"),
                # ft.Text("Namasthey ..!\nI am Lakshmi Shashank a Software Engineer who is passionate about crafting efficient solutions to various business needs and real world problems. I keep myself busy with learning new technologies, art forms and cooking.",italic=True,color="white",size=18,font_family="Titillium Web"),
                ft.Container(
                    padding=30,
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Text(
                                about_text,
                                size=16,
                                color="white",
                                font_family="Titillium Web",
                                style=ft.TextStyle(letter_spacing=1.5),
                                italic=True,
                            ),
                        ]
                    )
                ),
                ft.Container(height=20),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        *[
                            ft.Container(
                                col={"xs":12,"sm":6,"md":4,"lg":3},
                                padding=20,
                                bgcolor="#ffffff",
                                border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                                border_radius=8,
                                content=ft.Column(
                                    [
                                        ft.Container(
                                        expand=True,
                                        border_radius=8,
                                        alignment=ft.Alignment.CENTER,
                                        content=ft.Image(src=item['imgsr'],width=50,height=50)
                                    ),
                                    ft.Container(height=5),
                                    ft.Text(
                                        item['descr'], 
                                        color="black", 
                                        size=13,
                                        italic=True,
                                        align=ft.Alignment.CENTER,
                                        max_lines=15, # Keeps the box height consistent
                                    ),
                                    ]
                                )
                            )
                            for item in abt
                        ],
                        ft.Divider(height=20,color="white10"),
                        ft.Text("PHOTOGRAPHY",size=20,color="white100",font_family="Titillium Web",align=ft.Alignment.CENTER),
                        *[
                            ft.Container(
                                col={"xs":12,"sm":6,"md":4,"lg":3},
                                padding=20,
                                # bgcolor="#ffffff",
                                # border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                                border_radius=8,
                                content=ft.Column(
                                    [
                                        ft.Container(
                                            expand=True,
                                            border_radius=8,
                                            # scale=1.15,
                                            alignment=ft.Alignment.CENTER,
                                            content=ft.Image(src=item['imgsr'],width=250,height=250),
                                            tooltip=item['detls'],
                                        ),
                                    ]
                                )
                            )
                            for item in hob_pix
                        ]
                    ]
                ),
                ft.Row(
                    [
                        ft.Icon(ft.Icons.CONTACTS_ROUNDED, color="#e10600", size=40),
                        ft.Text(
                            "CONNECT", 
                            size=40, 
                            weight=ft.FontWeight.W_900, 
                            color="white",
                            font_family="Titillium Web Black"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(height=20,color="white10"),
                ft.Container(
                    expand=True,
                    padding=10,
                    bgcolor="white30",
                    border_radius=8,
                    content=ft.Column(
                        [
                            ft.Text(
                                connect_text,
                                font_family="Titillium Web",
                                size=16,
                                style=ft.TextStyle(letter_spacing=1.5),
                                italic=True,
                                color="white"
                            ),
                            ft.ResponsiveRow(
                                spacing=2,
                                run_spacing=2,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    *[
                                        ft.Container(
                                            col={"xs":12,"sm":6,"md":4,"lg":1},
                                            padding=10,
                                            # bgcolor="#ffffff",
                                            # border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                                            border_radius=8,
                                            content=ft.Column(
                                                [
                                                    ft.Container(
                                                        expand=True,
                                                        border_radius=8,
                                                        # scale=1.15,
                                                        alignment=ft.Alignment.CENTER,
                                                        content=ft.Image(src=item['imgsr'],width=50,height=50),
                                                        tooltip=item['detls'],
                                                        data=item.get('url') if item.get('url') else None,
                                                        on_click=handle_click,
                                                    ),
                                                ]
                                            )
                                        )
                                        for item in connect_icon
                                    ]
                                ]
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    expand=True,
                    bgcolor="black",
                    padding=25,
                    border_radius=8,
                    content=ft.Column(
                                [
                                    ft.Text(
                                        attr_text,
                                        size=13, 
                                        color="white", 
                                        font_family="Titillium Web",
                                        style=ft.TextStyle(letter_spacing=1.5)
                                    ),
                                    ft.Container(
                                        expand=True,
                                        border_radius=8,
                                        alignment=ft.Alignment.CENTER,
                                        content=ft.Text("Click here to view Credits",font_family="Titillium Web",color="white",italic=True,size=10),
                                        data="/html/credits.html",
                                        on_click=handle_click,
                                    ),
                                    ft.Container(height=10),
                                    ft.Row(
                                        spacing=10,
                                        controls=
                                        [
                                            ft.Divider(thickness=1,color="white60",expand=True),
                                            ft.Text("\u00A9 2026 Lakshmi Shashank. All rights reserved.",color="white60",font_family="Titillium Web",size=13),
                                            ft.Divider(thickness=1,color="white60",expand=True),
                                        ]
                                    ),
                                ]
                            )
                ),
            ]
        )
    )