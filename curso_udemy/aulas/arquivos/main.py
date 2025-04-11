 #? Criando arquivos com Python + Context Manager with
 #? Usamos a função open para abrir
 #? um arquivo em Python (ele pode ou não existir)
 #? Modos:
 #? r (leitura), w (escrita), x (para criação)
 #? a (escreve ao final), b (binário)
 #? t (modo texto), + (leitura e escrita)
 #? Context manager - with (abre e fecha)
 #? Métodos úteis
 #? write, read (escrever e ler)
 #? writelines (escrever várias linhas)
 #? seek (move o cursor)
 #? readline (ler linha)
 #? readlines (ler linhas)
 #? Vamos falar mais sobre o módulo os, mas:
 #? os.remove ou unlink - apaga o arquivo
 #? os.rename - troca o nome ou move o arquivo
 #? Vamos falar mais sobre o módulo json, mas:
 #? json.dump = Gera um arquivo json
 #? json.load


# caminho_arquivo = 'C:\\Users\\natan\\OneDrive\\Documentos\\Estudos\\Python\\curso_udemy\\aulas\\arquivos\\'
# caminho_arquivo += 'arquivo.txt'

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write("Linha 1\n")
#     arquivo.write("Linha 2\n")
#     arquivo.seek(0,0)
#     print(arquivo.read())
    

caminho = "C:\\Users\\natan\\OneDrive\\Documentos\\Estudos\\Python\\curso_udemy\\aulas\\arquivos\\"
caminho += "arquivo.txt"

arquivo = open(caminho, 'w')
arquivo.write("Teste 1\n")
arquivo.write("Teste 2\n")
arquivo.close()

arquivo = open(caminho, 'r')
for n, _ in enumerate(infile)
arquivo.close()
arquivo.

print(a)
