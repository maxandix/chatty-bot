import telegram_bot
import vk_bot 
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
VK_TOKEN = os.getenv('VK_TOKEN')


def main():
   telegram_bot.launch_bot(TELEGRAM_TOKEN)
   vk_bot.launch_bot(VK_TOKEN)


if __name__ == '__main__':
    main()