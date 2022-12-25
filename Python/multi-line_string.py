test_dict = {"user1": "pass1", "user2": "pass2", "user3": "pass3"}
if "user1" in test_dict:
    print("user1 is in the dictionary")

if "user1" in test_dict.keys():
    print("user1 is in the dictionary keys")

test1 = (f"{test_dict['user1']}\n"
         f"{test_dict['user2']}")

print(test1)

test2 = f"""{test_dict['user1']}
{test_dict['user2']}"""

print(test2)
