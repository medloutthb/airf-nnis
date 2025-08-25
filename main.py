from typing import Optional

from fastapi import FastAPI

from fastapi import FastAPI, HTTPException
from faker import Faker

app = FastAPI()
fake = Faker()

# Predefined dict of existing users
users = {
    "6734674111": {"date_naissance": "1995-08-25", "sexe": "M"},
    "5842881428": {"date_naissance": "2000-01-10", "sexe": "F"},
}


@app.get("/personne/{nni}")
def get_user_by_nni(nni: str):
    if not (nni.isdigit() and len(nni) == 10):
        raise HTTPException(status_code=400, detail="nni not exist")

    # If exists in dict → return it
    if nni in users:
        return {"nni": nni, **users[nni]}

    # Otherwise → generate fake data
    return {
        "nni": nni,
        "date_naissance": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
        "genre": fake.random_element(elements=["M", "F"])
    }
