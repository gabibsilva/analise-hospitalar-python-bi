# Análise de Dados Hospitalares: Integrando Python & Power BI
![Dashboard do Projeto](BI%20projeto%201.png)
## Sobre o Projeto
Este projeto demonstra o ciclo completo de um analista de dados: desde a identificação de um erro crítico na base de dados até a visualização estratégica para tomada de decisão.

## O Desafio
A base de dados utilizada apresentava um erro de escala na coluna de faturamento (`Billing Amount`), onde os valores estavam na casa dos quadrilhões. Isso inviabilizava a análise direta no Power BI devido ao consumo excessivo de memória e erros de processamento.

## Solução com Python (Pandas)
Utilizei Python para realizar o tratamento prévio dos dados:
* **Conversão de Tipos:** Garantia de que valores numéricos fossem tratados corretamente.
* **Correção de Escala:** Divisão matemática para ajustar os valores para a realidade financeira.
* **Otimização:** Exportação para um formato CSV limpo, facilitando a ingestão pelo Power BI.

## Dashboard Power BI
O resultado final é um dashboard interativo que explora:
* **Faturamento por Especialidade:** Identificação das áreas mais rentáveis.
* **Perfil do Paciente:** Idade média e distribuição de gênero.
* **Análise de Seguros:** Comparativo de arrecadação por operadora de saúde.

## Como Executar
1. Execute o script `limpeza_dados.py` para gerar o arquivo tratado.
2. Abra o arquivo `.pbix` no Power BI Desktop.
