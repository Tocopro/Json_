import json

data = {"key1": "value1", "key2": "values2"}
json.dumps(data)
print(json.dumps(data))

sampleJson = """{"key1": "value", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data['key2'])
