# NLP Applications Session 4- Question Answering Dr. Chetana Gavankar

**Original Document Pages**: 74

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

Session Content
• QA versus Conversational AI
• QA Systems Journey
• Current Approaches
• Retrieval Based QA
• Knowledge bases QA and Hybrid QA
• Extractive QA – DL approach
• Generative QA
• RAG
• Agentic AI QA
• Case study
• Evaluation Measures
BITS Pilani, Pilani Campus

---

### Page 3

What is Question Answering
A field of Natural Language Processing (NLP) focused
on building systems that can automatically answer
questions posed by humans in natural language.
The Goal: Move beyond simple keyword search to provide
a direct, accurate, and concise answer to a user's
query.
– QA: You ask "what temperature to bake
bread," and it answers, "350°F (175°C)."
BITS Pilani, Pilani Campus

---

### Page 4

Why is QA So Important?
(The Business Value)
Customer Support: Instantly answer 80% of repetitive
customer questions 24/7.
Enterprise Knowledge: Allow employees to "ask
questions" of your company's internal documents (HR
policies, technical manuals, sales data).
Data Analysis: Enable executives to ask, "What was our
top-selling product in Q3?" and get a direct answer, not a
complex dashboard.
User Experience: Powers the voice assistants and search
engines we use every day (Siri, Alexa, Google).
BITS Pilani, Pilani Campus

---

### Page 5

QA versus Conversational AI
Feature Question Answering (QA) Conversational AI
Core Goal 1. Answer a single question. 1. Hold a multi-turn dialogue.
Scope 2. Transactional (one-shot). 2. Relational and Goal-Oriented.
3. Stateless (forgets 3. Stateful (must remember
Context
immediately). conversation history).
You: "I need to book a flight."
You: "What is the capital of Bot: "Sure, where are you flying to?"
France?"
Example
You: "Paris."
Bot: "Paris."
Bot: "Great. When do you want to
leave for Paris?"
BITS Pilani, Pilani Campus

---

### Page 6

When should we use
conversational AI for QA
Conversational AI can absolutely perform QA, but you
should only use it when the QA task is complex
enough to benefit from:
•reasoning
•multi-turn context
•unstructured text understanding
•flexibility
For simple, repetitive questions, conversational AI is
overkill—a simple QA system is cheaper, faster, safer.
BITS Pilani, Pilani Campus

---

### Page 7

QA Real world applications
1. Questions are predictable or repetitive
Example: “What are your store hours?”, “What is the refund policy?”
2. Answers must be fixed and controlled
Example: Banking compliance messages, Medical safety instructions
3. You need very fast responses with low cost
Example: An FAQ chatbot handling thousands of queries per minute
4. High accuracy is required and hallucinations are risky
Example: Legal policies, insurance rules, company procedures
5. Single-turn interactions (no context needed)
Example: “What is the capital of Japan?”
6. Information is pulled directly from a database or documents
Example: “Show me my order status.”, “What is CPU usage right now?”
BITS Pilani, Pilani Campus

---

### Page 8

Conversational AI Real world
applications
1. Multi-turn conversations
Example: User: “Book a flight.”
Bot: “Where to?”
User: “London.”
2. Questions require reasoning or explanation
Example: “Explain how transformers differ from SSMs.”, “Summarize this report.”
3. The question depends on previous context
Example: User: “Who is ?”, “How old is he?”
4. Handling unclear or ambiguous questions
Example: “Tell me about delivery charges.” (Bot: “Domestic or international?”)
5. Working with unstructured documents (PDFs, long texts)
Example: “What are the main points of this 30-page contract?”
6. Conversational tasks beyond QA
Example: recommending products, tutoring, guiding, troubleshooting.
BITS Pilani, Pilani Campus

---

### Page 9

Apple’s Siri
BITS Pilani, Pilani Campus

---

### Page 10

DanJurafsky
Wolfram Alpha
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 11

