# SDN Network Delay Measurement Tool

## Problem Statement
Measure and analyze latency between hosts using SDN with OpenFlow.

## Setup
1. Install os-ken: `pip install os-ken`
2. Start controller: `python -m os_ken.cmd.manager delay_controller.py --verbose`
3. Start Mininet: `sudo mn --custom topo.py --topo delaytopo --controller remote,...`

## Expected Output
- h1 → h2 (same switch): ~10ms RTT
- h1 → h3 (cross-switch): ~40ms RTT

## How to Run

**Terminal 1 — Start the controller:**
```bash
source ~/ryu-venv/bin/activate
python -m os_ken.cmd.manager delay_controller.py --verbose
```

**Terminal 2 — Start Mininet:**
```bash
sudo mn --custom topo.py --topo delaytopo \
        --controller remote,ip=127.0.0.1,port=6633 \
        --switch ovsk,protocols=OpenFlow13 \
        --link tc
```

### Test scenario 1 - Latency comparison (ping)

Same-switch vs cross-switch RTT measured using `ping -c 20`.

**Mininet CLI — ping results:**
<img width="715" height="390" alt="Screenshot 2026-04-20 at 10 51 35 AM" src="https://github.com/user-attachments/assets/260514a5-ce41-4b87-9740-47ffd2e91967" />

---

### Test scenario 2 - Throughput measurement (iperf)

Bandwidth measured between hosts on same switch and across switches using `iperf`.

**iperf output — h1 to h2 (same switch) and h1 to h3 (cross switch)**
<img width="577" height="209" alt="Screenshot 2026-04-20 at 10 21 59 AM" src="https://github.com/user-attachments/assets/466d4c5d-5d74-45b9-a13d-0c70589cd0ca" />

---

## Flow table

Flow rules installed by the controller after `pingall`, captured using:
```bash
mininet> sh ovs-ofctl -O OpenFlow13 dump-flows s1
mininet> sh ovs-ofctl -O OpenFlow13 dump-flows s2
```

**Flow table — s1 and s2:**
<img width="557" height="229" alt="image" src="https://github.com/user-attachments/assets/61c0d9a6-231a-4904-9244-a7747ce91b3c" />

---

## Wireshark / tcpdump Capture

**ICMP packets captured on inter-switch link during cross-switch ping.**

<img width="747" height="585" alt="Screenshot 2026-04-20 at 10 25 06 AM" src="https://github.com/user-attachments/assets/26dcb661-93a3-4052-9b5b-8249dccc973d" />

---

## Mininet CLI Output

**Full Mininet session showing topology creation, pingall, and test results.**
<img width="956" height="574" alt="Screenshot 2026-04-20 at 10 50 57 AM" src="https://github.com/user-attachments/assets/702f33c5-101b-4686-970c-18ef70b1fbd1" />


**Creates the topology**
<img width="954" height="508" alt="image" src="https://github.com/user-attachments/assets/aa46f226-6e40-4054-8d5e-5f4b5aae8964" />

<img width="557" height="183" alt="image" src="https://github.com/user-attachments/assets/1a60de1a-2730-405f-9320-968bc0810ed6" />


<img width="424" height="256" alt="Screenshot 2026-04-20 at 10 51 47 AM" src="https://github.com/user-attachments/assets/4af8917f-ccfa-43ab-b8c1-9f3642e1f175" />

---

## References
[1] Mininet: http://mininet.org
[2] os-ken: https://opendev.org/openstack/os-ken
[3] OpenFlow 1.3 spec
