import pandas as pd
from datetime import datetime

usuarios = [
    {
        "id": 1,
        "nome": "Pedro",
        "curso": "Python",
        "nivel": "Iniciante"
    },
    {
        "id": 2,
        "nome": "Maria",
        "curso": "Data Science",
        "nivel": "Intermediário"
    },
    {
        "id": 3,
        "nome": "Lucas",
        "curso": "Machine Learning",
        "nivel": "Avançado"
    }
]

print("Dados extraídos com sucesso!")

def gerar_mensagem(usuario):
    return (
        f"Olá {usuario['nome']}! 🚀 "
        f"Você está evoluindo no curso de {usuario['curso']} "
        f"no nível {usuario['nivel']}. Continue estudando!"
    )

for usuario in usuarios:
    usuario["mensagem"] = gerar_mensagem(usuario)
    usuario["data_processamento"] = datetime.now().strftime("%d/%m/%Y %H:%M")

print("Dados transformados com sucesso!")

df = pd.DataFrame(usuarios)

df.to_csv("usuarios_processados.csv", index=False)

print("Arquivo CSV gerado com sucesso!")

print("\nResultado Final:")
print(df)