"""
Project 124: Word Frequency & Text Inspector
Concepts: collections.Counter, regex tokenization, string statistics.
"""
import re
from collections import Counter

SAMPLE_TEXT = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms."""

def analyze_text(text):
    words = re.findall(r"\b[a-zA-Z0-9_']+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]

    total_words = len(words)
    unique_words = len(set(words))
    counts = Counter(words)

    avg_word_len = sum(len(w) for w in words) / total_words if total_words else 0
    avg_sentence_len = total_words / len(sentences) if sentences else 0

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "counts": counts,
        "avg_word_len": avg_word_len,
        "avg_sentence_len": avg_sentence_len,
        "sentences_count": len(sentences)
    }

def main():
    print("=== WORD FREQUENCY & TEXT INSPECTOR ===")
    use_sample = input("Use sample text? (y/n, default y): ").strip().lower() != 'n'
    if use_sample:
        text = SAMPLE_TEXT
        print(f"\nSample Text:\n{text}\n")
    else:
        print("Enter text (finish with Enter):")
        text = input("> ")

    stats = analyze_text(text)
    print("=== ANALYSIS RESULTS ===")
    print(f"Total Words: {stats['total_words']}")
    print(f"Unique Words: {stats['unique_words']}")
    print(f"Total Sentences: {stats['sentences_count']}")
    print(f"Average Word Length: {stats['avg_word_len']:.2f} letters")
    print(f"Average Sentence Length: {stats['avg_sentence_len']:.2f} words")

    print("\nTop 5 Most Common Words:")
    for word, cnt in stats['counts'].most_common(5):
        print(f" • '{word}': {cnt} times")

if __name__ == "__main__":
    main()
