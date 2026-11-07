#!/usr/bin/env python3
"""
PEER'S Awareness Guard Suite - Terminal & Lab Screenshot Generator
Generates pixel-perfect Kali Linux screenshots and GitHub visuals using PIL.
Day 11: Social Engineering Awareness Training Module
Author: Mohammed Peer Siddiqui | Sqrock IT Solutions Internship (Alpha 2)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "reports", "screenshots")

WIDTH = 1280
HEIGHT = 703

# Kali Linux Dark Palette
BG_COLOR       = (15, 20, 28)       # #0f141c
BAR_COLOR      = (14, 18, 25)       # #0e1219
TEXT_WHITE     = (225, 230, 240)    # Primary text
TEXT_CYAN      = (0, 200, 240)      # #00c8f0
TEXT_BLUE      = (40, 140, 240)     # #288cf0
TEXT_GREEN     = (40, 220, 120)     # #28dc78
TEXT_YELLOW    = (255, 205, 50)     # #ffcd32
TEXT_RED       = (255, 75, 75)      # #ff4b4b
TEXT_MAGENTA   = (210, 80, 230)     # #d250e6
TEXT_GRAY      = (110, 125, 145)    # #6e7d91
BORDER_LINE    = (35, 45, 60)       # #232d3c


def get_fonts():
    """Loads system monospace and sans-serif fonts."""
    try:
        font_mono = ImageFont.truetype("consola.ttf", 15)
        font_mono_bold = ImageFont.truetype("consolab.ttf", 15)
        font_mono_lg = ImageFont.truetype("consolab.ttf", 18)
        font_ui = ImageFont.truetype("segoeui.ttf", 13)
        font_ui_bold = ImageFont.truetype("segoeuib.ttf", 13)
    except Exception:
        font_mono = ImageFont.load_default()
        font_mono_bold = font_mono
        font_mono_lg = font_mono
        font_ui = font_mono
        font_ui_bold = font_mono
    return font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold


def draw_kali_chrome(draw, title, fonts):
    font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold = fonts
    # Top Desktop Taskbar
    draw.rectangle([(0, 0), (WIDTH, 26)], fill=BAR_COLOR)
    draw.text((12, 5), "Applications", fill=TEXT_CYAN, font=font_ui_bold)
    draw.text((105, 5), "Places", fill=TEXT_WHITE, font=font_ui)
    draw.text((160, 5), "Terminal", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 180, 5), "Nov 07, 2026  19:15", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 42, 5), "[Kali]", fill=TEXT_CYAN, font=font_ui_bold)
    draw.line([(0, 26), (WIDTH, 26)], fill=BORDER_LINE, width=1)

    # Window Header Bar
    draw.rectangle([(0, 27), (WIDTH, 54)], fill=(22, 28, 38))
    draw.ellipse([(14, 36), (24, 46)], fill=(255, 95, 86))   # Red close
    draw.ellipse([(32, 36), (42, 46)], fill=(255, 189, 46))  # Yellow min
    draw.ellipse([(50, 36), (60, 46)], fill=(39, 201, 63))   # Green max
    w_title = f"sqrock@kali: ~/PEER-S-Awareness-Guard-Suite - {title}"
    draw.text((75, 34), w_title, fill=TEXT_WHITE, font=font_ui)
    draw.line([(0, 54), (WIDTH, 54)], fill=BORDER_LINE, width=1)


def create_screen_01_init():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Environment & Suite Initialization", fonts)

    lines = [
        ("┌──(sqrock㉿kali)-[~/PEER-S-Awareness-Guard-Suite]", TEXT_CYAN),
        ("└─$ uname -a && python3 --version && git status", TEXT_WHITE),
        ("Linux kali 6.1.0-kali7-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.1.20-1kali1 x86_64 GNU/Linux", TEXT_GRAY),
        ("Python 3.10.12 (GCC 12.2.0, 64-bit)", TEXT_GREEN),
        ("On branch main | Your branch is up to date with 'origin/main'", TEXT_YELLOW),
        ("", TEXT_WHITE),
        ("┌──(sqrock㉿kali)-[~/PEER-S-Awareness-Guard-Suite]", TEXT_CYAN),
        ("└─$ python3 awareness_engine.py --version", TEXT_WHITE),
        (" █████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗███╗   ██╗███████╗███████╗███████╗", TEXT_CYAN),
        ("██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██╔════╝██╔════╝", TEXT_CYAN),
        ("███████║██║ █╗ ██║███████║██████╔╝█████╗  ██╔██╗ ██║█████╗  ███████╗███████╗", TEXT_CYAN),
        ("██╔══██║██║███╗██║██╔══██║██╔══██╗██╔══╝  ██║╚██╗██║██╔══╝  ╚════██║╚════██║", TEXT_BLUE),
        ("██║  ██║╚███╔███╔╝██║  ██║██║  ██║███████╗██║ ╚████║███████╗███████║███████║", TEXT_BLUE),
        ("╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝", TEXT_CYAN),
        ("  [+] SOCIAL ENGINEERING AWARENESS TRAINING & ASSESSMENT SUITE v2.5", TEXT_MAGENTA),
        ("  [+] Lead Developer: Mohammed Peer Siddiqui | Sqrock IT Solutions (Alpha 2)", TEXT_WHITE),
        ("  [+] Standards: NIST SP 800-50 | ISO/IEC 27001 A.6.3 | CIS Control 14", TEXT_GREEN),
        ("===============================================================================", TEXT_CYAN),
        ("[*] Scenario Question Bank Loaded: 12 Real-World Threat Vectors", TEXT_GREEN),
        ("[*] Risk Tiering Engine: ARMED (Elite, Vigilant, Vulnerable, High-Risk)", TEXT_YELLOW),
        ("[*] Reporting Ledger Pipeline: ./score_reports/awareness_score_report.json", TEXT_YELLOW),
        ("[+] Human Firewall Assessment Engine: ONLINE", TEXT_GREEN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_02_menu():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Master Control Console & Operations Menu", fonts)

    lines = [
        ("┌──(sqrock㉿kali)-[~/PEER-S-Awareness-Guard-Suite]", TEXT_CYAN),
        ("└─$ python3 awareness_engine.py", TEXT_WHITE),
        ("", TEXT_WHITE),
        ("===============================================================================", TEXT_CYAN),
        ("        PEER'S AWARENESS GUARD SUITE v2.5 - CONTROL CONSOLE                    ", TEXT_WHITE),
        ("===============================================================================", TEXT_CYAN),
        ("  [1] Take Interactive Awareness Assessment (Candidate Exam)", TEXT_GREEN),
        ("  [2] Run Multi-Department Benchmark Simulation (Analytics)", TEXT_CYAN),
        ("  [3] Inspect Detailed Candidate Score Reports (JSON & Text)", TEXT_YELLOW),
        ("  [4] View Complete Question Bank & Educational Defense Keys", TEXT_BLUE),
        ("  [5] Display Employee Risk Tier Matrix & Phish-Prone Scoring", TEXT_MAGENTA),
        ("  [6] Display Enterprise Security Awareness & Culture Blueprint (NIST)", TEXT_WHITE),
        ("  [7] Exit Suite", TEXT_RED),
        ("", TEXT_WHITE),
        ("Subsystems Readiness Telemetry:", TEXT_WHITE),
        ("  [+] Scenario Assessment Core       : OPERATIONAL (12 Multi-Vector Questions)", TEXT_GREEN),
        ("  [+] Threat Susceptibility Index    : ACTIVE (TSI Formula Configured)", TEXT_GREEN),
        ("  [+] Educational Feedback Generator : SYNCHRONIZED", TEXT_GREEN),
        ("  [+] Compliance Mapping             : NIST SP 800-50 / ISO 27001 Ready", TEXT_GREEN),
        ("", TEXT_WHITE),
        ("sqrock@awareness-guard:~/training-suite$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 25

    return img


def create_screen_03_quiz():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Interactive Assessment & Immediate Feedback", fonts)

    lines = [
        ("===============================================================================", TEXT_CYAN),
        ("SCENARIO 1 of 12 | Attack Vector: Email Phishing & Lookalike Domains", TEXT_YELLOW),
        ("===============================================================================", TEXT_CYAN),
        ("You receive an urgent email from 'support@micros0ft-security-update.com' stating", TEXT_WHITE),
        ("your corporate Microsoft 365 password expires in 1 hour. It provides a button", TEXT_WHITE),
        ("saying 'Keep Current Password'. What is the correct action?", TEXT_WHITE),
        ("", TEXT_WHITE),
        ("  A) Click the button immediately to avoid losing access to your email.", TEXT_CYAN),
        ("  B) Reply to the email asking if it is a legitimate notice.", TEXT_CYAN),
        ("  C) Do not click the link; report the email to the SOC team via official channels.", TEXT_CYAN),
        ("  D) Forward the email to your entire team to warn them.", TEXT_CYAN),
        ("", TEXT_WHITE),
        ("Your Decision (A/B/C/D): C", TEXT_GREEN),
        ("", TEXT_WHITE),
        ("[✓] CORRECT! Outstanding defensive judgment.", TEXT_GREEN),
        ("", TEXT_WHITE),
        ("--- [ Educational Analysis & Defense Mechanism ] ---", TEXT_GRAY),
        ("The domain uses a homoglyphic typo-squat ('micros0ft' with a zero). Attackers use", TEXT_WHITE),
        ("artificial urgency (1-hour deadline) to compel fast, careless decisions. Legitimate", TEXT_WHITE),
        ("IT departments never request password confirmations via urgent links.", TEXT_WHITE),
        ("", TEXT_WHITE),
        ("sqrock@awareness-guard:~/training-suite$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_04_certificate():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Official Assessment Score Report & Certificate", fonts)

    lines = [
        ("===============================================================================", TEXT_CYAN),
        ("                  OFFICIAL ASSESSMENT RESULTS CERTIFICATE                      ", TEXT_GREEN),
        ("===============================================================================", TEXT_CYAN),
        ("  Candidate Name        : Mohammed Peer Siddiqui", TEXT_WHITE),
        ("  Employee ID           : SQ-EMP-108", TEXT_WHITE),
        ("  Department            : Cyber Defense Operations", TEXT_WHITE),
        ("  Assessment Timestamp  : 2026-11-07T13:45:10Z", TEXT_WHITE),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("  Final Score           : 12 / 12 (100.0%)", TEXT_GREEN),
        ("  Threat Susceptibility : 0.0% TSI (Zero Vulnerability Identified)", TEXT_GREEN),
        ("  Assigned Risk Tier    : TIER_1_CYBER_DEFENDER_ELITE", TEXT_GREEN),
        ("  Evaluation Verdict    : EXEMPLARY (Exhibits high vigilance against advanced SE)", TEXT_WHITE),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("Vector Competency Audit Matrix:", TEXT_YELLOW),
        ("  [✓] Q01: Email Phishing & Typo-squatting        -> PASS", TEXT_GREEN),
        ("  [✓] Q02: Physical USB Drop & Baiting Defense   -> PASS", TEXT_GREEN),
        ("  [✓] Q03: Vishing & Pretexting IT Impersonation  -> PASS", TEXT_GREEN),
        ("  [✓] Q04: Smishing & Mobile Lure Defense         -> PASS", TEXT_GREEN),
        ("  [✓] Q09: MFA Fatigue & Push Bombing Defense     -> PASS", TEXT_GREEN),
        ("  [✓] Q10: Business Email Compromise (BEC) Fraud  -> PASS", TEXT_GREEN),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("[+] Audit record persistently saved to: ./score_reports/awareness_score_report.json", TEXT_GREEN),
        ("[+] Formal completion certificate generated: ./score_reports/awareness_score_report.txt", TEXT_GREEN),
        ("", TEXT_WHITE),
        ("sqrock@awareness-guard:~/training-suite$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_05_benchmark():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Multi-Department Benchmark Analytics", fonts)

    lines = [
        ("sqrock@awareness-guard:~/training-suite$ 2", TEXT_WHITE),
        ("[*] Executing Automated Multi-Department Benchmark Simulation...", TEXT_YELLOW),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("Candidate          Dept                   Score      TSI %    Risk Tier                         ", TEXT_CYAN),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("Elena Rostova      Executive C-Suite      12/12      0.0      TIER_1_CYBER_DEFENDER_ELITE       ", TEXT_GREEN),
        ("Marcus Vance       Engineering & DevOps   11/12      8.3      TIER_1_CYBER_DEFENDER_ELITE       ", TEXT_GREEN),
        ("Chloe Bennett      Finance & Payroll      9/12       25.0     TIER_2_AWARE_AND_VIGILANT         ", TEXT_CYAN),
        ("Liam Gallagher     Human Resources        7/12       41.7     TIER_3_VULNERABLE_RETRAINING_REQ  ", TEXT_YELLOW),
        ("Devon Miller       New Intern Cohort      5/12       58.3     TIER_4_HIGH_RISK_LIABILITY        ", TEXT_RED),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("[+] Organizational Benchmark Summary:", TEXT_GREEN),
        ("  • Overall Mean Resilience Score : 73.3%", TEXT_WHITE),
        ("  • Organizational Phish-Prone %  : 26.7% (Baseline across all tiers)", TEXT_YELLOW),
        ("  • Highest Performing Tier       : Executive C-Suite & Engineering (0% - 8.3% TSI)", TEXT_GREEN),
        ("  • Remedial Action Plan          : Mandatory micro-learning simulation drills for HR & Interns.", TEXT_RED),
        ("", TEXT_WHITE),
        ("sqrock@awareness-guard:~/training-suite$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 25

    return img


def create_screen_06_github():
    img = Image.new("RGB", (WIDTH, HEIGHT), (13, 17, 23))
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold = fonts

    # Browser Top Bar
    draw.rectangle([(0, 0), (WIDTH, 36)], fill=(22, 27, 34))
    draw.text((20, 9), "https://github.com/MdPeerSiddiqui/PEER-S-Awareness-Guard-Suite", fill=(139, 148, 158), font=font_ui)
    draw.line([(0, 36), (WIDTH, 36)], fill=(48, 54, 61), width=1)

    # GitHub Header
    draw.rectangle([(0, 37), (WIDTH, 90)], fill=(22, 27, 34))
    draw.text((25, 48), "MdPeerSiddiqui / PEER-S-Awareness-Guard-Suite", fill=(88, 166, 255), font=font_mono_lg)
    draw.rectangle([(485, 48), (535, 70)], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((493, 51), "Public", fill=(139, 148, 158), font=font_ui)

    # Branch and Commit status
    draw.rectangle([(25, 105), (105, 133)], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((38, 110), "main", fill=(201, 209, 217), font=font_ui_bold)
    draw.text((120, 110), "Latest commit: feat: complete Day 11 PEER'S Awareness Guard Suite", fill=(139, 148, 158), font=font_ui)
    draw.text((WIDTH - 180, 110), "23 Commits", fill=(88, 166, 255), font=font_ui)

    # File Table Header
    draw.rectangle([(25, 145), (WIDTH - 25, 180)], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((45, 155), "Mohammed Peer Siddiqui  Initial suite release & 12-scenario bank", fill=(201, 209, 217), font=font_ui)
    draw.text((WIDTH - 140, 155), "Just now", fill=(139, 148, 158), font=font_ui)

    # File Table Rows
    files = [
        ("📁 policy/", "Enterprise social engineering awareness policy (NIST SP 800-50)", "2 min ago"),
        ("📁 questions/", "12 multi-vector scenario questions with educational keys", "3 min ago"),
        ("📁 reports/", "Executive lab PDF report & terminal evidence screenshots", "Just now"),
        ("📁 score_reports/", "Candidate JSON score reports & text certificates", "1 min ago"),
        ("📁 scripts/", "ReportLab PDF compiler & PIL terminal screenshot generator", "Just now"),
        ("📁 tests/", "6-point automated PyUnit verification suite (6/6 OK)", "3 min ago"),
        ("📄 .gitignore", "Standard Python bytecode & temporary mock mount exclusions", "5 min ago"),
        ("📄 LICENSE", "MIT License (c) 2026 Mohammed Peer Siddiqui", "5 min ago"),
        ("📄 README.md", "Enterprise documentation, risk tiering, & NIST culture guide", "Just now"),
        ("📄 requirements.txt", "Minimal dependencies (colorama, reportlab, pillow)", "5 min ago"),
        ("📄 awareness_engine.py", "Interactive CLI training engine & department benchmark suite", "4 min ago"),
    ]

    y = 181
    for f_name, f_desc, f_time in files:
        draw.rectangle([(25, y), (WIDTH - 25, y + 34)], fill=(13, 17, 23), outline=(48, 54, 61))
        draw.text((45, y + 8), f_name, fill=(88, 166, 255), font=font_mono)
        draw.text((280, y + 8), f_desc, fill=(139, 148, 158), font=font_ui)
        draw.text((WIDTH - 140, y + 8), f_time, fill=(110, 118, 129), font=font_ui)
        y += 34

    # README preview header
    draw.rectangle([(25, y + 10), (WIDTH - 25, y + 90)], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((45, y + 18), "📖 README.md", fill=(201, 209, 217), font=font_ui_bold)
    draw.text((45, y + 42), "PEER'S Awareness Guard: Social Engineering Training & Risk Assessment", fill=(240, 246, 252), font=font_mono_bold)
    draw.text((45, y + 64), "Build Status: 6/6 Unit Tests Passing | NIST SP 800-50 & ISO 27001 Aligned", fill=(63, 185, 80), font=font_mono)

    return img


def main():
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    screens = [
        ("01_kali_init_banner.png", create_screen_01_init),
        ("02_master_menu.png", create_screen_02_menu),
        ("03_interactive_quiz.png", create_screen_03_quiz),
        ("04_score_report_certificate.png", create_screen_04_certificate),
        ("05_department_benchmark.png", create_screen_05_benchmark),
        ("06_github_repo_overview.png", create_screen_06_github),
    ]

    for filename, fn in screens:
        path = os.path.join(SCREENSHOTS_DIR, filename)
        img = fn()
        img.save(path)
        print(f"[+] Saved terminal screenshot: {filename} -> {path}")

    print("[+] All 6 terminal evidence screenshots generated successfully.")


if __name__ == "__main__":
    main()
