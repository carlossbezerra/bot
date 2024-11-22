import subprocess
import json
import sys
config = {}
print("""
   ▄████████    ▄████████  ▄█   ▄█        ▄█     ▄████████                 
  ███    ███   ███    ███ ███  ███       ███    ███    ███                 
  ███    ███   ███    █▀  ███▌ ███       ███▌   ███    ███                 
  ███    ███  ▄███▄▄▄     ███▌ ███       ███▌   ███    ███                 
▀███████████ ▀▀███▀▀▀     ███▌ ███       ███▌ ▀███████████                 
  ███    ███   ███        ███  ███       ███    ███    ███                 
  ███    ███   ███        ███  ███▌    ▄ ███    ███    ███                 
  ███    █▀    ███        █▀   █████▄▄██ █▀     ███    █▀                  
                               ▀                                           
 ▄█     ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄    ▄█  ███▄▄▄▄      ▄██████▄  
███    ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███  ███▀▀▀██▄   ███    ███ 
███▌   ███    █▀    ███    ███ ███   ███   ███ ███▌ ███   ███   ███    █▀  
███▌  ▄███          ███    ███ ███   ███   ███ ███▌ ███   ███  ▄███        
███▌ ▀▀███ ████▄  ▀███████████ ███   ███   ███ ███▌ ███   ███ ▀▀███ ████▄  
███    ███    ███   ███    ███ ███   ███   ███ ███  ███   ███   ███    ███ 
███    ███    ███   ███    ███ ███   ███   ███ ███  ███   ███   ███    ███ 
█▀     ████████▀    ███    █▀   ▀█   ███   █▀  █▀    ▀█   █▀    ████████▀  
                 Faça parte da maior comunidade de igaming do Brasil, acesse:
                             www.afiliaigaming.com
""")
print("Bem-vindo à configuração do bot.\n")
api_key = input("Insira a API do bot: ")
config["api_key"] = api_key
chat_id = input("Insira a ID do canal: ")
config["chat_id"] = chat_id
affiliate_link = input("Insira o link de afiliado: ")
config["affiliate_link"] = affiliate_link
print("\nPor favor, instale as dependências do arquivo requirements.txt manualmente utilizando o seguinte comando:")
print("pip install -r requirements.txt")
try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("Dependências instaladas com sucesso.")
except Exception as e:
    print(f"Erro ao instalar dependências: {str(e)}")
    sys.exit(1)
with open('config.json', 'w') as config_file:
    json.dump(config, config_file)
print("Configuração concluída. Agora você pode rodar o seu bot.")
