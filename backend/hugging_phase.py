# -*- coding: utf-8 -*-


'''

import os
import PyPDF2
from transformers import pipeline



def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text
folder_path = 'C:\\Users\\Vritti Shah\\frontend_BE\\backend\\uploads'
merged_text = ''
# Loop through the list of PDFs and extract their text
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
      file_path = os.path.join(folder_path, filename)

      with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page_num in range(len(reader.pages)):
          page = reader.pages[page_num]
          page_text = page.extract_text()
          merged_text += page_text
  

def summarize_combined_text(text, summarizer, max_chunk_length=500):
    """
    Summarizes combined text from multiple PDFs using the Hugging Face summarizer.
    """
    # Split the text into manageable chunks
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

    summaries = []
    for chunk in chunks:
        # Summarize each chunk with max_length=50, min_length=25, and truncation enabled
        summary = summarizer(chunk, max_length=50, min_length=25, truncation=True, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    # Combine all the chunk summaries into a single summary
    return " ".join(summaries)

from transformers import pipeline

# Load the summarizer model (Hugging Face)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

final_summary = summarize_combined_text(merged_text, summarizer)
print("Final Summary:")
print(final_summary)

from transformers import pipeline

# Load the summarizer model (Hugging Face)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_combined_text(text, summarizer, max_chunk_length=500):
    """
    Summarizes combined text from multiple PDFs using the Hugging Face summarizer.
    """
    # Split the text into manageable chunks
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

    summaries = []
    for chunk in chunks:
        # Calculate max_length based on the chunk size
        current_max_length = min(50, len(chunk))  # If chunk is shorter than 50 tokens, use chunk length

        # Summarize each chunk with max_length, min_length, and truncation enabled
        summary = summarizer(chunk, max_length=current_max_length, min_length=25, truncation=True, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    # Combine all the chunk summaries into a single summary
    return " ".join(summaries)

final_summary = summarize_combined_text(merged_text, summarizer)

print("Final Summary:")
print(final_summary)

summary_word_count = len(final_summary.split())
print(summary_word_count)

from flask import jsonify


def get_variable():
    return jsonify(final_summary)
'''


# Save the final summary to a file in Google Drive
'''output_file_path = "/content/drive/My Drive/final_summary.txt"
with open(output_file_path, "w") as file:
    file.write(final_summary)

print(f"Summary saved to {output_file_path}")



from rouge_score import rouge_scorer

# Initialize the ROUGE scorer (you can compute ROUGE-1, ROUGE-2, and ROUGE-L)
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# Compute ROUGE scores
scores = scorer.score(merged_text, final_summary)

# Print the ROUGE scores
print(f"ROUGE-1: {scores['rouge1']}")
print(f"ROUGE-2: {scores['rouge2']}")
print(f"ROUGE-L: {scores['rougeL']}")'''



import os
import PyPDF2
from transformers import pipeline



def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text
folder_path = 'C:\\Users\\Vritti Shah\\frontend_BE\\backend\\uploads'
merged_text = ''
# Loop through the list of PDFs and extract their text
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
      file_path = os.path.join(folder_path, filename)

      with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page_num in range(len(reader.pages)):
          page = reader.pages[page_num]
          page_text = page.extract_text()
          merged_text += page_text

from sentence_transformers import SentenceTransformer, util

def remove_semantic_overlap_with_logging(text, similarity_threshold=0.8):

    model = SentenceTransformer('all-MiniLM-L6-v2')  # Load a pre-trained model
    sentences = text.split(". ")  # Split text into sentences
    embeddings = model.encode(sentences, convert_to_tensor=True)  # Compute sentence embeddings

    unique_sentences = []
    removed_sentences = []

    for i, sentence in enumerate(sentences):
        # Check similarity with existing unique sentences
        if all(util.cos_sim(embeddings[i], model.encode(s)) < similarity_threshold for s in unique_sentences):
            unique_sentences.append(sentence)  # Add unique sentence
        else:
            removed_sentences.append(sentence)  # Log removed sentence

    return ". ".join(unique_sentences), removed_sentences

cleaned_text, removed_sentences = remove_semantic_overlap_with_logging(merged_text, similarity_threshold=0.8)

# Print cleaned text
print("Cleaned Text Without Semantic Overlap:")
print(cleaned_text)

# Print removed sentences
print("\nRemoved Sentences:")
for sentence in removed_sentences:
    print(f"- {sentence}")

new_word_count = len(cleaned_text.split())
print(new_word_count) 

def summarize_combined_text(text, summarizer, max_chunk_length=500):
    """
    Summarizes combined text from multiple PDFs using the Hugging Face summarizer.
    """
    # Split the text into manageable chunks
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

    summaries = []
    for chunk in chunks:
        # Summarize each chunk with max_length=50, min_length=25, and truncation enabled
        summary = summarizer(chunk, max_length=50, min_length=25, truncation=True, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    # Combine all the chunk summaries into a single summary
    return " ".join(summaries)

from transformers import pipeline

# Load the summarizer model (Hugging Face)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

final_summary = summarize_combined_text(merged_text, summarizer)
print("Final Summary:")
print(final_summary)

from transformers import pipeline

# Load the summarizer model (Hugging Face)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_combined_text(text, summarizer, max_chunk_length=500):
    """
    Summarizes combined text from multiple PDFs using the Hugging Face summarizer.
    """
    # Split the text into manageable chunks
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

    summaries = []
    for chunk in chunks:
        # Calculate max_length based on the chunk size
        current_max_length = min(50, len(chunk))  # If chunk is shorter than 50 tokens, use chunk length

        # Summarize each chunk with max_length, min_length, and truncation enabled
        summary = summarizer(chunk, max_length=current_max_length, min_length=25, truncation=True, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    # Combine all the chunk summaries into a single summary
    return " ".join(summaries)

final_summary = summarize_combined_text(merged_text, summarizer)

print("Final Summary:")
print(final_summary)

summary_word_count = len(final_summary.split())
print(summary_word_count)

def format_summary_into_sections(summary, section_titles):

    sentences = summary.split(". ")  # Split summary into sentences
    num_sentences = len(sentences)

    # Calculate how many sentences to assign to each section
    sentences_per_section = num_sentences // len(section_titles)

    # Initialize an empty dictionary to hold the sentences for each section
    sections = {title: [] for title in section_titles}

    # Distribute sentences across sections. This is a basic distribution where sentences are evenly split.
    sentence_index = 0
    for title in section_titles:
        # Add sentences to the current section
        for _ in range(sentences_per_section):
            if sentence_index < num_sentences:
                sections[title].append(sentences[sentence_index].strip())  # Add sentence
                sentence_index += 1

    # If there are leftover sentences, add them to the last section
    if sentence_index < num_sentences:
        sections[section_titles[-1]].extend(sentences[sentence_index:])

    # Format the sections into a readable structure
    formatted_summary = ""
    for title, content in sections.items():
        formatted_summary += "\n"+f"{title}"+"\n\n"
        formatted_summary += "\n".join(f"- {sentence}." for sentence in content if sentence.strip()) + "\n\n"

    return formatted_summary

# Example usage
section_titles = ["Introduction", "Key Insights", "Conclusion"]
formatted_summary = format_summary_into_sections(final_summary, section_titles)

# Print the formatted summary
print("Formatted Summary with Sections:\n")
print(formatted_summary)


from flask import jsonify


def get_variable():
    return (formatted_summary)



