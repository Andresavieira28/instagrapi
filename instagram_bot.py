import time
from instagrapi import Client

# Substitua 'xxxxxx' e 'xxxxx' pelo seu usuário e senha do Instagram
cl = Client()
cl.login("xxxxxx", "xxxxx")

# Pegar ID da postagem a partir da URL que quer comentar
media_url = "https://www.instagram.com/"
media_id = cl.media_pk_from_url(media_url)

# Loop de comentários
try:
    while True:
        cl.media_comment(media_id, "Comentário de teste!")
        print("Comentado com sucesso!")
        time.sleep(30)  # Espera de 30 segundos entre comentários (evita bloqueio)
except KeyboardInterrupt:
    print("Bot interrompido manualmente.")
