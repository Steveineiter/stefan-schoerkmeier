from fastapi import FastAPI

app = FastAPI(
    # TODO as soon as we deploy we have to comment those in.
    # docs_url=None,
    # redoc_url=None,
)

@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}