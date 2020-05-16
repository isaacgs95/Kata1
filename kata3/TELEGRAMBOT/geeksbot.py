from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater("reghererh")

    updater.start_polling()

    #Capturamos señales  de parada
    updater.idle()

main()