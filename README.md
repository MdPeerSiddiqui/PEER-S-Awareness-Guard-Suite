# PEER'S Awareness Guard Suite: Social Engineering Training & Human Risk Assessment

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Standard](https://img.shields.io/badge/NIST-SP%20800--50-red.svg?style=for-the-badge&logo=nist)](https://csrc.nist.gov/)
[![Compliance](https://img.shields.io/badge/ISO%2FIEC%2027001-Control%20A.6.3-orange.svg?style=for-the-badge)](https://www.iso.org/)
[![CIS Controls](https://img.shields.io/badge/CIS%20Controls-v8%20Control%2014-blue.svg?style=for-the-badge)](https://www.cisecurity.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-6%2F6%20Passed-brightgreen.svg?style=for-the-badge)](tests/test_awareness_engine.py)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows-black.svg?style=for-the-badge&logo=linux)](https://www.kali.org/)

> **Day 11 Cybersecurity Internship Deliverable**  
> **Company:** Sqrock IT Solutions  
> **Specialization:** Social Engineering & Authentication Security Simulations Using Python  
> **Developer:** Mohammed Peer Siddiqui  
> **Repository:** [https://github.com/MdPeerSiddiqui/PEER-S-Awareness-Guard-Suite](https://github.com/MdPeerSiddiqui/PEER-S-Awareness-Guard-Suite)

---

## 📌 Executive Overview

Modern cybersecurity architectures universally recognize that technical perimeters (firewalls, secure email gateways, and endpoint detection agents) cannot prevent an employee from willingly disclosing corporate credentials, executing disguised attachments, or authorizing fraudulent wire transfers over the telephone. Building and maintaining an active, resilient **"Human Firewall"** represents the #1 defense against social engineering.

**PEER'S Awareness Guard Suite v2.5** is an enterprise-grade interactive training, assessment, and human risk profiling engine developed for **Day 11** of the Sqrock IT Solutions Cybersecurity Internship. It delivers:
1. **Interactive Scenario-Based Assessment:** Evaluates candidates across **12 multi-vector real-world attack scenarios** (Phishing, Vishing, Smishing, USB drops, Watering Holes, Impersonation, Tailgating, Shoulder Surfing, MFA Push Fatigue, and BEC fraud).
2. **Just-in-Time Pedagogical Feedback:** Provides immediate tactical breakdowns for every question, pinpointing the attacker's psychological trigger (Authority, Urgency, Scarcity, Fear) and reinforcing correct incident escalation.
3. **Threat Susceptibility Indexing (TSI) & 4-Tier Risk Taxonomy:** Computes standardized employee resilience scores, classifies personnel into actionable risk tiers (Elite Defender, Vigilant, Vulnerable, High-Risk), and exports structured audits aligned with **NIST SP 800-50** and **CIS Controls v8 Control 14**.

```
+========================================================================+
|             PEER'S AWARENESS GUARD SUITE v2.5 - ARCHITECTURE           |
+========================================================================+
|                                                                        |
|  [Candidate Employee / Assessment Cohort]                             |
|          |                                                             |
|          v                                                             |
|  [Awareness Guard Interactive CLI Assessment Core]                     |
|          |                                                             |
|   +------+----------------------------------------------------------+  |
|   | 12 Multi-Vector Scenario-Based Evaluation Bank                  |  |
|   |                                                                 |  |
|   |  * Q01: Homoglyphic Email Phishing & Urgency Trigger            |  |
|   |  * Q02: Removable Media Physical Baiting & USB Drop             |  |
|   |  * Q03: Vishing & Pretexting IT Helpdesk Authority             |  |
|   |  * Q04: Smishing Package Delivery Lure (.xyz TLD)               |  |
|   |  * Q05: Watering Hole Compromise & Drive-by Download            |  |
|   |  * Q06: LinkedIn Recruiter Lure & Macro-Enabled Attachment      |  |
|   |  * Q07: Physical Access Tailgating & Turnstile Piggybacking    |  |
|   |  * Q08: Shoulder Surfing & Public Airport Privacy Controls      |  |
|   |  * Q09: MFA Fatigue & Authenticator Push Bombing Defense        |  |
|   |  * Q10: Business Email Compromise (BEC) & Whale Baiting         |  |
|   |  * Q11: Quid Pro Quo Tech Survey & Gift Card Baiting           |  |
|   |  * Q12: Zero-Penalty Incident Escalation & SOC Reporting        |  |
|   |                                                                 |  |
|   | Real-Time Just-in-Time Feedback & Threat Susceptibility Index   |  |
|   |   1. Instant Pedagogical Explanations (Psychological Levers)    |  |
|   |   2. Resilience Percentage & Threat Susceptibility (TSI %)      |  |
|   |   3. 4-Tier Risk Classification (Elite to High-Risk Liability)  |  |
|   |   4. Multi-Department Cohort Benchmarking Analytics             |  |
|   |   5. Persistent Audit Reports (JSON & Text Certificates)        |  |
|   +-----------------------------------------------------------------+  |
+========================================================================+
```

---

## 🛡️ Core Capabilities

1. **Comprehensive Scenario Bank (`questions/question_bank.json`)**
   - 12 production-grade scenario questions covering all core social engineering vectors from Weeks 1 and 2.
   - Each scenario provides 4 realistic decision paths, an unambiguous correct answer, and an in-depth educational rationale.

2. **Immediate Just-In-Time Educational Feedback**
   - Eliminates delayed score delivery. Immediately exposes the underlying psychological manipulation (e.g., artificial deadlines, power gradients, curiosity triggers) to build lasting cognitive muscle memory.

3. **Threat Susceptibility Indexing (TSI) & Enterprise Risk Tiers**
   - Quantifies employee vulnerability using the formula: `TSI = 100.0 - Resilience Percentage`.
   - Formally categorizes personnel into four operational tiers:
     - **Tier 1 (90% - 100%): Cyber Defender (Elite)** — Exemplary vigilance; qualified as Security Champions.
     - **Tier 2 (75% - 89%): Aware & Vigilant** — Satisfies corporate baseline; low risk profile.
     - **Tier 3 (50% - 74%): Vulnerable (Retraining Required)** — Moderate susceptibility; 30-day micro-training assigned.
     - **Tier 4 (< 50%): High-Risk Liability** — Severe vulnerability; triggers supervisor escalation and access review.

4. **Multi-Department Benchmark Simulation**
   - Built-in simulation tool evaluating cohort resilience across Executive C-Suite, DevOps Engineering, Finance & Payroll, Human Resources, and New Interns.
   - Computes organizational phish-prone percentages and directs remedial training resources where needed most.

5. **Structured Audit Persistence**
   - Saves complete assessment histories to `score_reports/awareness_score_report.json` and human-readable certificates (`score_reports/awareness_score_report.txt`).

---

## 📂 Repository Structure

```
PEER-S-Awareness-Guard-Suite/
├── awareness_engine.py           # Interactive CLI training engine & department benchmark suite
├── requirements.txt              # Core project dependencies (colorama, reportlab, pillow)
├── LICENSE                       # MIT License
├── README.md                     # Technical documentation & usage guide
├── policy/
│   └── security_awareness_policy.md # Formal enterprise human risk management policy (NIST SP 800-50)
├── questions/
│   └── question_bank.json        # 12 multi-vector scenario questions with educational keys
├── score_reports/
│   ├── awareness_score_report.json # Persistent candidate score ledger
│   └── awareness_score_report.txt  # Formal candidate completion certificate
├── tests/
│   └── test_awareness_engine.py  # 6-point automated PyUnit verification suite
├── scripts/
│   ├── generate_terminal_screens.py # Headless PIL terminal screenshot generator
│   └── generate_day11_pdf.py     # ReportLab multi-page executive report compiler
└── reports/
    ├── Day11_SE_Awareness_Report_Sqrock_MdPeerSiddiqui.pdf # 7-page executive lab report
    └── screenshots/              # High-fidelity terminal evidence
        ├── 01_kali_init_banner.png
        ├── 02_master_menu.png
        ├── 03_interactive_quiz.png
        ├── 04_score_report_certificate.png
        ├── 05_department_benchmark.png
        └── 06_github_repo_overview.png
```

---

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher
- Git
- Kali Linux, Ubuntu, Debian, or Windows 10/11

### 2. Clone the Repository
```bash
git clone https://github.com/MdPeerSiddiqui/PEER-S-Awareness-Guard-Suite.git
cd PEER-S-Awareness-Guard-Suite
```

### 3. Create and Activate Virtual Environment
```bash
# On Linux / macOS / Kali:
python3 -m venv .venv
source .venv/bin/activate

# On Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Execution & Usage Guide

Launch the master interactive console:
```bash
python awareness_engine.py
```

### Operational Modes:
- **`[1] Take Interactive Awareness Assessment`**  
  Guides the candidate through the 12-scenario exam with live feedback, assigns a Risk Tier, and generates an official completion certificate.
- **`[2] Run Multi-Department Benchmark Simulation`**  
  Simulates cohort examination across 5 corporate business units, calculating mean resilience and organizational phish-prone percentages.
- **`[3] Inspect Detailed Candidate Score Reports`**  
  Queries and displays candidate records stored in the persistent JSON reporting ledger.
- **`[4] View Complete Question Bank & Educational Defense Keys`**  
  Lists all 12 scenario vectors and their corresponding attack vectors.
- **`[5] Display Employee Risk Tier Matrix & Phish-Prone Scoring`**  
  Presents the formal scoring breakdown, TSI thresholds, and remedial requirements.
- **`[6] Display Enterprise Security Awareness & Culture Blueprint`**  
  Outlines continuous micro-learning methodologies and non-punitive reporting principles aligned with NIST SP 800-50.

---

## 🧪 Automated Unit Verification

A comprehensive 6-point test suite is included in `tests/test_awareness_engine.py`:

```bash
python -m unittest tests/test_awareness_engine.py -v
```

### Test Suite Results:
| Test Method | Target Component | Status |
| :--- | :--- | :---: |
| `test_question_bank_structure` | Schema & Mandatory Key Validation | `PASSED` |
| `test_perfect_score_calculation` | 100% Score -> Tier 1 Cyber Defender Elite | `PASSED` |
| `test_passing_score_calculation` | 75% Score -> Tier 2 Aware & Vigilant | `PASSED` |
| `test_failing_score_classification` | < 50% Score -> Tier 4 High-Risk Liability | `PASSED` |
| `test_all_questions_have_valid_answers` | 4 Options & Valid A/B/C/D Key Integrity | `PASSED` |
| `test_score_report_serialization` | JSON & Text Disk Persistence Pipeline | `PASSED` |

**Verification Result: 6/6 Tests Passed (100% OK).**

---

## 📊 Multi-Department Benchmark Simulation Results

| Candidate Profile | Department | Score | TSI % | Risk Tier Classification | Action Plan |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Elena Rostova** | Executive C-Suite | **12 / 12 (100%)** | 0.0% | `TIER_1_CYBER_DEFENDER_ELITE` | Appointed Security Champion |
| **Marcus Vance** | Engineering & DevOps | **11 / 12 (91.7%)** | 8.3% | `TIER_1_CYBER_DEFENDER_ELITE` | Baseline Verified |
| **Chloe Bennett** | Finance & Payroll | **9 / 12 (75.0%)** | 25.0% | `TIER_2_AWARE_AND_VIGILANT` | Annual Recertification |
| **Liam Gallagher** | Human Resources | **7 / 12 (58.3%)** | 41.7% | `TIER_3_VULNERABLE_RETRAINING_REQ` | 30-Day Micro-Training |
| **Devon Miller** | New Intern Cohort | **5 / 12 (41.7%)** | 58.3% | `TIER_4_HIGH_RISK_LIABILITY` | Urgent Remedial Training |

---

## 📜 Compliance & Industry Standards

- **NIST SP 800-50:** Building an Information Technology Security Awareness and Training Program.
- **ISO/IEC 27001:2022 (Control A.6.3):** Information Security Awareness, Education, and Training.
- **CIS Controls v8 (Control 14):** Security Awareness and Skills Training.

---

## 👤 Author & Acknowledgments

- **Lead Developer:** Mohammed Peer Siddiqui
- **Internship Organization:** Sqrock IT Solutions
- **Track:** Social Engineering Attack Simulations Using Python (Alpha 2 Cohort)
- **LinkedIn:** [Mohammed Peer Siddiqui](https://www.linkedin.com)
- **GitHub:** [@MdPeerSiddiqui](https://github.com/MdPeerSiddiqui)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.
