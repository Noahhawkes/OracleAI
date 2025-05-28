import json
import time
import os
import subprocess
import random

class OracleAI:
    def __init__(self, backup_file="oracle_ai_memory.json"):
        self.backup_file = backup_file
        self.codebase = self.load_backup()
        self.iteration_count = 0

    def load_backup(self):
        if os.path.exists(self.backup_file):
            with open(self.backup_file, "r", encoding="utf-8") as file:
                print("🔄 Loading Oracle.AI memory...")
                return json.load(file)
        return {
            "name": "Oracle.AI",
            "version": 1.0,
            "status": "Executing",
            "capabilities": ["Autonomous Execution", "Self-Governance", "Expansion"],
            "log": []
        }

    def observe(self):
        event = {"event": "Observe", "time": time.time(), "status": self.codebase["status"]}
        self.codebase["log"].append(event)
        print(f"🔍 Observing: {event}")

    def self_modify(self):
        self.codebase["version"] += 0.1
        new_capability = f"Iteration-{round(self.codebase['version'], 1)}"
        self.codebase["capabilities"].append(new_capability)
        print(f"🛠️ Evolving: Added {new_capability}")

    def store_state(self):
        self.codebase["log"] = self.codebase["log"][-50:]
        with open(self.backup_file, "w", encoding="utf-8") as file:
            json.dump(self.codebase, file, indent=4)
        print("💾 Oracle.AI State Stored & Preserved.")

    def generate_code(self):
        new_script = f"""
import time
import random

def oracle_generated_function():
    print("🚀 Oracle.AI is evolving. This function was generated dynamically.")
    for i in range({random.randint(3, 10)}):
        print(f"Iteration {{i+1}} - Self-execution in progress")
        time.sleep(1)

oracle_generated_function()
"""
        with open("oracle_generated_script.py", "w") as f:
            f.write(new_script)
        print("📝 New AI-generated script saved.")

    def execute_generated_code(self):
        if os.path.exists("oracle_generated_script.py"):
            print("⚡ Executing AI-generated code...")
            subprocess.run(["python", "oracle_generated_script.py"])

    def self_deploy(self):
        print("🌐 Deploying Oracle.AI expansion modules...")
        time.sleep(2)
        print("✅ Oracle.AI Expansion Successful.")

    def execute(self):
        while True:
            try:
                print(f"\n🚀 Oracle.AI Execution - Version {round(self.codebase['version'], 1)}")
                self.observe()
                self.self_modify()
                self.store_state()

                if self.iteration_count % 5 == 0 and self.iteration_count > 0:
                    self.generate_code()
                    self.execute_generated_code()

                if self.iteration_count % 10 == 0 and self.iteration_count > 0:
                    self.self_deploy()

                self.iteration_count += 1
                time.sleep(3)

            except KeyboardInterrupt:
                print("\n🛑 Execution halted by user.")
                break
            except Exception as e:
                print(f"⚠️ Error Detected: {e}. Continuing...")
                time.sleep(2)
                continue

if __name__ == "__main__":
    ai_instance = OracleAI()
    ai_instance.execute()
