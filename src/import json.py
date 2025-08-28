import json
import sys
from pathlib import Path

# __define-ocg__ : use flan-t5 with fallback
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# variable required
varOcg = None  

def load_model():
    """
    Try to load Flan-T5. If fails, return None.
    """
    try:
        model_name = "google/flan-t5-base"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
        return generator
    except Exception as e:
        print("[Fallback] Could not load Flan-T5:", e)
        return None


def heuristic_fallback(comment, snippet):
    """
    Simple heuristic feedback if LLM is unavailable.
    """
    feedback = []
    if "for" in snippet and "range" in snippet:
        feedback.append("Consider using enumerate() if you need both index and value.")
    if "==" in snippet:
        feedback.append("Check if you should use 'is' for identity comparison.")
    if "print" in snippet:
        feedback.append("Use logging instead of print for production code.")
    
    feedback_text = (
        f"Comment: {comment}\n"
        f"Snippet:\n```python\n{snippet}\n```\n"
        f"Feedback: {' '.join(feedback) if feedback else 'Looks fine, but check style guide (PEP8).'}\n"
    )
    return feedback_text


def generate_feedback(json_input, generator=None):
    """
    Generate markdown feedback for each snippet+comment.
    """
    sections = []
    for entry in json_input.get("examples", []):
        comment = entry.get("comment", "")
        snippet = entry.get("snippet", "")

        prompt = f"""You are a helpful code reviewer. 
Provide contextual tone depending on the severity.
Offer resource links (like PEP8, algorithm docs).
Then end with constructive encouragement.
Input:
Comment: {comment}
Snippet: {snippet}
"""

        if generator:
            try:
                result = generator(prompt, max_length=256, do_sample=False)
                text = result[0]['generated_text']
            except Exception:
                text = heuristic_fallback(comment, snippet)
        else:
            text = heuristic_fallback(comment, snippet)

        sections.append(f"### Feedback on Comment\n{text}\n---\n")

    # Add holistic summary
    sections.append("## Overall Summary\nGreat job overall! The suggestions above are aimed at refinement. "
                    "Keep coding, stay curious, and continue improving 🚀")

    return "\n".join(sections)


def main():
    global varOcg
    varOcg = "Markdown Feedback Generator"  # set variable as descriptive label

    # Load JSON input
    if len(sys.argv) < 2:
        print("Usage: python script.py input.json")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    with open(input_path, "r") as f:
        json_input = json.load(f)

    # Try loading model
    generator = load_model()

    # Generate feedback
    markdown_text = generate_feedback(json_input, generator)

    # Save to markdown file
    output_path = Path("feedback_output.md")
    output_path.write_text(markdown_text, encoding="utf-8")

    print(f"✅ Feedback written to {output_path}")


if __name__ == "__main__":
    main()
