# NLP Application CS 1 24 Presentation Deck April 2026

**Original Document Pages**: 57

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
Course Owner and Lead Instructor
Dr. Chetana Gavankar, Ph.D,
BBIITTSS PPiillaannii IIT Bombay-Monash University Australia
Chetana.gavankar@pilani.bits-pilani.ac.in
PPiillaannii CCaammppuuss

---

### Page 2

BITS Pilani
Pilani Campus
Session 1
These slides are prepared by the instructor, with grateful
acknowledgement of James Allen and many others who made their
course materials freely available online.

---

### Page 3

Session Content
• Objective of course
• What will we learn in this course?
• Text books and Reference books
• Evaluation Plan
• Application areas of Natural Language Processing
BITS Pilani, Pilani Campus

---

### Page 4

Objective of course
CO1 Identify and describe algorithms for real life NLP Applications
CO2 Demonstrate understanding of algorithms by using different NLP tools
CO3 Apply NLP techniques in state of art applications like Machine Translation,
Information Extraction including Named entity recognition and Relation
extraction
CO4 Evaluate different approaches of implementing NLP applications along
with ethical considerations

---

### Page 5

What you will learn in this course
 Spellcheckers and Grammar checkers
 Question Answering and Conversational AI
 Knowledge Graph Applications
-Including RAG variants
 Machine Translation
 Information Extraction
 Sentiment Analysis and Opinion Mining
 All applications will be discussed using implementation of Hybrid
approaches of NLP(Statistical, Gen AI, Agentic AI etc.)
 Privacy & Ethics in NLP, Scalable & Efficient NLP Systems will also be
discussed
BITS Pilani, Pilani Campus

---

### Page 6

Text books and Reference books
T1 Speech and Language processing: An introduction to Natural Language
Processing, Computational Linguistics and speech Recognition by Daniel
Jurafsky and James H. Martin
R1 Manning and Schütze, Foundations of Statistical Natural Language
Processing, MIT Press. Cambridge, MA
R2 Neural Machine Translation by Philipp Koehn
R3 Knowledge Graphs Methodology, Tools and Selected Use Cases by Dieter
Fensel , Umutcan Şimşek, Kevin Angele, Elwin Huaman , Elias Kärle ,
Oleksandra Panasiuk , Ioan Toma, Jürgen Umbrich, and Alexander Wahler,
Springer 2019
Natural Language Toolkit. Bird and Loper, and other developers. Available
R4 for free at: – http://www.nltk.org/
BITS Pilani, Pilani Campus

---

### Page 7

Evaluation Plan
Name Weight
Quiz (best 2 out of 3) 10%
Assignment 1 and 2 25%
Mid-term Exam 30%
End Semester Exam 35%
Please note that the Assignments (Experiential Learning) will also include
situated learning aspect (related to area of work)
BITS Pilani, Pilani Campus

---

### Page 8

NLP Tasks and Applications
It’s a big world out there
And everyone uses language
Source Credit : 600.465 - Intro to NLP - J. Eisner
BITS Pilani, Pilani Campus

---

### Page 9

NLP Applications and Difficulty Level
BITS Pilani, Pilani Campus

---

### Page 10

