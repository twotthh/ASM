import requests

def log4shell_check(target):
    print(f"\n[+] {target} Log4Shell 취약점 확인 시작...\n")

    try:
        response = requests.get(
            f"{target}/solr/admin/cores",
            timeout=5
        )

        print("[+] 요청 전송 완료")
        print(f"상태 코드: {response.status_code}")

        result_text = "[+] Log4Shell PoC 결과\n"
        result_text += f"Target: {target}\n"
        result_text += f"Status Code: {response.status_code}\n\n"

        if response.status_code == 200:
            print("[!] Solr 응답 확인됨")
            print("[!] Log4Shell 취약 가능성 존재")

            result_text += "[!] Solr 응답 확인됨\n"
            result_text += "[!] Log4Shell 취약 가능성 존재\n"

        else:
            print("[-] 취약점 확인 실패")
            result_text += "[-] 취약점 확인 실패\n"

        with open(
            "../reports/log4shell_poc_result.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(result_text)

        print("\n[+] 결과 저장 완료 → reports/log4shell_poc_result.txt")

    except Exception as e:
        print(f"[-] 오류 발생: {e}")


if __name__ == "__main__":
    target = input(
        "URL 입력 (예: http://127.0.0.1:8983): "
    )
    log4shell_check(target)
