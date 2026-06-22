"""
BCG GenAI Consulting Team - Simple Financial Chatbot
Client: Global Finance Corp. (GFC)
Author: Junior Data Scientist (Hassan)
"""

def simple_chatbot(user_query):
    # Standardize input by making it lowercase and removing extra spaces
    query = user_query.lower().strip()

    # --- APPLE PREDEFINED QUERIES ---
    if query == "what is the total revenue of apple in 2023?":
        return "The total revenue for Apple in 2023 was $383,285 Million USD."
    elif query == "what is the total revenue of apple in 2024?":
        return "The total revenue for Apple in 2024 was $391,035 Million USD."
    elif query == "what is the total revenue of apple in 2025?":
        return "The total revenue for Apple in 2025 was $405,500 Million USD."
    elif query == "how has net income changed for apple over the last year?":
        return "Apple's net income increased from $100,345 Million in 2024 to $112,000 Million in 2025."

    # --- MICROSOFT PREDEFINED QUERIES ---
    elif query == "what is the total revenue of microsoft in 2023?":
        return "The total revenue for Microsoft in 2023 was $211,915 Million USD."
    elif query == "what is the total revenue of microsoft in 2024?":
        return "The total revenue for Microsoft in 2024 was $245,122 Million USD."
    elif query == "what is the total revenue of microsoft in 2025?":
        return "The total revenue for Microsoft in 2025 was $265,000 Million USD."
    elif query == "how has net income changed for microsoft over the last year?":
        return "Microsoft's net income increased from $88,136 Million in 2024 to $92,000 Million in 2025."

    # --- TESLA PREDEFINED QUERIES ---
    elif query == "what is the total revenue of tesla in 2023?":
        return "The total revenue for Tesla in 2023 was $96,773 Million USD."
    elif query == "what is the total revenue of tesla in 2024?":
        return "The total revenue for Tesla in 2024 was $98,500 Million USD."
    elif query == "what is the total revenue of tesla in 2025?":
        return "The total revenue for Tesla in 2025 was $102,000 Million USD."
    elif query == "how has net income changed for tesla over the last year?":
        return "Tesla's net income decreased from $10,500 Million in 2024 to $8,500 Million in 2025."

    # --- ERROR HANDLING ---
    else:
        return "Sorry, I can only provide information on predefined queries."


# Simple command-line interface loop to test the prototype
if __name__ == "__main__":
    print("Welcome to the GFC Financial Chatbot Prototype!")
    print("Ask about 2023-2025 Total Revenue or Net Income changes for Apple, Microsoft, or Tesla.")
    print("Type 'exit' to close the program.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
            
        response = simple_chatbot(user_input)
        print(f"🤖: {response}")
