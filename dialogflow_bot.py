from dialogflow_v2 import SessionsClient
from dialogflow_v2.types import TextInput, QueryInput


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = TextInput(text=text, language_code=language_code)
    query_input = QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    if not response.query_result.intent.is_fallback:
        return response.query_result.fulfillment_text
