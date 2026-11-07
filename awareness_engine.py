#!/usr/bin/env python3
"""
================================================================================
PEER'S AWARENESS GUARD SUITE v2.5 — Interactive SE Training & Assessment Engine
Author      : Mohammed Peer Siddiqui
Organization: Sqrock IT Solutions — Cybersecurity Internship (Alpha 2 Cohort)
Track       : Social Engineering Attack Simulations Using Python (Day 11)
Standard    : NIST SP 800-50 | ISO/IEC 27001:2022 Control A.6.3 | CIS Control 14
================================================================================
"""

import os
import sys
import json
import datetime
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN} █████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗███╗   ██╗███████╗███████╗███████╗
{Fore.CYAN}██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██╔════╝██╔════╝
{Fore.CYAN}███████║██║ █╗ ██║███████║██████╔╝█████╗  ██╔██╗ ██║█████╗  ███████╗███████╗
{Fore.BLUE}██╔══██║██║███╗██║██╔══██║██╔══██╗██╔══╝  ██║╚██╗██║██╔══╝  ╚════██║╚════██║
{Fore.BLUE}██║  ██║╚███╔███╔╝██║  ██║██║  ██║███████╗██║ ╚████║███████╗███████║███████║
{Fore.BLUE}╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
{Fore.MAGENTA}  [+] SOCIAL ENGINEERING AWARENESS TRAINING & ASSESSMENT SUITE v2.5
{Fore.LIGHTBLACK_EX}  [+] Author: Mohammed Peer Siddiqui | Sqrock IT Solutions Alpha 2
  [+] Standard: NIST SP 800-50 | CIS Control 14 | ISO 27001 A.6.3
==============================================================================={Style.RESET_ALL}"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, "questions", "question_bank.json")
REPORTS_DIR = os.path.join(BASE_DIR, "score_reports")
JSON_REPORT_FILE = os.path.join(REPORTS_DIR, "awareness_score_report.json")
TXT_REPORT_FILE = os.path.join(REPORTS_DIR, "awareness_score_report.txt")


def ensure_directories():
    """Ensure output report directories exist."""
    os.makedirs(REPORTS_DIR, exist_ok=True)


