mapping = {

    "Suspicious PowerShell Execution": "T1059 Command Execution",

    "Brute Force Attempt": "T1110 Credential Access",

    "Suspicious Process Spawn": "T1055 Process Injection"

}

def map_attack(alert):

    return mapping.get(alert, "Unknown")