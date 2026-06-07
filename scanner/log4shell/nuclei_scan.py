import subprocess

def run_nuclei(target):
    print(f"\n[+] {target} 취약점 탐지 시작...\n")

    command = ["nuclei", "-u", target]

    if "8983" in target:
        command.extend([
            "-tags",
            "solr"
        ])

    elif "2222" in target:
        command.extend([
            "-t",
            "network/cves/2018/CVE-2018-15473.yaml"
        ])

    print("[DEBUG] 실행 명령어:")
    print(" ".join(command))
    print()

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print("[+] 탐지 결과:\n")
        print(result.stdout)

        with open("../reports/nuclei_output.txt", "w", encoding="utf-8") as f:
            f.write(result.stdout)

        print("\n[+] 결과 저장 완료 → reports/nuclei_output.txt")

    if result.stderr:
        print("[!] nuclei 메시지:")
        print(result.stderr)

    if not result.stdout and not result.stderr:
        print("[-] 탐지 결과 없음")


if __name__ == "__main__":
    target = input("URL 입력: ")
    run_nuclei(target)
