import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    test_email = "teststudent@mergington.edu"
    activity = "Chess Club"

    # Unregister in case already present
    client.post(f"/activities/{activity}/unregister", params={"email": test_email})

    # Sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": test_email})
    assert resp.status_code == 200
    assert f"Signed up {test_email}" in resp.json()["message"]

    # Duplicate signup should fail
    resp_dup = client.post(f"/activities/{activity}/signup", params={"email": test_email})
    assert resp_dup.status_code == 400

    # Unregister
    resp_unreg = client.post(f"/activities/{activity}/unregister", params={"email": test_email})
    assert resp_unreg.status_code == 200
    assert f"Unregistered {test_email}" in resp_unreg.json()["message"]

    # Unregister again should fail
    resp_unreg2 = client.post(f"/activities/{activity}/unregister", params={"email": test_email})
    assert resp_unreg2.status_code == 404

def test_signup_activity_full():
    activity = "Photography Club"
    # Fill up the activity
    for i in range(12):
        email = f"fulltest{i}@mergington.edu"
        client.post(f"/activities/{activity}/signup", params={"email": email})
    # Try to sign up one more
    resp = client.post(f"/activities/{activity}/signup", params={"email": "overflow@mergington.edu"})
    assert resp.status_code == 400
    assert "Activity is full" in resp.json()["detail"]