def load_question_bank(filepath=QUESTIONS_FILE):
    """Loads scenario-based questions from JSON repository."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def calculate_risk_tier(score, total):
    """
    Computes candidate percentage, Threat Susceptibility Index (TSI),
    and assigns formal enterprise security tier.
    """
    if total <= 0:
        return 0.0, 100.0, "UNKNOWN", "N/A"
    
    pct = round((score / total) * 100, 1)
    tsi = round(100.0 - pct, 1)  # Threat Susceptibility Index

    if pct >= 90.0:
        tier = "TIER_1_CYBER_DEFENDER_ELITE"
        verdict = "EXEMPLARY (Exhibits high vigilance against advanced social engineering)"
    elif pct >= 75.0:
        tier = "TIER_2_AWARE_AND_VIGILANT"
        verdict = "PASS (Meets core corporate security awareness standards)"
    elif pct >= 50.0:
        tier = "TIER_3_VULNERABLE_RETRAINING_REQUIRED"
        verdict = "NEEDS IMPROVEMENT (Mandatory 30-day security retraining assigned)"
    else:
        tier = "TIER_4_HIGH_RISK_LIABILITY"
        verdict = "CRITICAL RISK (High susceptibility to phishing, vishing, and baiting)"

    return pct, tsi, tier, verdict


def save_score_report(report_data, json_path=JSON_REPORT_FILE, txt_path=TXT_REPORT_FILE):
    """Persists candidate evaluation record to JSON and human-readable text."""
    ensure_directories()
    
    # Save/Append to JSON ledger
    existing = []
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as jf:
                data = json.load(jf)
                existing = data if isinstance(data, list) else [data]
        except Exception:
            existing = []

    existing.append(report_data)
    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(existing, jf, indent=2)

    # Save to TXT Certificate
    with open(txt_path, "w", encoding="utf-8") as tf:
        tf.write("===============================================================================\n")
        tf.write("       SQROCK IT SOLUTIONS - SECURITY AWARENESS EVALUATION REPORT              \n")
        tf.write("===============================================================================\n")
        tf.write(f"Candidate Name       : {report_data['candidate_name']}\n")
        tf.write(f"Employee ID          : {report_data['employee_id']}\n")
        tf.write(f"Department           : {report_data['department']}\n")
        tf.write(f"Completion Timestamp : {report_data['timestamp_utc']}\n")
        tf.write(f"Assessment Score     : {report_data['score']} / {report_data['total_questions']} ({report_data['percentage']}%)\n")
        tf.write(f"Threat Susceptibility: {report_data['threat_susceptibility_index']}% (TSI)\n")
        tf.write(f"Assigned Risk Tier   : {report_data['risk_tier']}\n")
        tf.write(f"Formal Status        : {report_data['evaluation_status']}\n")
        tf.write("===============================================================================\n")
        tf.write("Itemized Assessment Question Audit:\n")
        for q in report_data.get("question_results", []):
            status_flag = "[PASS]" if q['is_correct'] else "[FAIL]"
            tf.write(f"  {status_flag} {q['question_id']}: {q['vector']} -> Answered: {q['user_answer']} (Correct: {q['correct_answer']})\n")
        tf.write("===============================================================================\n")


def run_interactive_assessment(candidate_name="Anonymous Candidate", employee_id="SQ-EMP-001", department="General Corporate"):
    """
    Executes the interactive scenario assessment with real-time feedback.
    """
    questions = load_question_bank()
    if not questions:
        print(f"{Fore.RED}[-] Question bank not found at {QUESTIONS_FILE}. Aborting.{Style.RESET_ALL}")
        return None

    print(f"\n{Fore.GREEN}[+] Beginning Assessment for: {Fore.WHITE}{candidate_name} ({employee_id}) [{department}]{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[i] 12 scenario-based questions will be presented. Select A, B, C, or D for each.{Style.RESET_ALL}\n")

    score = 0
    question_results = []

    for idx, q in enumerate(questions, 1):
        print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}SCENARIO {idx} of {len(questions)} | Attack Vector: {Fore.WHITE}{q['vector']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}{q['scenario']}\n{Style.RESET_ALL}")

        for opt in q["options"]:
            print(f"  {Fore.LIGHTCYAN_EX}{opt}{Style.RESET_ALL}")

        while True:
            ans = input(f"\n{Fore.GREEN}Your Decision (A/B/C/D): {Style.RESET_ALL}").strip().upper()
            if ans in ["A", "B", "C", "D"]:
                break
            print(f"{Fore.RED}[!] Invalid choice. Please enter A, B, C, or D.{Style.RESET_ALL}")

        is_correct = (ans == q["correct_answer"])
        if is_correct:
            score += 1
            print(f"\n{Fore.GREEN}[✓] CORRECT! Outstanding defensive judgment.{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}[x] INCORRECT! Your choice represents a security vulnerability.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}    Correct Answer: {q['correct_answer']}{Style.RESET_ALL}")

        print(f"\n{Fore.LIGHTBLACK_EX}--- [ Educational Analysis & Defense Mechanism ] ---{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{q['explanation']}{Style.RESET_ALL}\n")

        question_results.append({
            "question_id": q["id"],
            "vector": q["vector"],
            "user_answer": ans,
            "correct_answer": q["correct_answer"],
            "is_correct": is_correct
        })

    pct, tsi, tier, verdict = calculate_risk_tier(score, len(questions))

    report = {
        "candidate_name": candidate_name,
        "employee_id": employee_id,
        "department": department,
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "score": score,
        "total_questions": len(questions),
        "percentage": pct,
        "threat_susceptibility_index": tsi,
        "risk_tier": tier,
        "evaluation_status": verdict,
        "question_results": question_results
    }

    save_score_report(report)
    return report


def run_benchmark_simulation():
    """
    Simulates automated multi-department benchmark runs to demonstrate
    organizational resilience analytics across diverse corporate departments.
    """
    questions = load_question_bank()
    if not questions:
        return

    simulated_cohort = [
        {"name": "Elena Rostova", "id": "SQ-EXEC-01", "dept": "Executive C-Suite", "accuracy": 1.0},
        {"name": "Marcus Vance", "id": "SQ-DEV-14", "dept": "Engineering & DevOps", "accuracy": 0.92},
        {"name": "Chloe Bennett", "id": "SQ-FIN-08", "dept": "Finance & Payroll", "accuracy": 0.75},
        {"name": "Liam Gallagher", "id": "SQ-HR-03", "dept": "Human Resources", "accuracy": 0.58},
        {"name": "Devon Miller", "id": "SQ-INT-22", "dept": "New Intern Cohort", "accuracy": 0.42}
    ]

    print(f"\n{Fore.YELLOW}[*] Executing Automated Multi-Department Benchmark Simulation...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'Candidate':<18} {'Dept':<22} {'Score':<10} {'TSI %':<8} {'Risk Tier':<28}{Style.RESET_ALL}")
    print("-" * 92)

    total_score = 0
    total_cohort = len(simulated_cohort)

    for cand in simulated_cohort:
        sim_score = int(round(cand["accuracy"] * len(questions)))
        pct, tsi, tier, verdict = calculate_risk_tier(sim_score, len(questions))
        total_score += sim_score
        
        tier_col = Fore.GREEN if "ELITE" in tier else (Fore.CYAN if "AWARE" in tier else (Fore.YELLOW if "VULNERABLE" in tier else Fore.RED))
        print(f"{cand['name']:<18} {cand['dept']:<22} {sim_score}/{len(questions):<6} {tsi:<8} {tier_col}{tier[:28]}{Style.RESET_ALL}")

    avg_pct = round((total_score / (total_cohort * len(questions))) * 100, 1)
    org_phish_prone = round(100.0 - avg_pct, 1)

    print("-" * 92)
    print(f"{Fore.GREEN}[+] Organizational Benchmark Summary:{Style.RESET_ALL}")
    print(f"  • Overall Mean Resilience Score : {avg_pct}%")
    print(f"  • Organizational Phish-Prone %  : {Fore.YELLOW}{org_phish_prone}%{Style.RESET_ALL}")
    print(f"  • Recommended Intervention      : Automated micro-training modules for HR & New Interns.")


def print_menu():
    print(f"\n{Fore.LIGHTBLACK_EX}--- [ PEER'S AWARENESS GUARD CONTROL CONSOLE ] ---{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}[1]{Fore.WHITE} Take Interactive Awareness Assessment (Candidate Exam)")
    print(f"  {Fore.CYAN}[2]{Fore.WHITE} Run Multi-Department Benchmark Simulation (Analytics)")
    print(f"  {Fore.CYAN}[3]{Fore.WHITE} Inspect Detailed Candidate Score Reports (JSON & Text)")
    print(f"  {Fore.CYAN}[4]{Fore.WHITE} View Complete Question Bank & Educational Defense Keys")
    print(f"  {Fore.CYAN}[5]{Fore.WHITE} Display Employee Risk Tier Matrix & Phish-Prone Scoring")
    print(f"  {Fore.CYAN}[6]{Fore.WHITE} Display Enterprise Security Awareness & Culture Blueprint (NIST)")
    print(f"  {Fore.CYAN}[7]{Fore.RED} Exit Suite")


def interactive_cli():
    print(BANNER)
    ensure_directories()

    while True:
        print_menu()
        choice = input(f"\n{Fore.GREEN}sqrock@awareness-guard{Fore.WHITE}:{Fore.BLUE}~/training-suite{Fore.WHITE}$ ").strip()

        if choice == "1":
            print(f"\n{Fore.YELLOW}[*] Candidate Registration for Security Assessment:{Style.RESET_ALL}")
            c_name = input("Enter Candidate Full Name: ").strip() or "Mohammed Peer Siddiqui"
            e_id = input("Enter Employee ID (e.g., SQ-EMP-108): ").strip() or "SQ-EMP-108"
            dept = input("Enter Department (e.g., Cyber Defense Operations): ").strip() or "Cyber Defense Operations"
            
            report = run_interactive_assessment(c_name, e_id, dept)
            if report:
                print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
                print(f"{Fore.GREEN}                  OFFICIAL ASSESSMENT RESULTS CERTIFICATE                      {Style.RESET_ALL}")
                print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
                score_col = Fore.GREEN if report['percentage'] >= 75 else Fore.RED
                print(f"  Candidate Name        : {Fore.WHITE}{report['candidate_name']}")
                print(f"  Final Score           : {score_col}{report['score']} / {report['total_questions']} ({report['percentage']}%){Style.RESET_ALL}")
                print(f"  Threat Susceptibility : {Fore.YELLOW}{report['threat_susceptibility_index']}% TSI{Style.RESET_ALL}")
                print(f"  Assigned Risk Tier    : {score_col}{report['risk_tier']}{Style.RESET_ALL}")
                print(f"  Evaluation Verdict    : {report['evaluation_status']}")
                print(f"\n  [+] Audit record saved to: {JSON_REPORT_FILE}")

        elif choice == "2":
            run_benchmark_simulation()

        elif choice == "3":
            if not os.path.exists(JSON_REPORT_FILE):
                print(f"{Fore.YELLOW}[i] No score reports on disk yet. Run Option 1 to complete an exam.{Style.RESET_ALL}")
            else:
                with open(JSON_REPORT_FILE, "r", encoding="utf-8") as f:
                    records = json.load(f)
                records = records if isinstance(records, list) else [records]
                print(f"\n{Fore.GREEN}[+] Total Evaluated Candidates: {len(records)}{Style.RESET_ALL}")
                for idx, r in enumerate(records[-3:], 1):
                    print(f"  Record #{idx}: {r['candidate_name']} ({r['employee_id']}) -> {r['score']}/{r['total_questions']} ({r['percentage']}%) [{r['risk_tier']}]")

        elif choice == "4":
            questions = load_question_bank()
            print(f"\n{Fore.GREEN}[+] Question Bank Inventory ({len(questions)} Scenarios):{Style.RESET_ALL}")
            for q in questions:
                print(f"  • {Fore.CYAN}{q['id']}{Fore.WHITE}: {q['vector']} (Answer: {Fore.GREEN}{q['correct_answer']}{Fore.WHITE})")

        elif choice == "5":
            print(f"\n{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"{Fore.GREEN}        ENTERPRISE EMPLOYEE RISK TIER & SCORING TAXONOMY                       {Style.RESET_ALL}")
            print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"""
{Fore.GREEN}1. TIER 1: CYBER DEFENDER (ELITE) [90% - 100% Score | TSI <= 10%]:{Fore.WHITE}
   - Candidate demonstrates exemplary instinctive defense against advanced social engineering.
   - Eligible to serve as Department Security Champion and Phishing Triage Ambassador.

