
import flet as ft

def main(page: ft.Page):
    page.title = "Modern Collapsible Sidebar UI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_50

    btn_items = [
        {"icon": ft.Icons.HOME_OUTLINED, "label": "Home"},
        {"icon": ft.Icons.FOLDER_OPEN_OUTLINED, "label": "Main"},
        {"icon": ft.Icons.PERSON_OUTLINED, "label": "Profiles"},
        {"icon": ft.Icons.ADMIN_PANEL_SETTINGS_OUTLINED, "label": "Admins"},
        {"icon": ft.Icons.ANALYTICS_OUTLINED, "label": "Usage"},
    ]

    selected_index = 0
    is_collapsed = False

    content_area = ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(20),
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.GREY_300),
        alignment=ft.alignment.center,
        content=ft.Text("Select a section", size=22, color=ft.Colors.GREY_700),
        padding=30,
        margin=20,
    )

    sidebar_content = ft.Column(spacing=8, alignment=ft.MainAxisAlignment.START)

    sidebar = ft.Container(
        width=220,
       
        padding=ft.Padding(15, 15, 10, 15),
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_200),
        shadow=ft.BoxShadow(blur_radius=10, spread_radius=2, color=ft.Colors.GREY_200),
        animate=ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT),
        content=sidebar_content,
    )


    collapse_btn = ft.Container(
        alignment=ft.alignment.center,
        width=32,
        height=32,
        bgcolor=ft.Colors.TEAL_600,
        border_radius=ft.border_radius.all(8),
        content=ft.Icon(ft.Icons.ARROW_BACK_IOS_NEW, color=ft.Colors.WHITE, size=18),
        ink=True,
        on_click=lambda e: toggle_sidebar(),
    )

    def make_buttons():
        sidebar_content.controls.clear()
        for i, item in enumerate(btn_items):
            is_selected = (i == selected_index)
            btn = ft.Container(
                alignment=ft.alignment.center_left,
                height=48,
                border_radius=8,
                padding=ft.Padding(12, 0, 0, 0),
                content=ft.Row(
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            item["icon"],
                            size=22,
                            color=ft.Colors.TEAL_800 if is_selected else ft.Colors.GREY_700,
                        ),
                        ft.Text(
                            item["label"],
                            size=16,
                            weight=ft.FontWeight.W_500,
                            color=ft.Colors.TEAL_800 if is_selected else ft.Colors.GREY_700,
                            opacity=1 if not is_collapsed else 0,
                            animate_opacity=300,
                        ),
                    ],
                ),
                border=ft.Border(
                    right=ft.BorderSide(
                        3,
                        ft.Colors.TEAL_600 if is_selected else ft.Colors.TRANSPARENT,
                    )
                ),
                bgcolor=ft.Colors.TEAL_50 if is_selected else ft.Colors.WHITE,
                ink=True,
                on_click=lambda e, x=i: select_button(x),
                animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            )
            sidebar_content.controls.append(btn)
        page.update()

    def select_button(index):
        nonlocal selected_index
        selected_index = index
        make_buttons()
        content_area.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(btn_items[index]["icon"], size=60, color=ft.Colors.TEAL_700),
                ft.Text(
                    f"You are viewing: {btn_items[index]['label']}",
                    size=24,
                    color=ft.Colors.TEAL_700,
                    weight=ft.FontWeight.W_600,
                ),
                ft.Text(
                    "This section is under development with stunning modern UI ✨",
                    size=16,
                    color=ft.Colors.GREY_600,
                ),
            ],
        )
        page.update()

    def toggle_sidebar():
        nonlocal is_collapsed
        is_collapsed = not is_collapsed
        sidebar.width = 70 if is_collapsed else 220
        collapse_btn.content = ft.Icon(
            ft.Icons.ARROW_FORWARD_IOS if is_collapsed else ft.Icons.ARROW_BACK_IOS_NEW,
            color=ft.Colors.WHITE,
            size=18,
        )
        make_buttons()
        page.update()


    sidebar_stack = ft.Stack(
         clip_behavior=ft.ClipBehavior.NONE,
        controls=[
            sidebar,
            ft.Container(
                alignment=ft.alignment.center_right,
                content=collapse_btn,
                right=-10,
                bottom=20,
            ),
        ]
    )

    make_buttons()

    layout = ft.Row(
        expand=True,
        controls=[sidebar_stack, content_area],
    )

    page.add(layout)

ft.app(target=main)
