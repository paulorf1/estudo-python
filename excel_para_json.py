import pandas as pd
import json

def converter_excel_para_json(caminho_excel, caminho_json, nome_aba=0):
    try:
        # Lê o arquivo Excel na aba especificada
        df = pd.read_excel(caminho_excel, sheet_name=nome_aba)
        
        # Converte o DataFrame do pandas para uma lista de dicionários.
        dados = df.to_dict(orient='records')
        
        # Salva a lista de dicionários em um arquivo JSON.
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        
        print(f"Sucesso! O arquivo '{caminho_excel}' foi convertido para '{caminho_json}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_excel}' não foi encontrado. Verifique se o caminho está correto.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# --- Exemplo de uso ---
if __name__ == "__main__":
    # Use o caminho completo do seu arquivo Excel.
    # A letra 'r' antes da string garante que o Python interprete as barras corretamente (só mudar onde está 'teste' para o nome do arquivo)
    caminho_completo_excel = r'C:\Users\Paulo\Desktop\Estudo Python\curso_python\teste.xls'
    
    # Define o nome e o local do arquivo JSON de saída.
    # O arquivo JSON será salvo na mesma pasta do seu Excel.
    caminho_completo_json = r'C:\Users\Paulo\Desktop\Estudo Python\curso_python.json'
    
    # Chama a função para iniciar a conversão
    converter_excel_para_json(caminho_completo_excel, caminho_completo_json)