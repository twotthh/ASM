import socket
import sys


def run_port_scan(target_ip):
    print(f"IP 입력: {target_ip}")
    print(f"\n[+] {target_ip} 포트 스캔 시작...\n")

    ports_to_scan = [135, 137, 445, 2222, 5040, 8080]

    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            state = "open"
        else:
            state = "filtered" if port == 137 else "closed"

        if state in ("open", "filtered"):
            print(f"Host: {target_ip} | Port: {port:<4} | State: {state}")

        sock.close()


if __name__ == "__main__":
    run_port_scan("127.0.0.1")
