import flet as ft
import os
from datetime import datetime

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_project_name(client_name, app_name):
    date_today = datetime.today().strftime('%Y%m%d')
    project_name = f'{client_name[:2].upper()}_{"".join(part[0].upper() for part in app_name.split())}_{date_today}'
    return project_name

def create_directory(client_name, project_name):
    base_dir = os.path.join(os.path.expanduser('~'), "PortPyTech", client_name, project_name)
    os.makedirs(base_dir, exist_ok=True)
    return f"Directory created: {base_dir}"

def generate_invoice_name(client_name, invoice_type):
    date_today_invoice = datetime.today().strftime('%d%m%Y')
    invoice_types = {
        1: "D", 2: "Q", 3: "C", 4: "I"
    }
    invoice_name = f"F{client_name[0:1]}{date_today_invoice}{invoice_types[invoice_type]}"
    return invoice_name

def main(page: ft.Page):
    def on_generate_project_name(e):
        client_name = client_name_input.value
        app_name = app_name_input.value
        project_name = generate_project_name(client_name, app_name)
        result_text.value = project_name
        result_text.update()
        
        if create_directory_checkbox.value:
            directory_message = create_directory(client_name, project_name)
            result_text.value += f"\n{directory_message}"
            result_text.update()

    def on_generate_invoice_name(e):
        client_name = client_name_input.value
        invoice_type = int(invoice_type_input.value)
        invoice_name = generate_invoice_name(client_name, invoice_type)
        result_text.value = invoice_name
        result_text.update()
    
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = ft.padding.only(100, 0, 100, 0)

    icon_widget = ft.Image(src=f"Logo.png", height=380)
    client_name_input = ft.TextField(label="Client Name")
    app_name_input = ft.TextField(label="Application Name")
    invoice_type_input = ft.TextField(label="Invoice Type (1-4)")
    invoice_summary = ft.Text(value="1. Documentación\n2. QGIS\n3. Consultoría\n4. Ingeniería")
    
    generate_project_button = ft.ElevatedButton(
        text="Generate Project Name",
        on_click=on_generate_project_name
    )
    
    generate_invoice_button = ft.ElevatedButton(
        text="Generate Invoice Name",
        on_click=on_generate_invoice_name
    )
    
    create_directory_checkbox = ft.Checkbox(label="Create Directory", value=False)
    
    project_name_container = ft.Container(
        content=ft.Column([app_name_input, generate_project_button, create_directory_checkbox]),
        border=ft.border.all(2, ft.colors.BLACK),
        border_radius=10,
        padding=10,
        margin=10
    )
    
    project_invoice_container = ft.Container(
        content=ft.Column([invoice_summary, invoice_type_input, generate_invoice_button]),
        border=ft.border.all(2, ft.colors.BLACK),
        border_radius=10,
        padding=10,
        margin=10
    )
    
    result_text = ft.Text()
    
    page.add(
        icon_widget,
        client_name_input,
        project_name_container,
        project_invoice_container,
        result_text
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
