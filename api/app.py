from fastapi import FastAPI
from api.schemas import RecommendationRequest, RecommendationResponse

app = FastAPI(title="Retail Marketing API", version="0.1.0")


@app.get('/health')
def health() -> dict:
    return {"status": "ok"}


@app.get('/model-info')
def model_info() -> dict:
    return {"model_name": "marketing_incrementality_model", "stage": "staging", "note": "placeholder"}


@app.post('/recommend', response_model=RecommendationResponse)
def recommend(request: RecommendationRequest) -> RecommendationResponse:
    return RecommendationResponse(model_name="marketing_incrementality_model", model_version="0", recommendation=None, expected_incremental_value=None)