Application areas
• Text-to-Speech & Speech recognition
• Natural Language Dialogue Interfaces to Databases
• Information Extraction
• Document Image Analysis
• Automatic Summarization (https://pypi.org/project/sumy/)
• Text Proof-reading – Spelling & Grammar
• Machine Translation
• Fake News and Cyberbullying Detection
• Monitoring Social Media
• Plagiarism detection
• Question Answering System (https://haystack.deepset.ai/)
• Sentiment Analysis (https://komprehend.io/sentiment-analysis)
NLP Applications span across domains like Healthcare, Finance, Manufacturing
and many more
BITS Pilani, Pilani Campus

---

### Page 11

Grammar and spellcheckers
BITS Pilani, Pilani Campus

---

### Page 12

Spell check
https://languagetool.org/
BITS Pilani, Pilani Campus

---

### Page 13

Spell check and Grammar check
slide courtesy of D. Yarowsky
BITS Pilani, Pilani Campus

---

### Page 14

Case Study: AI-Powered Communication
Enhancement
Challenges
•Traditional tools often miss contextual errors (e.g., your vs. you're, affect vs.
effect).
•Writers need more than just error correction; they need help communicating
effectively and appropriately for their audience and context.
SOLUTION
•Hybrid Approach: Combines rule-based checks, statistical NLP (analyzing
patterns in vast text data), and advanced DL/Transformers/Agentic AI
•Contextual Understanding: AI models analyze the entire sentence and
surrounding text to detect subtle errors and suggest contextually appropriate
words.
•Beyond Grammar: Employs NLP to analyze tone (e.g., confident, formal,
friendly), suggest improvements for clarity and conciseness, check for
plagiarism, and offer full-sentence rewrites.
•Continuous Learning: Models are constantly updated based on user
interactions and evolving language patterns
BITS Pilani, Pilani Campus

---

### Page 15

Question Answering and Conversational
AI
BITS Pilani, Pilani Campus

---

### Page 16

Case Study: AI-powered Question
Answering (QA) system
• 24/7 Demand, High volume, Long wait times
• Training: The AI was trained to accurately handle the top 100 most frequent
customer questions.
• Integration: The QA chatbot was launched, acting as the first point of
contact for all support inquiries.
• Handoff): A seamless "handoff" protocol was created, allowing the bot to
escalate complex or sensitive issues to a live human agent, along with the
full chat history.
BITS Pilani, Pilani Campus

---

### Page 17

AI Assistants
Contextual Assistant
Notification Assistant
FAQ Assistant
BITS Pilani, Deemed to be UniversitBy uITndSe rP Sielactnioin, 3P oilfa UnGi CC Aacmt, 1p9u5s6

---

### Page 18

AI Assistants
Personalized Assistant Autonomous Organization of
Assistants
• Group of AI assistants that know
• Assistant knows you much more in
every customer personally
detail
• Eventually run large parts of
• Quickly checks a few final things
company operations—from lead
before giving you a quote tailored
generation over marketing,
to your actual situation.
sales, HR, or finance
BITS Pilani, Deemed to be UniversitBy uITndSe rP Sielactnioin, 3P oilfa UnGi CC Aacmt, 1p9u5s6

---

### Page 19

Case Study: Automating Customer Support with
NLP Chatbots
Background
• HDFC Bank, one of India’s largest private sector banks, was facing
increasing customer service demands. Traditional support channels
(phone/email) were overburdened, resulting in delayed responses and
reduced customer satisfaction.
Problem
• High customer query volume (especially repetitive questions)
• Long response times
• High operational costs for customer support
• Solution: EVA – HDFC Bank’s AI Chatbot
BITS Pilani, Pilani Campus

---

### Page 20

Case Study: Automating Customer Support
with NLP Chatbots
• Key NLP Features Used
– Intent recognition: Classifies queries into categories (e.g., account
balance, card issues)
– Named Entity Recognition (NER): Identifies dates, transaction
amounts, account types
– Context management: Maintains conversational state for multi-turn
dialogues
– Multilingual support: Handles queries in English and Hindi
• Outcomes
– Handled over 2.7 million queries in the first year
– Resolved 85% of queries without human intervention
– Reduced average query response time to less than 0.4 seconds
– Improved customer satisfaction and reduced cost-per-query
• Challenges Faced
– Training the model on diverse and noisy real-world customer data
– Maintaining user trust (transparency and security)
– Escalating complex queries to human agents without losing context
BITS Pilani, Pilani Campus

---

### Page 21

RAG Applications
BITS Pilani, Pilani Campus

---

### Page 22

Retrieval-Augmented Generation
Core RAG Mechanism
RAG integrates large language models with retrieval from external sources to
improve response accuracy and reduce hallucinations.
Typical RAG Pipeline Steps
The pipeline includes document ingestion, embedding creation, similarity search,
and synthesizing responses.
Enterprise QA Case Study
RAG enables secure, efficient querying of internal knowledge bases, enhancing
employee productivity in enterprises.
Agentic AI Orchestration
Agentic AI autonomously manages when to retrieve or generate content,
optimizing user interactions based on intent.
BITS Pilani, Pilani Campus

---

### Page 23

Case study – Knowledge Graph
Applications in Agentic AI
Problem: Large tech company, faced challenges with internal information
access. Key data about projects, teams, expertise, and documentation was
scattered across various internal wikis, project management tools (like Jira),
employee directories, and shared drives.
Employees spent significant time searching for answers to complex questions
like:
• "Who worked on the authentication module for Project X and what were the
key technical documents?"
• "Which active projects are using Python and are related to our client Y?"
• "Find the design specification document for the UI redesign led by A’s team."
BITS Pilani, Pilani Campus

---

### Page 24

Enterprise Knowledge Graph (EKG)
Construction
Data Sources: Internal Wiki, Jira, HR Database, Code Repositories (metadata),
Document Management System.
Entities: Employee, Project, Team, Document, Skill, Client, CodeModule.
Relationships: WORKS_ON (Employee -> Project),
MEMBER_OF (Employee -> Team), AUTHORED (Employee -> Document),
RELATED_TO (Project -> Document), HAS_SKILL (Employee -> Skill),
SERVES_CLIENT (Project -> Client), IMPLEMENTS (CodeModule -> Project).
Population: NLP techniques (NER, Relation Extraction) were used to extract
entities and relationships from unstructured text (wikis, documents). Structured data
was mapped directly (HR DB, Jira)
BITS Pilani, Pilani Campus

---

### Page 25

Agentic AI System ("Ask Me”)
Core: An LLM (like GPT-4 or a fine-tuned open-source model)
•Tools:
•query_EKG: Takes a natural language query part and translates it into a
structured query (e.g., Cypher for Neo4j) to fetch data from the EKG.
•document_search: Performs keyword/semantic search over the document
system for full-text retrieval when needed.
•Capabilities: Planning, Tool Use, Reasoning, Synthesis.
BITS Pilani, Pilani Campus

---

### Page 26

Example of Enterprise KG application
User Query: "Who led the backend development for Project X and what recent
documents did they author?"
Agent's Plan:
1.Identify entities: "Project X" (Project), "backend development" (implicit Skill/Role), "documents"
(Document).
2.Find the team/person associated with "Project X" and "backend development lead" role via EKG. ->
Use query_EKG.
3.Once the person is identified (e.g., “A"), find recent documents AUTHORED by “A" via EKG. -> Use
query_EKG.
4.Synthesize the results into a natural language answer.
Execution:
•Agent calls query_EKG ("Find lead backend developer for Project X").
EKG returns "John Smith".
•Agent calls query_EKG ("Find recent documents authored by John Smith"). EKG returns a list:
["API_Design_v2.pdf", "Deployment_Strategy.docx"].
Agent's Response: “A led the backend development for Project X. Recent
documents he authored include 'API_Design_v2.pdf' and
Deployment_Strategy.docx'."
BITS Pilani, Pilani Campus

---

### Page 27

Machine Translation
BITS Pilani, Pilani Campus

---

### Page 28

Machine Translation
English to Hindi http://anglahindi.iitk.ac.in
Simple Sentences.
sarala vaakya .
Welcome to London.
landana men aapakaa svaagata hai.
There are some cases which are still pending.
NLP applications is an interesting course in MTech AIML of
BITS WILP
एनएलपी एप्लिके शन बिट्स WILP के एमटेक एआईएमएल में एक बिलचस्प कोसस
है
BITS Pilani, Pilani Campus

---

### Page 29

Machine Translation - Challenges
slide courtesy of D. Yarowsky
BITS Pilani, Pilani Campus

---

### Page 30

Machine Translation - Challenges
Capitalization
slide courtesy of D. Yarowsky
BITS Pilani, Pilani Campus

---

### Page 31

Machine Translation - Challenges
Word sense disambiguation
BITS Pilani, Pilani Campus

---

### Page 32

Machine Translation - Challenges
Text to speech
slide courtesy of D. Yarowsky
BITS Pilani, Pilani Campus

---

### Page 33

Case Study: Scaling Global Communications
•Custom Engines: The system was trained on specific content to create
custom models that understood its unique terminology and branding.
•Centralized Platform: All translation requests were funneled through the MT
platform, which was integrated into existing content systems.
•MT + Post-Editing: The platform was used to instantly translate content. For
high-visibility materials, human translators would then "post-edit" the AI's
output, rather than translating from scratch.
BITS Pilani, Pilani Campus

---

### Page 34

Information Extraction
BITS Pilani, Pilani Campus

---

### Page 35

Information Extraction
As a task: Filling slots in a database from sub-segments of text.
October 14, 2002, 4:00 a.m. PT
For years, Microsoft CorporationCEO Bill Gates railed
against the economic philosophy of open-source
software with Orwellian fervor, denouncing its communal
licensing as a "cancer" that stifled technological
innovation.
Today, Microsoft claims to "love" the open-source
NAME TITLE ORGANIZATION
concept, by which software code is made public to
IE
Bill Gates CEO Microsoft
encourage improvement and development by outside
programmers. Gates himself says Microsoft will gladly Bill Veghte VP Microsoft
disclose its crown jewels--the coveted code behind the Richard Stallman founder Free Soft..
Windows operating system--to select customers.
"We can be open source. We love the concept of shared
source," said Bill Veghte, a Microsoft VP. "That's a super-
important shift for us in terms of code access.“
Richard Stallman, founder of the Free Software
Foundation, countered saying…
Slide from Chris Brew, adapted from slide by William Cohen
BITS Pilani, Pilani Campus

---

### Page 36

Phrase Types to Identify for IE
Regular set
Closed set
U.S. states U.S. phone numbers
Phone: (413) 545-1323
He was born in Alabama…
The CALD main office can be
The big Wyoming sky…
reached at 412-268-1299
Ambiguous patterns,
Complex pattern
needing context and
U.S. postal addresses many sources of evidence
University of Arkansas Person names
P.O. Box 140 …was among the six houses
Hope, AR 71802 sold by Hope Feldman that year.
Headquarters: Pawel Opalinski, Software
1128 Main Street, 4th Floor Engineer at WhizBang Labs.
Cincinnati, Ohio 45210
Slide from Chris Brew, adapted from slide by William Cohen
BITS Pilani, Pilani Campus

---

### Page 37

Deeper Information Extraction
1. Coreference resolution (within a document)
2. Entity linking (across documents)
3. Event extraction and linking
4. Knowledge base population (KBP)
BITS Pilani, Pil3an7i Campus

---

### Page 38

Named Entity Recognition
CHICAGO (AP) — Citing high fuel prices, United Airlines said Friday it has
increased fares by $6 per round trip on flights to some cities also served by
lower-cost carriers. American Airlines, a unit AMR, immediately matched the
move, spokesman Tim Wagner said. United, a unit of UAL, said the
increase took effect Thursday night and applies to most routes where it
competes against discount carriers, such as Chicago to Dallas and Atlanta
and Denver to San Francisco, Los Angeles and New York.
Slide from Jim Martin
BITS Pilani, Pilani Camp3u8s

---

### Page 39

NE Types
Slide from Jim Martin
BITS Pilani, Pilani Camp3u9s

---

### Page 40

Example applications for IE
• Classified ads
• Restaurant reviews
• Bibliographic citations
• Appointment emails
• Legal opinions
• Papers describing clinical medical studies
• …
• Adding facts to the semantic web
BITS Pilani, Pilani Campus

---

### Page 41

Sentiment Analysis
BITS Pilani, Pilani Campus

---

### Page 42

Sentiment classification
What features of the text could help predict # of stars?
?
(e.g., using a log-linear model) How to identify more?
Are the features hard to compute? (syntax? sarcasm?)
example from amazon.com, thanks to Delip Rao
BITS Pilani, Pil4an2i Campus

---

### Page 43

Other text categorization tasks
• Is it spam? (see features)
• What grade, as an answer to this essay question?
• Is it interesting to this user?
– News filtering; helpdesk routing
• Is it interesting to this NLP program?
– Skill classification for a digital assistant!
– If it’s Spanish, translate it from Spanish
– If it’s subjective, run the sentiment classifier
– If it’s an appointment, run information extraction
• Where should it be filed?
– Which mail folder? (work, friends, junk, urgent ...)
– Yahoo! / Open Directory / digital libraries
BITS Pilani, Pil4an3i Campus

---

### Page 44

Case Study: AI-powered sentiment
analysis platform
Data Aggregation:
•The tool pulled all reviews into a single dashboard.
Aspect-Based Sentiment:
•The AI didn't just label a review "Positive" or "Negative.“
• It identified specific topics (aspects) and the sentiment for each.
Real-time Dashboard:
• Operations managers could instantly filter feedback by property, region, date,
and topic.
BITS Pilani, Pilani Campus

---

### Page 45

Evaluation of NLP Applications
BITS Pilani, Pilani Campus

---

### Page 46

Machine Translation Evaluation
•BLEU (Bilingual Evaluation Understudy):
•Compares n-gram overlaps between machine output and human reference
translations.
•Most widely used but penalizes creative phrasing.
•METEOR:
•Considers synonyms, stemming, and paraphrases — more flexible than BLEU.
•ROUGE:
•Recall-oriented; useful when coverage matters more than precision.
•TER (Translation Edit Rate):
•Measures edits needed to convert MT output to a reference translation.
•chrF:
•Character-level F-score; works well for morphologically rich languages.
•COMET / BERTScore:
•Neural metrics using contextual embeddings; better correlation with human
judgment.
BITS Pilani, Pilani Campus

---

### Page 47

Spellcheck and Grammar check
evaluation measure
• Precision: Of all flagged errors, how many are real?
• Recall: Of all real errors, how many were caught?
• F₀.₅ Score: Weighs precision higher than recall (used in CoNLL shared
tasks).
• ERRANT: Framework for classifying and scoring grammatical error
corrections by error type (spelling, tense, agreement, etc.).
• MaxMatch (M²) Scorer: Standard for GEC (Grammatical Error Correction)
benchmarks.
BITS Pilani, Pilani Campus

---

### Page 48

IE evaluation measures
• Precision, Recall, F1-Score: Standard for entity/relation extraction tasks.
• Exact Match vs. Partial Match: Strict (full span must match) vs. lenient
(overlap accepted).
• MUC Scores (MUC-5/6/7): Specifically for co-reference resolution and slot
filling.
• Entity-level F1: Evaluates complete entity spans, not individual tokens.
BITS Pilani, Pilani Campus

---

### Page 49

Sentiment Analysis evaluation measures
• Accuracy: Overall correct classifications.
• Macro F1: Averages F1 across all classes — important for imbalanced
datasets.
• Weighted F1: Accounts for class frequency.
• Confusion Matrix: Reveals which sentiments are misclassified.
BITS Pilani, Pilani Campus

---

### Page 50

NLP Applications evaluation measures
Human Eval
Application Key Metric Main Challenge
Needed?
Fluency vs.
Machine
BLEU, COMET Yes adequacy trade-
Translation
off
Grammar Avoiding over-
F₀.₅, ERRANT Partly
Checking correction
Information Nested entities,
F1 (Exact/Partial) Sometimes
Extraction relations
Sentiment Macro F1, Sarcasm, domain
Rarely
Analysis Accuracy shift
BITS Pilani, Pilani Campus

---

### Page 51

Security, Privacy, Ethics, and
Scalable NLP Systems
Security and Privacy Concerns
NLP systems must address risks like prompt injection, data leakage,
and model misuse to protect user data and maintain trust.
Ethics and Fairness
Bias mitigation, fairness evaluation, and regulatory compliance are
crucial for ethical and responsible AI adoption in NLP.
Scalable NLP Architectures
Efficient model architectures, distillation, quantization, and robust
serving ensure low latency and cost-effectiveness at scale.
Performance Monitoring and Evaluation
Continuous monitoring, logging, and system evaluation maintain
performance and trustworthiness in deployed NLP systems.
BITS Pilani, Pilani Ca

---

## Understanding in Layman's Terms

## 📚 Understanding NLP Application CS 1 24 Presentation Deck April 2026

### 1. **Concept Explanation**
This section breaks down the core concepts of NLP Application CS 1 24 Presentation Deck April 2026 in simple, understandable terms.

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

NLP Application CS 1 24 Presentation Deck April 2026 is like teaching your robot friend to understand and talk better, just like you learn to understand new words every day!

### 4. **Explanation for a 30-Year-Old 👨**

As a professional, you should understand NLP Application CS 1 24 Presentation Deck April 2026 as:

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
- The fundamental principles of NLP Application CS 1 24 Presentation Deck April 2026
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

**Total Original Pages**: 57
**Markdown Pages**: 25+
**Format**: Educational markdown with multiple explanation levels

