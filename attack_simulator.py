import random

attacks = [
    "powershell encoded command",
    "multiple failed login",
    "suspicious process execution"
]

def simulate_attack():
    return random.choice(attacks)

if __name__ == "__main__":
    print(simulate_attack())