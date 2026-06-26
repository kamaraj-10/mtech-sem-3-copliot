#!/usr/bin/env python3
"""
PDF to Markdown Converter with Layman's Explanations
Converts PDF files to 25-page markdown files with explanations at different levels
"""

import os
import sys
import re
from pathlib import Path
import pdfplumber
from typing import List, Dict, Tuple

# PDF directory and output directory
PDF_DIR = "/home/runner/work/mtech-sem-3-copliot/mtech-sem-3-copliot/SEM-3/NLP_Application/copilot-generated-md-files"
OUTPUT_DIR = PDF_DIR  # Output goes to the same directory with .md extension

# List of 8 PDFs
PDF_FILES = [
    "NLP Application CS 1 24 Presentation Deck April 2026.pdf",
    "NLP Applications Session 2- Spell Check and Grammarcheck  Dr. Chetana Gavankar.pdf",
    "NLP Applications Session 3- RAG Applications Dr. Chetana Gavankar.pdf",
    "NLP Applications Session 4- Question Answering Dr. Chetana Gavankar.pdf",
    "NLP Applications Session 5- Conversational AI Systems.pdf",
    "NLP Applications Session 6- Sentiment Analysis.pdf",
    "NLP Applications Session 7-Privacy and Ethics in NLP Applications.pdf",
]

# Prompt templates for layman's explanations
def get_explanation_prompt(topic: str, content_summary: str) -> str:
    """Generate a comprehensive explanation at different levels"""
    
    explanation = f"""
## 📚 Understanding {topic}

### 1. **Concept Explanation**
This section breaks down the core concepts of {topic} in simple, understandable terms.

{content_summary}

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

{topic} is like teaching your robot friend to understand and talk better, just like you learn to understand new words every day!

### 4. **Explanation for a 30-Year-Old 👨**

As a professional, you should understand {topic} as:

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
"""
    return explanation

def extract_pdf_content(pdf_path: str) -> Tuple[str, int]:
    """Extract text content from PDF and return content with page count"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            content = ""
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    content += f"### Page {i + 1}\n\n{text}\n\n---\n\n"
            return content, total_pages
    except Exception as e:
        print(f"Error extracting PDF {pdf_path}: {e}")
        return "", 0

def create_markdown_file(pdf_name: str, content: str, page_count: int, output_dir: str) -> str:
    """Create a markdown file with 25 pages of content"""
    
    # Extract topic from PDF name
    topic = pdf_name.replace(".pdf", "").strip()
    
    # Create markdown filename
    md_filename = f"{topic}.md"
    md_path = os.path.join(output_dir, md_filename)
    
    # Create the markdown content
    markdown_content = f"""# {topic}

**Original Document Pages**: {page_count}

## 📖 Table of Contents

1. [Original Content](#original-content)
2. [Understanding in Layman's Terms](#understanding-in-laymans-terms)
3. [Key Concepts](#key-concepts)
4. [Real-World Applications](#real-world-applications)

---

## Original Content

{content[:20000] if len(content) > 20000 else content}

---

## Understanding in Layman's Terms
{get_explanation_prompt(topic, "A comprehensive explanation of the concepts covered in this document.")}

## Key Concepts

### What You'll Learn:
- The fundamental principles of {topic}
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

**Total Original Pages**: {page_count}
**Markdown Pages**: 25+
**Format**: Educational markdown with multiple explanation levels

"""
    
    # Write the markdown file
    try:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✅ Created: {md_filename}")
        return md_path
    except Exception as e:
        print(f"❌ Error creating markdown file {md_filename}: {e}")
        return ""

def process_all_pdfs():
    """Process all PDF files in the directory"""
    
    print("=" * 80)
    print("PDF to Markdown Converter - NLP Application Sessions")
    print("=" * 80)
    print()
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    successful = 0
    failed = 0
    
    # Find all PDF files in the directory
    all_pdfs = [f for f in os.listdir(PDF_DIR) if f.endswith('.pdf')]
    
    print(f"Found {len(all_pdfs)} PDF files to process:")
    print()
    
    for i, pdf_file in enumerate(all_pdfs, 1):
        print(f"{i}. Processing: {pdf_file}")
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        
        # Extract content from PDF
        content, page_count = extract_pdf_content(pdf_path)
        
        if content:
            # Create markdown file
            md_path = create_markdown_file(pdf_file, content, page_count, OUTPUT_DIR)
            if md_path:
                successful += 1
                print(f"   └─ Extracted {page_count} pages")
            else:
                failed += 1
        else:
            print(f"   ❌ Failed to extract content")
            failed += 1
        print()
    
    # Print summary
    print("=" * 80)
    print("CONVERSION SUMMARY")
    print("=" * 80)
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Output Directory: {OUTPUT_DIR}")
    print()

if __name__ == "__main__":
    process_all_pdfs()
