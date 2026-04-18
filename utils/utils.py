def parse_advice(text):
    sections = {
        "Budget": "",
        "Savings": "",
        "Debt": "",
        "Investment": "",
        "Goal": ""
    }

    current = None

    for line in text.split("\n"):
        line = line.strip()

        if line.upper().startswith("BUDGET"):
            current = "Budget"
        elif line.upper().startswith("SAVINGS"):
            current = "Savings"
        elif line.upper().startswith("DEBT"):
            current = "Debt"
        elif line.upper().startswith("INVESTMENT"):
            current = "Investment"
        elif line.upper().startswith("GOAL"):
            current = "Goal"
        elif current and line:
            sections[current] += line + "\n"

    return sections