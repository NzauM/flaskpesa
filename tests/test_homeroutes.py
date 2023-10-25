import json
from app import app

# https://circleci.com/blog/testing-flask-framework-with-pytest/

def test_homeroute():
    resp = app.test_client().get('/')
    res = json.loads(resp.data.decode('utf-8')).get("Message")
    assert res == "Karibu Sana"