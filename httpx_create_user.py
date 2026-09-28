import httpx

from tools.fakers import fake

payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "password": "string"
}
response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())