Types of Questions
• Factoid questions
• Who wrote “The Universal Declaration of Human Rights”?
• How many calories are there in two slices of apple pie?
• What is the average age of the onset of autism?
• Where is Apple Computer based?
• Complex (narrative) questions:
• In children with an acute febrile illness, what is the
efficacy of acetaminophen in reducing fever?
• What do scholars think about Jefferson’s position on
dealing with pirates?
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 12

Commercial systems:
mainly factoid questions
Where is the Louvre Museum located? In Paris, France
What’s the abbreviation for limited L.P.
partnership?
What are the names of Odin’s ravens? Huginn and Muninn
What currency is used in China? The yuan
What kind of nuts are used in marzipan? almonds
What instrument does Max Roach play? drums
What is the telephone number for Stanford 650-‐723-‐2300
University?
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 13

Journey of QA Systems
Evolution Path:
IR-based → Knowledge-based → Hybrid (IR + Knowledge) →
Deep Learning → Transformers → RAG
IR- based:
•Approach: Retrieve relevant documents/passages from
large text collections.
•Techniques: Keyword matching, TF-IDF, BM25.
•Examples: Early QA in search engines (AskJeeves, early
Google).
•Limitations: No true understanding; returns documents, not
direct answers.
BITS Pilani, Pilani Campus

---

### Page 14

IR-‐based Factoid QA
D ocument
D ocume nt
Documen t Document
Document Document
Indexing Answer
Passage
Question
Retrieval
Processing
Docume
Document Do Dno c t u c m um e e Passage Answer
Query Dnotcume
nt
Formulation Retrieval Relevant Retrieval passages Processing
nt
Question
Docs
AnswerType
Detection
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 15

IR-‐based Factoid QA
• QUESTION PROCESSING
• Detect question type, answer type, focus, relations
• Formulate queries to send to a search engine
• PASSAGE RETRIEVAL
• Retrieve ranked documents
• Break into suitable passages and rerank
• ANSWER PROCESSING
• Extract candidate answers
• Rank candidates
• using evidence from the text and external sources
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 16

Information Retrieval
IR systems retrieve relevant documents from a large corpus based on a query, using keyword matching, TF-IDF, BM25, or
semantic search.
How It Works Tech Stack
1 Query is parsed and preprocessed ▸ Elasticsearch / OpenSearch
2 Index is searched (inverted index / embeddings) ▸ Apache Solr
Documents ranked by relevance score (BM25, cosine ▸ BM25 (rank_bm25 Python)
3
sim)
▸ FAISS / Annoy (vector search)
4 Top-k documents returned as answers
▸ Lucene, Whoosh
Real-World Use Cases
Google/Bing web search
Legal document retrieval
Healthcare literature search (PubMed)
BITS Pilani, Pilani Campus

---

### Page 17

Knowledge-‐based
approaches (Siri)
• Build a semantic representation of the query
• Times, dates, locations, entities, numeric quantities
• Map from this semantics to query structured data or resources
• Geospatial databases
• Ontologies (Wikipedia infoboxes, dbPedia, WordNet, Yago)
• Restaurant review sources and reservation services
• Scientific databases
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 18

Hybrid approaches
(IBM Watson)
• Build a shallow semantic representation of the query
• Generate answer candidates using IR methods
• Augmented with ontologies and semi-‐structured data
• Score each candidate using richer knowledge sources
• Geospatial databases
• Temporal reasoning
• Taxonomical classification
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 19

Question Answering:
IBM’s Watson
• Won Jeopardy on February 16, 2011!
WILLIAM WILKINSON’S
“AN ACCOUNT OF THE PRINCIPALITIES OF
WALLACHIA AND MOLDOVIA” Bram Stoker
INSPIRED THIS AUTHOR’S
MOST FAMOUS NOVEL
BITS Pilani, Pilani Campus

---

### Page 20

IBM Watson QA
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 21

