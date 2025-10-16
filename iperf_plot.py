# iperf_plot.py
# Minimal EE250 Lab 5 plotter using Plotly (TCP & UDP vs Distance)

import glob
import pandas as pd
import plotly.express as px

def load_csv(pattern):
    files = sorted(glob.glob(pattern))
    data = []
    for f in files:
        df = pd.read_csv(f)
        df.columns = [c.strip() for c in df.columns]
        if "Distance" in df.columns and "Avg" in df.columns:
            data.append(df[["Distance", "Avg"]])
    if not data:
        return pd.DataFrame(columns=["Distance", "Avg"])
    out = pd.concat(data, ignore_index=True)
    out["Distance"] = pd.to_numeric(out["Distance"], errors="coerce")
    out["Avg"] = pd.to_numeric(out["Avg"], errors="coerce")
    return out.dropna().sort_values("Distance")

# Load all TCP and UDP CSVs
tcp_df = load_csv("iperf_tcp_*m.csv")
udp_df = load_csv("iperf_udp_*m.csv")

# Plot TCP
if not tcp_df.empty:
    fig_tcp = px.line(
        tcp_df,
        x="Distance",
        y="Avg",
        markers=True,
        title="TCP Throughput vs Distance",
        labels={"Avg": "Throughput (Mbps)", "Distance": "Distance (m)"}
    )
    fig_tcp.write_image("tcp_vs_distance.png")
    print("Saved tcp_vs_distance.png")

# Plot UDP
if not udp_df.empty:
    fig_udp = px.line(
        udp_df,
        x="Distance",
        y="Avg",
        markers=True,
        title="UDP Throughput vs Distance",
        labels={"Avg": "Throughput (Mbps)", "Distance": "Distance (m)"}
    )
    fig_udp.write_image("udp_vs_distance.png")
    print("Saved udp_vs_distance.png")



