from api.schemas import RecommendationRequest, RecommendationResponse


def test_recommendation_request_default_fields():
    payload = RecommendationRequest()
    assert payload.date is None
    assert payload.channel is None
    assert payload.audience_segment is None


def test_recommendation_response_creation():
    resp = RecommendationResponse(model_name="m", model_version="1", recommendation="increase_social", expected_incremental_value=10.5)
    assert resp.model_name == "m"
    assert resp.model_version == "1"
    assert resp.recommendation == "increase_social"
