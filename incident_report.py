from detection_engine import analyze_logs
from mitre_mapper import map_attack

def generate_report():

    alerts = analyze_logs()

    for log, alert in alerts:

        mitre = map_attack(alert)

        print("\n=== INCIDENT REPORT ===")

        print("Log:", log)

        print("Alert:", alert)

        print("MITRE Technique:", mitre)

        print("Recommended Action: Investigate system activity")


if __name__ == "__main__":
    generate_report()