#script that mutates itself on every run to evade signature detection.
#This is the basis for polymorphic malware, which changes code structure to avoid antivirus signatures.
import random

template = """
print("Running malicious logic...")
# real payload here
"""

mutation = template.replace("Running", random.choice(["Executing", "Launching", "Starting"]))
with open("malicious_mutant.py", "w") as f:
    f.write(mutation)
