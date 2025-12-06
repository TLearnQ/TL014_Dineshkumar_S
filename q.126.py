
database = {"items": []}

def get_items():
    return database["items"]

def post_items(payload):
    if not isinstance(payload, dict):
        return {"error": "Invalid payload"}
    database["items"].append(payload)
    return {"status": "added"}

def router(request, payload=None):
    try:
        method, path = request.split()
    except ValueError:
        return {"error": "Bad request format"}

    if path != "/items":
        return {"error": "Unknown path"}

    if method == "GET":
        return get_items()
    elif method == "POST":
        return post_items(payload)
    else:
        return {"error": "Invalid method"}
