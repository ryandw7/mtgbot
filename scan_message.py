import requests

def scan_message(message):

    queries = []
    start_bracket = None
    if '{' and '}' in message:
        for i in range(len(message)):
            if message[i] == '{' and start_bracket == None:
                start_bracket = i
        
            if message[i] == '}':
                if start_bracket:
                    queries.append(message[start_bracket+1:i])
                    start_bracket = None

        return queries
