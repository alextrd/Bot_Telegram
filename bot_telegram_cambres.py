import telepot
import time
import sys
import sqlite3



print('bot arduino activat.')
print('esperant comandos....')

def handle(msg):
    userName = msg['from']['first_name']
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if(content_type == 'text'):
        command = msg['text']
        print('comando obtingut: %s' %command)
        
        if '/start' in command:
            bot.sendMessage(chat_id, 'Hola, '+userName+'\n'+'sóc el bot encarregat de facilitar-te les temperatures de les cambres de LaVianderia.cat SCCL'+'\n'+'Els comandos que pots fer servir són: '+'\n'+'/cambra1'+'\n'+'/cambra2'+'\n'+'/cambra3'+'\n'+'/tancar'+'\n')
            conexion = sqlite3.connect('temperatures.db')
            cursor = conexion.cursor()
            bot.sendMessage('La base de dades s`ha connectat correctament!!!')
        elif '/cambra1' in command:
            cursor.execute('SELECT * FROM registre WHERE cambra = "cambra 1" ORDER BY id DESC LIMIT 1')
            conexion.commit()
            resultat = cursor.fetchone()
            bot.sendMessage(chat_id, 'la temperatura és de: '+resultat[-1])
        elif '/cambra2' in command:
            cursor.execute('SELECT * FROM registre WHERE cambra = "cambra 2" ORDER BY id DESC LIMIT 1')
            conexion.commit()
            resultat = cursor.fetchone()
            bot.sendMessage(chat_id, 'la temperatura és de: '+resultat[-1])
        elif '/cambra3' in command:
            cursor.execute('SELECT * FROM registre WHERE cambra = "cambra 3" ORDER BY id DESC LIMIT 1')
            conexion.commit()
            resultat = cursor.fetchone()
            bot.sendMessage(chat_id, 'la temperatura és de: '+resultat[-1])
        elif '/tancar' in command:
            
            conexion.close()
            bot.sendMessage(chat_id, 'la connexió s´ha tancat correctament')
            
        else:
            bot.sendMessage(chat_id, 'ho sento, no reconeixo el comando.... Sisplau tornar a probar uns dels següents: \n/start\n/cambra1\n/cambra2\n/cambra3\n/tancar')
   
bot = telepot.Bot('API KEY')    
bot.message_loop(handle)
    
while True:
    time.sleep(20)