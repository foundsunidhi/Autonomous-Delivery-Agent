import csv, matplotlib.pyplot as plt, os
# Read results/results.csv
csv_path = os.path.join("results", "results.csv")
rows = []
with open(csv_path, newline='') as cf:
    reader = csv.DictReader(cf)
    for r in reader:
        rows.append(r)
# prepare data
maps = sorted(list(set(r["map"] for r in rows)))
algos = sorted(list(set(r["algo"] for r in rows)))
# cost comparison per map
for m in maps:
    xs, ys = [], []
    for a in algos:
        rec = next((r for r in rows if r["map"]==m and r["algo"]==a), None)
        xs.append(a)
        ys.append(float(rec["cost"]) if rec and rec["cost"] not in ("inf","") else 0)
    plt.figure()
    plt.bar(xs, ys)
    plt.title(f"Path cost on {m}")
    plt.xlabel("Algorithm")
    plt.ylabel("Cost")
    plt.savefig(f"results/cost_{m}.png")
    plt.close()

# time comparison aggregated
for m in maps:
    xs, ys = [], []
    for a in algos:
        rec = next((r for r in rows if r["map"]==m and r["algo"]==a), None)
        xs.append(a)
        ys.append(float(rec["time"]) if rec and rec["time"] not in ("inf","") else 0)
    plt.figure()
    plt.bar(xs, ys)
    plt.title(f"Runtime on {m}")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (s)")
    plt.savefig(f"results/time_{m}.png")
    plt.close()

# nodes comparison
for m in maps:
    xs, ys = [], []
    for a in algos:
        rec = next((r for r in rows if r["map"]==m and r["algo"]==a), None)
        xs.append(a)
        ys.append(float(rec["nodes"]) if rec and rec["nodes"] not in ("inf","") else 0)
    plt.figure()
    plt.bar(xs, ys)
    plt.title(f"Nodes expanded on {m}")
    plt.xlabel("Algorithm")
    plt.ylabel("Nodes expanded")
    plt.savefig(f"results/nodes_{m}.png")
    plt.close()

print("Plots created in results/")
