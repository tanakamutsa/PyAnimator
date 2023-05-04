import json

class Framework:
    def __init__(self, json_source_file:str):
        self.header = dict()
        self.payload = list()

        with open(json_source_file, 'r') as f:
            source_data = json.loads(f.read())
            self.header = source_data['metadata']
            self.payload = source_data['payload']
            
        for instruction in self.payload: pass

class Standard:
    def __init__(self, json_source_file:str):
        pass

class Component:
    def __init__(self, json_source_file:str):
        pass

def read_string(payload_instruction:str) -> any:
    return