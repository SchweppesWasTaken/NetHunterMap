
import nmap
import json
import argparse
from mac_vendor_lookup import MacLookup
import networkx as nx
import matplotlib.pyplot as plt

def scan_network(network_range):
    print(f"[+] Scanning network: {network_range}. " "Made by SchweppesWasTaken on Github")
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments='-O -T4')
    results = []
    for host in nm.all_hosts():
        data = {
            "ip": host,
            "hostname": nm[host].hostname(),
            "state": nm[host].state(),
            "mac": nm[host]['addresses'].get('mac', 'N/A'),
            "vendor": "Unknown",
            "os": nm[host]['osmatch'][0]['name'] if 'osmatch' in nm[host] and nm[host]['osmatch'] else "Unknown",
            "ports": []
        }
        if data["mac"] != 'N/A':
            try:
                data["vendor"] = MacLookup().lookup(data["mac"])
            except:
                pass
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                data["ports"].append({
                    "port": port,
                    "state": nm[host][proto][port]["state"],
                    "name": nm[host][proto][port]["name"]
                })
        results.append(data)
    return results

def visualize_network(devices):
    G = nx.Graph()
    for device in devices:
        label = f"{device['ip']}\n{device['vendor']}\n{device['os']}"
        G.add_node(label)
        for port in device['ports']:
            if int(port['port']) in [80, 443, 22, 23]:
                G.add_edge(label, f"Service:{port['name']}:{port['port']}")
    plt.figure(figsize=(14, 10))
    nx.draw(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=10)
    plt.title("NetHunter Map - Local Network")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NetHunterMap - Scan and visualize your local network.")
    parser.add_argument("-r", "--range", required=True, help="Network range to scan (e.g., 192.168.1.0/24)")
    args = parser.parse_args()
    devices = scan_network(args.range)
    with open("network_scan.json", "w") as f:
        json.dump(devices, f, indent=4)
    visualize_network(devices)
