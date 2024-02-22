## Heurística gulosa com Python

Este repositório contém um código em Python para resolver o problema da Mochila (Knapsack Problem) utilizando duas heurísticas diferentes: uma gulosa pelo lucro e outra gulosa pela eficiência.

### Como utilizar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório em seu ambiente local.
3. Certifique-se de ter um arquivo de dados `dados.txt` seguindo o formato descrito abaixo.
4. Execute o código Python `mochila.py`.
5. O programa mostrará os resultados das duas abordagens para resolver o problema da mochila.

### Formato do arquivo de dados (`dados.txt`)

O arquivo de dados `dados.txt` deve seguir o seguinte formato:

```
N, CAP
id1, peso1, valor1
id2, peso2, valor2
...
idN, pesoN, valorN
```

Onde:
- `N` é o número de itens disponíveis.
- `CAP` é a capacidade máxima da mochila.
- Cada linha subsequente representa um item, contendo:
  - `id` é o identificador único do item.
  - `peso` é o peso do item.
  - `valor` é o valor do item.

### Exemplo de arquivo de dados (`dados.txt`)

```
5, 10
1, 2, 4
2, 3, 5
3, 5, 7
4, 7, 8
5, 1, 3
```

### Execução do código

Para executar o código, abra o terminal, navegue até o diretório do projeto e execute o seguinte comando:

```
python busca_gulosa.py
```

### Resultado

O programa exibirá a tabela de dados, seguida pelos resultados da heurística gulosa pelo lucro e pela eficiência, mostrando o peso total, lucro total e os itens selecionados para a mochila em cada caso.
