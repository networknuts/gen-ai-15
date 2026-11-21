sample_dict = {"role":"user","content":"hello, my name is john"}

user_data = {"name": "john", "age": 33}

user_data_extra = {
    "name": "jane",
    "age": 31,
    "experience": 8,
    "location": "India"
}

data_list = ["networknuts","india","python","ai"]
#print(data_list[0])

complex_dict = {
    "timestamp": "17:25:00",
    "permissions": ["read","write","execute"],
    "info": {"name":"john","location":"India"}
}

print(complex_dict['info']['location'])