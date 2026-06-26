# NLP Applications Session 7-Privacy and Ethics in NLP Applications

**Original Document Pages**: 32

## 📖 Table of Contents

1. [Original Content](#original-content)
2. [Understanding in Layman's Terms](#understanding-in-laymans-terms)
3. [Key Concepts](#key-concepts)
4. [Real-World Applications](#real-world-applications)

---

## Original Content

### Page 1

Natural Language Processing
Applications
Dr. Chetana Gavankar, Ph.D,
IIT Bombay-Monash University Australia
BITS Pilani
Chetana.gavankar@pilani.bits-pilani.ac.in
Pilani Campus

---

### Page 2

BITS Pilani
Pilani Campus
Session 7: Privacy and Ethics in NLP
Applications
These slides are prepared by the instructor, with grateful acknowledgement of
Prof. Dan Jurafsky and many others who made their course materials freely
available online.

---

### Page 3

Agenda
01 Introduction to Privacy & Ethics in NLP 02 Data Issues — Collection, Consent & Bias
Deployment Issues — Safety &
03 Model Issues — Fairness & Explainability 04
Accountability
05 Real-World Use Case Examples 06 Tools, Techniques & Production-Ready Setup

---

### Page 4

Why Privacy & Ethics Matter in NLP
Massive Data Usage
82%
NLP systems ingest emails, chats, medical records — highly personal
data
of users worry about AI privacy
Re-identification Risk
Models can memorize and leak PII from training data $20M
max GDPR fine per violation
Bias & Discrimination
Biased training data leads to discriminatory outputs at scale
4%
Regulations
of global turnover penalty
GDPR,DPDP (India) CCPA(USA), EU AI Act impose strict obligations on AI
deployments

---

### Page 5

Data Issues
Consent & Collection Dataset Bias PII & Leakage
• Scraping public data
Underrepresented minorities in
Names, emails, SSNs in training data
corpora
without explicit
consent
Historical bias baked into text Model memorization of rare examples
• No opt-out
mechanisms for data
subjects Label bias from annotators Inference attacks on embeddings
• Unclear data
retention policies
Geographic & language imbalance No data provenance tracking
• Lack of purpose
limitation

---

### Page 6

Model Issues
Demographic Parity Violations Key Fairness Metrics
Sentiment models score identical text differently based on inferred gender,
race, or religion
Demographic Parity
Equal positive rates across groups
Lack of Explainability
Equal Opportunity
Black-box transformers provide no rationale — impossible to audit for
compliance (GDPR Art. 22) Equal true positive rates
Equalized Odds
Training Data Memorization
Equal TPR & FPR across groups
Large LLMs can regurgitate verbatim PII seen during training via extraction
attacks
Counterfactual
Prediction unchanged if group changes
Calibration & Hallucination
Individual Fairness
Overconfident predictions mislead decision-makers; hallucinated facts cause
downstream harm
Similar people treated similarly

---

### Page 7

Deployment Issues
No Output Filtering Lack of Monitoring Audit Trail Gaps
Deployed models may generate harmful, Absence of drift detection, fairness
No logging of model decisions — unable to
hateful, or toxic outputs without dashboards, or anomaly alerting post-
explain outcomes during regulatory audits
guardrails deployment
Access Control Failures Adversarial Attacks Vendor Lock-in Risk
Broad API access without authentication; Prompt injection, jailbreaks, and Closed-source models offer no visibility
sensitive inference exposed to adversarial inputs bypass safety into data handling, updates, or bias
unauthorized users mechanisms corrections

---

### Page 8

Tools & Techniques
Privacy & PII Fairness & Bias
Microsoft Presidio PII detection & anonymization in text IBM AI Fairness 360 Bias detection & mitigation toolkit
spaCy + custom NER Named entity masking pipeline Fairlearn (Microsoft) Fairness constraints in model training
Google DLP API Automated PII scanning at scale What-If Tool (Google) Visual model fairness exploration
Differential Privacy (DP-
Training with privacy guarantees Aequitas Audit tool for ML pipelines
SGD)
Explainability Safety & Red-Teaming
Shapley value-based feature
SHAP Garak LLM vulnerability scanning
importance
Output validation & constraint
LIME Local model-agnostic explanations Guardrails AI
enforcement
Captum (PyTorch) Gradient-based interpretability LangKit / NeMo Guardrails Toxicity & jailbreak detection
Attention visualization for
BertViz Rebuff Prompt injection detection
transformers

---

### Page 9

Production-Ready Privacy & Ethics Setup
1 2 3 4 5
Data Pipeline Model Training Evaluation Deployment Monitoring
PII scrubbing (Presidio) Fairness constraints Demographic parity Guardrails output filter Drift detection
Consent validation Bias audit (AIF360) SHAP / LIME reports Rate limiting & auth Fairness dashboards
DP-SGD training Calibration checks Red-team testing Audit logging (SIEM) Incident response SOP
Data lineage logging Model cards Adversarial robustness Rollback strategy GDPR deletion pipeline

---

### Page 10

Ethics & Privacy Governance Checklist
Fairness metrics evaluated across demographic
Legal basis established for all training data
groups
PII identified and anonymized or removed Explainability report generated (SHAP/LIME)
Data Model
Data retention & deletion policy documented Model card published with limitations & risks
Provenance and lineage tracked throughout
Differential privacy applied where feasible
pipeline
Output safety filters and guardrails in place Automated drift & fairness monitoring running
Access controls and authentication enforced Regular red-team / adversarial testing scheduled
Deploy
Ongoing
ment All decisions logged with timestamp & model
GDPR right-to-erasure pipeline implemented
version
Incident response playbook documented Ethics review board approval obtained

---

### Page 11

Privacy and Ethics in NLP Applications
• Personal and sensitive text data can be embedded in corpora, logs, and
prompts.
• Fairness concerns arise when demographic, dialect, or domain
representation is uneven.
• Ethical NLP requires consent awareness, traceability, transparency, and
human accountability.
• Evaluation should extend beyond accuracy to include harm, bias, and
misuse scenarios.
Connect ethics to the full NLP Application lifecycle, not only model training.

---

### Page 12

Data Issues
• Noisy, duplicated, or stale training data can reduce generalization and
trustworthiness.
• Annotation guidelines may encode human subjectivity or social
stereotypes.
• Data imbalance can suppress minority dialects, languages, or rare but
critical intents.
• Data governance must address provenance, retention, consent, and data
minimization.

---

### Page 13

Model Issues
• Models can amplify patterns present in data, including harmful
stereotypes.
• Large models may hallucinate fluent but unsupported answers.
• Explainability remains limited for many deep neural architectures.
• Model behavior can shift across domains, languages, and adversarial
inputs.

---

### Page 14

Deployment Issues
• Latency, scalability, and cost constraints affect user experience and
operational viability.
• Monitoring is essential for drift, abuse, privacy leakage, and safety
regressions.
• Fallback design and human escalation are necessary in high-stakes
workflows.
• Policies for logging, access, and red-team testing must be part of
deployment governance.

---

### Page 15

Diagram: Ethical Risk Lifecycle in NLP Applications
Data Collection Annotation Model Training Evaluation Deployment
PII, consent, label bias, sensitive bias amplification, fairness, monitoring, abuse,
representativeness categories leakage explainability, governance
robustness
Governance spans the entire lifecycle
Bad Data → Biased Labels → Biased Model → Unfair Decisions → Harm

---

### Page 16

Diagram: Deployment Risk Stack for NLP Systems
Controls
Access control
Safety filters
Application Layer: UX, misuse, prompt injection
Red-team testing
Continuous monitoring
Model Layer: hallucination, drift, explainability
Data Layer: privacy, retention, stale knowledge
Infrastructure Layer: latency, scaling, logging, security

---

### Page 17

Risk Stack in NLP Systems
• Infrastructure Layer (scaling, security, logging)
Example: OpenAI / ChatGPT outages & rate limits
High demand leads to latency issues and degraded user experience
Scalability failures directly impact usability and trust
• Data Layer (privacy, retention, stale knowledge)
Example: Samsung data leak via ChatGPT (2023)
Employees pasted sensitive code into chatbot
unintended data exposure
Poor data handling policies → privacy violations
• Model Layer (hallucination, drift, explainability)
Example: Google Bard factual errors during demo
→ Incorrect astronomical fact caused credibility issues
–Hallucinations can damage trust, especially in high-stakes domains
• Application Layer (misuse, prompt injection)
–Example: Prompt injection attacks on LLM apps
→ Malicious inputs bypass safeguards and extract hidden instructions
–User-facing systems are vulnerable to adversarial misuse

---

### Page 18

Discussion
1 If a model is accurate overall but fails disproportionately on one user group, is deployment acceptable?
2 What should be logged for debugging without violating privacy or retaining excessive personal data?
3 Who is accountable when an NLP assistant gives harmful advice in a high-stakes domain?
Should organizations prefer smaller, auditable models when explainability is more important than
4
raw accuracy?

---

### Page 19

Discussions:
Is deployment acceptable
–“Deploy the model (accuracy is acceptable)”
–“Do NOT deploy (fairness issues)”

---

### Page 20

Discussions: What to Log?
What to log without violating privacy?

---

### Page 21

Discussions: What to Log?
• Safe to log:
–Model outputs
–Timestamp
–Model version
–Error types / system metrics
• Avoid logging:
–Raw user inputs containing PII
–Full conversations (unless anonymized)
–Sensitive personal identifier
• Key idea:
Log for debugging, but minimize personal data exposure

---

### Page 22

Discussions: Accountability
Responsibility for harmful outputs
Ask:
• Who is responsible?
• Developer
• Company
• User

---

### Page 23

Discussions: Accountability
Primary accountability: Organization deploying the system
Shared responsibility:
• Developers → design & safeguards
• Company → deployment & monitoring
• Regulators → compliance enforcement
• Key idea:
Accountability is distributed but led by the deploying entity

---

### Page 24

Discussion:
Smaller vs large models?
Prefer explainable models when:
• Healthcare
• Finance
• Legal decision-making
Prefer large models when:
• Low-risk applications (chatbots, recommendations)
Key idea:
• Tradeoff between accuracy vs interpretability depends on
risk level

---

### Page 25

Activity: Model Choice Scenario
• Scenario:
• Option A: Black-box LLM (high accuracy)
• Option B: Smaller interpretable model
• Task: Choose for-
• Healthcare NLP system
• Chatbot for customer support
• Expected Insight:
• High-stakes → explainability preferred
• Low-stakes → accuracy acceptable

---

### Page 26

Activity: Accountability mapping
Scenario:
An NLP healthcare chatbot gives incorrect medical advice, causing harm to a
user.
Task:
1. Who should be responsible?
- Developer
- Company
- User
- Regulator

---

### Page 27

Case study: Chatbot data leaks
Case: A chatbot trained on customer data leaks sensitive user
information.
Task:
1. Which stage caused the issue? (Data / Model /
Deployment)
2. What risks are involved? (privacy, bias, deployment, etc.)
3. Suggest fixes

---

### Page 28

Case study: Chatbot data leaks
Stage →
Data Collection + Training
Risk → PII leakage / memorization
Fix →
• PII scrubbing (Presidio)
• Differential privacy
Monitoring →
Output filters + red-teaming

---

### Page 29

Real-World Use Case Examples
Data & Model
Amazon Rekognition / NLP Hiring Tool GPT-3 / ChatGPT Memorization PII Leakage
Bias
Amazon's ML hiring tool trained on 10 years of male-dominated Researchers extracted verbatim personal data (emails, phone
resumes — systematically downgraded applications from women numbers) from GPT-3 via targeted extraction prompts
Differential privacy & PII scrubbing must be applied before training
Training data must reflect desired future parity, not historical bias
at scale
Deployment
Clearview AI Consent Violation Twitter Sentiment API
Fairness
Scraped 3B+ facial images without consent for a facial recognition Twitter's photo-cropping algorithm (CLIP) consistently cropped out
NLP pipeline; fined €20M in Italy, banned in EU Black faces in favor of white faces
Data sourcing must include legal basis — consent or legitimate Continuous fairness audits across demographic groups are
interest — under GDPR required post-deployment

---

### Page 30

Industry Case Deep Dive: Amazon Recruiting Tool
Core issue: Bias in model outcomes
What happened Teaching takeaways
The system reportedly learned patterns Dataset history matters as much as model
from historical hiring data rather than an architecture.
unbiased notion of merit. Fairness review should be part of feature
Past data can reflect organizational design, threshold setting, and pre-deployment
imbalance, which then appears as a sign-off.
predictive signal to the model. Human review must challenge model outputs
The case is widely used to teach why rather than merely approve them.
accuracy alone is not a sufficient
deployment criterion.

---

### Page 31

Industry Case Deep Dive: Google Translate and Gender Stereotypes
Core issue: Stereotypical outputs driven by data patterns
What happened Teaching takeaways
Translation systems can mirror social stereotypes Evaluation must include representative
present in multilingual text corpora. prompt sets, not just random samples.
Occupation-related translations are often Bias testing should cover occupations,
discussed in class because they reveal how bias pronouns, dialect variation, and low-
appears in a familiar application. resource settings.
The example helps separate linguistic ambiguity Mitigation can involve balanced examples,
from social bias in training data. constrained decoding, or post-processing
policies.

---

### Page 32

Summary
• Data stage:
–Ensure PII removal and user consent
• Training stage:
Apply differential privacy to prevent memorization
• Model stage:
–Check for bias and data leakage
• Deployment stage:
–Use guardrails and access control
• Monitoring stage:
–Perform continuous auditing and data deletion support
Privacy and ethics must be integrated across the entire NLP lifecycle, not
just at one stage

---



---

## Understanding in Layman's Terms

## 📚 Understanding NLP Applications Session 7-Privacy and Ethics in NLP Applications

### 1. **Concept Explanation**
This section breaks down the core concepts of NLP Applications Session 7-Privacy and Ethics in NLP Applications in simple, understandable terms.

A comprehensive explanation of the concepts covered in this document.

### 2. **Intuition & Real-World Examples**

#### What does this mean in real life?
Think about your daily experiences:
- **Example 1**: When you use a spell checker in Microsoft Word that underlines misspelled words in red, that's an example of text processing.
- **Example 2**: When your phone's autocomplete suggests the next word you might want to type, it's using prediction models similar to concepts in this topic.
- **Example 3**: When Netflix recommends movies based on your watch history, it uses similar computational techniques.

#### Why does this matter?
Understanding these concepts helps us:
- Communicate more effectively with technology
- Build better applications that understand human language
- Solve real-world problems that involve text and language

### 3. **Explanation for a 5-Year-Old 👶**

Imagine you have a toy robot that wants to be your friend. To be friends with you:
- The robot needs to understand what you're saying (just like your parents listen to you)
- It needs to know lots of words and what they mean
- It needs to learn from talking to many children
- Sometimes it makes mistakes, but it learns from them
- It tries really hard to give you the right answer

NLP Applications Session 7-Privacy and Ethics in NLP Applications is like teaching your robot friend to understand and talk better, just like you learn to understand new words every day!

### 4. **Explanation for a 30-Year-Old 👨**

As a professional, you should understand NLP Applications Session 7-Privacy and Ethics in NLP Applications as:

**Technical Foundation:**
- These techniques form the backbone of modern Natural Language Processing
- They involve machine learning algorithms that process textual data at scale
- Understanding them helps in building production-grade NLP systems

**Business Impact:**
- Enables better customer service through chatbots and automated systems
- Improves content recommendation engines
- Reduces operational costs through automation
- Enhances user experience through better language understanding

**Career Relevance:**
- Critical skill for NLP engineers, ML specialists, and data scientists
- Understanding these concepts helps in troubleshooting complex language models
- Essential for building enterprise-level language applications
- Important for staying current in the rapidly evolving AI/ML landscape

**Professional Considerations:**
- Privacy implications when processing personal text data
- Bias detection and mitigation in language models
- Scalability and performance optimization
- Integration with existing enterprise systems

---


## Key Concepts

### What You'll Learn:
- The fundamental principles of NLP Applications Session 7-Privacy and Ethics in NLP Applications
- How these concepts apply in practice
- Real-world examples and use cases
- Why these concepts matter in the industry

### Core Ideas:
1. **Foundation**: Understanding the basic building blocks
2. **Application**: How these concepts are used in practice
3. **Importance**: Why professionals need to understand this
4. **Future**: How these concepts are evolving

---

## Real-World Applications

### Industry Use Cases:
- **Healthcare**: Analyzing medical texts and patient records
- **Finance**: Processing financial documents and news sentiment
- **E-commerce**: Understanding customer reviews and feedback
- **Social Media**: Moderation and content understanding
- **Customer Service**: Automated support and chatbots

### Hands-On Examples:
- Building a simple text classifier
- Creating a sentiment analyzer
- Implementing spell checking
- Developing question-answering systems

---

## 🎯 Key Takeaways

1. These concepts are fundamental to modern AI and NLP
2. They have real-world applications across many industries
3. Understanding them prepares you for the future of technology
4. Practice and hands-on experience are crucial for mastery

---

## 📚 Next Steps

To deepen your understanding:
1. Review the original content multiple times
2. Try implementing simple versions of these concepts
3. Explore real-world applications
4. Practice with real datasets
5. Join communities of NLP practitioners

---

## 🔗 Related Topics

- Natural Language Processing Basics
- Machine Learning Fundamentals
- Text Processing and Analysis
- Deep Learning for NLP
- Transformer Models and Attention Mechanisms

---

**Total Original Pages**: 32
**Markdown Pages**: 25+
**Format**: Educational markdown with multiple explanation levels

