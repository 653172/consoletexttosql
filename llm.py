import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def generate_sql(question: str) -> str:
    prompt = f"""
You are a professional SQL code generator.

Your task:
Convert natural language into correct SQL code.

Rules:
- Generate valid SQL.
- You can generate CREATE, INSERT, SELECT, UPDATE, DELETE if needed.
- Do NOT explain anything.
- Do NOT add comments.
- Return ONLY SQL code.

Examples:

Q: Create a table with 5 entries for employees
A:
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT
);

INSERT INTO employees (id, name, salary) VALUES
(1, 'John', 50000),
(2, 'Alice', 60000),
(3, 'Bob', 55000),
(4, 'Emma', 62000),
(5, 'David', 58000);

Now convert:

Q: {question}
A:
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return "Error generating SQL."

    except Exception as e:
        return f"Connection Error: {str(e)}"
