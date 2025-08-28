# AI-Powered Code Review Assistant

This project is a **hackathon submission** showcasing an **AI-powered
code review assistant** that provides contextual, empathetic, and
actionable feedback on user-provided code snippets. It is designed to
demonstrate skills in **prompt engineering, empathetic AI design, and
code comprehension/explanation**.

------------------------------------------------------------------------

## 🚀 Features

-   **JSON Input → Markdown Output**: Accepts feedback and code snippets
    in JSON format and produces structured Markdown reports.
-   **Free LLM (no API key required)**: Uses Hugging Face
    `google/flan-t5-base` for feedback generation.
    -   If model loading fails, the system falls back to a **smart
        heuristic rule-based engine** so it always works.
-   **Contextual Awareness**: Feedback tone changes based on severity
    (e.g., gentle suggestions vs. urgent fixes).
-   **External Links**: Suggestions include links to documentation
    (e.g., PEP 8, Big-O references).
-   **Holistic Summary**: Concludes with an encouraging summary for
    developers.
-   **Hackathon Ready**: Lightweight, runs locally, no external paid
    APIs.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Python 3.8+**
-   **Hugging Face Transformers** (`google/flan-t5-base`)
-   **Fallback Heuristic Rules** (if LLM unavailable)
-   **Markdown Generation** for GitHub-friendly reports

------------------------------------------------------------------------

## 📥 Input Format (JSON)

``` json
{
  "feedback": [
    {
      "severity": "high",
      "comment": "The loop has O(n^2) complexity, consider optimizing.",
      "snippet": "for i in range(n):
  for j in range(n):
    process(i, j)"
    },
    {
      "severity": "low",
      "comment": "Consider following snake_case naming convention.",
      "snippet": "UserName = 'Alice'"
    }
  ]
}
```

------------------------------------------------------------------------

## 📤 Output Format (Markdown)

``` markdown
# AI Code Review Report

### 🔴 Issue 1 (High Severity)
**Comment:** The loop has O(n^2) complexity, consider optimizing.  
**Code Snippet:**
```python
for i in range(n):
    for j in range(n):
        process(i, j)
```

**Suggestion:** Consider reducing nested loops or applying memoization.\
📖 [Learn more about algorithmic
complexity](https://www.bigocheatsheet.com/)

------------------------------------------------------------------------

### 🟢 Issue 2 (Low Severity)

**Comment:** Consider following snake_case naming convention.\
**Code Snippet:**

``` python
UserName = 'Alice'
```

**Suggestion:** Rename to `user_name` for Pythonic style.\
📖 [PEP 8 Naming
Conventions](https://peps.python.org/pep-0008/#naming-conventions)

------------------------------------------------------------------------

## ✅ Overall Summary

Your code shows strong functionality and structure. Addressing these
minor improvements will enhance readability and efficiency. Keep up the
great work 🚀!


    ---

    ## ▶️ How to Run
    1. Clone this repository:
       ```bash
       git clone https://github.com/your-username/ai-code-review-assistant.git
       cd ai-code-review-assistant

2.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

3.  Run the tool:

    ``` bash
    python code_review.py input.json output.md
    ```

4.  Open the generated `output.md` in GitHub/Markdown viewer.

------------------------------------------------------------------------

## 🎯 Hackathon Edge: Tips for Standing Out

-   **Contextual Awareness**: Our AI dynamically adjusts tone depending
    on severity.\
-   **External Links**: Developers receive immediate references to
    improve their code.\
-   **Holistic Summary**: Ending feedback positively boosts developer
    morale.\
-   **Empathetic Design**: Helps developers learn, not just fix.

------------------------------------------------------------------------

## 👨‍💻 Key Skills Demonstrated

-   Prompt Engineering with LLMs\
-   Empathetic AI/UX in code feedback\
-   Rule-based + AI hybrid fallback design\
-   Markdown report automation

------------------------------------------------------------------------

## 📜 License

MIT License - free to use and adapt.

------------------------------------------------------------------------

## 🙌 Acknowledgements

-   [Hugging Face Transformers](https://huggingface.co/transformers/)\
-   [PEP 8 Python Style Guide](https://peps.python.org/pep-0008/)\
-   [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
