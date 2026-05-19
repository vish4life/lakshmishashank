import flet as ft

about_text ="""Engineering solutions for over 16 years in the Information Technology spectrum, I have developed expertise in Banking and Financial domains. For the past 5+ years, I have led high-performing development teams as a Manager, focusing on delivering robust, scalable, and secure integration solutions. My career is built on a foundation of technical excellence and strategic leadership, ensuring technology serves as a powerful enabler for financial services."""

exp = [
    {
        'title':'Manager',
        'compn':'Capgemini Canada Solutions Inc., Mississauga - Canada',
        'years':'DEC 2018 - PRESENT',
        'roles':'- Corebanking Developer & Consultant\n- Expertise in Clearing and Payments\n- Knowledge on MX messaging (ISO20022)\n- Experience in handling cross-functional teams\n- Experience in mentoring and training peers\n- Excellent communication skills with ability to translate business needs in technical features',
        'imgsr':'work/capg1.png',
    },
    {
        'title':'Senior Consultant',
        'compn':'Capgemini America, Chicago - USA',
        'years':'SEP 2016 - DEC 2018',
        'roles':'- Corebanking Developer & Consultant\n- Lead development teams in implementing Zelle (POS P2P), ACH, X9.37 (Cheques) projects\n- Successfully implemented OFAC, Balance+, Grayhair & FICO DMP integration projects\n- On-call Production support for Banking operations\n- Lead monthly install activities by coordinating between 50+ teams\n- Experience in Waterfall, Agile (Scrum, SAFe, Kanban) methodologies',
        'imgsr':'work/capg1.png',
    },
    {
        'title':'Programmer Analyst',
        'compn':'The Diligent LLC, Hoover - USA',
        'years':'MAR 2016 - SEP 2016',
        'roles':'- Lead the test strategy and implementation of NOLB\n       * PopMoney (P2P money transfer)\n       * Visa-checkout (one click payment system))',
        'imgsr':'work/dg1.png',
    },
    {
        'title':'Deputy Manager',
        'compn':'ICICI Bank Ltd, Hyderabad - India',
        'years':'SEP 2011 - DEC 2014',
        'roles':'- Lead the migration of corebanking application from 7X to 10X version\n- Product lead for Loans & EOD/BOD operations\n- Lead Data mapping & Gap analysis for Lending line of business\n- Coordinated with stakeholders, external and internal vendors to implement new features\n- Managed UAT and Business Analyst teams for the entire project\n- Developed daily status reports for Executive level stakeholders on project updates\n- Successfully integrated RTGS/NEFT systems with newer version',
        'imgsr':'work/icici1.png',
    },
    {
        'title':'Probationary Officer',
        'compn':'ICICI Bank Ltd, Bengaluru - India',
        'years':'AUG 2010 - SEP 2011',
        'roles':'- Learning & Foundations of\n       * Banking and Insurance\n       * Branch Operations and Management\n       * Banking Technology and Architecture',
        'imgsr':'work/icici1.png',
    },
    {
        'title':'Associate Analyst',
        'compn':'Dell International Services Pvt Ltd., Hyderabad - India',
        'years':'MAY 2009 - MAY 2010',
        'roles':'- Created BRD, FRD for new product launches\n- Created mockups & wireframes for IDT payment system',
        'imgsr':'work/dell.png',
    },
    {
        'title':'Analyst',
        'compn':'Wipro Ltd., Hyderabad - India',
        'years':'APR 2008 - MAY 2009',
        'roles':'- Performed UAT, Regression and Performance testing',
        'imgsr':'work/wipro1.png',
    },
]

def experience_view():
    return ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    [
                        ft.Icon(ft.Icons.WORK, color="#e10600", size=40),
                        ft.Text(
                            "WORK EXPERIENCE", 
                            size=40, 
                            weight=ft.FontWeight.W_900, 
                            color="white",
                            font_family="Titillium Web Black"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(
                    padding=20,
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
                ft.Container(height=30),
                *[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            # 1. The Year
                            ft.Text(
                                job['years'], 
                                size=16, 
                                weight="bold", 
                                color="white70",
                            ),
                            
                            # 2. Centered Vertical Line
                            ft.Container(
                                width=2,
                                height=40,
                                bgcolor="#e10600",
                            ),
                            
                            # 3. Centered Detail Box with Fixed Width
                            ft.Container(
                                width=700,  # Adjusted width for better readability
                                padding=25,
                                bgcolor="#1e1e2c",
                                border_radius=10,
                                # CORRECT WAY: Define the specific left side within ft.Border
                                border=ft.Border(
                                    left=ft.BorderSide(5, "#e10600"),
                                    top=ft.BorderSide(1, "white10"),
                                    right=ft.BorderSide(1, "white10"),
                                    bottom=ft.BorderSide(1, "white10"),
                                ),
                                content=ft.Column([
                                    ft.Row([
                                        ft.Text(job['title'], size=22, weight="bold", color="white"),
                                        ft.Container(expand=True,border_radius=8,alignment=ft.Alignment.CENTER_RIGHT,content=ft.Image(src=job['imgsr'],width=50,height=50),),
                                    ]),
                                    ft.Text(job['compn'], size=18, color="#e10600", weight="w-500"),
                                    ft.Divider(color="white10", height=20),
                                    ft.Text(job['roles'], color="white70", size=14),
                                ], spacing=5)
                            ),
                            
                            # 4. Spacing between entries
                            ft.Container(height=40),
                        ]
                    )
                    for job in exp
                ]
            ]
        )
    )