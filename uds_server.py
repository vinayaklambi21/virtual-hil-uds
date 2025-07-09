import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
print("🔧 ECU UDS server started... Waiting for requests")

while True:
    msg = bus.recv()
    if msg.arbitration_id == 0x7DF and msg.data[1] == 0x22:
        response = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x62, msg.data[2], 0x12, 0x34, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(response)
        print(f"🟢 Responded to UDS request: {msg.data}")

