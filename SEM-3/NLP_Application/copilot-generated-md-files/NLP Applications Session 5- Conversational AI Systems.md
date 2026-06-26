# NLP Applications Session 5- Conversational AI Systems

**Original Document Pages**: 41

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
BBIITTSS PPiillaannii
Chetana.gavankar@pilani.bits-pilani.ac.in
PPiillaannii CCaammppuuss

---

### Page 2

BITS Pilani
Pilani Campus
Session 5:
Conversational AI
These slides are prepared by the instructor, with grateful
acknowledgement of Prof. Dan Jurafskyand many others who made
their course materials freely available online.

---

### Page 3

Session Content
01 Conversational AI Fundamentals
02 Large Language Models (LLM)
03 Retrieval-Augmented Generation (RAG)
04 Agentic AI Systems
05 Evaluation Frameworks
06 Production Tech Stack
BITS Pilani, Pilani Campus

---

### Page 4

AI Assistants
Contextual Assistant
Notification Assistant
FAQ Assistant
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 5

AI Assistants
Autonomous Organization of Assistants
Personalized Assistant
• Group of AI assistants that know every
• Assistant knows you much more in detail
customer personally
• Quickly checks a few final things before
• Eventually run large parts of company
giving you a quote tailored to your
operations—from lead generation over
actual situation.
marketing, sales, HR, or finance
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 6

Conversational AI Approaches
and real world applications
Approach Short Summary Real-World Applications
• IVR phone menus • Banking/telecom
Fixed rules, decision trees,
Rule-Based FAQ bots • HR onboarding flows • Simple
predictable responses
customer support chat
Retrieves best match from a • Enterprise FAQ search • E-commerce
IR-Based knowledge base using keywords or support • Airline & telecom chatbots •
vector search Government info portals
Seq2Seq / early Transformer • Smart reply suggestions • Domain-
Deep Learning (Pre-LLM) models that generate basic specific assistants • Simple virtual
responses assistants
Large pretrained models with • Advanced chatbots • Coding assistants •
LLM-Based reasoning, context understanding, Legal/medical Q&A (supervised) •
and generative ability Enterprise RAG systems
• Travel booking agents • Financial
LLM + tools + memory →
analysis bots • Customer service copilots
Agentic AI autonomous task execution and
• DevOps/coding agents • Workflow
multi-step planning
automation
BITS Pilani, Pilani Campus

---

### Page 7

QA versus conversational AI
Aspect Question Answering (QA) Conversational AI
A system that engages in a
A system that answers
Definition multi-turn dialogue with
specific user questions.
users.
Broad: Dialogue, intent
Narrow: Answering
Scope detection, emotion,
questions (often factual).
context, etc.
“I’m planning a trip.” →
“What is the capital of
Example Task “Great! Where are you
France?” → “Paris”
going?”
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 8

Conversational Agents
AKA Dialog Agents
• Phone-based Personal Assistants
• SIRI (Apple), Alexa (Amazon),
• Cortana (Microsoft), Google Assistant
• Talking to your car, Pay bills…
• Sales, Marketing, Insurance….
• Clinical uses for mental health, Nurses,
Dr. Bot
• Lawyer bots
• Chatting for fun, Mr. FriendBot
BITS Pilani, Pilani Campus

---

### Page 9

Context and Conversation
in Virtual Assistants like Siri
• Coreference helps resolve ambiguities
U: “Book a table at Il Fornaio at 7:00 with my mom”
U: “Also send her an email reminder”
• Clarification questions:
U: “Chicago pizza”
S: “Did you mean pizza restaurants in Chicago
or Chicago-‐style pizza?”
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 10

Conversation Characteristics
Turns
– dialogue is a sequence of turns
– C1: I need to travel in May.
A1: And, what day in May did you want to travel?
C2: OK uh I need to be there for a meeting that’s from the 12th to the 15th.
A2: And you’re flying into what city? C3: Seattle.
Speech Acts of Dialog Acts:
– Constatives: answering, claiming, confirming, denying, disagreeing, stating)
– Directives: to do something (advising, asking, forbidding, inviting, ordering,
requesting)
– Commissives: committing the speaker to some future course of action
(promising, planning, vowing, betting, opposing)
– Acknowledgments: apologizing, greeting, thanking, accepting an
acknowledgment
BITS Pilani, Pilani Campus

