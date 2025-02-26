import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams

#summary 
summary="""Sure! Here's a summary of Large Language Models (LLMs) with "Transformer" as the central topic:

---

**Transformer** models have revolutionized the field of Natural Language Processing (NLP) and are the backbone of many state-of-the-art LLMs. Introduced in the paper "Attention is All You Need" by Vaswani et al. in 2017, Transformers utilize a mechanism called **self-attention** to process input data, allowing them to handle long-range dependencies more effectively than previous models like RNNs and LSTMs.

### Key Components:
1. **Self-Attention**: This mechanism enables the model to weigh the importance of different words in a sentence relative to each other, capturing context more effectively.
2. **Positional Encoding**: Since Transformers do not process data sequentially, positional encodings are added to input embeddings to retain the order of words.
3. **Multi-Head Attention**: This allows the model to focus on different parts of the input simultaneously, improving its ability to understand complex patterns.

### Applications:
- **GPT (Generative Pre-trained Transformer)**: Developed by OpenAI, GPT models are used for text generation, translation, and summarization. GPT-3, with 175 billion parameters, is one of the largest and most powerful LLMs.
- **BERT (Bidirectional Encoder Representations from Transformers)**: Developed by Google, BERT is designed for understanding the context of words in search queries, improving tasks like question answering and sentiment analysis.
- **T5 (Text-To-Text Transfer Transformer)**: Also by Google, T5 treats every NLP problem as a text-to-text task, making it highly versatile.

### Advancements:
- **Fine-Tuning**: LLMs can be fine-tuned on specific tasks or domains, enhancing their performance on specialized applications.
- **Transfer Learning**: Pre-trained Transformers can be adapted to new tasks with relatively small amounts of data, making them highly efficient.

### Challenges:
- **Computational Resources**: Training large Transformers requires significant computational power and memory.
- **Ethical Concerns**: Issues like bias in training data and the potential misuse of generated content are ongoing challenges.

---

You can use this summary to test the mind map code. Let me know if you need any further assistance!"""


central_topic="Transformers"



# Download stopwords
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenize and remove stop words
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def generate_ngrams(words, n):
    return [' '.join(gram) for gram in ngrams(words, n)]

def determine_optimal_branches(summary, central_topic):
    words = preprocess_text(summary)
    
    # Generate unigrams, bigrams, and trigrams
    unigrams = words
    bigrams = generate_ngrams(words, 2)
    trigrams = generate_ngrams(words, 3)
    
    all_grams = unigrams + bigrams + trigrams
    word_freq = Counter(all_grams)

    # Exclude the central topic
    filtered_words = [word for word in word_freq if central_topic not in word]

    # Determine the optimal number of branches (e.g., top 15-20 most frequent n-grams)
    optimal_num_branches = min(len(filtered_words), 20)

    return optimal_num_branches, filtered_words[:optimal_num_branches]

def create_mind_map(summary, central_topic):
    G = nx.Graph()

    # Add the central topic
    G.add_node(central_topic)

    # Determine optimal branches
    num_branches, branches = determine_optimal_branches(summary, central_topic)

    # Add branches and edges
    for branch in branches:
        G.add_node(branch)
        G.add_edge(central_topic, branch)

    # Draw the mind map
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    plt.show()


create_mind_map(summary, central_topic)