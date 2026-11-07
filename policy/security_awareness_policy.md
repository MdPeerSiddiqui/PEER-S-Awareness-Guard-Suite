# Enterprise Social Engineering Awareness & Training Policy

**Document ID:** SEC-POL-AWARENESS-2026-V1  
**Organization:** Sqrock IT Solutions / Cyber Defense & Human Risk Management  
**Standard Compliance:** NIST SP 800-50 (Building an Information Technology Security Awareness and Training Program), ISO/IEC 27001:2022 (Control A.6.3), CIS Controls v8 (Control 14: Security Awareness and Skills Training)  
**Author:** Mohammed Peer Siddiqui, Lead Security Intern  
**Approved By:** Chief Information Security Officer (CISO)  
**Effective Date:** November 2026  

---

## 1. Executive Summary & Purpose

The human element remains the single most targeted vulnerability across enterprise security perimeters. Regardless of technological controls (Next-Gen Firewalls, EDR, Email Gateways), social engineering threat actors exploit fundamental human cognitive biases—such as **authority, urgency, scarcity, fear, and helpfulness**—to bypass perimeter defenses.

This policy mandates enterprise-wide, scenario-based security awareness education and continuous testing to cultivate a resilient corporate security culture (the "Human Firewall") and reduce organizational Phish-Prone percentages below industry baselines (< 5%).

---

## 2. Core Social Engineering Vectors Addressed

```
+--------------------------------------------------------------------------+
|            ENTERPRISE SOCIAL ENGINEERING THREAT TAXONOMY                 |
+--------------------------------------------------------------------------+
|  1. Phishing & Spear Phishing                                            |
|     * Deceptive emails, lookalike domains (homoglyphs), urgency lures.   |
|     * Business Email Compromise (BEC) and executive whale-baiting.       |
|                                                                          |
|  2. Voice Phishing (Vishing) & Pretexting                                |
|     * Impersonated IT helpdesk, bank fraud alerts, authority pressure.   |
|                                                                          |
|  3. SMS Phishing (Smishing) & MFA Bypass                                 |
|     * Urgent parcel alerts, fake banking links, push notification fatigue.|
|                                                                          |
|  4. Physical Baiting & Removable Media Drops                             |
|     * Infected USB flash drives in parking lots, cafeterias, lounges.    |
|                                                                          |
|  5. Physical Infiltration (Tailgating & Shoulder Surfing)                |
|     * Unauthorized building entry, observing screens in public spaces.   |
|                                                                          |
|  6. Watering Hole & Digital Baiting Traps                                |
|     * Compromised supplier websites, trojanized software update alerts.  |
+--------------------------------------------------------------------------+
```

---

## 3. Mandatory Training & Assessment Framework

### 3.1. Onboarding & Continuous Annual Recertification
* Every new employee, contractor, and intern must complete the interactive Social Engineering Awareness Assessment within their first 14 business days.
* All active personnel must undergo mandatory annual recertification and quarterly simulated attack exercises (simulated phishing and vishing drills).

### 3.2. Minimum Passing Threshold & Scoring Matrix
* The minimum passing threshold for the assessment is **75% (9 out of 12 questions)**.
* Employees are categorized into four Risk Tiers based on their Threat Susceptibility Index (TSI):
  - **Tier 1 (90% - 100%): Cyber Defender (Elite)** — Exemplary security vigilance.
  - **Tier 2 (75% - 89%): Aware & Vigilant** — Passed core standards; low vulnerability.
  - **Tier 3 (50% - 74%): Vulnerable (Retraining Required)** — Mandatory 30-day retraining.
  - **Tier 4 (< 50%): High-Risk Liability** — Immediate supervisor notification & technical restrictions.

### 3.3. Zero-Penalty Reporting & "Report First" Culture
* Employees who immediately report real or simulated phishing attempts within 15 minutes of receipt receive formal recognition and "Defense Champion" badges.
* Reporting takes precedence over punitive action to foster transparent, non-punitive incident notification.

---

## 4. Incident Escalation Protocols

1. **Immediate Disconnect:** If an employee clicks an unverified link or inputs credentials, they must immediately disconnect the workstation from the corporate Wi-Fi/Ethernet.
2. **SOC Direct Notification:** The incident must be reported directly to `soc@sqrock.com` or via the one-click PhishAlarm button in Microsoft Outlook.
3. **No Forwarding:** Employees must NEVER forward suspicious phishing emails to colleagues; only forward directly to the designated SOC abuse mailbox.
