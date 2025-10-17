# Lab 5

## Team Members
- Ardaan Bhatia ardaanbh@usc.edu github: ardaanbhatia7
- Kyna Rochlani rochlani@usc.edu github: kynarochlani2006

## Lab Question Answers

Answer for Question 1: 


dBm (decibel-milliwatts) is a logarithmic unit that measures power relative to one milliwatt. It’s commonly used to express signal strength.

Strong signal: around –30 dBm to –50 dBm (excellent connection)

Good signal: around –50 dBm to –67 dBm (stable and reliable)

Weak signal: around –67 dBm to –80 dBm (slow or unstable)

Very weak / unusable: below –90 dBm (likely disconnects)

Answer for Question 2: 

Different operating systems use different system utilities and command formats to display Wi-Fi information.

Linux uses the iwconfig command.

Windows uses netsh wlan show interfaces.

macOS (Darwin) uses wdutil info.
Because each command outputs text in a unique format, the program must check the OS to run the correct command and use the right regular expression to extract the signal strength.

Answer for Question 3: 

subprocess.check_output() runs a shell command from inside the Python script and waits for it to finish. It captures the command’s output (the same text that would normally appear in the terminal) and returns it as a byte string. This allows the program to read and process command results programmatically.

Answer for Question 4: 

re.search() scans through a text string to find the first location where a pattern matches. If it finds one, it returns a match object that contains the matched text and captured groups. If no match is found, it returns None. In this code, it’s used to extract numeric signal strength values from the command output.

Answer for Question 5: 

Windows reports Wi-Fi quality as a percentage (0–100%), not in dBm. To compare results across all systems, the program converts that percentage to an estimated dBm value using an approximate formula:

dBm = -100 + (quality/2)

This gives a consistent unit of measurement for signal strength regardless of OS.

Answer for Question 6: 

The standard deviation measures how much the Wi-Fi signal readings at each location varied around the average (mean) value. A smaller standard deviation means the signal was consistent over time, while a larger one means it fluctuated a lot during sampling.

From my data and the plot:

Bedroom 1 had a mean signal of about –42 dBm with a small deviation, showing a strong and stable connection.

Living room and bathroom were around –55 dBm, also fairly consistent.

Bedroom 2 and outside the apartment had weaker signals (around –60 to –70 dBm) and slightly larger error bars, meaning the connection there was less reliable.

By calculating the standard deviation, I can tell which areas have stable Wi-Fi and which experience more variation or interference, rather than relying only on average strength.

Answer for Question 7: 

A DataFrame (from the pandas library) is a two-dimensional data structure similar to a spreadsheet or SQL table, with labeled columns and rows. It’s useful because it makes it easy to organize, analyze, and visualize data—allowing operations like averaging, filtering, and plotting with minimal code.


Answer for Question 8: 

Error bars visually represent data variability—in this case, one standard deviation above and below the mean. They show how consistent the Wi-Fi signal was at each location. Longer error bars mean greater fluctuation, while shorter ones indicate a stable signal.

Answer for Question 9: 

Typically, the plot shows that signal strength decreases as you move farther from the router or through walls. Rooms separated by thick walls, floors, or metal appliances tend to have weaker signals. The living room or near-router areas usually show higher (less negative) dBm values, while bathrooms or outside areas often show lower (more negative) ones due to interference and distance. 

Answer for Question 10: 

As the distance between the transmitter and receiver increased, TCP throughput consistently decreased.

At 2 m, throughput was around 24 Mbps.

By 8 m, it dropped below 20 Mbps, and by 12 m, it fell to around 13–15 Mbps.
This shows that greater distance leads to higher signal attenuation and lower throughput due to weaker signal strength and more retransmissions.
UDP throughput, however, remained nearly constant at around 10 Mbps, since UDP doesn’t adapt its sending rate based on network conditions.

Answer for Question 11: 

Significant UDP packet loss began to appear around 10 m and beyond.
Although the UDP throughput line stays nearly flat, the actual received data rate doesn’t increase with distance indicating packets are being sent but not successfully received at longer distances due to weakened signal and interference.

Answer for Question 12: 

UDP is a connectionless protocol, meaning it sends packets without checking whether they arrive correctly or in order. It doesn’t perform retransmissions or congestion control.
In contrast, TCP is connection-oriented it acknowledges every packet, resends lost ones, and adjusts transmission speed dynamically. So when the signal weakens, TCP slows down but remains reliable, while UDP keeps transmitting at the same rate, causing more loss.

Answer for Question 13: 

If you increase UDP bandwidth to -b 100M, the sender will try to transmit data much faster likely exceeding the available channel capacity.
This causes:

Massive packet loss, as the receiver can’t process packets that quickly.

Increased jitter and unstable throughput.

Potential network congestion that could affect other traffic.
Essentially, UDP will overwhelm the link since it doesn’t throttle itself like TCP.

Answer for Question 14: 

Yes performance would differ significantly:

5 GHz Wi-Fi provides higher bandwidth and faster speeds but has shorter range and is more affected by walls and obstacles.

2.4 GHz Wi-Fi offers longer range and better wall penetration but lower throughput and more interference (since many devices use it).
So at short distances, 5 GHz would outperform 2.4 GHz; at longer distances, 2.4 GHz would maintain a more stable connection.
