# Banking Technology, Digital Payments & IT Governance Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, SBI SO, FinTech)**

---

## 1. PAYMENT SYSTEMS IN INDIA COMPARISON

| Feature | UPI | IMPS | NEFT | RTGS |
| :--- | :--- | :--- | :--- | :--- |
| **Operated By** | NPCI | NPCI | RBI | RBI |
| **Settlement** | Real-Time Immediate | Real-Time Immediate | Batch-wise (Half-hourly) | Real-Time Gross Settlement |
| **Operating Hours** | 24x7x365 | 24x7x365 | 24x7x365 | 24x7x365 |
| **Minimum Limit** | ₹1 | ₹1 | ₹1 | **₹2,00,000** |
| **Maximum Limit** | ₹1 Lakh to ₹5 Lakh (varies) | ₹5 Lakh | No upper ceiling | No upper ceiling |
| **Identifier** | Virtual Payment Address (VPA) / Mobile | Mobile No. + MMID / Acc+IFSC | Account Number + IFSC | Account Number + IFSC |

---

## 2. CORE BANKING SOLUTION (CBS)
* **Definition:** Centralized software system that allows customers to operate their accounts from any branch of the bank ("Anywhere, Anytime Banking").
* **Leading Platforms:**
  * **Finacle:** Developed by Infosys (used by SBI, PNB, Canara Bank).
  * **BaNCS:** Developed by TCS.
  * **Flexcube:** Developed by Oracle.
* **Key Architecture Components:** Central Database cluster, High-Availability Hot Standby Disaster Recovery site (RPO $\approx 0$, RTO $< 30$ mins), Integration Middleware (MQ / ESB).

---

## 3. FINANCIAL MESSAGING STANDARDS
* **ISO 8583:** Legacy point-of-sale and ATM transaction interchange messaging format (bitmap-driven).
* **ISO 20022:** Modern XML/JSON financial industry messaging standard replacing SWIFT MT format. Supports rich, structured metadata to combat AML/CFT fraud.
* **SWIFT (Society for Worldwide Interbank Financial Telecommunication):** Global messaging network for international financial wire transfers.

---

## 4. MUST REMEMBER & REGULATORY COMPLIANCE
1. **IFSC (Indian Financial System Code):** 11 characters alphanumeric. First 4 characters = Bank code, 5th character = Reserved `0`, Last 6 characters = Branch code.
2. **MICR Code:** 9 digits numerical for cheque clearing. First 3 = City, Next 3 = Bank, Last 3 = Branch.
3. **CTS (Cheque Truncation System):** Electronic image of cheque sent to clearing house instead of physical movement.
4. **NPCI Payment Rails:** RuPay, UPI, IMPS, NACH, AePS (Aadhaar-enabled Payment System), BBPS (Bharat Bill Payment System).
