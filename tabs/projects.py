import flet as ft

intern =[
    {
        'compn':'Anzeon Inc.',
        'place':'Kansas City, USA',
        'roles':'Database Administrator',
        'years':'DEC 2015 - MAR 2016',
        'imgsr':'internships/anzeon.png',
        'descr':'As a programmer Intern performed\n- Database backup & recovery\n-Database performance tuning\n- Batch scheduler for monitoring'
    },
    {
        'compn':'Hindustan Aeronautical Ltd.',
        'place':'Bengaluru, India',
        'roles':'Stress Analysis Apprentice',
        'years':'JAN 2008 - MAR 2008',
        'imgsr':'internships/hal.png',
        'descr':'As an apprentice\n- Examined Nosewheel landing gear issue\n-Stress Analysis using NASTRAN/PATRAN\n- Live project on Surya Kiran aircraft'
    },
    {
        'compn':'Air India Ltd.',
        'place':'Hyderabad, India',
        'roles':'Aircraft Maintenance Apperentice',
        'years':'OCT 2007 - DEC 2007',
        'imgsr':'internships/air.svg',
        'descr':'As an apprentice\n- Monitored Radio signals reception\n-Checklist of pre and post flight tasks\n- Assisting maintenance crew'
    },
]

proj = [
    {
        'title':'Particle Scattering',
        'descr':'JS, HTML, CSS \nCanvas',
        'types':'Generative Art App',
        'imgsr':'projects/particles.png',
        'url':'https://github.com/vish4life/acodeofarts'
    },
    {
        'title':'Birds of Metaverse',
        'descr':'JS, HTML, CSS \nCanvas',
        'types':'Generative Art App',
        'imgsr':'projects/birds.png',
        'url':'https://github.com/vish4life/acodeofarts'
    },
    {
        'title':'Peach House Restaurant',
        'descr':'ReactJS, HTML, CSS \nDjango, Sqlite',
        'types':'Web App',
        'imgsr':'projects/reactfe.jpg',
        'url':'https://github.com/vish4life/PeachHouse-Fullstack/blob/8034079c13693c4a8f24f14d990dd6cf912764e3/snapshots/homepage.jpg'
    },
    {
        'title':'Little Lemon Restaurant',
        'descr':'ReactJS, HTML, CSS \n ',
        'types':'Web App',
        'imgsr':'projects/fullstack.jpeg',
        'url':'https://github.com/vish4life/LittleLemon-FullStack'
    },
    {
        'title':'Crypto Analyzer',
        'descr':'ReactJS, HTML, CSS \nDjango, Postgres',
        'types':'Web App',
        'imgsr':'projects/crypto.png',
        'url':'https://github.com/vish4life/kucoinapi_frontend'
    },
    {
        'title':'Portfolio',
        'descr':'Ptyhon (Flet) \n ',
        'types':'Web App',
        'imgsr':'projects/portfolio.png',
        'url':'https://github.com/vish4life/acodeofarts'
    },
    {
        'title':'Peach House',
        'descr':'ReactNative, CSS \nDjango, Sqlite',
        'types':'Mobile App',
        'imgsr':'projects/reactexpoph.png',
        'url':'https://github.com/vish4life/peachhousemobile/blob/main/README.md'
    },
    {
        'title':'Todo App',
        'descr':'ReactNative (Expo), CSS \nDjango, Sqlite',
        'types':'Mobile App',
        'imgsr':'projects/todo.png',
        'url':'https://github.com/vish4life/todoTasks'
    },
    {
        'title':'Bolt Vault',
        'descr':'ReactNative (BareNative), CSS \nDjango, Sqlite',
        'types':'Mobile App',
        'imgsr':'projects/boltvault.png',
        'url':'https://github.com/vish4life/bv_v01_bare_RN'
    },
    {
        'title':'YoQuiz',
        'descr':'ReactNative, CSS \nDjango, Sqlite',
        'types':'Mobile App',
        'imgsr':'projects/yoquiz.png',
        'url':'https://github.com/vish4life/yoquiz'
    },
    {
        'title':'PDF Analyzer',
        'descr':'ReactJS, HTML, CSS \nDjango, Postgres, RAG',
        'types':'Generative AI App',
        'imgsr':'projects/rag.jpg',
        'url':'https://github.com/vish4life/RAGLite'
    },
    {
        'title':'Zero Click Banking',
        'descr':'ReactJS, HTML, CSS \nFastAPI, Postgres, FastMcp',
        'types':'Generative AI App',
        'imgsr':'projects/iva.png',
        'url':'https://github.com/vish4life/iva'
    },
]
stack =[
    {
        'detls':'HTML',
        'imgsr':'lang/html.png',
        'type':'lang'
    },
    {
        'detls':'CSS',
        'imgsr':'lang/css.png',
        'type':'lang'
    },
    {
        'detls':'JS',
        'imgsr':'lang/js.png',
        'type':'lang'
    },
    {
        'detls':'REACT',
        'imgsr':'lang/react.png',
        'type':'lang'
    },
    {
        'detls':'PYTHON',
        'imgsr':'lang/python.png',
        'type':'lang'
    },
    {
        'detls':'DJANGO',
        'imgsr':'lang/django.png',
        'type':'lang'
    },
    {
        'detls':'FASTAPI',
        'imgsr':'lang/fastapi.png',
        'type':'lang'
    },
    {
        'detls':'FLET',
        'imgsr':'lang/flet.png',
        'type':'lang'
    },
    {
        'detls':'SQL',
        'imgsr':'lang/sql.png',
        'type':'lang'
    },
    {
        'detls':'XML',
        'imgsr':'lang/xml.png',
        'type':'lang'
    },
    {
        'detls':'JSON',
        'imgsr':'lang/json.png',
        'type':'lang'
    },
    {
        'detls':'VSCODE',
        'imgsr':'tools/vscode.png',
        'type':'tool'
    },
    {
        'detls':'VSTUDIO',
        'imgsr':'tools/vstudio.png',
        'type':'tool'
    },
    {
        'detls':'TEAMS',
        'imgsr':'tools/teams.png',
        'type':'tool'
    },
    {
        'detls':'EXCEL',
        'imgsr':'tools/excel.png',
        'type':'tool'
    },
    {
        'detls':'WORD',
        'imgsr':'tools/word.png',
        'type':'tool'
    },
    {
        'detls':'POWERPOINT',
        'imgsr':'tools/powerpoint.png',
        'type':'tool'
    },
    {
        'detls':'AWS',
        'imgsr':'tools/aws.png',
        'type':'tool'
    },
    {
        'detls':'ORACLECLOUD',
        'imgsr':'tools/oci.png',
        'type':'tool'
    },
    {
        'detls':'MYSQL',
        'imgsr':'tools/mysql.png',
        'type':'tool'
    },
    {
        'detls':'JENKINS',
        'imgsr':'tools/jenkins1.png',
        'type':'tool'
    },
    {
        'detls':'GITHUB',
        'imgsr':'tools/github.png',
        'type':'tool'
    },
    {
        'detls':'XCODE',
        'imgsr':'tools/xcode.png',
        'type':'tool'
    },
    {
        'detls':'INSOMNIA',
        'imgsr':'tools/insomnia1.png',
        'type':'tool'
    },
    {
        'detls':'OLLAMA',
        'imgsr':'tools/ollama.png',
        'type':'tool'
    },
    {
        'detls':'COPILOT',
        'imgsr':'tools/copilot.png',
        'type':'tool'
    },
    {
        'detls':'CLAUDE',
        'imgsr':'tools/claude.png',
        'type':'tool'
    },
    {
        'detls':'ANTIGRAVITY',
        'imgsr':'tools/antigravity.png',
        'type':'tool'
    },
    {
        'detls':'POSTGRES',
        'imgsr':'tools/postgre.png',
        'type':'tool'
    },
]
certs = [
    {
        'detls':'OCI GEN AI PROFESSIONAL',
        'imgsr':'certs/ocigenaipro.png',
        'type':'cert',
        'url':'https://catalog-education.oracle.com/ords/certview/sharebadge?id=36F40722E2847530F7A709E3927B3DF84B55A49893740B9B04BC8A3A66CA1FC0',
    },
    {
        'detls':'OCI VECTOR SEARCH PROFESSIONAL',
        'imgsr':'certs/ocivector.png',
        'type':'cert' ,
        'url':'http://catalog-education.oracle.com/ords/certview/sharebadge?id=074910E12B1C4CE56CD164CFAC8128D941D395BE8405D4D3CC2C53B7AD98D6D3'
    },
    {
        'detls':'OCI AI ASSOCIATE',
        'imgsr':'certs/ociaiassoc.png',
        'type':'cert',
        'url':'https://catalog-education.oracle.com/ords/certview/sharebadge?id=002C7A617457F39AB133531F583C0C92A8F72CACE4D6DCE816A4EBDD26241A64'
    },
    {
        'detls':'OCI CLOUD ASSOCIATE',
        'imgsr':'certs/ocicloudassoc.png',
        'type':'cert' ,
        'url':'https://catalog-education.oracle.com/ords/certview/sharebadge?id=5E03F13EF70701FD69A9C04FA5557CE07A7ED79530649699DF9D81D4A2CD9FE0'
    },
    {
        'detls':'META FULLSTACK',
        'imgsr':'certs/fullstack.png',
        'type':'cert' ,
        'url':'https://www.credly.com/badges/3c549179-a6f4-46a7-8840-e91fd1da499d/public_url'
    },
    {
        'detls':'META REACT (JS/NATIVE)',
        'imgsr':'certs/fe.png',
        'type':'cert' ,
        'url':'https://www.credly.com/badges/70c71cc2-f5dd-4d5f-9f8c-8f4c54946423/public_url'
    },
    {
        'detls':'META DJANGO (PYTHON)',
        'imgsr':'certs/be.png',
        'type':'cert' ,
        'url':'https://www.credly.com/badges/5cddcab0-b5e0-4ebe-89c8-bcc256e0a9f0/public_url'
    },
    {
        'detls':'AWS CLOUD PRACTIONER',
        'imgsr':'certs/aws.png',
        'type':'cert' ,
        'url':'https://www.credly.com/badges/e2161c78-1e7a-4c89-902e-c92167884d98/public_url'
    },
]
def projects_view(page: ft.Page):
    async def handle_click(e):
        print('came into the handle click: ',e)
        url = e.control.data
        if url:
            await page.launch_url(url,web_popup_window_name="_blank")
    return ft.Container(
        padding=20,
        content=
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Column(
                            [
                                ft.Text(
                                    "My portfolio features a blend of professional internships and personal projects that reflect my technical versatility. My personal projects serve as a playground for refining my skills in ReactJS, React Native, Django, FastAPI, FastMCP, Flet and Python, with a particular focus on integrating Artificial Intelligence to solve real-world problems. From full-stack web applications to AI-powered chat systems, these projects demonstrate my commitment to hands-on learning and staying at the forefront of the industry.",
                                    size=16, 
                                    color="white",
                                    font_family="Titillium Web",
                                    italic=True,
                                ),
                            ]
                        ),
                        ft.Divider(height=20,color="white10"),
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.DASHBOARD, color="#e10600", size=40),
                                ft.Text(
                                    "INTERNSHIP", 
                                    size=40, 
                                    weight=ft.FontWeight.W_900, 
                                    color="white",
                                    font_family="Titillium Web Black"
                                ),
                            ],
                        ),
                        *[
                            ft.Container(
                                # 4 items per row on large screens (col=3)
                                # 2 items per row on tablets (col=6)
                                # 1 item per row on mobile (col=12)
                                col={"xs": 12, "sm": 6, "lg": 4}, 
                                padding=20,
                                bgcolor="#1e1e2c",
                                border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                                border_radius=8,
                                # Set a height to keep them uniform and "neat"
                                height=300, 
                                content=
                                ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    cpt['compn'], 
                                                    size=16, 
                                                    weight="bold", 
                                                    color="white",
                                                    max_lines=2,
                                                    overflow=ft.TextOverflow.ELLIPSIS
                                                ),
                                                ft.Text(
                                                    cpt['roles'], 
                                                    size=16, 
                                                    weight="bold", 
                                                    color=ft.Colors.WHITE_38,
                                                    max_lines=2,
                                                    overflow=ft.TextOverflow.ELLIPSIS
                                                ),
                                                ft.Text(cpt['years'], size=11, color="white54"),
                                                ft.Text(cpt['place'], size=11, color="white54"),
                                                ft.Container(height=5),
                                                ft.Text(
                                                    cpt['descr'], 
                                                    color="white70", 
                                                    size=13,
                                                    max_lines=6, # Keeps the box height consistent
                                                ),
                                            ]
                                        ),
                                        ft.Container(
                                            expand=True,
                                            border_radius=8,
                                            alignment=ft.Alignment.CENTER,
                                            content=ft.Image(src=cpt['imgsr'],width=150,height=200)
                                        ),
                                    ],
                                spacing=5)
                            )
                            for cpt in intern
                        ],
                        ft.Container(expand=True,height=20),
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.NOTES, color="#e10600", size=40),
                                ft.Text(
                                    "PROJECTS", 
                                    size=40,
                                    color="white",
                                    font_family="Titillium Web Black",
                                    weight="bold",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        *[
                            ft.Container
                            (
                                # 4 items per row on large screens (col=3)
                                # 2 items per row on tablets (col=6)
                                # 1 item per row on mobile (col=12)
                                col={"xs": 12, "sm": 6, "lg": 2}, 
                                padding=10,
                                bgcolor="#1e1e2c",
                                border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                                border_radius=3,
                                # Set a height to keep them uniform and "neat"
                                height=300, 
                                content=
                                    ft.Column
                                    (
                                            [
                                                ft.Container(
                                                    expand=True,
                                                    border_radius=8,
                                                    alignment=ft.Alignment.CENTER,
                                                    content=ft.Image(src=proj['imgsr'],width=150,height=150,border_radius=20),
                                                    data=proj.get('url') if proj.get('url') else None,
                                                    on_click=handle_click,
                                                    tooltip="View Project",
                                                ),
                                                ft.Divider(color="white10", height=20),
                                                ft.Text(
                                                    proj['title'], 
                                                    size=16, 
                                                    weight=ft.FontWeight.W_400, 
                                                    color="white",
                                                    max_lines=2,
                                                    overflow=ft.TextOverflow.ELLIPSIS,
                                                    align=ft.Alignment.CENTER
                                                ),
                                                ft.Text(
                                                    proj['types'], 
                                                    size=16, 
                                                    weight="bold", 
                                                    color=ft.Colors.WHITE_38,
                                                    max_lines=1,
                                                    overflow=ft.TextOverflow.ELLIPSIS,
                                                    align=ft.Alignment.CENTER
                                                ),
                                                ft.Container(height=5),
                                                ft.Text(
                                                    proj['descr'], 
                                                    color="white70", 
                                                    size=13,
                                                    max_lines=6, # Keeps the box height consistent
                                                    align=ft.Alignment.CENTER
                                                ),
                                            ],
                                        spacing=2,
                                    ),
                            )
                            for proj in proj
                        ],
                        ft.Container(expand=True,height=20),
                        ft.Divider(height=20,color="white10"),
                        ft.Column(
                            [
                                ft.Text(
                                    "I am deeply passionate about technology and make it a priority to stay updated with the rapidly evolving tech landscape. Whether it's exploring the latest features in modern web frameworks or diving into the potential of Generative AI, I am constantly learning and experimenting. My commitment to excellence is backed by certifications in Cloud Computing, AI, and Full-Stack Development, allowing me to build end-to-end solutions that are both modern and reliable.",
                                    size=16, 
                                    color="white",
                                    font_family="Titillium Web",
                                    italic=True,
                                ),
                            ]
                        ),
                        ft.Divider(height=20,color="white10"),
                        ft.Row(
                            [
                                ft.Icon(ft.Icons.COMPUTER, color="#e10600", size=40),
                                ft.Text(
                                    "TECHNICAL STACK", 
                                    size=40, 
                                    weight=ft.FontWeight.W_900, 
                                    color="white",
                                    font_family="Titillium Web Black"
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        *[
                            ft.Container
                            (
                                # 4 items per row on large screens (col=3)
                                # 2 items per row on tablets (col=6)
                                # 1 item per row on mobile (col=12)
                                col={"xs": 12, "sm": 6, "lg": 0.75}, 
                                padding=5,
                                bgcolor="#ffffff",
                                # border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                                border_radius=8,
                                # Set a height to keep them uniform and "neat"
                                height=50, 
                                content=
                                    ft.Column
                                    (
                                            [
                                                ft.Container(
                                                    expand=True,
                                                    border_radius=8,
                                                    alignment=ft.Alignment.CENTER,
                                                    content=ft.Image(src=proj['imgsr']),
                                                    tooltip=proj.get('detls')
                                                ),
                                            ],
                                        spacing=2,
                                    ),
                            )
                            for proj in stack
                        ],
                        # ft.Container(expand=True,height=20),
                        # ft.Row(
                        #     [
                        #         ft.Icon(ft.Icons.PAGES, color="#e10600", size=40),
                        #         ft.Text(
                        #             "CERTIFICATIONS", 
                        #             size=40, 
                        #             weight=ft.FontWeight.W_900, 
                        #             color="white",
                        #             font_family="Titillium Web Black"
                        #         ),
                        #     ],
                        #     alignment=ft.MainAxisAlignment.END,
                        # ),
                        ft.Divider(color="white10",height=2),
                        ft.Text("CERTIFICATIONS",size=20,color="white100",font_family="Titillium Web",align=ft.Alignment.CENTER),
                        *[
                            ft.Container
                            (
                                # 4 items per row on large screens (col=3)
                                # 2 items per row on tablets (col=6)
                                # 1 item per row on mobile (col=12)
                                col={"xs": 12, "sm": 6, "lg": 1}, 
                                padding=3,
                                bgcolor="#ffffff",
                                # border=ft.Border(left=ft.BorderSide(4, "#e10600")),
                                border_radius=8,
                                # Set a height to keep them uniform and "neat"
                                height=60,
                                content=
                                    ft.Column
                                    (
                                            [
                                                ft.Container(
                                                    expand=True,
                                                    border_radius=8,
                                                    alignment=ft.Alignment.CENTER,
                                                    content=ft.Image(src=proj['imgsr']),
                                                    data=proj.get('url') if proj.get('url') else None,
                                                    on_click=handle_click,
                                                    tooltip=proj.get('detls'),
                                                ),
                                            ],
                                        spacing=2,
                                    ),
                            )
                            for proj in certs
                        ],
                    ]
                )
            ]
        ),
    )
