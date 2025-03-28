clients = [
    " Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
    " Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
    "luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
    " ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURARAMOS",
    "carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
    "alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
    "patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
    "MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
    "SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
    "Damián Castillo ", None, "", " "
]

def clean_clients(clients):
    """Limpia el listado de clientes."""
    cleaned_clients = []
    for client in clients:
        if client and client.strip() :  # Ignorar valores nulos o vacíos
            cleaned_client = client.strip().title()  # Eliminar espacios y formatear
            if cleaned_client not in cleaned_clients:  # Evitar duplicados
                cleaned_clients.append(cleaned_client)
    return cleaned_clients

# Limpiar la lista de clientes
cleaned_clients = clean_clients(clients)

# Mostrar la lista limpia
print(cleaned_clients)