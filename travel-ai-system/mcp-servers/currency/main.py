from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/tools/convert_currency")
async def convert_currency(data: dict):
    try:
        amount = data.get("amount")
        from_currency = data.get("from")
        to_currency = data.get("to")

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url).json()

        rate = response["rates"].get(to_currency)

        if rate is None:
            return {"error": "Invalid currency"}

        converted_amount = amount * rate

        return {
            "converted_amount": converted_amount,
            "rate": rate
        }

    except Exception as e:
        return {"error": str(e)}