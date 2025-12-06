def classify_machine(cpu, users):
    if cpu < 20 and users < 2:
        return "Idle"
    elif cpu < 60 and users < 5:
        return "Normal"
    elif cpu < 85:
        return "Busy"
    else:
        return "Overloaded"