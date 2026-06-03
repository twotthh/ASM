import nmap


def detect_service(target):
    scanner = nmap.PortScanner()

    print(f"\n[+] {target} 서비스 식별 시작...\n")

    try:
        scanner.scan(target, arguments='-sV -p 1-10000 -Pn')

        for host in scanner.all_hosts():
            print(f"Host: {host}")

            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()

                for port in ports:
                    port_info = scanner[host][proto][port]

                    if port_info['state'] == 'open':
                        service = port_info.get('name', 'unknown')
                        product = port_info.get('product', '')
                        version = port_info.get('version', '')

                        print(
                            f"Port: {port} | "
                            f"Service: {service} | "
                            f"Product: {product} | "
                            f"Version: {version}"
                        )

    except Exception as e:
        print(f"오류 발생: {e}")


if __name__ == "__main__":
    target = input("IP 입력: ")
    detect_service(target)