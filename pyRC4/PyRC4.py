
# coding: utf-8

# ## Universidade Federal do Rio de Janeiro (UFRJ)
# ### Disciplina: EEL840
# ### Vinícius Silva Campos DRE: 113023327

# ## Implementação em python para encriptar e decriptar textos planos utilizando usando RC4 disponível na biblioteca pyCryptodome (fork da biblioteca pycrypto para python 3.0+).

# ### Instalando e importando os pacotes necessários:

# In[1]:

get_ipython().system('pip install pycryptodome')

from Crypto.Cipher import ARC4
import secrets


# ### Implementação da função de encriptação.

# In[2]:

def encrypt(file_path, output_path, key, nonce):
    """Recebe como argumento o path de um arquivo e escreve o conteúdo encriptado no arquivo especificado no argumento."""
    # Abre o arquivo.
    file = open(file_path, 'r')
    # Le o conteúdo do arquivo.
    file_content = file.read()
    # Fecha o arquivo.
    file.close()    
    # Cria a cifra que será utilizada.
    cipher = ARC4.new(nonce + key)
    # Conteúdo encriptado com encode especificado como sendo utf-8.
    #encrypted_content = nonce + cipher.encrypt(file_content.encode("utf-8"))    
    encrypted_content = cipher.encrypt(file_content.encode("utf-8"))    
    # Abre o arquivo no qual deseja-se armazenar o conteúdo encriptado.
    output_file = open(output_path, 'wb')
    # Escreve o conteúdo encriptado no arquivo de saída.
    output_file.write(encrypted_content)
    # Fecha o arquivo.
    output_file.close()


# ### Implementação do função de decriptação

# In[3]:

def decrypt(file_path, output_path, key, nonce):
    """Recebe como argumento o path do arquivo cujo conteúdo está encriptado e 
    escreve o conteúdo decriptado no arquivo especificado no argumento."""
    # Abre o arquivo.
    file = open(file_path, 'rb')
    # Le o conteúdo do arquivo.
    file_content = file.read()
    # Fecha o arquivo.
    file.close()
    # Cria a cifra que será utilizada.
    cipher = ARC4.new(nonce + key)        
    # Decripta o conteúdo do arquivo fornecido especificando que o decode deve ser utf-8.
    decrypted_content = cipher.decrypt(file_content).decode("utf-8")    
    # Abre o arquivo no qual deseja-se armazenar o conteúdo encriptado.
    output_file = open(output_path, 'w')
    # Escreve o conteúdo encriptado no arquivo de saída.
    output_file.write(str(decrypted_content))
    # Fecha o arquivo.
    output_file.close()


# ### Especificação do conjunto de variáveis que serão utilizados para os testes abaixo.

# In[4]:

# Cria a chave que será utilizada contendo 16 bits.
key = secrets.token_bytes(16)
# Cria o nonce que será utilizado para troca de mensagens.
nonce = secrets.token_bytes(16)
# Path do arquivo que deverá ser encriptado.
initial_file_path = "resumo-artigo.txt"
# Path do arquivo encriptado.
encrypted_file_path = "encrypted.txt"
# Path do arquivo decriptado.
decrypted_file_path = "decrypted.txt"


# ### Testes:

# In[5]:

# Encriptação do arquivo.
encrypt(initial_file_path, encrypted_file_path, key, nonce)

# Decriptação do arquivo.
decrypt(encrypted_file_path, decrypted_file_path, key, nonce)

# Lê conteudo do arquivo inicial.
initial_file_content = open(initial_file_path, 'r').read()

# Lê conteudo do arquivo decriptado.
decrypted_file_content = open(decrypted_file_path, 'r').read()

assert initial_file_content == decrypted_file_content


# ## Bibliografia

# * http://pycryptodome.readthedocs.io/en/latest/src/cipher/arc4.html
# * https://pt.wikipedia.org/wiki/RC4
