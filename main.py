import requests
import time
import json
import pandas as pd
import telebot
import bd
#token:AAGCURd3kLMArkzMRENrCrY8_mgJppoavZc
#id 1001770325808
api_key = "5801389718:AAGCURd3kLMArkzMRENrCrY8_mgJppoavZc"
chat_id= "-1001770325808"


bot = telebot.TeleBot(api_key)

#bot.send_message(chat_id, text="")

while True:
    url =('https://blaze.com/api/roulette_games/recent')

    response = requests.get(url)

    r = response.json()

    ray = []

    for x in range (len(r)):
        val = r[x]['color']
        if val == 1:
            val = 'V'
        if val == 2:
            val = 'P'
        if val == 0:
            val = 'B'
        ray.append(val)
    print(ray)
    #P = PRETO - V = VERMELHO -  B = BRANCO


    def  resultado(num):
        if num[0:6] == ['P', 'V', 'V', 'V','V','P']:
            msg = '''✅ GREEN no Preto '''
            mensagem = bot.send_message(chat_id=chat_id, text=msg)
            time.sleep(30)
           # mensagem.delete()
            return

        elif num[0:6] == ['V','V', 'V', 'V', 'V', 'V']:

            text = '''❌ LOSS '''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:7] == ['P', 'V', 'V', 'V', 'V','V','P']:
                msg = '''✅ GREEN no Gale ⚫'''
                mensagem = bot.send_message(chat_id=chat_id, text=msg)
                time.sleep(30)
                return


        elif num[0:5] == ['V', 'V', 'V', 'V','V']:
            text = ''' GALE NO PRETO ⚫
            PROTEÇÃO: BRANCO🔥⚪'''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:4] == ['V', 'V','V','V']:

            text = '''🔰 ENTRADA CONFIRMADA 🔰
            ENTRADA: PRETO ⚫️
            PROTEÇÃO: BRANCO🔥⚪️'''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:3] == ['V','V','V']:

            text = '''⚠️Possivel entrada no PRETO ⚫️⚠️
                    ️'''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:5] == ['V', 'P', 'P', 'P','P']:

            text = '''✅ GREEN no VERMELHO 🔴'''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:6] == ['P', 'P', 'P', 'P', 'P', 'P']:
            text = '''❌ LOSS '''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:7] == ['V', 'P', 'P', 'P', 'P','P','V']:
            msg = '''✅ GREEN no Gale 🔴'''
            mensagem = bot.send_message(chat_id=chat_id, text=msg)
            time.sleep(30)
            return

        elif num[0:5] == ['P','P', 'P', 'P','P']:
            text = '''GALE NO VERMELHO 🔴
            PROTEÇÃO: BRANCO🔥⚪'''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:4] == ['P', 'P','P','P']:

            text = '''🔰 ENTRADA CONFIRMADA 🔰
            ENTRADA: VERMELHO 🔴
            PROTEÇÃO: BRANCO🔥⚪️'''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return

        elif num[0:3] == ['P','P','P']:

            text = '''⚠️ Possivel entrada no VERMELHO 🔴⚠️
               ️'''
            url_base = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(30)
            return



    resultado(ray)

    time.sleep(5)