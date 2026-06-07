# ASM Project

### 팀 구성 및 담당 역할

* **김서현** : Log4Shell (CVE-2021-44228)
* **이솔희** : SSH User Enumeration (CVE-2018-15473)
* **맹수아** : SambaCry (CVE-2017-7494)

### 대상 취약점

* **Log4Shell (CVE-2021-44228)**
* **SSH User Enumeration (CVE-2018-15473)**
* **SambaCry (CVE-2017-7494)**

## 프로젝트 목표

1. 대상 시스템의 공격 표면(Attack Surface) 탐지
2. 서비스 및 운영체제 식별
3. CVE 기반 취약점 탐지 자동화
4. 탐지된 취약점에 대한 관리자 조치 가이드 제공
5. PoC 기반 취약 가능성 검증


## 프로젝트 구조

```text
ASM/
│
├── README.md
├── requirements.txt
│
├── docker/
│   ├── log4shell/
│   ├── sambacry/
│   └── ssh_enum/
│
├── scanner/
│   ├── port_scan.py
│   ├── service_detect.py
│   ├── os_detect.py
│   ├── nuclei_scan.py
│   ├── result_parser.py
│   └── remediation.py
│
├── poc/
│   ├── log4shell_poc.py
│   ├── sambacry_poc.py
│   └── ssh_enum_poc.py
│
├── data/
│   └── cve_solution.json
│
└── reports/
    ├── nuclei_output.txt
    ├── scan_result.json
    ├── final_report.txt
    └── log4shell_poc_result.txt
```

## 실행 순서 - Log4Shell 기준

```text
1. port_scan.py
2. service_detect.py
3. os_detect.py
4. nuclei_scan.py
5. result_parser.py
6. remediation.py
7. log4shell_poc.py
```

### 1. 포트 스캔

Nmap을 활용하여 대상 시스템의 열린 포트를 탐지

주요 기능

* 열린 포트 탐지
* 서비스 버전 탐지(`-sV`)
* 공격 표면 파악

예시:

```bash
python port_scan.py
```

출력 예시:

```text
Port: 8983 | State: open
```

### 2. 서비스 식별

열린 포트에서 실제 어떤 서비스가 동작 중인지 확인

주요 기능

* 서비스 이름 식별
* Product 정보 확인
* Version 정보 확인

예시:

```bash
python service_detect.py
```

출력 예시:

```text
Port: 8983 | Service: http | Product: Apache Solr
```

### 3. 운영체제 탐지

OS Fingerprinting을 통해 대상 시스템의 운영체제를 추정

주요 기능

* OS Fingerprinting
* Accuracy 기반 추정

예시:

```bash
python os_detect.py
```

출력 예시:

```text
추정 OS: Microsoft Windows 11
정확도: 100%
```

### 4. 취약점 탐지 (Nuclei)

오픈소스 취약점 스캐너인 Nuclei를 활용하여 CVE를 탐지

지원 취약점

* Log4Shell (CVE-2021-44228)
* SSH User Enumeration (CVE-2018-15473)
* SambaCry (CVE-2017-7494)

예시:

```bash
python nuclei_scan.py
```

출력 예시:

```text
[apache-solr-log4j-rce]
[critical]
```

결과 저장:

```text
reports/nuclei_output.txt
```

### 5. 탐지 결과 분석

Nuclei 탐지 결과를 분석하여 탐지된 CVE 정보를 추출

예시:

```bash
python result_parser.py
```

출력 예시:

```text
CVE-2021-44228
```

결과 저장:

```text
reports/scan_result.json
```

### 6. 관리자 조치 가이드 제공

탐지된 취약점에 대해 관리자 입장에서 필요한 대응 방안을 제공

주요 기능

* 취약점 이름 제공
* 위험도 제공
* 대응 방안 출력

예시:

```bash
python remediation.py
```

출력 예시:

```text
[!] CVE-2021-44228 탐지

취약점 이름: Log4Shell
위험도: Critical

권장 조치:
1. Log4j 2.17 이상으로 업데이트
2. JndiLookup.class 제거
3. 외부 LDAP/RMI 통신 차단
```

결과 저장:

```text
reports/final_report.txt
```

### 7. PoC 기반 취약 가능성 검증

탐지된 취약점이 실제로 영향을 줄 수 있는지 PoC를 통해 확인

예시:

```bash
python log4shell_poc.py
```

출력 예시:

```text
상태 코드: 200
Log4Shell 취약 가능성 존재
```

결과 저장:

```text
reports/log4shell_poc_result.txt
```
