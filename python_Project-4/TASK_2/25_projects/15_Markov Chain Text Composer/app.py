import random

def build_markov_chain(text):
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store the Markov chain
    markov_chain = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        # Add next_word to the list of possible words after current_word
        if current_word not in markov_chain:
            markov_chain[current_word] = []
        markov_chain[current_word].append(next_word)
    
    return markov_chain

def generate_text(markov_chain, start_word, length=50):
    # Start with the given start_word
    current_word = start_word
    generated_text = [current_word]
    
    # Generate text by randomly selecting the next word
    for _ in range(length - 1):
        if current_word not in markov_chain:
            break
        
        next_word_options = markov_chain[current_word]
        next_word = random.choice(next_word_options)
        generated_text.append(next_word)
        current_word = next_word
    
    return " ".join(generated_text)

# Example usage
if __name__ == "__main__":
    # Input text (lyrics or any text corpus)
    input_text = """
    I love music. Music makes me happy. Happy days are here again.
    Love brings joy. Joy is everywhere. Everywhere I look, I see love.
    """
    
    # Build the Markov chain
    markov_chain = build_markov_chain(input_text)
    
    # Generate new text starting with a specific word
    start_word = "Love"
    generated_lyrics = generate_text(markov_chain, start_word, length=20)
    
    print("Generated Lyrics:")
    print(generated_lyrics)