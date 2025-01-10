from data import EventLog
import csv
import json
from dataclasses import asdict
#import logging



#logging.basicConfig(level=logging.DEBUG)

class Parser:

    def __init__(self):
        self.event = EventLog
        self.event_logs = []
        #logging.debug("Parser initialized")

    def parse_file(self, filename: str) -> None:
        #logging.debug(f"Opening file: {filename}")
        with open(filename, mode = 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            next(csv_reader)
            for line in csv_reader:
                #logging.debug(f"Processing line: {line}")
                if len(line) == 4:
                    event = EventLog(date=line[0], event=line[1], user=line[2], status=line[3])
                    self.event_logs.append(event)
        
        #logging.debug(f"Parsed events: {self.event_logs}")

    
    def to_json(self) -> None:
        
        grouped_data = {}

        for log in self.event_logs:
            name = log.user
            if name not in grouped_data:
                grouped_data[name] = []
            log_dict = asdict(log)  
            log_dict.pop('user', None) 
            grouped_data[name].append(log_dict)
            
        #logging.debug(f"JSON output: {grouped_data}")
        return json.dumps(grouped_data, indent = 4)
        
