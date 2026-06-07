import nmap


def scan_ports(target):
    scanner = nmap.PortScanner()

    print(f"\n[+] {target} 포트 스캔 시작...\n")

    # 포트만 확인
    scanner.scan(target, arguments='-p 1-10000 -Pn')

    for host in scanner.all_hosts():
        print(f"Host: {host}")

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()

            for port in ports:
                state = scanner[host][proto][port]['state']

                print(
                    f"Port: {port} | State: {state}"
                )


if __name__ == "__main__":
    target = input("IP 입력: ")
    scan_ports(target)