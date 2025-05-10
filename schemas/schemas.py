def individual_serial(todo)->dict:
    return {
        "id" : str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "status": todo["status"]
    }

def list_of_serials(todos) -> list:
    return [individual_serial(todo) for todo in todos]