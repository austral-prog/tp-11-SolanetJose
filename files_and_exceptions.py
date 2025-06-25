def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    result = {}
    with open(filename) as f:
        content = f.read().strip()
        if content:
            sales = content.split(';')
            for sale in sales:
                if sale:
                    product, amount = sale.split(':')
                    amount = float(amount)
                    if product not in result:
                        result[product] = []
                    result[product].append(amount)
    return result


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
        for producto, ventas in data.items():
        total = sum(ventas)
        promedio = total / len(ventas)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
    pass