{Fore.CYAN}2. TIER 2: AWARE & VIGILANT [75% - 89% Score | TSI 11% - 25%]:{Fore.WHITE}
   - Successfully satisfies baseline corporate security requirements.
   - Low vulnerability; scheduled for routine annual recertification.

{Fore.YELLOW}3. TIER 3: VULNERABLE (RETRAINING REQUIRED) [50% - 74% Score | TSI 26% - 50%]:{Fore.WHITE}
   - Demonstrates susceptibility to targeted authority and urgency triggers.
   - Mandatory assignment to 30-day interactive remedial micro-learning modules.

{Fore.RED}4. TIER 4: HIGH-RISK LIABILITY [< 50% Score | TSI > 50%]:{Fore.WHITE}
   - Severe vulnerability to credential harvesting, baiting, and vishing pretexts.
   - Immediate notification dispatched to Department Supervisor and Security Operations.
""")

        elif choice == "6":
            print(f"\n{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"{Fore.GREEN}    ENTERPRISE SECURITY AWARENESS & HUMAN DEFENSE BLUEPRINT (NIST SP 800-50)   {Style.RESET_ALL}")
            print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"""
{Fore.YELLOW}1. Continuous Micro-Training over Annual Lectures:{Fore.WHITE}
   - Modern research proves that annual one-hour security presentations suffer an 80% retention decay within 30 days.
   - Deploy monthly 3-minute scenario-based interactive challenges and simulated phishing drills.

{Fore.YELLOW}2. Multi-Vector Coverage:{Fore.WHITE}
   - Do not focus exclusively on email phishing. Integrate Vishing, Smishing, USB Drops, and Physical Tailgating.

{Fore.YELLOW}3. Just-In-Time Educational Feedback:{Fore.WHITE}
   - When an employee fails a simulated phishing drill, provide immediate, constructive feedback highlighting the specific red flags.

{Fore.YELLOW}4. Transparent, Non-Punitive Culture:{Fore.WHITE}
   - Encourage rapid reporting. A reported phishing email within 5 minutes saves millions in incident containment costs.
""")

        elif choice == "7":
            print(f"\n{Fore.CYAN}[+] Exiting PEER'S Awareness Guard Suite. Security active.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[-] Invalid option. Please select 1 through 7.{Style.RESET_ALL}")


if __name__ == "__main__":
    interactive_cli()
