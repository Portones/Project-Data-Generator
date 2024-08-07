import os
from datetime import datetime

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_client_info():
    print("Introduce los siguientes datos")
    client_name = input("Nombre del cliente: ")
    return client_name

def generate_project_name(client_name):
    app_name = input("Nombre de la aplicación: ")
    date_today = datetime.today().strftime('%Y%m%d')
    project_name = f'{client_name[:2].upper()}_{"".join(part[0].upper() for part in app_name.split())}_{date_today}'
    return project_name

def create_directory(client_name, project_name):
    base_dir = os.path.join(os.path.expanduser('~'), "PortPyTech", client_name, project_name)
    os.makedirs(base_dir, exist_ok=True)
    print(f"Directorio creado: {base_dir}")

def generate_invoice_name(client_name):
    date_today_invoice = datetime.today().strftime('%d%m%Y')
    invoice_types = {
        1: "D", 2: "Q", 3: "C", 4: "I"
    }
    invoice_type = int(input(f"1. Documentación\n2. QGIS\n3. Consultoría\n4. Ingeniería\n"))
    invoice_name = f"F{client_name[0:1]}{date_today_invoice}{invoice_types[invoice_type]}"
    return invoice_name

def main():
    clear_console()
    client_name = get_client_info()
    
    option = int(input(f"Opción?\n1. Nombre Proyecto\n2. Nombre Factura\n"))
    print("Procesando...\n")
    
    if option == 1:
        project_name = generate_project_name(client_name)
        print(project_name)
        
        create_option = int(input(f"Quiere crear el directorio?\n1. Si\n2. No\n"))
        if create_option == 1:
            create_directory(client_name, project_name)
    elif option == 2:
        invoice_name = generate_invoice_name(client_name)
        print(invoice_name)

if __name__ == "__main__":
    main()