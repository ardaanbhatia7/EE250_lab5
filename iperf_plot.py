# iperf_plot.py
# Generates 5 graphs (2m, 5m, 8m, 10m, 12m) showing TCP & UDP throughput across Run1–Run5

import pandas as pd
import matplotlib.pyplot as plt
import glob, re, os

def read_runs(file):
    """Reads the single data line and splits the space-separated runs."""
    with open(file, "r") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    if len(lines) < 2:
        raise ValueError(f"No data rows in {file}")
    # second line has 'distance, runs_blob, avg'
    parts = [p.strip() for p in lines[1].split(",")]
    distance = int(float(parts[0]))
    runs_blob = parts[1]
    runs = [float(x) for x in runs_blob.split() if x]
    return distance, runs

tcp_files = sorted(glob.glob("iperf_tcp_*m.csv"))

for tcp in tcp_files:
    dist = re.search(r"iperf_tcp_(\d+)m\.csv", tcp).group(1)
    udp = f"iperf_udp_{dist}m.csv"
    if not os.path.exists(udp):
        print(f"Skipping {dist}m — missing {udp}")
        continue

    tcp_dist, tcp_runs = read_runs(tcp)
    udp_dist, udp_runs = read_runs(udp)

    runs_labels = [f"Run{i}" for i in range(1, len(tcp_runs) + 1)]
    plt.figure()
    plt.plot(runs_labels, tcp_runs, marker="o", color="orange",
             label="TCP Throughput (Mbps)")
    plt.plot(runs_labels, udp_runs, marker="s", linestyle="--", color="brown",
             label="UDP Throughput (Mbps)")
    plt.title(f"TCP & UDP Throughput at {dist} m Distance")
    plt.xlabel("Test Runs")
    plt.ylabel("Throughput (Mbps)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"throughput_{dist}m.png", dpi=200)
    plt.show()
    print(f"Saved throughput_{dist}m.png")
