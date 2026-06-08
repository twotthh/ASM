import subprocess
import os


def run_nuclei_ssh(target_ip, port):
    target = f"{target_ip}:{port}"
    print(f"[*] Nuclei 종합 스캐너 구동 중... 타겟: {target}")

    output_path = os.path.join("reports", "nuclei_output.txt")

    command = [
        "nuclei",
        "-target", target,
        "-tags", "ssh",
        "-t", "network/cve/2018/CVE-2018-15473.yaml",
        "-jsonl",
        "-o", output_path,
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e:
        try:
            backup_command = [
                "nuclei",
                "-target", target,
                "-tags", "ssh",
                "-jsonl",
                "-o", output_path,
            ]
            result = subprocess.run(backup_command, capture_output=True, text=True, check=True)
            return result.stdout
        except Exception as e:
            print(f"[-] Nuclei 실행 중 오류 발생: {e}")
            return ""
