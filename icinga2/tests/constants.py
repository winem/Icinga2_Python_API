class constants():
    username = "root"
    password = "icinga"
    url = "https://localhost:5665"

    TestHost_data = {
        "templates": ["generic-host"],
        "attrs": {
            "name": "test.localdomain",
            "address": "192.168.1.1",
            "check_command": "hostalive",
            "vars.os": "Linux"
        }
    }

    TestService_name = "TestService"

    TestService_data = {
        "templates": ["generic-service"],
        "attrs": {
            "check_command": "ping4",
            "check_interval": 10,
            "retry_interval": 30
        }
    }
