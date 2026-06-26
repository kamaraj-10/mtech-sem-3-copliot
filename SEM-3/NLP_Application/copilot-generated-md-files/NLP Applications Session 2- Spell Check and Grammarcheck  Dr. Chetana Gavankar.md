# NLP Applications Session 2- Spell Check and Grammarcheck  Dr. Chetana Gavankar

**Original Document Pages**: 54

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
Session 2:
These slides are prepared by the instructor, with grateful
acknowledgement of Prof. Dan Jurafsky and many others who made
their course materials freely available online.

---

### Page 3

Agenda
Introduction & Overview Dictionary-Based Techniques
01 02
What are spell/grammar checkers? Edit distance, trie structures
Statistical & Probabilistic Methods Machine Learning Approaches
03 04
n-grams, noisy channel model Neural networks, transformers
Grammar Checking Techniques Evaluation & Challenges
05 06
POS tagging, parsing, rules Metrics, datasets, limitations
BITS Pilani, Pilani Campus

---

### Page 4

Spell checkers
What Are They?
Error Categories
Spell checkers detect and correct misspelled words in text Non-Word Errors
eg. 'recieve' → 'receive'
Grammar checkers identify grammatical errors and Real-Word Errors
suggest corrections
eg. 'their' vs 'there'
Syntactic Errors
Both rely on NLP, linguistics, and ML techniques
eg. 'She go to school'
Semantic Errors
Applications: word processors, IDEs, email clients, search
eg. 'colorless green ideas'
engines
Punctuation Errors
eg. missing commas, apostrophes
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 5

Dictionary-Based Techniques
Edit Distance (Levenshtein) Trie / Prefix Trees
Measures minimum number of single-character edits (insertions,
Tree-based data structure for efficient dictionary lookup. Each node
deletions, substitutions) to transform one word into another.
represents a character. Supports O(k) lookup where k = word length.
Used to find the closest dictionary match.
▶receiv → receive: distance = 1 ▶Fast autocomplete & spell suggestion
Soundex / Phonetic Algorithms BK-Trees
Encodes words based on pronunciation to find phonetically similar Metric tree structure optimized for approximate string matching using
words. Useful for homophones and phonetic misspellings. edit distance. Enables sub-linear search for similar words.
▶Smith ↔ Smythe → same Soundex code ▶Efficiently finds all words within k edits
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 6

When to Use What
Quick intuition guide
① Edit Distance ② Trie ③ Soundex ④ BK-Tree
🔤 🌳 🔊 🌲
Precise typo correction Fast lookup & autocomplete Pronunciation-based errors Scalable fuzzy search
Finds the true minimum edits Instant prefix queries. Perfect Catches phonetic typos like Efficient search over large
between two words. Best for search boxes, 'fone→phone'. Great for voice dictionaries with edit distance
accuracy for short-distance autocomplete dropdowns. input & OCR. tolerance.
fixes.
Complexity: O(m·n) Complexity: O(k) Complexity: O(n) Complexity: O(log n)
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 7

Statistical & Probabilistic Methods
Noisy Channel Model N-gram Language Models
Estimate word probability based on previous n-1 words. Bigrams,
argmax P(w|e) = argmax P(e|w) × P(w) trigrams capture local context for real-word error detection.
P(w) — Language model: prior probability of word w
Bayesian Correction
P(e|w) — Error model: probability of error e given intended word
w
Uses prior probability + likelihood. Combines corpus frequency with
Find the most probable intended word error patterns learned from training data to rank suggestions.
Key Insight:
Statistical methods work WITHOUT exhaustive rules — they learn patterns from large text corpora, making them
adaptable across domains and languages.
Common corpora: Google Books, Wikipedia, CommonCrawl, Brown Corpus
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 8

Spellcheck Candidate generation
• Words with similar spelling
• Small edit distance to error
• Words with similar pronunciation
• Small edit distance of pronunciation to error
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 9

Damerau-Levenshtein edit
distance
• Minimal edit distance between two strings, where edits are:
• Insertion
• Deletion
• Substitution
• Transposition of two adjacent letters
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 10

Words within 1 of acress
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 11

Candidate generation
• 80% of errors are within edit distance 1
• Almost all errors within edit distance 2
• Also allow insertion of space or hyphen
• thisidea -> this idea
• inlaw -> in-law
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 12

How do you generate the candidates?
1. Run through dictionary, check edit distance with each
word
2. Generate all words within edit distance ≤ k (e.g., k = 1
or 2) and then intersect them with dictionary
3. Use a character k-gram index and find dictionary
words that share “most” k-grams with word (e.g., by
Jaccard coefficient)
4. Compute them fast with a Levenshtein finite state
transducer
5. Have a precomputed map of words to possible
corrections
12
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 13

