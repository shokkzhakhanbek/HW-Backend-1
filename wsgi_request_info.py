import json

def application(environ, start_response):
    method = environ.get("REQUEST_METHOD", "")
    path = environ.get("PATH_INFO", "")
    protocol = environ.get("SERVER_PROTOCOL", "")

    if method == "GET" and path == "/info":
        payload = {
            "method": method,
            "url": path,
            "protocol": protocol,
        }
        body = json.dumps(payload).encode("utf-8")

        start_response("200 OK", [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ])
        return [body]

    body = b"Not Found"
    start_response("404 Not Found", [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ])
    return [body]