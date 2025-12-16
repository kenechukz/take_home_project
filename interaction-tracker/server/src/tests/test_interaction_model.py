from src.main import app
from fastapi.testclient import TestClient

# client = TestClient()

def test_addition():
    """Test that 1 + 1 equals 2"""
    result = 1 + 1
    assert result == 2



# test interaction creation 
def test_create_interaction_return_201_and_object():  # pytest function
    with TestClient(app=app) as client:
        response = client.post(
            "/api/interactions",
            json={
                "user_id": "user_001",
                "event_type": "page_view",
                "metadata": {"page": "/dashboard"}
            },
        )

    assert response.status_code == 201
    data = response.json() 
    assert isinstance(data, dict) 


def test_create_interaction_detects_badly_formatted_data():
    with TestClient(app=app) as client:
        response = client.post("/api/interactions", 
            json={
                "event_type": "page_view",
                "metadata": {
                    "page": "/dashboard",
                    "referrer": "https://google.com",
                    "device": "desktop",
                    "browser": "Chrome"
                }
            }  
        )  # Use TestClient

    # should raise:
    # raise HTTPException(
    # status_code=422,
    # detail="Missing required field: user_id"
    assert response.status_code == 422

def test_create_interaction_detects_invalid_type():
    """In this test, event_type is of type integer when it should be enum, also metadata is not a object"""
    with TestClient(app=app) as client:
        response = client.post("/api/interactions", 
            json={ "user_id": "user_123", "event_type": 123, "metadata": "not-an-object" }
        )
    assert response.status_code == 422


def test_get_interactions_filters_by_user_id():
    with TestClient(app=app) as client:
        response = client.get("/api/interactions?user_id=user_001")
    assert response.status_code == 200

def test_get_interactions_filters_by_event_type():
    with TestClient(app=app) as client:
        response = client.get("/api/interactions?event_type=click")
    assert response.status_code == 200

def test_get_interactions_filters_by_user_id_and_event_type():
    with TestClient(app=app) as client:
        response = client.get("/api/interactions?user_id=user_001&event_type=page_view")
    assert response.status_code == 200


def test_stats_summary_returns_200():
    with TestClient(app=app) as client:
        response = client.get("/api/interactions/stats")

    assert response.status_code == 200


