import pyshark
def read_pcap(file_path):
    capture = pyshark.FileCapture(file_path)
    for packet in capture:
        print(packet)
        break

read_pcap('../data/pcap/modbus/modbus.pcap')