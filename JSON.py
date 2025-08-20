'''Converting Python to JSON'''
# import json 
# data = {"name": "km_abro", "age:": 19, "city": "Sukkur"}
# json_data = json.dumps(data)
# print(json_data)
# print(type(json_data))

'''Converting JSON to Python'''
# import json 
# json_str = '{"name": "km_abro", "age": 19, "city": "Sukkur"}'
# py_data = json.loads(json_str)
# print(py_data)
# print(type(py_data))

'''Parse and display key-value pairs from a JSON string.'''
# import json
# data = '''
# {
#   "name": "km_abro",
#   "age": 19,
#   "city": "Sukkur"
# }
# '''

# info = json.loads(data)
# for i in info:
#     print(i,": ", info[i])
# print(info)

'''Parse and display nested JSON data.'''
# import json

# json_data = '''
# {
#   "person": {
#     "name": "km_abro",
#     "location": {
#       "city": "Sukkur",
#       "zip": 65200
#     },
#     "skills": ["Python", "HTML", "CSS"]
#   }
# }
# '''

# data = json.loads(json_data)
# print(data["person"]["location"]["city"])
# print(data["person"]["skills"][1])
