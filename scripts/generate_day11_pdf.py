#!/usr/bin/env python3
"""
PEER'S Awareness Guard Suite - Executive Multi-Page Lab Report Compiler (Day 11)
Sqrock IT Solutions Cybersecurity Internship Track: Social Engineering Attack Simulations Using Python

Compiles an authoritative 7-page executive engineering report integrating:
- 6 empirical execution screenshots (Kali Linux CLI cold boot, master menu, live quiz scenario, score certificate, department benchmark, GitHub repo)
- In-depth forensic explanations for every screenshot
- Deep technical analyses of human risk management, cognitive exploit vectors, threat susceptibility indexing, and NIST SP 800-50 training standards
- Automated 6-point unit test validation ledger and ethical compliance statements
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
OUTPUT_PDF = os.path.join(REPORTS_DIR, "Day11_SE_Awareness_Report_Sqrock_MdPeerSiddiqui.pdf")

# Palette definitions
NAVY_PRIMARY = colors.HexColor("#0B192C")
CYAN_ACCENT  = colors.HexColor("#008DDA")
DARK_BLUE    = colors.HexColor("#1E3E62")
SLATE_GRAY   = colors.HexColor("#415A77")
LIGHT_BG     = colors.HexColor("#F4F6F9")
BORDER_COLOR = colors.HexColor("#D0D7DE")
SUCCESS_COL  = colors.HexColor("#0E703C")
CRIT_COL     = colors.HexColor("#A8201A")
TEXT_DARK    = colors.HexColor("#1A1A1A")


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and render total page count
    and persistent running headers and footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        page_num = self._pageNumber
        
        # Running Header (pages 2+)
        if page_num > 1:
            self.setStrokeColor(BORDER_COLOR)
            self.setLineWidth(0.6)
            self.line(36, 756, 576, 756)
            
            self.setFont("Helvetica", 7.5)
            self.setFillColor(SLATE_GRAY)
            self.drawString(36, 762, "Sqrock IT Solutions | Cybersecurity Internship — Day 11 Lab Report")
            self.drawRightString(576, 762, "PEER'S Awareness Guard Suite v2.5")

        # Running Footer (all pages)
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.6)
        self.line(36, 36, 576, 36)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(SLATE_GRAY)
        self.drawString(36, 24, "Author: Mohammed Peer Siddiqui | Authorized Lab Environment | Confidential & Educational")
        self.drawRightString(576, 24, f"Page {page_num} of {total_pages}")
        
        self.restoreState()


def create_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=42,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=NAVY_PRIMARY,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=CYAN_ACCENT,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=NAVY_PRIMARY,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=DARK_BLUE,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        spaceAfter=5
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=DARK_BLUE
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=TEXT_DARK
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    story = []

    def load_screenshot(filename, w=540, h=195):
        path = os.path.join(SCREENSHOTS_DIR, filename)
        if os.path.exists(path):
            return Image(path, width=w, height=h)
        return Paragraph(f"<b>[Screenshot missing: {filename}]</b>", callout_style)

    # =========================================================================
    # PAGE 1: TITLE, METADATA & EXECUTIVE SUMMARY
    # =========================================================================
    story.append(Paragraph("SQROCK IT SOLUTIONS — CYBERSECURITY INTERNSHIP", subtitle_style))
    story.append(Paragraph("Day 11: Social Engineering Awareness Training Module & Human Risk Profiling", title_style))
    story.append(Spacer(1, 4))

    # Metadata Card
    meta_data = [
        [
            Paragraph("<b>Intern:</b> Mohammed Peer Siddiqui", table_cell),
            Paragraph("<b>Track:</b> Social Engineering Simulations (Python)", table_cell),
            Paragraph("<b>Date:</b> November 07, 2026", table_cell)
        ],
        [
            Paragraph("<b>Target Domain:</b> Human Risk Assessment & Education", table_cell),
            Paragraph("<b>Standard:</b> NIST SP 800-50 / ISO/IEC 27001 A.6.3", table_cell),
            Paragraph("<b>Framework:</b> CIS Controls v8 (Control 14: Awareness Training)", table_cell)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[180, 180, 180])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "Modern cybersecurity architectures universally acknowledge that the human element represents the primary vulnerability across "
        "the corporate attack surface. While firewalls, email filters, and endpoint detection and response (EDR) solutions inspect technical "
        "signatures, social engineering threat actors bypass perimeter perimeters by directly manipulating psychological cognitive biases—including "
        "<b>authority, artificial urgency, scarcity, fear, and helpfulness</b>. Consequently, building and maintaining an active, resilient "
        "'Human Firewall' via continuous scenario-based training is the most cost-effective defensive measure in enterprise infosec.",
        body_style
    ))
    story.append(Paragraph(
        "Under <b>Day 11</b> of the Sqrock IT Solutions Cybersecurity Internship, this laboratory research project developed and evaluated "
        "<b>PEER'S Awareness Guard Suite v2.5</b>. The system delivers an interactive, scenario-driven training and assessment engine that "
        "tests candidates across 12 high-fidelity threat vectors (phishing, vishing, smishing, USB drops, watering holes, impersonation, "
        "tailgating, shoulder surfing, MFA fatigue, and BEC fraud). By providing immediate educational feedback and calculating a standardized "
        "<b>Threat Susceptibility Index (TSI)</b>, the framework fulfills <b>NIST SP 800-50</b> and <b>CIS Controls v8 Safeguard 14.1–14.8</b>.",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("2. Security Awareness Training Architecture Comparison", h1_style))
    matrix_data = [
        [
            Paragraph("Training Dimension", table_header),
            Paragraph("Traditional Annual Lecture / Slides", table_header),
            Paragraph("PEER'S Awareness Guard Engine", table_header)
        ],
        [
            Paragraph("Pedagogical Methodology", table_cell),
            Paragraph("<font color='#A8201A'>Passive slide viewing (80% retention decay)</font>", table_cell),
            Paragraph("<font color='#0E703C'>Active scenario decision-making & immediate feedback</font>", table_cell)
        ],
        [
            Paragraph("Attack Vector Coverage", table_cell),
            Paragraph("<font color='#A8201A'>Generic email phishing only</font>", table_cell),
            Paragraph("<font color='#0E703C'>12 Multi-Vector Vectors (Vishing, USB, MFA, Tailgating)</font>", table_cell)
        ],
        [
            Paragraph("Risk Quantification", table_cell),
            Paragraph("<font color='#A8201A'>Simple pass/fail attendance tracking</font>", table_cell),
            Paragraph("<font color='#0E703C'>Threat Susceptibility Index (TSI) & 4-Tier Risk Matrix</font>", table_cell)
        ],
        [
            Paragraph("Feedback Latency", table_cell),
            Paragraph("<font color='#A8201A'>Delayed end-of-quarter test score</font>", table_cell),
            Paragraph("<font color='#0E703C'>Instantaneous tactical analysis per question</font>", table_cell)
        ],
        [
            Paragraph("Compliance Alignment", table_cell),
            Paragraph("<font color='#A8201A'>Superficial checkbox compliance</font>", table_cell),
            Paragraph("<font color='#0E703C'>NIST SP 800-50, ISO 27001 A.6.3, CIS Control 14</font>", table_cell)
        ]
    ]
    t_mat = Table(matrix_data, colWidths=[140, 195, 205])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_mat)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: THREAT MODELING, COGNITIVE VULNERABILITY & INITIAL STATE
    # =========================================================================
    story.append(Paragraph("3. Threat Modeling & Cognitive Exploitation Mechanics", h1_style))
    story.append(Paragraph(
        "Social engineering attacks succeed because they bypass technological logic by targeting psychological heuristics. "
        "Adversaries structure pretexts around five core psychological levers:",
        body_style
    ))
    story.append(Paragraph(
        "<b>1. Authority & Power Gradients:</b> Impersonating executive management (CEO/CFO in BEC fraud) or regulatory auditors to "
        "intimidate victims into bypassing established controls.<br/>"
        "<b>2. Artificial Urgency & Time Scarcity:</b> Creating artificial deadlines ('password expires in 1 hour', 'wire must close today') "
        "to force hurried cognitive shortcuts and suppress analytical verification.<br/>"
        "<b>3. Fear of Adverse Consequences:</b> Threatening account suspension, employment termination, or legal liability.<br/>"
        "<b>4. Sympathy & Social Politeness:</b> Exploiting basic courtesy to gain physical access (holding secure turnstiles for tailgaters) "
        "or disclosing sensitive internal directory details to vishers.<br/>"
        "<b>5. Financial Greed & Quid Pro Quo:</b> Baiting victims with executive salaries, gift cards, or fake consulting bonuses.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 1: Kali Linux Terminal Initialization & Environment Verification", h2_style))
    story.append(load_screenshot("01_kali_init_banner.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 1:</b> The cold-boot trace in Figure 1 confirms deployment within Kali Linux kernel 6.1.0-kali7-amd64 "
        "with Python 3.10.12. Git status confirms synchronization on the <code>main</code> branch. The initialization sequence arms the "
        "Human Firewall Assessment Engine, loads the 12-scenario question bank, configures the Risk Tiering engine (Elite, Vigilant, "
        "Vulnerable, High-Risk), and establishes persistent JSON reporting into <code>score_reports/awareness_score_report.json</code>.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: SUITE ARCHITECTURE & MASTER CONTROL CONSOLE
    # =========================================================================
    story.append(Paragraph("4. Suite Architecture & Modular Control Interface", h1_style))
    story.append(Paragraph(
        "To provide a comprehensive instructional platform bridging offensive social engineering awareness and defensive human risk profiling, "
        "<b>PEER'S Awareness Guard Suite v2.5</b> was engineered into six modular subsystems accessible via an interactive command console:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Option 1 (Interactive Awareness Assessment):</b> Launches candidate examination, guiding employees through 12 real-world "
        "scenarios with real-time feedback and certification generation.<br/>"
        "• <b>Option 2 (Multi-Department Benchmark Simulation):</b> Simulates automated cohort test runs across 5 corporate tiers "
        "(Executive, Engineering, Finance, HR, Interns) to evaluate organizational phish-prone percentages.<br/>"
        "• <b>Option 3 (Candidate Score Reports):</b> Inspects historical examination records stored in the persistent JSON ledger.<br/>"
        "• <b>Option 4 (Question Bank Inventory):</b> Lists all 12 scenario vectors, answer keys, and defense mechanisms.<br/>"
        "• <b>Option 5 (Risk Tier & Scoring Matrix):</b> Displays formal criteria for enterprise Risk Tiers and TSI formulas.<br/>"
        "• <b>Option 6 (NIST SP 800-50 Culture Blueprint):</b> Outlines continuous micro-learning and non-punitive reporting policies.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 2: PEER'S Awareness Guard Master Control Console", h2_style))
    story.append(load_screenshot("02_master_menu.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 2:</b> Figure 2 illustrates the master operator interface. The readiness telemetry pane confirms "
        "that the Scenario Assessment Core is loaded with 12 multi-vector questions, the Threat Susceptibility Index calculation pipeline is "
        "active, and compliance mappings to NIST SP 800-50 and ISO 27001 are established. The prompt provides clean POSIX terminal navigation.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: INTERACTIVE ASSESSMENT ENGINE & IMMEDIATE FEEDBACK
    # =========================================================================
    story.append(Paragraph("5. Scenario Simulation Execution & Just-in-Time Learning", h1_style))
    story.append(Paragraph(
        "Traditional awareness tests fail because employees receive only a numerical score days after examination without understanding "
        "<i>why</i> specific choices constituted vulnerabilities. In contrast, <b>PEER'S Awareness Guard Engine</b> incorporates "
        "<b>Just-in-Time Educational Feedback</b> directly into the assessment flow (Option 1).",
        body_style
    ))
    story.append(Paragraph(
        "As demonstrated in Scenario 1 (Email Phishing & Lookalike Domains), when a candidate selects an option, the engine validates the "
        "decision in real time. Regardless of whether the choice was correct or incorrect, the system prints an explicit forensic breakdown "
        "pinpointing the attacker's psychological trigger (artificial 1-hour urgency) and technical indicator (homoglyphic typo-squatting in "
        "<code>micros0ft-security-update.com</code>), reinforcing proper incident escalation.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 3: Interactive Assessment & Immediate Feedback", h2_style))
    story.append(load_screenshot("03_interactive_quiz.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 3:</b> The terminal trace in Figure 3 captures Candidate Decision execution on Scenario 1. "
        "The candidate evaluated four potential actions and selected Option C ('Do not click the link; report the email to the SOC team'). "
        "The engine immediately validated the correct defensive choice, awarded points, and presented the detailed educational rationale. "
        "This pedagogical approach reinforces cognitive muscle memory against urgency-driven email manipulation.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: CANDIDATE RISK PROFILING & FORMAL CERTIFICATION
    # =========================================================================
    story.append(Paragraph("6. Candidate Evaluation Metrics & Threat Susceptibility Index (TSI)", h1_style))
    story.append(Paragraph(
        "Upon completing the 12-scenario assessment, the engine computes two critical quantitative metrics: (1) <b>Resilience Percentage</b> "
        "(correct answers / total questions), and (2) <b>Threat Susceptibility Index (TSI)</b> (calculated as <code>100.0 - Percentage</code>). "
        "Candidates are formally categorized into four enterprise Risk Tiers:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Tier 1: Cyber Defender (Elite) [90% - 100% | TSI <= 10%]:</b> Exemplary security vigilance; qualified as Security Champions.<br/>"
        "• <b>Tier 2: Aware & Vigilant [75% - 89% | TSI 11% - 25%]:</b> Satisfies corporate baseline; low risk profile.<br/>"
        "• <b>Tier 3: Vulnerable [50% - 74% | TSI 26% - 50%]:</b> Moderate susceptibility; assigned 30-day remedial micro-learning.<br/>"
        "• <b>Tier 4: High-Risk Liability [< 50% | TSI > 50%]:</b> Severe vulnerability; triggers supervisor notification & access review.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 4: Official Assessment Score Report & Certificate", h2_style))
    story.append(load_screenshot("04_score_report_certificate.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 4:</b> Figure 4 captures the generated Assessment Certificate for Mohammed Peer Siddiqui (SQ-EMP-108, "
        "Cyber Defense Operations). The candidate attained a perfect <b>12/12 (100.0%)</b> score with a <b>0.0% TSI</b>, achieving "
        "<b>TIER_1_CYBER_DEFENDER_ELITE</b> status. The certificate provides an itemized competency matrix confirming mastery across phishing, "
        "USB baiting, vishing, smishing, MFA fatigue, and BEC fraud. The audit record was persistently archived to JSON and text formats.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: MULTI-DEPARTMENT BENCHMARKING & RESILIENCE ANALYTICS
    # =========================================================================
    story.append(Paragraph("7. Enterprise Cohort Benchmarking & Departmental Risk Profiling", h1_style))
    story.append(Paragraph(
        "Enterprise risk managers cannot treat an organization as a homogenous population; different business units exhibit starkly different "
        "threat exposure. Finance personnel face relentless BEC fraud; HR teams receive untrusted resume attachments daily; and software "
        "engineers are targeted with trojanized dependency packages. Under <b>Option 2</b>, the suite executes an automated cohort benchmark "
        "simulating test-takers across five organizational departments.",
        body_style
    ))
    story.append(Paragraph(
        "The simulation reveals critical organizational insights:<br/>"
        "• <b>Executive C-Suite & DevOps (100% & 91.7%):</b> Demonstrates elite threat awareness against targeted spear-phishing.<br/>"
        "• <b>Finance & Payroll (75.0%):</b> Meets passing thresholds but exhibits vulnerability to urgent out-of-band wire transfer lures.<br/>"
        "• <b>Human Resources (58.3%) & Interns (41.7%):</b> Highlights significant phish-prone vulnerability (TSI 41.7% - 58.3%), "
        "mandating tailored remedial training on macro attachments and physical tailgating.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 5: Multi-Department Benchmark Analytics", h2_style))
    story.append(load_screenshot("05_department_benchmark.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 5:</b> Figure 5 depicts the multi-department benchmark simulation output. Across all evaluated cohorts, "
        "the mean organizational resilience reached <b>73.3%</b>, with an aggregate <b>Phish-Prone Percentage of 26.7%</b>. The system emitted "
        "automated remediation directives recommending immediate micro-learning assignments for vulnerable departments.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: AUTOMATED UNIT TESTS, POLICY BLUEPRINT & GITHUB REPO
    # =========================================================================
    story.append(Paragraph("8. Automated Unit Test Verification & Quality Assurance", h1_style))
    test_data = [
        [
            Paragraph("Test Method Identifier", table_header),
            Paragraph("Target Functional Component", table_header),
            Paragraph("Verification Metric", table_header),
            Paragraph("Result", table_header)
        ],
        [
            Paragraph("<code>test_question_bank_structure</code>", table_cell),
            Paragraph("Question Schema Engine", table_cell),
            Paragraph("Validates >= 10 questions with all schema keys", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_perfect_score_calc</code>", table_cell),
            Paragraph("Scoring Mathematics", table_cell),
            Paragraph("Verifies 100% assigns Tier 1 Cyber Defender", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_passing_score_calc</code>", table_cell),
            Paragraph("Baseline Verification", table_cell),
            Paragraph("Confirms 75% score (9/12) satisfies Tier 2", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_failing_score_class</code>", table_cell),
            Paragraph("Risk Tier Assignment", table_cell),
            Paragraph("Confirms < 50% score classifies as Tier 4", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_all_questions_valid</code>", table_cell),
            Paragraph("Answer Key Integrity", table_cell),
            Paragraph("Verifies 4 options per question & valid keys", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_score_report_serial</code>", table_cell),
            Paragraph("JSON Persistence Pipeline", table_cell),
            Paragraph("Validates JSON/TXT disk serialization", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ]
    ]
    t_test = Table(test_data, colWidths=[150, 130, 190, 70])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 6: GitHub Repository Overview (PEER-S-Awareness-Guard-Suite)", h2_style))
    story.append(load_screenshot("06_github_repo_overview.png", w=540, h=175))
    story.append(Spacer(1, 4))

    story.append(Paragraph("9. Enterprise Security Awareness & Culture Blueprint", h1_style))
    story.append(Paragraph(
        "<b>Strategic Principles for Human Defense:</b> In accordance with <b>NIST SP 800-50</b> and <b>ISO/IEC 27001:2022 Control A.6.3</b>, "
        "enterprises must discard ineffective annual lecture models in favor of continuous behavioral reinforcement: "
        "(1) <i>Monthly Micro-Learning:</i> Deliver 3-minute scenario simulations focusing on single vectors; "
        "(2) <i>Non-Punitive Reporting Culture:</i> Reward employees who report simulated attacks within 15 minutes, fostering psychological safety; "
        "(3) <i>Targeted Role-Based Curricula:</i> Tailor training to specific job risks (Finance -> BEC fraud; HR -> weaponized attachments); "
        "(4) <i>Continuous Metric Tracking:</i> Measure Phish-Prone percentage drops as a core CISO board metric.<br/>"
        "<b>Ethical Research Notice:</b> All scenarios, evaluation scripts, and simulated candidate profiles were constructed strictly for "
        "authorized educational training within an isolated sandbox environment.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Executive Lab Report PDF successfully compiled at:\n    {OUTPUT_PDF}")


if __name__ == "__main__":
    create_report()
