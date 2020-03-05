import dialogflow_v2
import json
from dotenv import load_dotenv
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('training_data_path', help='Example: questions.json')
    return parser


def create_intent(intent):
    client = dialogflow_v2.IntentsClient()
    parent = client.project_agent_path('my-chatty-bot')
    response = client.create_intent(parent, intent)


def main():
    load_dotenv()
    training_data_path = create_parser().parse_args().training_data_path
    with open(training_data_path, "r") as my_file:
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
