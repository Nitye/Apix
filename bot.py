import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Apix')
bot.set_trainer(ListTrainer)
langFile = os.listdir('C:/Users/dell/Desktop/Chat-Bot-main/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/')

# for file in langFile:
#     print(file)

for file in langFile:
    data = open('C:/Users/dell/Desktop/Chat-Bot-main/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+file,'r',encoding='utf-8').readlines()
    bot.train(data)

while True:
    ip = input('You: ')
    if ip.strip()!='bye' or ip.strip()!='Bye':
        reply = bot.get_response(ip)
        print("Apix: ", reply)

    elif ip=='bye' or ip ==  'Bye':
        print("I will miss you")
        break