---

### Page 11

Challenges of Dialog Systems
Grounding:
– acknowledging that the hearer has understood the speaker
Dialog Structure:
– QUESTIONS set up an expectation for an ANSWER. PROPOSALS are followed
by ACCEPTANCE (or REJECTION). COMPLIMENTS (“Nice jacket!”) often give
rise to adjacency pair DOWNPLAYERS (“Oh, this old thing?”). These pairs,
called adjacency pairs are composed of a first pair part and a second pair part
Clarification/correction question
– Which can form a sub dialogue between a REQUEST and a RESPONSE
– Ex: User: What do you have going to UNKNOWN WORD on the 5th?
System: Let’s see, going where on the 5th?
Inference:
–A1: And, what day in May did you want to travel? C2: OK uh I need to be there for
a meeting that’s from the 12th to the 15th. Notice that the client does not in fact
answer the agent’s question. The client merely mentions a meeting at a certain time
BITS Pilani, Pilani Campus

---

### Page 12

Conversational AI journey
ELIZA (1960s): pattern matching.
1990s–2000s: statistical dialogue models.
2010s: deep learning & seq2seq.
2020+: transformers & LLMs, Agentic AI
BITS Pilani, Pilani Campus

---

### Page 13

Architectures
 Rule-based
– Pattern-action rules (Eliza)
 Corpus-based
– Information Retrieval
– Neural network encoder-decoder
– Transformers and LLM
– Agentic AI
BITS Pilani, Pilani Campus

---

### Page 14

Eliza: Weizenbaum (1966)
Dialog in Green are by Eliza system.
Men are all alike.
IN WHAT WAY
They're always bugging us about something or other.
CAN YOU THINK OF A SPECIFIC EXAMPLE
Well, my boyfriend made me come here.
YOUR BOYFRIEND MADE YOU COME HERE
He says I'm depressed much of the time.
I AM SORRY TO HEAR YOU ARE DEPRESSED
...
WHO ELSE IN YOUR FAMILY TAKES CARE 0F YOU?
My father
YOUR FATHER
BITS Pilani, Pilani Campus

---

### Page 15

Woebot
• Chatbot for delivering Cognitive Behavior Therapy via
brief daily conversations
– Little decision tree of language and menu responses
"What's going on in your world right now?"
"How are you feeling?"
In response to endorsed loneliness:
"I'm so sorry you're feeling lonely. I guess we all feel a
little lonely sometimes"
• In a 2-week experiment seemed to reduce depression,
but not anxiety
Fitzpatrick, Darcy, Vierhile, 2017. Delivering Cognitive Behavior Therapy to Young Adults
with Symptoms of Depression and Anxiety Using a Fully Automated Conversational Agent
(Woebot): A Randomized Controlled Trial. JMIR Ment Health 4:2.
BITS Pilani, Pilani Campus

---

### Page 16

Simple Chatbot – Rule based Demo
• NLTK has a module, nltk.chat, which simplifies building
Chatbots
• Chat: This is a class that has all the logic that is used
by the chatbot.
• Reflections: This is a dictionary that contains a set of
input values and its corresponding output values. It is
an optional dictionary that you can use. You can also
create your own dictionary in the same format as
below and use it in your code.

---

### Page 17

