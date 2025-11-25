# Rule-Based Chatbot

A conversational AI chatbot built using Python's if-elif-else logic for pattern matching and response generation.

## Features

- ✅ Interactive conversation loop
- ✅ Pattern matching with if-elif-else statements
- ✅ Multiple conversation topics
- ✅ Greetings and farewells
- ✅ Time and date information
- ✅ Jokes and entertainment
- ✅ Basic calculations
- ✅ Name recognition
- ✅ Personalized responses
- ✅ Exit mechanism

## Installation

No external dependencies required! Uses only Python standard library.

**Requirements:**
- Python 3.6+

## Usage

### Basic Usage

Run the chatbot:
```bash
python chatbot.py
```

### Example Conversation

```
============================================================
Welcome to BotAI - Your Friendly Chatbot!
============================================================
Type 'quit', 'exit', or 'bye' to end the conversation.

BotAI: Hello! I'm BotAI. How can I help you today?

You: hi
BotAI: Hi there! I'm BotAI, your virtual assistant.

You: what's your name?
BotAI: I'm BotAI, a rule-based chatbot created to assist you!

You: tell me a joke
BotAI: Why don't programmers like nature? It has too many bugs! 😄

You: what time is it?
BotAI: The current time is 14:30:45

You: my name is John
BotAI: Nice to meet you, John! How can I help you today?

You: what is 5 + 3?
BotAI: The result is: 8

You: bye
BotAI: Goodbye! Have a great day!
============================================================
```

## Supported Queries

### Greetings
- "hi", "hello", "hey"
- "good morning", "good afternoon", "good evening"

### Personal Information
- "what's your name?"
- "who are you?"
- "my name is [name]"
- "how old are you?"

### Time & Date
- "what time is it?"
- "what's the date today?"
- "what day is it?"

### Small Talk
- "how are you?"
- "tell me a joke"
- "give me advice"
- "what's your favorite color?"

### Capabilities
- "what can you do?"
- "help"

### Calculations
- "what is 5 + 3?"
- "calculate 10 * 2"

### Exit Commands
- "quit", "exit", "bye", "goodbye"

## Code Structure

```python
class SimpleChatbot:
    """Main chatbot class"""
    
    def __init__(self, name):
        # Initialize chatbot with name
        
    def process_message(self, user_input):
        # Process user input and return response
        # Uses if-elif-else for pattern matching
        
    def run(self):
        # Main conversation loop
```

## How It Works

The chatbot uses a rule-based approach with if-elif-else statements:

1. **Input Processing**: Converts user input to lowercase for case-insensitive matching
2. **Pattern Matching**: Checks for keywords using `in` operator
3. **Response Generation**: Returns appropriate response or random variation
4. **Loop**: Continues until user types an exit command

### Example Logic

```python
if 'hello' in message or 'hi' in message:
    return "Hello! How can I help you?"
elif 'time' in message:
    return get_current_time()
elif 'joke' in message:
    return random.choice(jokes_list)
else:
    return "I don't understand. Could you rephrase?"
```

## Customization

### Adding New Responses

To add new conversation patterns, edit the `process_message()` method:

```python
elif 'your_keyword' in message:
    return "Your custom response"
```

### Adding Random Responses

Use Python's `random.choice()` for variety:

```python
responses = [
    "Response 1",
    "Response 2",
    "Response 3"
]
return random.choice(responses)
```

### Changing Bot Name

Modify the bot name when creating the instance:

```python
bot = SimpleChatbot(name="MyBot")
```

## Understanding NLP Basics

This chatbot demonstrates fundamental Natural Language Processing concepts:

### 1. **Text Preprocessing**
```python
message = user_input.lower().strip()
```

### 2. **Keyword Matching**
```python
if 'keyword' in message:
    # Respond appropriately
```

### 3. **Intent Recognition**
```python
if 'time' in message and 'what' in message:
    return get_time()
```

### 4. **Context Tracking**
```python
self.user_name = extract_name(message)
# Use in future responses
```

### 5. **Response Generation**
```python
return random.choice(response_options)
```

## Limitations

As a rule-based chatbot, it has limitations:

- ❌ No machine learning or AI understanding
- ❌ Limited to predefined patterns
- ❌ Cannot handle complex queries
- ❌ No learning capability
- ❌ Responses are deterministic based on rules

## Future Enhancements

Potential improvements:

- 🔄 Add more conversation topics
- 🔄 Implement spell checking
- 🔄 Add sentiment analysis
- 🔄 Store conversation history
- 🔄 Add multiple languages
- 🔄 Integrate with APIs (weather, news, etc.)
- 🔄 Use machine learning for better responses

## Learning Outcomes

By implementing this chatbot, you learn:

- ✅ Control flow with if-elif-else
- ✅ String manipulation in Python
- ✅ User input handling
- ✅ Loop structures
- ✅ Function organization
- ✅ Object-oriented programming basics
- ✅ Basic NLP concepts
- ✅ Pattern matching techniques

## Troubleshooting

### Issue: Bot doesn't recognize my input
**Solution**: Make sure you're using keywords from the supported queries list.

### Issue: Math calculations don't work
**Solution**: Use format like "what is 5 + 3" with spaces between numbers and operators.

### Issue: Bot repeats same responses
**Solution**: Random responses are implemented - you might see repeats occasionally.

## Project Structure

```
Task 8/
├── chatbot.py          # Main chatbot script
├── requirement.md      # Task requirements
└── README.md          # This file
```

## License

MIT License - Feel free to use and modify!

## Author

Built as part of the ElevenLabs task series to demonstrate rule-based conversational AI.

---

**Have fun chatting! 🤖💬**
