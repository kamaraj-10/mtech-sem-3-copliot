# NLP Applications Session 3- RAG Applications Dr. Chetana Gavankar

**Original Document Pages**: 57

## 📖 Table of Contents

1. [Original Content](#original-content)
2. [Understanding in Layman's Terms](#understanding-in-laymans-terms)
3. [Key Concepts](#key-concepts)
4. [Real-World Applications](#real-world-applications)

---

## Original Content

### Page 1

Natural Language
Processing Applications
Dr. Chetana Gavankar, Ph.D,
BBIITTSS PPiillaannii IIT Bombay-Monash University Australia
PPiillaannii CCaammppuuss Chetana.gavankar@pilani.bits-pilani.ac.in

---

### Page 2

BITS Pilani
Pilani Campus
Session 3:
These slides are prepared by the instructor, with grateful
acknowledgement of all those who made their course materials
freely available online.

---

### Page 3

Agenda — What We'll Cover
RAG Foundations Naïve RAG Deep Dive
01 02
Classic pipeline, chunking, retrieval, embeddings &
Why RAG, core architecture, NLP context, key components
limitations
Graph RAG Agentic RAG
03 04
Knowledge graphs, entity extraction, community summaries Autonomous agents, tool use, planning & multi-step reasoning
Real-World Case Studies Latest Research (2024–25)
05 06
Frontier papers, benchmarks, open problems & future
Healthcare, Legal, Finance, Customer Service deployments
directions
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 4

RAG Foundations — What & Why
Core RAG Pipeline
What is RAG?
RAG augments large language models by dynamically
📝 🔍
retrieving relevant external knowledge at inference time —
grounding answers in verifiable, up-to-date information
User Query Retriever
without costly retraining.
Problems RAG Solves in NLP
✂ 📚
✕ Hallucination — LLMs confabulate facts not in training
Top-K Chunks Knowledge Base
✕ Knowledge cutoff — Static weights miss recent events
✕ No citations — Cannot trace generation to sources
🧠 💬
✕ Domain blind spots — General models lack specialist depth
LLM + Context Grounded Answer
✔ ↓ 40–60% hallucinations ✔ ↑ Source traceability ✔ No fine-tuning needed ✔ Real-time knowledge ✔ Domain adaptable
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 5

RAG Flow
• User Query: A user asks a question,
e.g., "What is our policy on international travel?"
• Semantic Search: The system searches the external knowledge base (e.g., HR policy
documents) for text chunks semantically related to the query.
• Context Retrieval: It retrieves the most relevant paragraphs, such as the section on
"Overseas Business Trips and Expense Approval."
• Prompt Enhancement: It creates a new, detailed prompt for the LLM:
– "Using the following context: [insert retrieved text here], answer this question: What is our
policy on international travel?"
• LLM Generation: The LLM generates a clear, concise answer based only on the provided
context, preventing hallucination and ensuring accuracy.
BITS Pilani, Pilani Campus

---

### Page 6

Naïve RAG — The Classic Pipeline
1 2 3 4 5 6
Load & Parse Chunk Text Embed Index Retrieve K Generate
📄 ✂ 🔢 🗄 🔍 🧠
PDFs, HTML, DB Fixed / Semantic Dense vectors Vector DB store Cosine / BM25 LLM + context
Chunking Strategies Retrieval Techniques
Fixed-size N tokens with overlap Dense (Bi-encoder) FAISS cosine / dot-product search
Simple
Sparse (BM25/TF-IDF) Exact keyword term matching
Recursive Para → sentence → word
Semantic
Fuse dense & sparse with
Hybrid + RRF
reranking
Semantic Cluster similar embeddings
Coherent
Maximal Marginal Relevance
MMR
diversity
Atomic factual
Proposition
Precise
decomposition
Precision pass over top-K
⚠ Single-hop only ⚠ Flat chunk retrieval ⚠ No query plannin C g ross-encode ⚠ r R Co e n ra te n x k t window limits ⚠ No entity linking
candidates
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 7

How RAG Works
https://hatchworks.com/blog/gen-ai/rag-for-financial-services/
BITS Pilani, Pilani Campus

---

### Page 8

Vector RAG
Ingestion: External data (documents, web pages, etc.) is processed, broken into
chunks, and converted into numerical representations called embeddings.
Indexing: These embeddings are stored in a specialized database called a Vector
Database.
Retrieval: When a user asks a query, it is also converted into an embedding. The
vector database then searches for the most similar data chunks (based on the
query embedding).
Augmentation: The original user query and the retrieved data chunks are
combined into a comprehensive prompt for the LLM.
Generation: The LLM uses this augmented prompt to generate a response that is
informed by the retrieved context.
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 9

Vector embedding Search
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 10

Vector RAG
https://arxiv.org/abs/2501.09136
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 11

CODE DEMO RAG
BITS Pilani, Pilani Campus

---

### Page 12

Advanced RAG
While Vector RAG is powerful, it can fall short with multi-
faceted or complex questions. This has led to the
development of more sophisticated RAG architectures:
Graph RAG: Leverages the relationships within structured
data (knowledge graphs) for more precise and context-
aware retrieval.
Agentic RAG: Introduces autonomous "agents" that can
reason, plan, and use tools to improve the retrieval
process.
BITS Pilani, Pilani Campus

---

### Page 13

GraphRAG
Graph RAG utilizes knowledge graphs—databases that store information
as nodes (entities) and edges (relationships)—to enhance retrieval. This
is ideal for domains with highly interconnected data, such as finance.
How it Works:
Entity and Relationship Extraction: Key entities and their relationships
are identified in the user query.
Graph Traversal: The system navigates the knowledge graph to find
relevant nodes and their connections.
Contextualized Retrieval: Retrieves not just individual facts, but also the
surrounding context and relationships.
BITS Pilani, Pilani Campus

---

### Page 14

Knowledge Graph Embedding
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 15

Knowledge Graph use to ground LLM
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 16

Knowledge Graph
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 17

Improve results with knowledge graph
using Neo4j
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 18

Graph RAG
https://www.ontotext.com/blog/matching-skills-and-candidates-with-graph-rag/
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 19

Graph RAG — Knowledge Graphs Meet LLMs
Why Knowledge Graphs?
Disease
Drug
X
A
• Explicit entity & relationship modelling
Knowledge Graph
• Multi-hop reasoning across graph paths
Protein
• Community summaries for global queries
B
• Structured traversal, not flat similarity
Gene
• Handles contradictions via provenance
Trial D
C
Graph RAG Architecture (3 Phases)
Phase 1 — Graph Construction Phase 2 — Indexing Phase 3 — Query Time
• LLM extracts entities & relations • Neo4j / Memgraph / NetworkX • Classify: local vs global query
• Build S-P-O triple store • Vector embeddings per node • Local → graph traversal
• Leiden community detection • Entity resolution mappings • Global → summary aggregation
• Generate community summaries • Hierarchical summary index • Merge → LLM generation
🔬 Microsoft GraphRAG (2024) — 3× better global sensemaking vs standard RAG on multi-document corpora benchmarks
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 20

Naïve/Vector RAG vs. Graph RAG
Feature Naïve RAG Graph RAG
Data Format Unstructured Text Structured Graph
Graph
Retrieval Method Dense Vector Search
Traversal/Querying
Reasoning Capability Limited Enhanced (Multi-hop)
Explainability Low High
Integration
Moderate High
Complexity
Domain-Specific
Use Cases General QA
Applications
BITS Pilani, Pilani Campus

---

### Page 21

Agentic RAG
Agentic RAG utilizes AI agents to make intelligent decisions about how to
best retrieve information. Instead of a linear pipeline, agents can:
• Decompose Complex Queries: Break down a broad question into
smaller, manageable sub-queries.
• Iterative Retrieval: Refine search queries based on initial results to
find more relevant information.
• Tool Use: Interact with various tools, such as APIs, vector database,
graph, or code interpreters, to gather information from diverse sources.
• Self-Correction: Analyze the retrieved information for relevance and
quality, and re-attempt retrieval if necessary.
This approach is particularly effective for complex research, planning, and
problem-solving tasks.
BITS Pilani, Pilani Campus

---

### Page 22

Agentic RAG
A framework where the LLM acts as an agent, not just a passive generator.
The agent:
– Sets subgoals.
– Plans retrieval steps.
– Executes tool use (e.g., search, APIs).
– Iteratively refines answers.
Core Idea: Make RAG interactive, iterative, and autonomous.
BITS Pilani, Pilani Campus

---

### Page 23

Agentic RAG
Key Components:
1.LLM Agent – orchestrates reasoning and control.
2.Memory / Scratchpad – stores context, subgoals,
past actions.
3.Retrievers / Tools – for search, API calls,
calculations.
4.Planner / Executor – decomposes queries,
sequences actions.
Workflow Example:
User query → Plan → Retrieve → Reason → Iterate
→ Final answer
BITS Pilani, Pilani Campus

---

### Page 24

Agentic RAG — Autonomous Retrieval & Reasoning
The Shift: Static one-shot retrieval → Dynamic, multi-step agents that decide WHAT to retrieve, WHEN, and HOW to synthesize
across tools
Key Agentic Patterns
Query Sub-task Tool Corrective RAG
Analysis Planning Execution
Self-eval → web search fallback
Self-RAG
Reflection tokens: RETRIEVE / ISREL
Sufficient? Synthesize Evaluate
Adaptive RAG
✓ Done Answer Result
Query routing by complexity class
Multi-Agent RAG
Re-query / Re-plan loop
Orchestrated specialist agents
Tool Use Planning Self-Correct Memory Collaboration
APIs, code runners, Breaks query into Re-retrieves when Short-term context Specialist agents
search engines decomposed sub-tasks result is insufficient + episodic store with defined roles
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 25

Agentic RAG Example
Query: “Compare the annual energy output of nuclear vs solar in 2024
globally.”
Agentic RAG Flow:
Decomposes into sub-queries.
Searches for energy reports.
Extracts numbers, units, timeframes.
Performs calculations.
Returns synthesized answer with citations.
BITS Pilani, Pilani Campus

---

### Page 26

Agentic RAG
https://blog.dailydoseofds.com/p/rag-vs-agentic-rag
BITS Pilani, Pilani Campus

---

### Page 27

AI Agentic RAG - Example
Conversation AI (AIMLCZG521)
BITS Pilani, Pilani Campus

---

### Page 28

RAG Variants — Side-by-Side Comparison
Dimension Naïve RAG Graph RAG Agentic RAG
Retrieval Method Flat vector similarity Graph traversal + community Dynamic multi-step tool use
Reasoning Depth Single-hop only Multi-hop via entity links Unlimited iterative loops
Setup Complexity ⭐⭐ Low ⭐⭐⭐⭐ High ⭐⭐⭐ Medium-High
Latency Very low (< 1s) Medium (graph queries) Variable (multi-step)
Best NLP Tasks QA, summarisation, FAQs Biomedical, legal research Complex reasoning, research
Traceability Chunk-level citations Entity + relation paths Full agent + tool trace logs
Scalability Linear with vector DB size Graph size is bottleneck Scales with orchestration
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 29

Multimodal RAG
Our knowledge isn't just in .txt files. It's in:
Images: Product photos, diagrams in manuals, satellite imagery.
Documents: PDFs containing charts, tables, and complex layouts.
Videos: How-to tutorials, product demos, security footage.
Audio: Customer support calls, meeting recordings.
The Limitation of Standard RAG:
A text-only RAG system is blind to this rich, multimodal information. It can't
answer questions like:
"Which of our products looks most like this picture?"
"What were the Q3 revenue trends based on this chart in the annual
report?"
"Find the part in the video where the presenter explains the system
architecture."
BITS Pilani, Pilani Campus

---

### Page 30

Multimodal RAG
Multimodal RAG is an advanced AI framework that retrieves information from a
knowledge base containing multiple data types (modalities) to generate a
comprehensive answer.
It understands: Text, images, tables, and potentially audio/video.
It connects: The description of a product with its picture. The text of a report
with the data in its charts.
It enables: Users to ask questions using any modality (text or image) and get
answers synthesized from all relevant data.
BITS Pilani, Pilani Campus

---

### Page 31

Multimodal RAG
Data Ingestion & Chunking: Documents (like PDFs) are broken down. Text is
extracted, images are isolated, and tables are identified.
Multimodal Embeddings: A specialized model creates numerical
representations (vectors) for all data types. Critically, it places the vector for
an image of a dog near the vector for the word "dog" in a shared "meaning
space."
Vector Database: These multimodal embeddings are stored and indexed for
fast similarity search.
BITS Pilani, Pilani Campus

---

### Page 32

Multimodal RAG
Hybrid Retrieval: When a user asks a query (text or image), the system
converts the query into an embedding and retrieves the most similar text
chunks, images, or tables from the vector database.
Generation: The retrieved multimodal context (e.g., a paragraph of text and a
relevant chart image) is passed to a powerful Multimodal LLM (like GPT-4o or
Gemini) which generates the final, synthesized answer.
BITS Pilani, Pilani Campus

---

### Page 33

Multimodal RAG
Processes More Than Text: It integrates diverse data types like images, audio, and
video, not just text, for a richer understanding.
Unified Data Representation: It uses embedding's to create a common language for
different data formats, enabling cross-modal comparisons.
Improves Accuracy: By drawing from multiple data types, it gains better context,
leading to more accurate and comprehensive answers.
Enables "Any-to-Any" Search: You can use one data type to find another, such as
using a text query to retrieve relevant images or vice-versa.
Drives Advanced Applications: This technology powers innovative tools like visual
search, interactive education, and complex document analysis.
BITS Pilani, Pilani Campus

---

### Page 34

Multimodal RAG Tools and Technology
Core Technology: Multimodal embedding models (like CLIP) create a unified search space for
text, images, and audio.
Infrastructure: Vector databases (e.g., Milvus, Pinecone) are required to store and efficiently
query these diverse embeddings.
Orchestration: Frameworks like LangChain and LlamaIndex are used to build and manage the
entire RAG pipeline.
Specialized Tools: New open-source projects like Morphik (visual-first) and RAG-Anything (all-
in-one) are emerging to solve specific multimodal challenges.
Generation Power: Advanced LLMs like GPT-4o and Gemini simplify the process by directly
accepting multimodal inputs for the final response generation.
Enterprise Solutions: Cloud platforms from Google (Vertex AI), AWS, and Azure offer managed
services for building scalable, production-grade applications.
BITS Pilani, Pilani Campus

---

### Page 35

Classical vs Multimodal RAG
Multimodal RAG extends classical RAG by indexing and retrieving documents containing text, images, tables, and
video frames — then fusing those retrieved contexts before generation.
Classical RAG Multimodal RAG Key Enablers
✓ ✓ ✓
Text chunks only Text + Images + Video CLIP / SigLIP encoders
✓ ✓ ✓
Single-modality index Joint embedding space Vision-language models
✓ ✓ ✓
BM25 or dense vectors Cross-modal retrieval Multi-vector stores
✓ ✓ ✓
Text-to-text generation Grounded multimodal output Instruction-tuned LLMs
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 36

Architecture Pipeline
1 2 3 4 5
Document Modal-Specific Unified Hybrid Context
Ingestion Encoding Vector Store Retrieval Fusion + LLM
PDF, DOCX, CLIP, OCR, Weaviate, Dense + Sparse GPT-4o, Claude
Images, Video ASR, VLM Pinecone, Qdrant Cross-Modal Gemini 1.5
💡 Key Insight: Each modality is encoded independently into a shared semantic space, enabling cross-modal similarity search at retrieval
time.
◀INDEXING PHASE QUERY PHASE ▶
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 37

Case Study — Healthcare: Clinical Decision Support
Challenge Measurable Outcomes
• 300+ new clinical guidelines per year
34%
reduction in adverse drug events
• EMR data siloed from latest research
• Drug interaction DB outdated by months
• High cognitive load → diagnostic errors 60%
faster clinical guideline lookup
RAG Solution
2.1×
• Graph RAG over PubMed + clinical guidelines improvement in evidence citation rate
• Real-time retrieval from patient EMR context
• Drug-interaction knowledge graph traversal 92%
clinician satisfaction (NPS survey)
• HIPAA-compliant on-premise vector store
Tech Stack: LangChain · Neo4j Graph RAG · GPT-4 · FHIR API Connector
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 38

Case Study: RAG in the Financial Sector
Problem: Financial analysts need to process vast amounts of unstructured data
(e.g., earnings call transcripts, SEC filings, news articles) to make informed
investment decisions. This process is time-consuming and prone to human
error.
Solution: An investment firm implemented an Agentic RAG system to create
an "AI Research Assistant."
Key Goals:
Accelerate the analysis of financial documents.
Uncover hidden insights and relationships within the data.
Provide analysts with concise, data-driven summaries and answers to complex
financial questions.
BITS Pilani, Pilani Campus

---

### Page 39

Case Studies — Legal & Financial Services
⚖️ LEGAL — Contract Intelligence Platform 💹 FINANCE — Investment Research Automation
Setup Setup
• Agentic RAG over 50k+ KB articles • Multi-agent RAG over SEC, Bloomberg, news
• Hybrid BM25 + dense retrieval on clauses • Parallel async retrieval across 4 sources
• Jurisdiction-aware metadata filtering • Cross-document reconciliation for conflicts
• Citation trail for every finding • Confidence scoring on every data point
Results Results
80% manual review time reduction 75% faster research report generation
99.2% clause extraction accuracy 4× more sources analysed per query
$2.4M annual cost savings per firm SEC-auto compliance citation automation
6hr→20min per 500-page contract 15% alpha improvement in backtests
Stack: LlamaIndex · Cohere Reranker · pgvector · Claude 3 Stack: LangGraph · Pinecone · GPT-4o · Bloomberg API
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 40

Case Studies — Customer Service & E-Commerce
🎧 CUSTOMER SERVICE — Intelligent Support Agent 🛒 E-COMMERCE — Personalised Product Discovery
Architecture Architecture
• Agentic RAG over 50k+ support KB articles • Multimodal RAG: text + image embeddings
• Live order + inventory data retrieval • Real-time catalog sync — no retraining
• Confidence-based escalation routing • User history injection for personalisation
• 32-language multilingual retrieval • Inventory-aware retrieval filters
Business Impact Business Impact
68% automated resolution rate 3× click-through rate improvement
41% CSAT improvement 22% average order value increase
12 sec mean handle time (was 1.8min) 45% fewer zero-result searches
$18M annual support cost saved <200ms p95 retrieval latency
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 41

RAG Across NLP Tasks — Where RAG Excels
NLP Task × RAG Variant Map
Text Summarisation 55 Question Answering
Multi-document open-domain QA,
Naïve RAG
NQ, TriviaQA
Code Generation 60
Fact Verification
Dialogue Systems 75 FEVER benchmark — entity link
Graph RAG
verification
Financial Research 83
Dialogue & Chatbots
Session memory + real-time
Agentic RAG
knowledge retrieval
Medical Diagnosis Assist 85
Summarisation
Legal Search 88 Multi-docu

---

## Understanding in Layman's Terms

## 📚 Understanding NLP Applications Session 3- RAG Applications Dr. Chetana Gavankar

### 1. **Concept Explanation**
This section breaks down the core concepts of NLP Applications Session 3- RAG Applications Dr. Chetana Gavankar in simple, understandable terms.

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

NLP Applications Session 3- RAG Applications Dr. Chetana Gavankar is like teaching your robot friend to understand and talk better, just like you learn to understand new words every day!

### 4. **Explanation for a 30-Year-Old 👨**

As a professional, you should understand NLP Applications Session 3- RAG Applications Dr. Chetana Gavankar as:

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
- The fundamental principles of NLP Applications Session 3- RAG Applications Dr. Chetana Gavankar
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

