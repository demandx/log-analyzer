from openai import OpenAI

def analyze_logs_with_ai(log_text: str):
    client = OpenAI()  # client created at runtime, not import time

    prompt = f"""
You are a Linux system analyst.
Analyze the following logs and respond with:
1. Summary
2. Severity (low/medium/high)
3. Possible causes

Logs:
{log_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
