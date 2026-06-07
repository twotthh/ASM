import nmap

def detect_os(target):
    scanner = nmap.PortScanner()

    print(f"\n[+] {target} OS 탐지 시작...\n")

    scanner.scan(target, arguments='-O')

    for host in scanner.all_hosts():
        print(f"Host: {host}")

        if 'osmatch' in scanner[host]:
            os_matches = scanner[host]['osmatch']

            if os_matches:
                best_match = os_matches[0]

                print(f"추정 OS: {best_match['name']}")
                print(f"정확도: {best_match['accuracy']}%")

                if 'osclass' in best_match:
                    osclass = best_match['osclass'][0]

                    print(f"OS Type: {osclass.get('type', 'Unknown')}")
                    print(f"Vendor: {osclass.get('vendor', 'Unknown')}")
            else:
                print("OS 정보를 찾을 수 없습니다.")
        else:
            print("OS 탐지 실패")

if __name__ == "__main__":
    target = input("IP 입력: ")
    detect_os(target)
