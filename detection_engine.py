def detect(log):

    if "powershell" in log:
        return "Suspicious PowerShell Execution"

    if "failed login" in log:
        return "Brute Force Attempt"

    if "process execution" in log:
        return "Suspicious Process Spawn"

    return None


def analyze_logs():

    alerts = []

    with open("logs.txt") as f:
        logs = f.readlines()

    for log in logs:

        result = detect(log)

        if result:
            alerts.append((log.strip(), result))

    return alerts


if __name__ == "__main__":

    alerts = analyze_logs()

    for alert in alerts:
        print(alert)