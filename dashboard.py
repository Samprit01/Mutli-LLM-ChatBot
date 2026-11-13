from utility import gemini_call, ollama_call, openai_call

print("-----------DASHBOARD FOR LLM CHOICE---------------")
print("1. OpenAI (GPT-4o)")
print("2. Ollama (Gemma4)")
print("3. Google Gemini")
print("4. Exit")
print("\n")

while True:
    choice = int(input("Enter your choice: "))
    
    match choice: 
        case 1:
            question = input("Enter your question: ")
            answer, duration = openai_call(question)
            print(f"Response: {answer}")
            print(f"Response Time: {duration:.2f} seconds\n")
            
        case 2:
            question = input("Enter your question: ")
            answer, duration = ollama_call(question)
            print(f"Response: {answer}")
            print(f"Response Time: {duration:.2f} seconds\n")
            
        case 3:
            question = input("Enter your question: ")
            answer, duration = gemini_call(question)
            print(f"Response: {answer}")
            print(f"Response Time: {duration:.2f} seconds\n")
            
        case 4: 
            print("Exiting...")
            break
            
        case _: 
            print("Not available.\n")