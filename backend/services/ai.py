from openai import OpenAI

client = OpenAI(
    api_key="g4f_u_mnlj3n_97afcf132daff7aafe278ee6e26c58b39cc4920465080170_794b53f6",
    base_url="https://g4f.space/v1"
)

def generate_json(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )

    return response.choices[0].message.content
