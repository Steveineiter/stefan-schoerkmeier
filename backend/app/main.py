from fastapi import FastAPI
# from app.self_hosted_machine_learning import models as self_hosted_machine_learning_models  # TODO needed as soon as we have a DB
from app.self_hosted_machine_learning.router import self_hosted_machine_learning_router
app = FastAPI(
    # TODO as soon as we deploy we have to comment those in.
    # docs_url=None,
    # redoc_url=None,
)

# TODO add in full product
# app.add_middleware()

# self_hosted_machine_learning.Base.metadata.create_all(bind=engine)  # TODO needed as soon as we have a DB
app.include_router(self_hosted_machine_learning_router)

@app.get("/healthy")
def health_check():
    return {"status": "healthy"}