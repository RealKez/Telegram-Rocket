with open("messages.txt", "r", encoding="utf-8") as file:
    messages = [line.strip() for line in file if line.strip()]
