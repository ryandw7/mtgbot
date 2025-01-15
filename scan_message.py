
def scan_message(message):
   
    queries = []
    start_bracket = None
    if '{' in message and '}' in message:
        for i, char in enumerate(message):
            if char == '{' and start_bracket is None:
                start_bracket = i
        
            if char == '}':
                if start_bracket is not None:
                    queries.append(message[start_bracket+1:i])
                    start_bracket = None
    print(queries)
    return queries

