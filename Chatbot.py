from bot import ChatBot
from bot.trainers import ListTrainer

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

while True:
    message = input('You:')
    reply = bot.get_response(message)
    print('Apix:', reply)
    if message.strip() == 'Bye':
        print('Apix: Bye')
        break
