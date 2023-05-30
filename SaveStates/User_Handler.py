import json

path = "sessions/"

def saveUserData():
    test_data = {
        "users": [
            {
                'email': 'test@tester.com',
                'pass': 'worldseasiestpass',
            },
            {
                'email': 'johndoe@tester.com',
                'pass': 'worldshardestpass5369955690489t579ehbdshidy879hbdfzhvdfuihbs89aebh',
            },
        ]
    }

    json_data = json.dumps(test_data, indent=2)

    with open(f"{path}testdata.json", 'w') as data:
        data.write(json_data)