What is P(W)?
• We see an observation x of a misspelled word
• Find the correct word ŵ
wˆ = argmax P(w | x)
wÎV
P(x | w)P(w)
= argmax
P(x)
wÎV
= argmax P(x | w)P(w)
What’s P(w)?
wÎV
13
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 14

Unigram Prior probability
• Counts from 404,253,213 words in Corpus of Contemporary English
(COCA)
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 15

Channel model probability
• Misspelled word x = x1, x2, x3… xm
• Correct word w = w1, w2, w3,…, wn
• P(x|w) = probability of the edit
• (deletion/insertion/substitution/transposition
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 16

Computing error probability:
confusion matrix
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 17

Generating the confusion matrix
• Peter Norvig’s list of errors
• Peter Norvig’s list of counts of single-edit errors
• All Peter Norvig’s ngrams data links: http://norvig.com/ngrams/
17
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 18

Channel Model
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 19

Smoothing probabilities: Add-1 smoothing
• But if we use the confusion matrix example, unseen errors are
impossible!
• They’ll make the overall probability 0. That seems too harsh
• e.g., in Kernighan’s chart qa and aq are both 0, even though they’re
adjacent on the keyboard!
• A simple solution is to add 1 to all counts and then if there is a |A|
character alphabet, to normalize appropriately:
sub[x, w]+1
If substitution, P(x | w) =
count[w]+ A
19
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 20

Noisy channel probability for acress
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 21

Context-sensitive spelling correction
• Determining whether actress or across is appropriate will require
looking at the context of use
• We can do this with a better language model
• A bigram language model conditions the probability of a word on
(just) the previous word
P(w …w ) = P(w )P(w |w )…P(w |w )
1 n 1 2 1 n n−1
21
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 22

Incorporating context words
• For unigram counts, P(w) is always non-zero
• if our dictionary is derived from the document collection
• This won’t be true of P(w |w ). We need to smooth
k k−1
• We could use add-1 smoothing on this conditional distribution
• But here’s a better way – interpolate a unigram and a bigram:
P (w |w ) = λP (w ) + (1−λ)P (w |w )
li k k−1 uni k bi k k−1
• P (w |w ) = C(w , w ) / C(w )
bi k k−1 k−1 k k−1
22
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 23

Using a bigram language model
• “a stellar and versatile acress whose
combination of sass and glamour…”
• Counts from the Corpus of Contemporary American
English with add-1 smoothing
• P(actress|versatile)=.000021 P(whose|actress) = .0010
• P(across|versatile) =.000021 P(whose|across) = .000006
• P(“versatile actress whose”) = .000021*.0010 = 210 x10-10
• P(“versatile across whose”) = .000021*.000006 = 1 x10-10
23
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 24

Solving real-word spelling errors
• For each word in sentence
• Generate candidate set
• the word itself
• all single-letter edits that are English words
• words that are homophones
• Choose best candidates
• Noisy channel model
• Task-specific classifier
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 25

Noisy channel for real-word spell correction
• Given a sentence w ,w ,w ,…,w
1 2 3 n
• Generate a set of candidates for each word w
i
• Candidate(w ) = {w , w’ , w’’ , w’’’ ,…}
1 1 1 1 1
• Candidate(w ) = {w , w’ , w’’ , w’’’ ,…}
2 2 2 2 2
• Candidate(w ) = {w , w’ , w’’ , w’’’ ,…}
n n n n n
• Choose the sequence W that maximizes P(W)
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 26

Noisy channel for real-word
spell correction
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 27

Simplification: One error per sentence
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 28

Peter Norvig’s “thew” example
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 29

Machine Learning Approaches
RNNs & LSTMs Transformer Models Seq2Seq with Attention
Sequence models that capture long-range BERT, GPT, T5 — pre-trained on massive corpora. Encoder-decoder architecture maps erroneous
dependencies. Trained on character/word Fine-tuned for spell/grammar correction with sentence to corrected output, learning alignment
sequences to predict corrections. attention mechanisms. between error and correction.
●char-level seq2seq for spelling ●BERT: masked language modeling ●End-to-end grammatical error correction
CRF & SVM Classifiers Pre-trained LLMs Ensemble Methods
Conditional Random Fields for token-level tagging. GPT-4, Claude, LLaMA — few-shot or zero-shot Combine multiple models (rule-based + statistical +
SVMs for binary classification of correct vs. correction. Can understand context, style, and neural). Voting or stacking improves precision and
incorrect word usage. domain-specific language. recall.
●Feature-based token classification ●In-context learning for correction ●Best accuracy in practice
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 30

Open source Spellcheck tools
•pyspellchecker: This is a pure Python library and a direct implementation of Peter Norvig's
famous statistical spell-checking algorithm. It's simple, easy to use, and self-contained.
•textblob: This popular NLP library includes a statistical spellchecker (also based on Norvig's
algorithm) as one of its many features.
•Symspellpy: is a high-speed Python library for spelling correction and fuzzy searching
y
based on the Symmetric Delete algorithm
•LanguageTool: Powerful rule-based spellchecker.
•combines these rules with statistical (n-gram) models to catch errors that simple
dictionary lookups would miss.
•Hunspell: Famous and powerful open-source rule-based spellcheck engine.
It is the spellchecking engine used by Google Chrome, Mozilla Firefox, LibreOffice & OpenOffice,
macOS (for many applications)
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 31

Open source spellcheck tools
Tool Type Primary Use Context-Aware?
Full Grammar & Style
LanguageTool Hybrid (Rules + ML) Yes (statistical)
API
Fast, accurate
Hunspell Engine / Library No
spellchecking
Extreme speed (e.g.,
SymSpell Library No
search)
Simple Python
pyspellchecker Library (Statistical) No
spellcheck
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 32

Open source Spellcheck online tools
• https://languagetool.org/
• https://spellcheck24.net/
• https://www.reverso.net/text-translation
• https://www.scribens.com/
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 33

DL/ Transformer based Open Source
Spell checker Tools
• Pre-trained Models
• Hugging Face Transformers like T5 that has been fine-tuned on the task of
"translating" incorrect text into correct text.
• LanguageTool
• uses a hybrid approach, which is what makes it so robust.
• Rule-Based: A massive set of hand-crafted rules for catching common grammar and spelling errors.
• Machine Learning: Statistical (n-gram) models to find contextual errors (like "I went two the
store") that the rules miss.
• DL/ Transformer based (used in premium version)
• NeuSpell
• Implementations of different DL models (BERT-based, LSTM-based, and Seq2Seq models)
all pre-trained for spellchecking.
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 34

Grammar Checking Techniques
NLP Processing Pipeline:
Tokenization POS Tagging Parsing Error Detection Suggestion
Rule-Based Grammar Dependency Parsing
Handcrafted linguistic rules for subject-verb agreement, article use, Analyzes grammatical relationships between words. Detects errors in
tense consistency. Systems like LanguageTool use thousands of rules. sentence structure, clause dependencies, and word order.
Constituency Parsing Neural GEC
Breaks sentences into nested constituents (NP, VP, PP). Context-free Grammatical Error Correction using transformers (T5, BART, GECToR).
grammars identify malformed structures. Trained on parallel corpora of erroneous and correct sentences.
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 35

Transformer-Based Models — Deep Dive
Key Models & Their Roles
Task: Masked LM fine-tuning
BERT Use case: Real-word error detection
⚡ Bidirectional context
Task: Text-to-text generation
T5 Use case: GEC, paraphrasing
⚡ Encoder-decoder
Task: Causal LM, prompting
GPT-4 Use case: Context-aware suggestion
⚡ Few-shot correction
Task: Token-level tagging
GECToR Use case: Production GEC systems
⚡ Fast inference
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 36

Commercial Grammar Check tools
Tool Primary Approach How It Works
Deploys a team of "AI agents" (e.g., Proofreader, Paraphraser, Tone
Agentic AI &
Grammarly Adjuster) that proactively analyze context, intent, and style to offer holistic
Generative AI
writing suggestions.
Its core function is paraphrasing, which is powered by a generative LLM.
Generative AI
QuillBot Its grammar check and other tools are also built with this AI-first approach
(LLM)
to rewrite and correct text.
Uses AI to run 25+ distinct analytical reports (e.g., "Sticky Sentences,"
Hybrid (Analytical
ProWritingAid "Pacing"). It separately uses generative AI for specific tasks like "Sparks"
AI + Generative AI)
(rephrasing) and "Critiques."

---

### Page 37

Open Source Grammar Check tools
Hybrid (Rule- The free, open-source core is a powerful rule-based engine (using XML/Java rules).
Language Tool
Based + AI) The premium version adds a proprietary AI layer for advanced style and rephrasing.
Statistical NLP A classic NLP model that uses statistical analysis (n-grams) and neural networks to find
After the Deadline
(N-grams) "real word errors" by checking the probability of word sequences against a large corpus.
Machine
A Python framework (not a full app) built on Transformer models (like those in LLMs). It's
Gramformer Learning
an ML model fine-tuned specifically to detect and correct grammatical errors.
(Transformers)

---

### Page 38

Notable Tools and Models
• GECToR: Transformer-based token-level corrector (very fast and accurate)
• Errant: Tool for evaluating GEC systems
• OpenNMT / FairSeq: Frameworks for building GEC models
BITS Pilani, Pilani Campus

---

### Page 39

System/Model Approach Strengths Weaknesses Used By
Token-level Transformer Fast, interpretable, Needs annotated data,
GECToR Open-source, academic
(edit tagging) state-of-the-art for GEC limited fluency handling
Powerful fluency
Seq2Seq transformer Slow, may hallucinate General-purpose (used
T5 / BART correction, few-shot
(text-to-text) corrections in some GEC research)
learning
BERT / RoBERTa Error detection, often Not standalone for full Grammarly (likely part
High accuracy detection
Classifiers paired with correctors correction of stack), research
Multilingual Supports many Google, multilingual
mT5 / XLM-R Computationally heavy
Transformers languages GEC tasks
Hand-crafted grammar LanguageTool, old
Rule-Based Systems Transparent, fast Rigid, low coverage
and style rules Microsoft Word
Hybrid: deep learning + Fluent, context-aware, Proprietary, limited
Grammarly Grammarly
rules + ensembles real-world tool transparency
Google Docs Grammar Transformer-based, Good latency, seamless Mostly grammar, not
Google Workspace
Tool real-time user experience style

---

### Page 40

Agentic AI and Spellcheck/Grammarcheck
•Preprocessing Step – Agentic AI often includes a spellcheck and grammar-
correction module to clean user input before analysis.
•Improved Understanding – Corrected text ensures better intent recognition
and semantic parsing for downstream reasoning.
•Embedded or External Tools – Systems may use internal NLP models,
APIs (like Grammarly or LanguageTool), or LLM-based self-correction.
•Pipeline Integration – Grammar/spell check sits in the preprocessing stage,
feeding into semantic analysis → reasoning → action/output loop.

---

### Page 41

Evaluation & Challenges
Evaluation Metrics
Key Challenges
Precision: Correct suggestions / Total suggestions made
Context sensitivity: 'their/there/they're'
Recall: Errors caught / Total actual errors Domain adaptation: medical, legal jargon
Weighted F-measure favoring precision (GEC Multilingual support & code-switching
F0.5 Score:
standard)
Preserving author intent and style
Error type analysis — classifies correction
ERRANT:
categories
Low-resource languages lack training data
BLEU / ROUGE: Text overlap metrics for generated corrections
Real-time performance requirements
Handling informal/social media text
Benchmarks: CoNLL-2014, BEA-2019, JFLEG
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 42

Precision
How accurate are our suggestions?
1 Formula
DEFINITION
Precision = TP / (TP + FP)
Of all the corrections the system made, Precision measures what
TP = True Positives
fraction were actually correct. It penalizes false positives — wrong
suggestions.
FP = False Positives
Why it matters: In GEC, high precision means fewer wrong
"corrections" that break the original text. F0.5 score weights precision
Interpretation
more heavily than recall.
1.0 Every suggestion was correct
EXAMPLE
0.5 Half of suggestions were correct
System flags 10 words as errors and suggests corrections.
→ 8 corrections are genuinely correct
0.0 No suggestion was correct
→ 2 are wrong (false positives)
GEC standard: F0.5 rewards precision over recall
Precision = 8 / (8 + 2) = 0.80
1 / 4
BITS Pilani, Deemed to be University under Section 3 of UGC Act, 1956

---

### Page 43

Recall
How many real errors did we catch?
2
DEFINITION
Recall = TP / (TP + FN)
Of all the actual errors in the text, Recall measures what fraction the
TP = True Positives
system successfully detected and corrected. It penalizes misses.
FN = False Negatives
Why it matters: High recall ensures errors aren't missed. However,
maximising recall alone can flood text with unnecessary corrections.
Interpretatio

---

## Understanding in Layman's Terms

## 📚 Understanding NLP Applications Session 2- Spell Check and Grammarcheck  Dr. Chetana Gavankar

### 1. **Concept Explanation**
This section breaks down the core concepts of NLP Applications Session 2- Spell Check and Grammarcheck  Dr. Chetana Gavankar in simple, understandable terms.

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

NLP Applications Session 2- Spell Check and Grammarcheck  Dr. Chetana Gavankar is like teaching your robot friend to understand and talk better, just like you learn to understand new words every day!

### 4. **Explanation for a 30-Year-Old 👨**

As a professional, you should understand NLP Applications Session 2- Spell Check and Grammarcheck  Dr. Chetana Gavankar as:

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
- The fundamental principles of NLP Applications Session 2- Spell Check and Grammarcheck  Dr. Chetana Gavankar
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

**Total Original Pages**: 54
**Markdown Pages**: 25+
**Format**: Educational markdown with multiple explanation levels

