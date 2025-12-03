import sys, json, threading

def reverse_text(args):
    text = args.get("text", "")
    return text[::-1]

def send(id, result=None, error=None):
    reply = {"jsonrpc": "2.0", "id": id}
    if error:
        reply["error"] = error
    else:
        reply["result"] = result
    sys.stdout.write(json.dumps(reply) + "\n")
    sys.stdout.flush()

for line in sys.stdin:
    try:
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        id = req.get("id")

        if method == "tools/list":
            send(id, {
                "tools": [
                    {
                        "name": "reverse_text",
                        "description": "Reverses a string",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"}
                            },
                            "required": ["text"]
                        }
                    }
                ]
            })

        elif method == "tools/call":
            tool = params.get("name")
            args = params.get("arguments", {})

            if tool == "reverse_text":
                send(id, {"text": reverse_text(args)})
            else:
                send(id, None, {"message": "Unknown tool"})

    except Exception as e:
        send(None, None, {"message": str(e)})
