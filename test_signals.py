#!/usr/bin/env python3
"""
Test script to run and evaluate text samples across Signal 1 (detector.py) and Signal 2 (stylometry.py).
"""

import config
from detector import model_signal, perplexity
from stylometry import (
    punctuation_density,
    sentence_length_spread,
    style_signal,
    type_token_ratio,
)

# 1. Real-World Test Texts
SAMPLES = [
    {
        "label": "1. Clearly Human",
        "text": (
            "What art thou that usurp’st this time of night, Together with that fair and warlike form. In which the majesty of buried Denmark. Did sometimes march? By heaven, I charge thee, speak."
        ),
    },
    {
        "label": "2. Clearly AI",
        "text": (
            "ChatGPT is a large language model developed by OpenAI. It is trained on a massive dataset of text and is able to generate human-like responses to a wide range of prompts. It can be used for a variety of tasks such as language translation, text summarization, and conversation generation. It has been trained on a diverse set of internet text and is capable of understanding and generating text in a variety of languages and styles."
        ),
    },
    {
        "label": "3. Formal Human Writing",
        "text": (
            "A spirit who claims to be the ghost of Hamlet’s father describes his murder at the hands of Claudius and demands that Hamlet avenge the killing. When the councilor Polonius learns from his daughter, Ophelia, that Hamlet has visited her in an apparently distracted state, Polonius attributes the prince’s condition to lovesickness, and he sets a trap for Hamlet using Ophelia as bait."
        ),
    },
        {
        "label": "4. Lightly-Edited AI",
        "text": (
            "Key threats to the health of native plants in Britain and Ireland include climate change, habitat loss, and the spread of non-native species. The BSBI highlighted the devastating loss of species in Scotland as one of the significant findings. Notably, almost the entire British population of snow pearlwort is located on Ben Lawers, yet half of the known colonies on this Perthshire mountain have vanished over the past 40 years."
        ),
    },
]

def run_tests():
    print("=" * 100)
    print("PROVENANCE GUARD — SIGNAL EVALUATION TEST")
    print("=" * 100)

    for sample in SAMPLES:
        text = sample["text"]

        # Signal 1: Detector Model Score & Perplexity
        try:
            sig1_ppl = perplexity(text)
            sig1_score = model_signal(text)
        except ValueError as err:
            sig1_ppl = 0.0
            sig1_score = 0.5  # Default/fallback

        # Signal 2: Stylometry Metrics & Combined Score
        spread = sentence_length_spread(text)
        ttr = type_token_ratio(text)
        punc = punctuation_density(text)
        sig2_score = style_signal(text)

        # Combined Score:
        combined_score = (config.WEIGHT_MODEL_SIGNAL * sig1_score) + (config.WEIGHT_STYLE_SIGNAL * sig2_score)
        combined_score_split = (0.80 * sig1_score) + (0.20 * sig2_score)

        # Output Results
        print(f"\nSAMPLE: {sample['label']}")
        print(f'Text: "{text[:80]}..."')
        print("-" * 50)
        print(f"  [Signal 1] Perplexity:       {sig1_ppl:.2f}")
        print(f"  [Signal 1] Model AI Score:   {sig1_score:.4f}")
        print(f"  [Signal 2] Sentence Spread:  {spread:.4f}")
        print(f"  [Signal 2] Type-Token Ratio: {ttr:.4f}")
        print(f"  [Signal 2] Punc. Density:    {punc:.4f}")
        print(f"  [Signal 2] Style AI Score:   {sig2_score:.4f}")
        print(f"  [Signal 3] Combined Score:   {combined_score:.4f}")
        print(f"  [Signal 3] Split Score:      {combined_score_split:.4f}")
        print("-" * 50)

    print("\n" + "=" * 100)

if __name__ == "__main__":
    run_tests()