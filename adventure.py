import json

with open("stats.json") as f: 
    d = json.load(f)
    HP = d["health"]
    ATCK = d["attack"]

def damageTaken(enemyDmg):
    HP = HP - enemyDmg
    with open("stats.json", "w") as f:
        json.dump(HP, f)

input("Press any key to exit...")
sys.exit()