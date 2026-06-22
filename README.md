
# GFC Financial Chatbot Engine Documentation

### ⚙️ How it Works
The application uses strict rule-based string evaluation. It tokenizes user inputs to pull key variables: the **Entity** (Apple, Microsoft, Tesla), the **Timeline** (2023-2025), and the **Target Metric** (Revenue, Net Income, Balance Sheet Health, or Growth trends). Once found, it runs lookup sequences or real-time calculations directly against the underlying structured data dictionary.

### ❓ Supported Queries
1. **Revenue Lookup:** e.g., *"What is the total revenue of Apple in 2024?"*
2. **Profitability Check:** e.g., *"Show me Microsoft net income in 2025."*
3. **Capital Structure Analysis:** e.g., *"What is Tesla's financial health in 2023?"*
4. **Time-Series Growth Trends:** e.g., *"How did revenue change for Apple in 2025?"*

### ⚠️ Prototype Limitations
* **Exact Matching Strings:** Lacks true natural language intent processing; users must specify the valid names and years for logic triggers to activate.
* **Limited Scope:** Constrained exclusively to the hardcoded database of 3 companies across a 3-year timeline.
* **Static Memory:** Operates statelessly; it treats every conversation line entirely as a separate query without tracking context across prompts.
