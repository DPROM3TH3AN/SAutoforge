# tests/test_chatbot.py

from src.chatbot import get_chatbot_response

def test_get_chatbot_response():
    prompt = "Test prompt for a smart contract"
    response = get_chatbot_response(prompt)
    # Ensure that the response is a non-empty string
    assert isinstance(response, str)
    assert len(response.strip()) > 0

def test_get_chatbot_response_contains_keywords():
    prompt = "Test prompt for a smart contract"
    response = get_chatbot_response(prompt)
    keywords = ["contract", "blockchain", "decentralized"]
    # Ensure that the response contains at least one of the keywords
    assert any(keyword in response for keyword in keywords)