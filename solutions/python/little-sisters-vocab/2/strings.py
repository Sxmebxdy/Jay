"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word
    
    


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a formatted string.

    :param vocab_words: list - of vocabulary words with prefix in the first index.
    :return: str - prefix followed by vocabulary words with the prefix applied.

    Example:
    make_word_groups(['en', 'close', 'joy', 'lighten'])
    returns: 'en :: enclose :: enjoy :: enlighten'
    """
    prefix = vocab_words[0]
    new_vocab = [prefix + word for word in vocab_words[1:]]  # Apply prefix to words
    return " :: ".join([prefix] + new_vocab)  # Join with ' :: ' separator


def remove_suffix_ness(word):
    """Remove the suffix 'ness' from the word while keeping spelling in mind.

    :param word: str - word to remove suffix from.
    :return: str - word with suffix removed & spelling adjusted.

    Examples:
    - "heaviness" → "heavy" (change 'i' to 'y')
    - "sadness" → "sad" (no change needed)
    """
    if word.endswith("ness"):
        root = word[:-4]  # Remove 'ness'

        # If the root ends in 'i' after removing 'ness', change it to 'y'
        if root[-1] == "i":
            root = root[:-1] + "y"

        return root
    
    return word  # Return unchanged if 'ness' is not at the end

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in a sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    Example:
    - ("It got dark as the sun set.", 2) → "darken"
    """
    words = sentence.strip().split()  # Split sentence into words
    adjective = words[index].rstrip(".,!?")  # Remove punctuation if present
    return adjective + "en"