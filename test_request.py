import requests

res = requests.post(
    "https://solution-challenge-9bby.onrender.com/barcode",
    json={
        "barcode": "8801007403182",
        "disease_name": "Galactosemia"
    }
)

print(res.status_code)
print(res.json())
