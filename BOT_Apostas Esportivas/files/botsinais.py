from datetime import datetime, timedelta
import telebot
import random
from pytz import timezone
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
print('''
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
                                                                           
''')
def iniciar_bot(api_key):
    try:
        bot = telebot.TeleBot(token=api_key)
        return bot
    except Exception as e:
        print(f"Erro ao iniciar o bot: {e}")
        return None

def enviar_mensagem_telegram(bot, chat_id, mensagem, imagem_path, affiliate_link):
    try:
        with open(imagem_path, 'rb') as imagem_file:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("⚽️APOSTE AQUI!⚽️", url=affiliate_link))
            
            bot.send_photo(chat_id, imagem_file, caption=mensagem, reply_markup=markup, parse_mode='Markdown')
        
        print("Mensagem enviada com sucesso! Hehe :)")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def main():
    # Carregar configurações do arquivo config.json
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)

    api_key = config_data.get('api_key', '')
    chat_id = config_data.get('chat_id', '')
    affiliate_link = config_data.get('affiliate_link', '')

    print(f"API Key: {api_key}")
    print(f"Chat ID: {chat_id}")
    print(f"Affiliate Link: {affiliate_link}")

    bot = iniciar_bot(api_key)

    if bot:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tz = timezone('America/Sao_Paulo')

        bot_message = '''
🔥 *ATENÇÃO! ANÁLISES INICIADAS!* 🔥

*Passo a passo para tomar a melhor decisão:*

✅ *1°:* Cadastre-se na plataforma indicada para garantir as melhores ODD's.
✅ *2°:* Deposite na plataforma. 
✅ *3°:* Aguarde as análises.
✅ *4°:* Garanta seu *lucro* com *gerenciamento*.

💙 Lembrando que a plataforma dobra o seu primeiro depósito.

👇 Promoção válida somente no link abaixo: 👇🏻
'''

        imagem_path = os.path.join(script_dir, 'inicio.png')
        enviar_mensagem_telegram(bot, chat_id, bot_message, imagem_path, affiliate_link)

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.playscores.com/scanner-futebol-online/ao-vivo')

        mensagens_enviadas = []

        sleep(120)

        while True:
            sleep(5)
            jogos = driver.find_elements(By.TAG_NAME, 'app-fixture-list-line')

            for jogo in jogos:
                lista = jogo.text.split('\n')
                try:
                    tempo = int(lista[0].replace("'", ''))
                    if (35 <= tempo <= 40) or (75 <= tempo <= 85):
                        if tempo < 45:
                            t = '1'
                        else:
                            t = '2'
                        lista_inf = lista[1:-1]
                        inf = [lista_inf[i:i+2] for i in range(0, len(lista_inf), 2)]
                        controle_mensagens = f'{inf[0][0]} x {inf[0][1]}{t}'
                        if (float(inf[5][0]) >= 0.0 or float(inf[5][1]) >= 0.0) and controle_mensagens not in mensagens_enviadas:

                            mensagem = f'''
✅ *ANÁLISE INICIADA*

⚽️ *JOGO:* {inf[0][0]} x {inf[0][1]}

📊 *ESTATÍSTICAS*

🕐 *Tempo:* {tempo} min
🔢 *Placar:* {inf[1][0]} - {inf[1][1]}
⛳️ *Escanteios:* {inf[10][0]} - {inf[10][1]}
✅ *Chutes ao gol:* {inf[11][0]} - {inf[11][1]}
❌ *Chutes fora do gol:* {inf[12][0]} - {inf[12][1]}
🟨 *Cartão Amarelo:* {inf[15][0]} - {inf[15][1]}
🟥 *Cartão Vermelho:* {inf[14][0]} - {inf[14][1]}
🎯 *Appm ult. 10 min:* {inf[6][0]} - {inf[6][1]}
🎯 *Appm Jogo:* {inf[5][0]} - {inf[5][1]}

🤑 *Tome a melhor decisão e lucre* 👇
'''
                            imagem_path = os.path.join(script_dir, 'sinal.png')
                            enviar_mensagem_telegram(bot, chat_id, mensagem, imagem_path, affiliate_link)
                            mensagens_enviadas.append(controle_mensagens)
                            
                except Exception as e:
                    print(f"Erro ao processar jogo (relaxa, erro normal): {e}")
                    pass
            sleep(60)

if __name__ == "__main__":
    main()
