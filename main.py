import ollama

print("=" * 50)
print("       AI CUSTOMER SUPPORT ASSISTANT")
print("=" * 50)

customer_name = input("\nCustomer name: ")
customer_message = input("Customer message: ")

prompt = f"""
You are a professional customer support assistant.

Customer name: {customer_name}

Customer message:
{customer_message}

Write a short, polite and professional reply.

Rules:
- Do not invent information.
- Do not promise a refund unless the customer specifically asks for one.
- Do not mention that you are an AI.
- Keep the response under 150 words.
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

reply = response["message"]["content"]

print("\n" + "=" * 50)
print("AI SUGGESTED REPLY")
print("=" * 50)
print(reply)