# iperf_plot.py
# Reads iperf_tcp_*.csv and iperf_udp_*.csv and saves:
#   tcp_vs_distance.png
#   udp_vs_distance.png

import glob
import pandas as pd
import matplotlib.pyplot as plt

def load_tcp():
    paths = sorted(glob.glob("iperf_tcp_*m.csv"))
    if not paths:
        return pd.DataFrame(columns=["Distance","Avg"])
    frames = []
    for p in paths:
        df = pd.read_csv(p)
        df.columns = [c.strip() for c in df.columns]
        frames.append(df[["Distance","Avg"]])
    out = pd.concat(frames, ignore_index=True)
    out["Distance"] = pd.to_numeric(out["Distance"], errors="coerce")
    out["Avg"] = pd.to_numeric(out["Avg"], errors="coerce")
    return out.dropna().sort_values("Distance")

def load_udp():
    paths = sorted(glob.glob("iperf_udp_*m.csv"))
    if not paths:
        return pd.DataFrame(columns=["Distance","Avg"])
    frames = []
    for p in paths:
        df = pd.read_csv(p)
        df.columns = [c.strip() for c in df.columns]
        frames.append(df[["Distance","Avg"]])
    out = pd.concat(frames, ignore_index=True)
    out["Distance"] = pd.to_numeric(out["Distance"], errors="coerce")
    out["Avg"] = pd.to_numeric(out["Avg"], errors="coerce")
    return out.dropna().sort_values("Distance")

def plot_simple(df, title, ylabel, outfile):
    if df.empty:
        print(f"Skipping {outfile} (no data).")
        return
    plt.figure()
    plt.plot(df["Distance"], df["Avg"], marker="o")
    plt.xlabel("Distance (m)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.savefig(outfile, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"Saved {outfile}")

def main():
    df_tcp = load_tcp()
    df_udp = load_udp()
    plot_simple(df_tcp, "TCP Throughput vs Distance", "Throughput (Mbps)", "tcp_vs_distance.png")
    plot_simple(df_udp, "UDP Throughput vs Distance", "Throughput (Mbps)", "udp_vs_distance.png")

if __name__ == "__main__":
    main()
