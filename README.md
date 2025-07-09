# Virtual HIL Testing with Python + CAN + UDS

This is a simulation project that mimics HIL testing using open-source tools on Ubuntu.

## ✅ Features
- Simulate UDS diagnostic requests (0x10, 0x11, 0x22)
- Send/receive CAN frames over virtual CAN (`vcan0`)
- DBC decoding with cantools
- Log messages to CSV
- Basic test automation runner

## 🧰 Technologies
- Python 3
- python-can
- cantools
- vCAN / SocketCAN
- Ubuntu

## 🚀 How to Run

```bash
# Setup vcan0
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

# Activate Python environment
source venv/bin/activate

# Run mock ECU
python3 scripts/uds_server.py

# Run UDS tester
python3 scripts/uds_tester.py
