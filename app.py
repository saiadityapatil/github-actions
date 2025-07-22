import json
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b

def lambda_handler(event, context):
    try:
        body = json.loads(event['body']) if isinstance(event.get('body'), str) else event
    except Exception as e:
        return {"statusCode": 400, "body": json.dumps({"error": "Invalid JSON"})}

    op = body.get("operation")
    a = body.get("a")
    b = body.get("b")

    try:
        if op == "add":
            result = add(a, b)
        elif op == "subtract":
            result = subtract(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        elif op == "divide":
            result = divide(a, b)
        else:
            return {"statusCode": 400, "body": json.dumps({"error": "Invalid operation"})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
