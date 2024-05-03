import os
from log_parser import parse_log_line

def load_logs(file_name: str) -> list:
    logs = []
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as file:
        for line in file:
            logs.append(parse_log_line(line.strip()))
    return logs
