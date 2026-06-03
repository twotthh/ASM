import json

def remediation_guide():
    try:
        with open("../reports/scan_result.json", "r", encoding="utf-8") as f:
            cve_data = json.load(f)

        print("\n[+] 관리자 조치 가이드\n")

        report_text = "=== ASM 취약점 조치 보고서 ===\n\n"

        if not cve_data:
            print("[-] 탐지된 CVE가 없습니다.")
            return

        for cve in cve_data:

            print(f"[!] {cve['cve']} 탐지")
            print(f"취약점 이름: {cve['name']}")
            print(f"위험도: {cve['severity']}")
            print("권장 조치:")

            report_text += f"[+] {cve['cve']}\n"
            report_text += f"취약점 이름: {cve['name']}\n"
            report_text += f"위험도: {cve['severity']}\n"
            report_text += "권장 조치:\n"

            for idx, solution in enumerate(cve["solution"], start=1):
                print(f"{idx}. {solution}")

                report_text += f"{idx}. {solution}\n"

            print()

            report_text += "\n"

        with open(
            "../reports/final_report.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(report_text)

        print("[+] 보고서 저장 완료 → reports/final_report.txt")

    except FileNotFoundError:
        print("[-] scan_result.json 파일이 없습니다.")


if __name__ == "__main__":
    remediation_guide()