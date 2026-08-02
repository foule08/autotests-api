import json

json_data = """
{
  "name": "Иван",
  "age": 30,
  "is_student": true,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "address": {
    "city": "Moscow",
    "zip": "101000"
  }
}
"""
parsed_data = json.loads(json_data)

print(parsed_data['courses'])

data = {
"name": "Alex",
  "age": 25,
  "is_student": True,
}
json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", "r", encoding="utf-8") as f:
    read_data = json.load(f)
    print(data)

with open("json_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)