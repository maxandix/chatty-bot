import dialogflow_v2
import json
from dotenv import load_dotenv


def create_intent(intent):
    client = dialogflow_v2.IntentsClient()
    parent = client.project_agent_path('my-chatty-bot')
    response = client.create_intent(parent, intent)


def main():
    load_dotenv()
    with open("questions.json", "r") as my_file:
        training_data: object = json.load(my_file)

    for name, body in training_data.items():
        intent = {'display_name': name, 'messages': [{
            "text":
                {"text": [body['answer']]}
        }], 'training_phrases': []}
        for phrase in body['questions']:
            intent['training_phrases'].append({"parts": [{"text": phrase}]})

        create_intent(intent)
        print('done')


if __name__ == '__main__':
    main()
