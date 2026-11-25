# Poder de compra e cesta básica

Meu primeiro projeto de análise de dados em Python.

## Pergunta

O poder de compra do brasileiro caiu?

## Dados utilizados

- Cesta básica de Belo Horizonte (DIEESE / SGS 7481)
- Salário mínimo (SGS 1619)
- IPCA mensal (SGS 433)

## Ferramentas

- Python
- Pandas
- Matplotlib

## Metodologia

1. Leitura dos dados da cesta básica.
2. Coleta do IPCA pela API do Banco Central.
3. Ajuste dos valores da cesta para reais de junho de 2025.
4. Coleta da série do salário mínimo.
5. Cálculo do indicador:

```python
cestas_por_salario = salario_minimo / valor_cesta_bh
```

Esse indicador mostra quantas cestas básicas podem ser compradas com um salário mínimo.

## Resultados

### Cesta básica em valores reais

A cesta básica de Belo Horizonte custava R$ 95,17 em janeiro de 1998. Corrigindo pela inflação (IPCA), esse valor equivale a aproximadamente R$ 481,77 em reais de junho de 2025.

### Poder de compra

- Janeiro de 1998: aproximadamente 1,26 cestas por salário mínimo.
- Junho de 2025: aproximadamente 2,09 cestas por salário mínimo.

Os resultados sugerem que o poder de compra medido pela quantidade de cestas básicas aumentou no longo prazo. Entretanto, o indicador atingiu níveis mais elevados por volta de 2018-2019 e apresentou queda nos anos seguintes, seguida de recuperação parcial.

## Limitações

- A análise utiliza Belo Horizonte como cidade-proxy.
- O cálculo utiliza o salário mínimo bruto.
- A série da cesta básica possui um mês ausente (maio de 2021).
- A série publicada no SGS foi descontinuada em junho de 2025.
- Ainda será investigado o possível impacto do recálculo da cesta básica de Belo Horizonte divulgado pelo DIEESE.

## Aprendizados

Durante o projeto pratiquei:

- Consumo de APIs
- Manipulação de dados com Pandas
- Merge de tabelas
- Séries temporais
- Ajuste por inflação
- Visualização de dados com Matplotlib
- Uso de Git e GitHub