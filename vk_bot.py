import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import dialogflow_bot
from dotenv import load_dotenv
import os


def respond_to_an_message(event, api):
    answer = dialogflow_bot.detect_intent_texts('my-chatty-bot', event.user_id, event.text, 'ru')
    if answer:
        api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


def launch_bot(token):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            respond_to_an_message(event, api)


def main():
    load_dotenv()
    token = os.getenv('VK_TOKEN')
    launch_bot(token)


if __name__ == '__main__':
    main()
