def analyze_log_file(filename):
    info_count = 0
    warning_count = 0
    error_count = 0

    with open(filename, "r") as file:
        for line in file:

            if "INFO" in line:
                info_count += 1

            elif "WARNING" in line:
                warning_count += 1

            elif "ERROR" in line:
                error_count += 1

    return info_count, warning_count, error_count

def get_health_status(error_count):
    if error_count == 0:
        return "NORMAL"
    return "ATTENTION"

def display_report(filename):
    info, warning, error = analyze_log_file(filename)
    total = info + warning + error
    health = get_health_status(error)

    print("================================")
    print("       LOG ANALYSIS REPORT")
    print("================================")

    print(f"INFO     : {info}")
    print(f"WARNING  : {warning}")
    print(f"ERROR    : {error}")
    print(f"\nTotal Logs: {total}")
    print(f"\nApplication Health: {health}")
    print("================================")


if __name__ == "__main__":
    display_report("app.log")