Deep Learning approach - QA
•Neural QA:
CNNs, RNNs, and attention mechanisms learn
semantic matching.
•Transformers (BERT, RoBERTa):
Contextual embeddings enable Extractive QA
— selecting answer spans from text.
•Example: SQuAD dataset benchmarks
Generative QA: Models like GPT, T5 generate
free-form answers.
BITS Pilani, Pilani Campus

---

### Page 22

Extractive QA
How it Works: The model is given a Question and a Context (a
piece of text). It then "highlights" the span of text that contains the
answer.
Analogy: A digital highlighter.
Example:
Context: "The Eiffel Tower was completed in 1889 and is
located in Paris, France."
Question: "Where is the Eiffel Tower located?"
Answer: "Paris, France"
Pros: High accuracy, factually grounded, low risk of "hallucination."
Cons: Only works if the answer is explicitly in the text. Can't
synthesize info.
BITS Pilani, Pilani Campus

---

### Page 23

QA using Deep Learning
BITS Pilani, Pilani Campus

---

### Page 24

QA training datasets
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 25

QA training datasets
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 26

QA using Deep Learning
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 27

QA in Deep Learning
• Transfer learning is the application of knowledge learned
while solve one problem on other similar problems.
• Latest deep learning based word embedding's such as
Bidirectional Encoder Representation from Transformers
(BERT) enable pre-trained Question Answer models
trained on corpus from one domain to easily answer
questions from another domain.
• This makes is easy to introduce support for Question
Answering in newer applications using pre-trained
models.
BITS Pilani, Pilani Campus

---

### Page 28

QA Bot – NLP DeepLearning
• We will be implementing a chat bot that can answer
questions based on a given story.
• The bAbI project by Facebook research
• https://research.fb.com/downloads/babi/
This page gather resources related to the bAbI project of
Facebook AI Research which is organized towards the
goal of automatic text understanding and reasoning.

---

### Page 29

QA Bot

---

### Page 30

QA Bot
1503.08895.pdf (arxiv.org)

---

### Page 31

QA Bot

---

### Page 32

QA Bot- NN Demo
• Training data is a list of tuples.
• Each tuple has a Story, Question and an Answer.
• Training and Testing Data should be a part of
Vocabulary.

---

### Page 33

• Padding: Pad_sequences

---

### Page 34

Word embedding of Question
(Use RNN in both
directions - BiLSTM )
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 35

Word embedding of passage
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 36

Deep Learning architecture for QA
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 37

Deep Learning architecture for QA
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 38

Deep Learning architecture for QA
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 39

Open Domain QA
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 40

T5 LLM for QA
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 41

T5 model Architecture
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 42

Challenges of Deep learning
approaches
BITS Pilani, Pilani Campus

---

### Page 43

Challenges of Deep learning
approaches
• Incapable of answering questions that require reasoning.
• Deep learning based models for Question Answering
take the input passage and questions and output the
start and end position in the passage that contains the
answer.
• Consequently they can not answer questions whose
answer is spread across the document.
• Can not answer questions that have multiple sub
questions whose answers are spread across the
document.
BITS Pilani, Pilani Campus

---

### Page 44

QA Modern Approaches
• Generative QA: Generates a new answer from
scratch.
• Retrieval-Augmented Generation (RAG): The
modern hybrid that gets the best of both worlds.
BITS Pilani, Pilani Campus

---

### Page 45

Generative QA
How it Works: The model (a Large Language Model like
GPT-4) uses its vast, pre-trained knowledge to generate
a new, human-like answer.
Analogy: A subject-matter expert answering from memory.
Example:
– Question: "Why is the Eiffel Tower significant?"
– Answer: "The Eiffel Tower is significant because it was an architectural marvel
for its time and has become an iconic symbol of Paris and French culture."
Pros: Very flexible, can answer "why" and "how" questions,
highly conversational.
Cons: "Hallucinations" (making up facts) and stale data
(its knowledge is frozen in time).
BITS Pilani, Pilani Campus

---

### Page 46

