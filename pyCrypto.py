
# coding: utf-8

# ## Universidade Federal do Rio de Janeiro (UFRJ)
# ### Disciplina: EEL840
# ### Vinícius Silva Campos DRE: 113023327

# ## Implementação em python para encriptar e decriptar textos planos utilizando o algoritmo DES implementado pela biblioteca pyDES.

# ### Instalando e importando os pacotes necessários:

# In[ ]:

get_ipython().system('pip install pydes')

import pyDes
import secrets


# ### Implementação da função de encriptação.

# In[ ]:

def encrypt(file_path, output_path, key):
    """Recebe como argumento o path de um arquivo e escreve o conteúdo encriptado no arquivo especificado no argumento."""
    # Abre o arquivo.
    file = open(file_path, 'r')
    # Le o conteúdo do arquivo.
    file_content = file.read()
    # Fecha o arquivo.
    file.close()
    # Inicializando a classe que implementa o algoritmo DES.
    des = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    # Conteúdo encriptado com encode especificado como sendo utf-8.
    encrypted_content = des.encrypt(file_content.encode("utf-8"))
    # Abre o arquivo no qual deseja-se armazenar o conteúdo encriptado.
    output_file = open(output_path, 'wb')
    # Escreve o conteúdo encriptado no arquivo de saída.
    output_file.write(encrypted_content)
    # Fecha o arquivo.
    output_file.close()


# ### Implementação do função de decriptação

# In[ ]:

def decrypt(file_path, output_path, key):
    """Recebe como argumento o path do arquivo cujo conteúdo está encriptado e 
    escreve o conteúdo decriptado no arquivo especificado no argumento."""
    # Abre o arquivo.
    file = open(file_path, 'rb')
    # Le o conteúdo do arquivo.
    file_content = file.read()
    # Fecha o arquivo.
    file.close()    
    # Inicializando a classe que implementa o algoritmo DES.
    des = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    # Decripta o conteúdo do arquivo fornecido especificando que o decode deve ser utf-8.
    decrypted_content = des.decrypt(file_content).decode("utf-8")
    # Abre o arquivo no qual deseja-se armazenar o conteúdo encriptado.
    output_file = open(output_path, 'w')
    # Escreve o conteúdo encriptado no arquivo de saída.
    output_file.write(str(decrypted_content))
    # Fecha o arquivo.
    output_file.close()


# ### Especificação do conjunto de variáveis que serão utilizados para os testes abaixo.

# In[ ]:

# Cria a chave que será utilizada contendo 8 bits (exigência da biblioteca pyDES).
key = secrets.token_bytes(8)
# Path do arquivo que deverá ser encriptado.
initial_file_path = "C:\\Users\\vinic\\Documents\\Projects\\pyCrypto\\resumo-artigo.txt"
# Path do arquivo encriptado.
encrypted_file_path = "C:\\Users\\vinic\\Documents\\Projects\\pyCrypto\\encrypted.txt"
# Path do arquivo decriptado.
decrypted_file_path = "C:\\Users\\vinic\\Documents\\Projects\\pyCrypto\\decrypted.txt"


# ### Testes:

# In[ ]:

# Encriptação do arquivo.
encrypt(initial_file_path, encrypted_file_path, key)

# Decriptação do arquivo.
decrypt(encrypted_file_path, decrypted_file_path, key)

# Lê conteudo do arquivo inicial.
initial_file_content = open(initial_file_path, 'r').read()

# Lê conteudo do arquivo decriptado.
decrypted_file_content = open(decrypted_file_path, 'r').read()

assert initial_file_content == decrypted_file_content


# ## Bibliografia

# https://twhiteman.netfirms.com/des.html
