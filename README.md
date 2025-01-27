# Aplicação de Ingestão e Relatório de Pedidos

## Descrição
Esta aplicação realiza a leitura de um arquivo posicional contendo informações de pedidos, processa os dados e gera um relatório com os 5 pedidos de maior valor total. O cálculo do valor total de cada pedido é baseado na fórmula:


## Estrutura do Projeto
- **`ingestao_pedidos.py`**: Código-fonte principal da aplicação.
- **`arquivo_entrada.txt`**: Arquivo de entrada posicional com dados dos pedidos.
- **`relatorio_saida.txt`**: Arquivo de saída contendo o relatório com os top 5 pedidos.
- **`README.md`**: Documentação técnica com explicações e instruções de uso.

---

## Processo de Solução

1. **Leitura do Arquivo Posicional**: 
   O programa lê cada linha do arquivo de entrada (`arquivo_entrada.txt`) e interpreta os campos com base nas posições definidas:
   - **Número do Pedido**: Posição 1 a 10.
   - **Quantidade**: Posição 11 a 15.
   - **Valor Unitário**: Posição 16 a 25.

2. **Cálculo do Valor Total**:
   Para cada linha, a aplicação calcula o valor total do pedido utilizando a fórmula mencionada.

3. **Ordenação e Seleção**:
   Os pedidos são ordenados em ordem decrescente com base no valor total. Os 5 pedidos de maior valor total são selecionados.

4. **Geração do Relatório**:
   O relatório com os top 5 pedidos é salvo em um arquivo de saída (`relatorio_saida.txt`).

---

## Decisões de Projeto e Justificativas

- **Uso de Arquivo Posicional**: O layout fixo simplifica a leitura e interpretação dos dados.
- **Uso de Python**: Escolhido por sua robustez e capacidade de manipular arquivos e realizar cálculos com eficiência.
- **Relatório em Arquivo**: Facilita o compartilhamento e a análise posterior dos resultados.

---

## Desafios Enfrentados e Soluções

1. **Interpretação do Layout Posicional**:
   - Desafio: Garantir que os campos sejam interpretados corretamente.
   - Solução: Validação rigorosa da posição e formato de cada campo no arquivo de entrada.

2. **Ordenação de Dados**:
   - Desafio: Garantir que a ordenação seja eficiente.
   - Solução: Uso da função `sorted` com chave personalizada para ordenar com base no valor total.

3. **Gerenciamento de Arquivos**:
   - Desafio: Manter consistência nos arquivos de entrada e saída.
   - Solução: Tratamento de erros para garantir a integridade dos arquivos.

---

## Possíveis Melhorias Futuras

1. **Validação de Dados**: Implementar verificações para garantir que os valores no arquivo de entrada sejam válidos (e.g., evitar valores negativos).
2. **Suporte a Outros Formatos**: Permitir a leitura de arquivos em formatos alternativos (e.g., CSV).
3. **Interface Gráfica**: Adicionar uma interface visual para facilitar a interação com o programa.
4. **Conexão com Bancos de Dados**: Armazenar os pedidos e relatórios em um banco de dados para maior escalabilidade.

---

## Instruções de Execução

1. **Pré-requisitos**:
   - Python 3.x instalado.

2. **Passos para Executar**:
   1. Clone ou baixe este repositório.
   2. Certifique-se de que o arquivo `arquivo_entrada.txt` está no mesmo diretório do script.
   3. Execute o programa com o comando:
      ```
      python ingestao_pedidos.py
      ```
   4. O relatório gerado será salvo no arquivo `relatorio_saida.txt`.

---

## Exemplo de Entrada e Saída

### Exemplo de Arquivo de Entrada (`arquivo_entrada.txt`)