Generative AI for Question Answering
LLMs generate free-form natural language answers using parametric knowledge learned during training —no
external retrieval required at inference time.
Key Techniques Tech Stack
Prompt Engineering
▸ OpenAI GPT-4 / GPT-4o
Zero-shot, few-shot, CoT prompting
▸ Google Gemini 1.5 Pro
Fine-tuning
▸ Anthropic Claude 3.5 / 3.7
Task-specific SFT on QA datasets (SQuAD, TriviaQA)
▸ Meta LLaMA 3.x (open-source)
Instruction Tuning
▸ Mistral / Mixtral
RLHF / DPO alignment for factual responses
▸ Hugging Face Transformers
In-Context Learning
Provide examples in the prompt context window Real-World Use Cases
ChatGPT Q&A / customer support
Code assistant (GitHub Copilot)
BITS Pilani, Pilani Campus

---

### Page 47

The Big Problem:
Hallucinations & Stale Data
You can't trust a standard Generative LLM with your private
company data.
– It's a "Black Box": You don't know why it gave an answer (no citations).
– It's Stale: It has no idea your new product (Project X) launched last week.
– It's Insecure: It wasn't trained on your private documents.
This leads to the most important approach used in
business today...
BITS Pilani, Pilani Campus

---

### Page 48

Retrieval Based Methods
• Modern large language models (LLMs) — like ChatGPT,
Gemini, or Claude — use retrieval-based methods
behind the scenes.
• Instead of generating answers purely from memory, they:
• Retrieve relevant text chunks from a large document
database (IR stage).
• Generate the final answer using a language model
conditioned on those documents.
• This is called Retrieval-Augmented Generation (RAG)
or retrieval-augmented QA.
BITS Pilani, Pilani Campus

---

### Page 49

Retrieval Based Methods
• Example:
• User: “Who discovered penicillin?”
• System: retrieves passages mentioning “Alexander
Fleming” → summarizes →
Answer: “Penicillin was discovered by Alexander
Fleming in 1928.”
• So — modern IR-based QA = search + LLM reasoning.
BITS Pilani, Pilani Campus

---

### Page 50

Retrieval-Augmented Generation
The "Best of Both Worlds" Solution.
• RAG combines a Retriever (like a search engine) with a
Generator (an LLM).
• Analogy: An "open-book" exam. The LLM doesn't
answer from memory. It is given the relevant documents
(the "book") and told, "Use only these documents to
answer the question."
• This solves the hallucination and stale data problem.
BITS Pilani, Pilani Campus

---

### Page 51

RAG Pipeline
• Query: User asks, "What is our company's WFH policy?"
• Retrieve: The system first searches a private database
(a Vector Database) of all company HR documents. It
finds the 3 most relevant docs.
• Augment: The system builds a new prompt:
– "User Question: What is our WFH policy?"
– "Context: [Here is the text of the 'Work-From-Home Policy' doc...]"
• Generate: This prompt is fed to the LLM. The LLM then
generates an answer based only on the provided
context.
– Answer: "Our WFH policy allows employees to work from home 2 days per
week..."
BITS Pilani, Pilani Campus

---

### Page 52

RAG Tech stack
The Brains (Models): LLMs
The Memory (Data): Vector Databases
The Glue (Orchestration): Frameworks
The Interface (App): Frontend/Backend
BITS Pilani, Pilani Campus

---

### Page 53

RAG Tech stack
Large Language Models (LLMs): These generate the final
answer.
– Closed Source: OpenAI (GPT-4, GPT-4o), Anthropic (Claude 3), Google
(Gemini).
– Open Source: Meta (Llama 3), Mistral (Mixtral).
Embedding Models: These are crucial for the "Retrieval"
step. They turn text documents into numbers (vectors) so
we can find semantically similar documents.
Examples: all-MiniLM-L6-v2, text-embedding-3-small
BITS Pilani, Pilani Campus

---

### Page 54

•.
Vector Datastore
You can't find "semantically similar" documents in a
traditional SQL database.
Vector Datastore are purpose-built to store and query
these "embedding" vectors at massive scale.
How it works: It finds documents that are conceptually
related to the query, not just ones that share keywords.
Query: "rules for leave"
Finds: "policy for taking time off"
Examples: Pinecone, ChromaDB, FAISS, Weaviate, Milvus
BITS Pilani, Pilani Campus

