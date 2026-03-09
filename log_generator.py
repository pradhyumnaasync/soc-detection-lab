from datetime import datetime
from attack_simulator import simulate_attack

def generate_log():

    attack = simulate_attack()

    log = f"{datetime.now()} | EVENT | {attack}"

    with open("logs.txt", "a") as f:
        f.write(log + "\n")

    print("Log Generated:", log)

if __name__ == "__main__":
    generate_log()