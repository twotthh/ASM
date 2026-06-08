import json
import os


def get_remediation(cve_id):
    json_path = os.path.join("data", "cve_solution.json")

    if not os.path.exists(json_path):
        return "[-] 조치 가이드 데이터베이스를 찾을 수 없습니다."

    with open(json_path, "r", encoding="utf-8") as f:
        solutions = json.load(f)

    if cve_id in solutions:
        data = solutions[cve_id]
        guide = f"\n[📢 조치 가이드 - {cve_id}]\n"
        guide += f"취약점명: {data['title']}\n"
        guide += f"위험도: {data['severity']}\n"
        guide += f"설명: {data['description']}\n"
        guide += f"대응 방안:\n{data['solution']}\n"
        return guide

    return f"[-] {cve_id}에 대한 등록된 조치 가이드가 없습니다."
