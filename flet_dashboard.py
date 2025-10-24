
import flet as ft


def main(page: ft.Page):
    page.title = "Modern Dashboard with Login"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1200
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_100
    page.spacing=0,

    name_field = ft.TextField(label="Enter your name", width=300)
    pass_field = ft.TextField(label="Enter your password", width=300, password=True, can_reveal_password=True)

    def go_home(e):
        name = name_field.value.strip().lower()
        password = pass_field.value.strip().lower()
        if name == "noman" and password == "admin":
            page.session.set("username", name)
            page.go("/home")
        else:
            page.open(ft.SnackBar(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.ERROR_OUTLINE, color="white"),
                        ft.Text("Wrong credentials!", color="white", size=16, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                bgcolor="#D32F2F",
                behavior="floating",
                margin=ft.Margin(10, 0, 10, 20),
                padding=20,
                duration=3000,
                elevation=10,
            ))
             
            page.update()

    login_page = ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Login Page")),
            ft.Container(
                ft.Column(
                    [
                        ft.Icon(name=ft.Icons.LOCK_OUTLINE, size=70, color=ft.Colors.TEAL_700),
                        ft.Text("Welcome Back!", size=25, weight=ft.FontWeight.BOLD),
                        name_field,
                        pass_field,
                        ft.ElevatedButton("Login", on_click=go_home, width=300),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                ),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
    )

    sidebar_items = [
        ("Dashboard", ft.Icons.DASHBOARD_OUTLINED),
        ("Patients", ft.Icons.PEOPLE_OUTLINE),
        ("Doctors", ft.Icons.MEDICAL_SERVICES_OUTLINED),
        ("Settings", ft.Icons.SETTINGS_OUTLINED),
        ("Logout", ft.Icons.LOGOUT_OUTLINED),
    ]

    current_section = ft.Text("Dashboard")
    selected_index = 0


    def dashboard_content():
        return ft.Column(
            [
                ft.Text("📊 Dashboard Overview", size=24, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Icon(ft.Icons.PEOPLE, size=40, color="white"),
                                    ft.Text("Patients", color="white"),
                                    ft.Text("120", size=22, weight=ft.FontWeight.BOLD, color="white"),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=ft.Colors.TEAL_400,
                            border_radius=15,
                            padding=20,
                            expand=1,
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Icon(ft.Icons.MEDICAL_SERVICES, size=40, color="white"),
                                    ft.Text("Doctors", color="white"),
                                    ft.Text("45", size=22, weight=ft.FontWeight.BOLD, color="white"),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=ft.Colors.AMBER_400,
                            border_radius=15,
                            padding=20,
                            expand=1,
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Icon(ft.Icons.MONETIZATION_ON_OUTLINED, size=40, color="white"),
                                    ft.Text("Revenue", color="white"),
                                    ft.Text("$12.5k", size=22, weight=ft.FontWeight.BOLD, color="white"),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=ft.Colors.LIGHT_GREEN_400,
                            border_radius=15,
                            padding=20,
                            expand=1,
                        ),
                    ],
                    spacing=15,
                ),
            ],
            spacing=25,
        )

    def patients_content():
        return ft.Column(
            [
                ft.Text("👥 Patients", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("List of registered patients will appear here."),
            ]
        )

    def doctors_content():
        return ft.Column(
            [
                ft.Text("🩺 Doctors", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Doctor management screen."),
            ]
        )

    def settings_content():
        return ft.Column(
            [
                ft.Text("⚙️ Settings", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Customize your system preferences here."),
            ]
        )


    def get_content(name):
        if name == "Dashboard":
            return dashboard_content()
        elif name == "Patients":
            return patients_content()
        elif name == "Doctors":
            return doctors_content()
        elif name == "Settings":
            return settings_content()
        else:
            return ft.Text("Unknown section")


    def home_view():
           
            username = page.session.get("username") or "Guest"

            def get_sidebar(update_callback):
                return ft.Container(
                    
                    ft.Column(
                        [
                            ft.Text("DR'NOM", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_800),
                            *[
                                sidebar_button(title, icon, i, update_callback)
                                for i, (title, icon) in enumerate(sidebar_items)
                            ],
                        ],
                        spacing=8,
                    ),
                    width=220,
                    padding=15,
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(blur_radius=6, color=ft.Colors.GREY_300),
                )

            def sidebar_button(title, icon, index, update_callback):
                def on_click(e):
                    nonlocal selected_index
                    selected_index = index
                    if title == "Logout":
                        page.session.clear()
                        page.go("/")
                        return
                    update_callback(title)

                return ft.Container(
                    ft.Row(
                        [
                            ft.Icon(icon, size=22, color=ft.Colors.TEAL_800),
                            ft.Text(title, size=16, weight=ft.FontWeight.W_500),
                        ],
                        spacing=10,
                    ),
                    on_click=on_click,
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.Colors.TEAL_50 if current_section.value == title else None,
                    animate=ft.Animation(200, "easeInOut"),
                )

            content_area = ft.Container(
                ft.AnimatedSwitcher(get_content(current_section.value), transition=ft.AnimatedSwitcherTransition.FADE, duration=300),
                expand=True,
                padding=25,
            )

           
            def update_content(new_title):
                current_section.value = new_title
                content_area.content = ft.AnimatedSwitcher(
                    get_content(new_title), transition=ft.AnimatedSwitcherTransition.FADE, duration=300
                )
               
                sidebar.content = get_sidebar(update_content).content
                page.update()

            sidebar = get_sidebar(update_content)

            return ft.View(
                "/home",
                [
                    ft.Row(
                        [
                            sidebar,
                            # ft.VerticalDivider(width=1, color=ft.Colors.GREY_300),
                            ft.Column(
                                [
                                    ft.Container( content=ft.Text(f"Welcome, {username.upper()} 👋", size=22, weight=ft.FontWeight.BOLD), margin=ft.Margin(top=20,left=0,right=0,bottom=0) ),
                                    ft.Divider(),
                                    content_area,
                                ],
                                expand=True,
                                spacing=15,
                            ),
                        ],
                        expand=True,
                    ),
                ],
                padding=0,         
                spacing=0,           
                
            )

    def route_change(e):
        page.views.clear()
        page.padding=0
        if page.route == "/":
            page.views.append(login_page)
        elif page.route == "/home":
            page.views.append(home_view())
        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")


ft.app(target=main)