IR-based chatbots
• Idea: Mine conversations of human chats
or human-machine chats
– Microblogs: Twitter or Weibo
– Movie dialogs
• Cleverbot (Carpenter 2017
http://www.cleverbot.com)
BITS Pilani, Pilani Campus

---

### Page 18

A Cleverbot conversation
User: Do you like Doctor Who?
Cleverbot: Yes, so funny
User: What's your favorite show?
Cleverbot: I don't have one
User: What's your name?
Cleverbot: Jason I already told you.
User: No your real name.
Cleverbot: Stephanie IS my real name.
User: I thought it was Jason?
Cleverbot: How did you come to that conclusion.
User: Because you said so.
Cleverbot: I have to do my homework.
BITS Pilani, Pilani Campus

---

### Page 19

Two IR-based chatbot architectures
1. Return the response to the most similar turn
– Take user's turn (q) and find a (tf-idf) similar turn t in the corpus C
q = "do you like Doctor Who"
t' = "do you like Doctor Strangelove"
– Grab whatever the response was to t.
Yes, so funny
2. Return the most similar turn
Do you like Doctor Strangelove
BITS Pilani, Pilani Campus

---

### Page 20

IR-based models of chatbots
• Also fine to use other features like user
features, or prior turns
• Or non-dialogue text
– COBOT chatbot (Isbell et al., 2000)
• sentences from the Unabomber Manifesto
by Theodore Kaczynski, articles on alien
abduction, the scripts of “The Big
Lebowski” and “Planet of the Apes”.
– Wikipedia text
BITS Pilani, Pilani Campus

---

### Page 21

IR based Chatbot Demo
• Web scraping using Python
• Retrieve Web page on Chatbots
• Bot answers questions related to the Web page
content.

---

### Page 22

Components of
Conversational AI systems
BITS Pilani, Pilani Campus

---

### Page 23

Components of
Conversational AI systems
Building blocks of systems that understand and generate natural language
Natural Language Understanding (NLU) Dialogue Management Natural Language Generation (NLG)
Intent classification & slot filling Conversation state tracking Template-based generation
Named Entity Recognition (NER) Rule-based & neural policy Neural text generation
Semantic parsing Context window management Persona & tone consistency
Coreference resolution Multi-turn coherence Fluency & coherence scoring
Sentiment & tone detection Clarification strategies Multi-modal output support
Hybrid Approach: Combines rule-based precision with neural flexibility for robust, enterprise-ready conversational systems
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 24

Approaches for different components of
conversational AI system
NLU (Understand Dialog
NLG (Generate Example
Approach Intent + Extract Management
Responses) Applications
Slots) (Planning Flow)
Manual rules, Template-based Hard-coded IVR systems, early
Rule-Based (Finite
pattern matching responses; no flowcharts; state chatbots (ELIZA),
State / Pattern
(if–else, regex). No variation; machines; rigid FAQ bots, customer
Matching)
learning. deterministic. paths. service scripts.
Machine learning
classifiers (SVM, Template-based Early Dialogflow,
Statistical NLP (Pre- CRF, HMM) for with statistical Probabilistic dialog IBM Watson,
DL, ML Models) intent & slot ranking. Limited policies (POMDPs). telecom/banking
tagging; requires generation. bot NLU engines.
labelled data.
Neural intent Policy networks,
Seq2Seq or
classifiers; BiLSTM- trained with
Deep Learning encoder–decoder Alexa Skills (early
CRF slot tagging; supervised or
(RNNs, LSTMs, models; limited versions), Rasa DL,
moderate reinforcement
Seq2Seq) creativity; domain- Siri NLU pipelines.
generalization; still learning; still
tuned.
domain-specific. domain-specific.
BITS Pilani, Pilani Campus

---

### Page 25

Approaches for different components of
conversational AI system
NLU (Understand Dialog
NLG (Generate Example
Approach Intent + Extract Management
Responses) Applications
Slots) (Planning Flow)
Intent + slots
extracted implicitly LLM predicts next ChatGPT-style
LLM-Based Free-form, high-
using prompts/in- system actions; can assistants,
Conversational AI quality generation;
context learning; no manage context enterprise Q&A,
(GPT, Claude, style control; multi-
task-specific dynamically; no customer support
Gemini) modal; creative.
training needed; fixed flow. bots.
works zero-shot.
Autonomous dialog
LLM extracts AI agents, workflow
Multi-step planning using
intents/slots in automation bots,
Agentic AI (ReAct, reasoning, tool- reasoning loops
structured format enterprise
Tool Use, Function calling, API (Thought → Action
(JSON, schema) for assistants,
Calling, execution, planning. → Observation →
tools; works travel/finance/HR
Frameworks) NLG adapts after Response);
zero/low-shot; multi-step task
actions. dynamic workflows;
highly robust. assistants.
memory.
BITS Pilani, Pilani Campus

---

### Page 26

Large Language Models (LLMs) based
Conversational AI
Foundation models powering modern conversational AI
Transformer Architecture Pre-training Strategies Prompt Engineering Fine-tuning Methods
Self-attention mechanism Causal language modeling Zero-shot & few-shot Full parameter fine-tuning
Multi-head attention Masked LM (BERT-style) Chain-of-Thought (CoT) LoRA & QLoRA (PEFT)
Positional encoding RLHF & DPO alignment Tree-of-Thought (ToT) Adapter layers
Feed-forward networks Instruction tuning (SFT) ReAct prompting Supervised Fine-Tuning (SFT)
Layer normalization Constitutional AI (CAI) System / user / assistant roles Direct Preference Optimization
Popular LLMs for Conversational AI
Model Size Key Strengths
GPT-4o / GPT-4 ~1T (est) Reasoning, multimodal, instruction following
Claude 3.5 / 4 ~100B+ Long context, safety, nuanced dialogue
Gemini Ultra/Pro ~1T (est) Multimodal, Google ecosystem
LLaMA 3.x 8B–405B Open-source, fine-tuning friendly, on-prem
Mistral / Mixtral 7B–56B Efficient MoE, multilingual support
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 27

Retrieval-Augmented Generation (RAG)
for Conversational AI
Grounding LLM responses in verified, up-to-date knowledge sources
Documents › Chunking › Embedding › Vector › Retriever › LLM +
& Sources & Parsing Model Store Context
Retrieval Strategies Vector Databases Advanced RAG Patterns
Dense retrieval (bi-encoder) Pinecone —managed, scalable HyDE (hypothetical doc embeddings)
Sparse retrieval (BM25, TF-IDF) Weaviate —hybrid search native RAPTOR (tree-based recursive)
Hybrid = dense + sparse fusion Chroma —lightweight, local dev Self-RAG with reflection tokens
Re-ranking with cross-encoders pgvector —PostgreSQL extension Graph RAG for structured data
Contextual compression Qdrant —Rust-based, fast Agentic RAG with tool calling
Parent-child chunking FAISS —Meta, in-memory Multi-hop reasoning chains
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 28

Agentic AI for Conversational AI Systems
Autonomous AI agents that reason, plan, and act to complete complex goals
Observe → Reason → Plan → Act → Evaluate
Tool Use & Function Calling Memory Systems
• API calls, web search, code execution • Short-term: in-context window
• Calculator, database lookup, file I/O • Long-term: vector DB memory stores
• Structured output parsing & validation • Episodic & semantic memory patterns
• MCP (Model Context Protocol) integration • Session persistence across turns
Multi-Agent Orchestration Planning & Reasoning
• Supervisor → worker agent hierarchy • ReAct: Reasoning + Acting loop
• Parallel task execution & aggregation • Tree-of-Thought deliberate search
• LangGraph, AutoGen, CrewAI, Swarm • MCTS-based decision planning
• Error recovery & retry logic • Reflection & self-correction
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 29

Hybrid Conversational AI Architecture
Combining LLM, RAG, and Agentic AI into a unified, production-grade system
User Interface Layer
Chat UI · Voice Assistant · REST API · SDK · Omnichannel
Orchestration Layer
LangChain · LangGraph · LlamaIndex · Semantic Kernel · Custom Router
Hybrid Reasoning Core
LLM (GPT-4o / Claude / Gemini) + RAG Pipeline + Agentic Planner
Memory & Context
Short-term (context window) · Long-term (vector DB) · Session state store
Tools & Integrations
Web Search · Databases · External APIs · Code Execution · File I/O
Knowledge & Data Layer
Vector Store · Document DB · Graph DB · Structured Data Sources
Hybrid advantage: Structured precision + neural flexibility + retrieval accuracy + autonomous planning = robust enterprise deployments
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 30

Comparison of approaches
Approach Architecture Pros Cons Best Used For / Applications
- Hard-coded- Not
Decision trees, - Easy to implement- - Simple FAQs-IVR systems-
1. Rule-Based scalable- Poor with
flowcharts Predictable behavior Basic customer service
ambiguity
2. Slot-Filling - Structured- Good for - Struggles with context- - Food ordering bots- Travel
NLU → DM → NLG
(Modular) well-defined tasks Needs labeled data booking assistants
- Learns dialogue - Requires lots of data-
3. End-to-End - Open-domain chat- Virtual
Seq2Seq / Transformer patterns- More fluid Poor
Neural companions- Dynamic support
conversations control/explainability
Query + Similarity
4. Retrieval- - Fast- Accurate with - Limited to existing - Customer support- Helpdesk
Match → Predefined
Based proper data- Grounded replies- Low flexibility bots- FAQ assistants
Reply
- Flexible- Handles - Costly- May
Prompt → Foundation - Virtual agents- General
5. LLM-Based multiple tasks- Few-shot hallucinate- Lacks
Model (e.g., GPT) assistant bots- Support chatbots
capable structure
6. Hybrid (LLM LLM + Dialogue - Best of both worlds- - Complex to design- - Enterprise assistants-
+ Rules/APIs) Manager + Tools/APIs Robust and natural Needs integration effort Multistep workflows-Copilots
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 31

Evaluation of Conversational AI Systems
Systematic assessment of accuracy, safety, and user experience
Evaluation Tools & Frameworks
RAG Evaluation (RAGAS)
Faithfulness RAGAS
Answer Relevancy End-to-end RAG pipeline evaluation with LLM-as-judge scoring
Context Precision
LangSmith
Context Recall
Tracing, debugging and evaluation for LangChain apps
LLM Quality Metrics
TruLens
BLEU / ROUGE scores
Feedback functions and RAG quality scoring (TruEra)
BERTScore (semantic sim.)
Perplexity & coherence
Promptfoo
Hallucination rate
Automated red-teaming and prompt regression testing
Conversational Metrics
OpenAI Evals
Turn-level coherence
Model-graded evals, classification, string match
Task success rate
User satisfaction (CSAT) Human Eval
Dialogue act accuracy Likert-scale ratings, A/B testing, expert annotation
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 32

Evaluation
• Natural Language Understanding component Evaluation:
1. Slot Error Rate for a Sentence =
# of inserted/deleted/substituted slots
# of total reference slots for sentence
Slot tagging is most important since it contributes maximum to
quality of Dialog System
2. Intent Accuracy: Correct intent identified
• Dialog Manager Component Evaluation
1. State tracking Accuracy
2. End-to-end evaluation (Task Success)
BITS Pilani, Pilani Campus

---

### Page 33

Evaluation Metrics
“Make an appointment with Chris at 10:30 in Gates 104”
Slot Filler
PERSON Chris
TIME 11:30 a.m.
ROOM Gates 104
Slot error rate: 1/3
Task success: At end, was the correct meeting
added to the calendar?
BITS Pilani, Pilani Campus

---

### Page 34

Dialog System Design:
User-centered Design
1. Study the user and task
2. Iteratively test the design on users
BITS Pilani, Pilani Campus

---

### Page 35

Ethical Issues in Dialog System Design
• Machine learning systems replicate biases that occurred
in the training data.
• Microsoft's Tay chatbot
– Went live on Twitter in 2016
– Taken offline 16 hours later
• In that time it had started posting racial slurs, conspiracy
theories, and personal attacks
– Learned from user interactions (Neff and Nagy 2016)
BITS Pilani, Pilani Campus

---

### Page 36

Ethical Issues in Dialog System Design
• Machine learning systems replicate biases that occurred
in the training data.
• Dialog datasets
– Henderson et al. (2017) examined standard datasets (Twitter, Reddit, movie
dialogs)
– Found examples of hate speech, offensive language, and bias
• Both in the original training data, and in the output
of chatbots trained on the data.
• Fairness in Machine Learning
• Dialog agents overwhelmingly given female names,
perpetuating female servant stereotype(Paolino, 2017).
BITS Pilani, Pilani Campus

---

### Page 37

Ethical 

---

## Understanding in Layman's Terms

## 📚 Understanding NLP Applications Session 5- Conversational AI Systems

### 1. **Concept Explanation**
This section breaks down the core concepts of NLP Applications Session 5- Conversational AI Systems in simple, understandable terms.

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

NLP Applications Session 5- Conversational AI Systems is like teaching your robot friend to understand and talk better, just like you learn to understand new words every day!

### 4. **Explanation for a 30-Year-Old 👨**

As a professional, you should understand NLP Applications Session 5- Conversational AI Systems as:

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
- The fundamental principles of NLP Applications Session 5- Conversational AI Systems
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

**Total Original Pages**: 41
**Markdown Pages**: 25+
**Format**: Educational markdown with multiple explanation levels

