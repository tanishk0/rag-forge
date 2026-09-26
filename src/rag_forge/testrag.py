from rag_forge.rag import ask

question = "What is this document about?"

answer = ask(question)

print("ANSWER TYPE:", type(answer))
print("ANSWER:", repr(answer))