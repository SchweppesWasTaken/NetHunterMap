# 🧭 NetHunterMap — Interactive Local Network Visualizer

**NetHunterMap** is a Python-based tool that scans your local network and builds an interactive graph of connected devices — like a star map of your Wi-Fi or LAN. It uses `nmap` for discovery, retrieves OS/MAC/vendor info, and visualizes the relationships between services and hosts.

---

## 🔍 Features

- 📡 Scan local Wi-Fi/LAN networks using `nmap`
- 🔍 Detect IP, MAC address, device vendor, and operating system (with `-O`)
- 🌐 Identify open ports and services (HTTP, SSH, Telnet, etc.)
- 🧠 Auto-visualize the network as a graph (IP ↔ Services)
- 💾 Save results in structured `JSON`
- 🧭 Clean, interactive visual output with `networkx` and `matplotlib`

---

## 🛠️ Requirements

- Python 3.8+
- `nmap` installed and available in `$PATH`
- Python dependencies:
  ```bash
  pip install -r requirements.txt

🚀 Example Usage
Fast Mode (No OS detection):

    python3 nethunter_map.py -r 192.168.0.0/24

Full Mode (with OS detection — slower, requires root):

    sudo python3 nethunter_map.py -r 192.168.0.0/24

💡 Sample Output

    A file network_scan.json will be saved with all discovered data.

    A live window will display the graph of connected devices and services.


📦 What's Inside?

    python-nmap – Nmap wrapper

    mac-vendor-lookup – Resolves vendor name from MAC address

    matplotlib, networkx – Graph rendering engine

⚠️ Notes:

    AS A SUDO IT WILL LOAD MUCH LONGER THAN WITHOUT

    MIGHT NOT WORK WITHOUT DOING ALL THE REQUIREMENTS WITHOUT SUDO (ill fix that)

    OS detection (-O) requires root privileges.

    If you're running as sudo and encounter GTK display issues, try:

    xhost +SI:localuser:root

    Graphical output requires a display. If you're running on a headless machine, consider adding --no-gui mode (planned).

🚧 Roadmap / Future Plans

    ✅ Save network graph to .png instead of just displaying it

    🔜 --no-gui CLI flag for headless scanning (CI/CD, remote, servers)

    🔜 Export to HTML / interactive map with D3.js

    🔜 Generate vulnerability recommendations (based on open ports)

    🔜 GUI version (Tkinter or PyQt)

    🔜 Telegram bot for remote command & report delivery

    🔜 ZIP report pack (graph + JSON + HTML) for audits

    🔜 Support for IPv6 and segmented VLAN scanning

🤝 Contributing

Ideas, bug reports, or pull requests are welcome! Open an issue or create a PR if you want to contribute to the galaxy of network visibility.

📜 License

MIT License. Use responsibly.



made by Schweppeswastaken when Schweppeswastaken was 14 years old.
