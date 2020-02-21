from dialogflow_v2 import SessionsClient
from dialogflow_v2.types import TextInput, QueryInput

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = SessionsClient()

    session = session_client.session_path(project_id, session_id)
    # print('Session path: {}\n'.format(session))

    text_input = TextInput(text=text, language_code=language_code)
    query_input = QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    # print('=' * 20)
    # print('Query text: {}'.format(response.query_result.query_text))
    # print('Detected intent: {} (confidence: {})\n'.format(response.query_result.intent.display_name, response.query_result.intent_detection_confidence))
    # print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
    
    if response.query_result.intent.is_fallback:
        return ''
    else:
        return response.query_result.fulfillment_text

    