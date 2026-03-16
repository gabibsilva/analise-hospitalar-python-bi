import pandas as pd

# 1. Configurações iniciais


arquivo_entrada = 'healthcare_dataset.xlsx'
arquivo_saida = 'hospital_limpo_final.csv'

print("Iniciando o processamento dos dados...")

# 2. Carregamento dos dados
try:
    df = pd.read_excel(arquivo_entrada)
    print("Dados carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")

# 3. Tratamento e Limpeza (Data Cleaning)
# Convertendo para numérico e tratando possíveis erros de digitação na base original
df['Billing Amount'] = pd.to_numeric(df['Billing Amount'], errors='coerce')

# Correção de Escala: A base original (Kaggle) apresenta valores com erro de 12 casas decimais.
# Ajustando para valores reais dividindo por 1 trilhão (10^12).
df['Billing Amount'] = df['Billing Amount'] / 10**12

# Arredondamento para 2 casas decimais (padrão monetário)
df['Billing Amount'] = df['Billing Amount'].round(2)

# 4. Exportação
# Exportamos para CSV sem o índice (coluna de contagem lateral) para otimizar o Power BI.
df.to_csv(arquivo_saida, index=False)

print(f"Processo finalizado! Arquivo '{arquivo_saida}' gerado e pronto para o Power BI.")
