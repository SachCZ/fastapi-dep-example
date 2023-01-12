from fastapi import FastAPI
import app.adyen_api as adyen_api


app = FastAPI()

app.include_router(adyen_api.router)
