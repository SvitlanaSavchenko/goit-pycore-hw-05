import re

def parse_log_line(line: str) -> dict:
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$"
    match = re.match(pattern, line)
    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3),
        }
    else:
        raise ValueError("Invalid log line format")