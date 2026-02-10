#simulates backend request handling logic
def handle_request(request):
    if "action" not in request:
        return {"error" : "missing action"}
    if request["action"] == "ping":
        return {"status": "ok"}
    if request["action"] == "increment":
        if "value" not in request:
            return {"error" : "missing value"}
        return {"result" : request["value"] + 1}
    return {"error" : "unknown action"}

request1 = {"action" : "ping"}
request2 = {"action" : "increment", "value" : 10}
request3 = {"action" : "increment"}
request4 = {}

print(handle_request(request1))
print(handle_request(request2))
print(handle_request(request3))
print(handle_request(request4))

request5 = {"action" : "increment", "value" : -1}
print(handle_request(request5))