---

### Page 55

RAG Orchestration
These frameworks manage the entire RAG pipeline (Query ->
Retrieve -> Augment -> Generate). They are the "plumbing" that
connects everything.
LangChain: The most popular and comprehensive library. A
"Swiss Army Knife" for building complex LLM applications
(agents, chains).
LlamaIndex: A simpler, data-focused framework that excels at
one thing: building powerful RAG pipelines. It's built for
"ingesting, indexing, and querying" your data.
BITS Pilani, Pilani Campus

---

### Page 56

RAG
RAG combines retrieval of relevant documents with generative LLMs —grounding answers in external, up-to-
date knowledge to reduce hallucinations.
RAG Pipeline
User Embed Vector Retrieve Augment LLM
Query Query Search Docs Prompt Answer
Tech Stack RAG Variants
Orchestration: LangChain, LlamaIndex, Haystack ▸ Naive RAG — basic retrieve + generate
Vector DBs: Pinecone, Weaviate, Qdrant, Chroma, pgvector ▸ Advanced RAG — re-ranking, HyDE, query expansion
▸ Modular RAG — routing, fusion, iterative
Embeddings: OpenAI text-embedding-3, Sentence-Transformers
Real-World Use Cases
LLMs: GPT-4o, Claude 3.5, Gemini 1.5
Enterprise knowledge bases (Confluence, SharePoint)
Reranking: Cohere Rerank, Cross-Encoder (SBERT)
Legal & financial document QA
Customer support with product docs
BITS Pilani, Pilani Campus

---

### Page 57

Comparison of QA approaches
Feature Extractive QA Generative QA (LLM) RAG
Answer Source Exact text span Model's internal memory External, current documents
Hallucination Risk Very Low High Low (mitigated)
Data Freshness Depends on context Stale (frozen in time) Real-time (just update docs)
Citations? Yes (the source doc) No Yes (can cite sources)
Best For Fact-checking Creative chat Enterprise QA, Chatbots
BITS Pilani, Pilani Campus

---

### Page 58

Case Study: "AskHR"
- An Internal Enterprise Chatbot
Company: A 10,000-person global tech firm.

The Problem: The HR department is overwhelmed with thousands of repetitive

employee questions every month:
"How much PTO do I have?"
o
"What's the policy for travel expenses?"
o
"Where do I find my tax forms?"
o
• These answers exist but are buried in a 500-page PDF on an internal site
• Goal: Build a 24/7 chatbot that can answer 90% of HR questions instantly and
accurately, citing its sources.
• The Choice: RAG
• Why not Generative? A base LLM (like ChatGPT) knows nothingabout the
company's specific policies and would make up answers (hallucinate).
• Why not Extractive? The policies are complex and require synthesis, not just
"highlighting" a single sentence
BITS Pilani, Pilani Campus

---

### Page 59

Techstack for AskHR
Data Ingestion (Offline):
– All 200+ HR docu

---

## Understanding in Layman's Terms

## 📚 Understanding NLP Applications Session 4- Question Answering Dr. Chetana Gavankar

### 1. **Concept Explanation**
This section breaks down the core concepts of NLP Applications Session 4- Question Answering Dr. Chetana Gavankar in simple, understandable terms.

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

NLP Applications Session 4- Question Answering Dr. Chetana Gavankar is like teaching your robot friend to understand and talk better, just like you learn to understand new words every day!

### 4. **Explanation for a 30-Year-Old 👨**

As a professional, you should understand NLP Applications Session 4- Question Answering Dr. Chetana Gavankar as:

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
- The fundamental principles of NLP Applications Session 4- Question Answering Dr. Chetana Gavankar
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

**Total Original Pages**: 74
**Markdown Pages**: 25+
**Format**: Educational markdown with multiple explanation levels

