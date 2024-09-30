import json


values_file_name = input()

tests_file_name = input()

report_file_name = input()

with open(values_file_name, "r") as values_file:
    values_json = values_file.read()
    values_data = json.loads(values_json)
    # print(values_data)

with open(tests_file_name, "r") as tests_file:
    tests_json = tests_file.read()
    tests_data = json.loads(tests_json)
    # print(tests_data)


 # Matches ID in Tests and Values
 # fills in the blanks in Tests
 # then removes set value from Values
def check_id(t_dict, v_dict):
    for index_1 in range(len(v_dict)):
        if t_dict["id"] == v_dict[index_1]["id"]:
           t_dict["value"] = v_dict[index_1]["value"]
           # print("id: " + str(v_dict[index_1]["id"])) # Prints out matched ID
           del v_dict[index_1]["value"]


# Recursive function that digs into nesting file
def new_nesting(t_dict):
    for index_2 in range(len(t_dict)):
        check_id(t_dict[index_2], values_data["values"])
        if t_dict[index_2].get('values', None):
            new_nesting(t_dict[index_2]['values'])


# Initial call for recursion
new_nesting(tests_data["tests"])


# print(tests_data)

with open(report_file_name, "w") as report_file:
    report_json = json.dumps(tests_data, indent = 2)
    report_file.write(report_json)

# print(report_json)
input()