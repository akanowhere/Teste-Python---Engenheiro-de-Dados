import os

def parse_line(line):
    """
    Processa uma linha do arquivo posicional.
    
    Args:
        line (str): Linha do arquivo.
    
    Returns:
        dict: Dados do pedido com número, quantidade e valor unitário.
    """
    numero_pedido = int(line[0:10])  # Posição 1-10
    quantidade = int(line[10:15])  # Posição 11-15
    valor_unitario = int(line[15:25]) / 100  # Posição 16-25 (convertido para decimal)
    valor_total = quantidade * valor_unitario
    return {
        "numero_pedido": numero_pedido,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "valor_total": valor_total
    }

def process_file(file_path):
    """
    Processa o arquivo posicional para calcular os valores totais dos pedidos.

    Args:
        file_path (str): Caminho do arquivo de entrada.
    
    Returns:
        list: Lista de dicionários com os dados processados.
    """
    pedidos = []
    with open(file_path, "r") as file:
        for line in file:
            pedido = parse_line(line.strip())
            pedidos.append(pedido)
    return pedidos

def generate_report(pedidos, output_path):
    """
    Gera um relatório com os 5 pedidos de maior valor total.
    
    Args:
        pedidos (list): Lista de pedidos processados.
        output_path (str): Caminho do arquivo de saída.
    """
    # Ordena os pedidos pelo valor total, em ordem decrescente
    pedidos_ordenados = sorted(pedidos, key=lambda x: x["valor_total"], reverse=True)
    top_pedidos = pedidos_ordenados[:5]

    # Escreve o relatório
    with open(output_path, "w") as file:
        file.write("Relatório: Top 5 Pedidos por Valor Total\n")
        file.write("=======================================\n")
        for i, pedido in enumerate(top_pedidos, 1):
            file.write(
                f"{i}. Número do Pedido: {pedido['numero_pedido']}, "
                f"Quantidade: {pedido['quantidade']}, "
                f"Valor Unitário: {pedido['valor_unitario']:.2f}, "
                f"Valor Total: {pedido['valor_total']:.2f}\n"
            )

def main():
    # Arquivos de entrada e saída
    input_file = "input.txt"
    output_file = "output.txt"

    if not os.path.exists(input_file):
        print(f"Erro: Arquivo de entrada '{input_file}' não encontrado.")
        return

    # Processa o arquivo de entrada
    pedidos = process_file(input_file)

    # Gera o relatório
    generate_report(pedidos, output_file)

    print(f"Relatório gerado com sucesso: {output_file}")

if __name__ == "__main__":
    main()
