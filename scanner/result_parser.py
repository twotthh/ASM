import json


def parse_result():
    try:
        with open("../reports/nuclei_output.txt", "r", encoding="utf-8") as f:
            data = f.read()

        detected = []

        print("\n[+] 탐지 결과 분석 시작...\n")

        # Log4Shell
        if "apache-solr-log4j-rce" in data:
            detected.append({
                "cve": "CVE-2021-44228",
                "name": "Log4Shell",
                "severity": "Critical",
                "solution": [
                    "Log4j 2.17 이상으로 업데이트",
                    "JndiLookup.class 제거",
                    "외부 LDAP/RMI 통신 차단"
                ]
            })

        # SSH User Enumeration
        if "CVE-2018-15473" in data:
            detected.append({
                "cve": "CVE-2018-15473",
                "name": "SSH User Enumeration",
                "severity": "Medium",
                "solution": [
                    "OpenSSH 최신 버전 업데이트",
                    "인증 실패 메시지 통일",
                    "로그인 시도 모니터링"
                ]
            })

        # SambaCry
        if "CVE-2017-7494" in data:
            detected.append({
                "cve": "CVE-2017-7494",
                "name": "SambaCry",
                "severity": "Critical",
                "solution": [
                    "Samba 최신 버전 업데이트",
                    "쓰기 가능한 공유 디렉터리 제한",
                    "외부 SMB 접근 제한"
                ]
            })

        if detected:
            print("[+] 탐지된 취약점:")

            for item in detected:
                print(f"- {item['cve']}")

            with open(
                "../reports/scan_result.json",
                "w",
                encoding="utf-8"
            ) as f:
                json.dump(
                    detected,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            print("\n[+] 결과 저장 완료 → reports/scan_result.json")

        else:
            print("[-] 탐지된 취약점 없음")

    except FileNotFoundError:
        print("[-] nuclei_output.txt 파일이 없습니다.")


if __name__ == "__main__":
    parse_result()