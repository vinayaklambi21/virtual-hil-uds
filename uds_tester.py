import can
import time

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

msg = can.Message(
    arbitration_id=0x7DF,
    data=[0x02, 0x22, 0xF1, 0x90, 0x00, 0x00, 0x00, 0x00],
    is_extended_id=False
)

bus.send(msg)
print("📤 UDS request sent.")

response = bus.recv(timeout=1)
if response:
    print(f"📥 UDS response: {response.data}")
else:
    print("❌ No response received.")

