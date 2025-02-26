import spacy
import nltk
import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize

# Initialize spacy for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Example summary text
summary_text = """
Machine learning is a branch of artificial intelligence. It involves the development of algorithms that allow computers to learn from and make predictions or decisions based on data. 
There are three primary types of machine learning: supervised learning, unsupervised learning, and reinforcement learning.
Supervised learning uses labeled data, unsupervised learning uses unlabeled data, and reinforcement learning uses reward feedback.
"""

# Function to extract entities (topics/sub-topics) using spaCy
def extract_entities(text):
    doc = nlp(text)
    topics = []
    
    for ent in doc.ents:
        topics.append(ent.text)
    
    return topics

# Function to create a hierarchical structure
def build_hierarchy(topics):
    G = nx.DiGraph()  # Directed graph to represent the hierarchy
    root = "Machine Learning"

    # Add the root topic
    G.add_node(root)
    
    # Iterate over extracted topics and form hierarchical relationships
    for topic in topics:
        if "learning" in topic.lower():
            G.add_edge(root, topic)  # Root -> Sub-topic relationship
            
    return G

# Function to visualize the mind map
def visualize_mind_map(G):
    pos = nx.spring_layout(G)  # Positioning of nodes
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=12, font_weight="bold", edge_color="gray")
    plt.title("Mind Map of Text Summary", size=15)
    plt.show()

# Main flow
def generate_mind_map(text):
    topics = extract_entities(text)  # Extract key topics
    mind_map = build_hierarchy(topics)  # Build hierarchy graph
    visualize_mind_map(mind_map)  # Visualize the mind map

# Run the mind map generation
generate_mind_map(summary_text)
