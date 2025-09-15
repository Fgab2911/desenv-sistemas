#pesquisar como alterar e excluir registros do arquivo.txt,e criar um comentario no arquio do python com a aplicação

# Este script em Python realiza a leitura de um arquivo chamado "arquivo.txt",
# que contém registros em texto no formato "nome,idade" (um por linha).
# Ele percorre os registros para modificar e excluir determinados dados:
# - Altera a idade de "João" para 31.
# - Remove o registro de "Maria".
# - Mantém os demais registros inalterados.
# Após o processamento, o arquivo original é sobrescrito com os dados atualizados.

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

novas_linhas = []

for linha in linhas:
    nome, idade = linha.strip().split(",")

    if nome == "Maria":
        continue  # Exclui o registro da Maria
    elif nome == "João":
        novas_linhas.append(f"{nome},31\n")  # Altera a idade de João
    else:
        novas_linhas.append(linha)  # Mantém os demais registros

with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(novas_linhas)
