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


# def test_create_interaction_detects_badly_formatted_data():
#     response = client.post("/api/interactions", 
#         json={
#             "event_type": "page_view",
#             "metadata": {
#                 "page": "/dashboard",
#                 "referrer": "https://google.com",
#                 "device": "desktop",
#                 "browser": "Chrome"
#             }
#         }  
#     )  # Use TestClient

#     # should raise:
#     # raise HTTPException(
#     # status_code=422,
#     # detail="Missing required field: user_id"
#     assert response.status_code == 422

# def test_create_interaction_detects_invalid_json_format():

#     response = client.post("/api/interactions", 
#         json={ "user_id": "user_123", "event_type": 123, "metadata": "not-an-object" }
#     )  # Use TestClient

#     # should raise:
#     # raise HTTPException(
#     # status_code=422,
#     # detail="Metadata not an object"
#     assert response.status_code == 422


# # def test_missing_user_id_raises_validation_error()
# # def test_get_interactions_filters_by_user_id()