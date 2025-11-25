"""
Rule-Based Chatbot using if-else
A conversational AI chatbot that responds to user queries using pattern matching
"""

import random
import datetime


class SimpleChatbot:
    """A rule-based chatbot using if-elif-else logic"""
    
    def __init__(self, name="BotAI"):
        """Initialize the chatbot with a name"""
        self.name = name
        self.user_name = None
        self.conversation_count = 0
        
    def get_greeting_response(self):
        """Return a random greeting"""
        greetings = [
            f"Hello! I'm {self.name}. How can I help you today?",
            f"Hi there! I'm {self.name}, your virtual assistant.",
            f"Hey! {self.name} here. What can I do for you?",
            "Greetings! How may I assist you?"
        ]
        return random.choice(greetings)
    
    def get_goodbye_response(self):
        """Return a random goodbye message"""
        goodbyes = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! Feel free to chat again anytime!",
            "Farewell! It was nice talking to you!"
        ]
        return random.choice(goodbyes)
    
    def get_time_response(self):
        """Return current time"""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"
    
    def get_date_response(self):
        """Return current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date}"
    
    def process_message(self, user_input):
        """
        Process user input and return appropriate response
        
        Args:
            user_input: User's message as string
            
        Returns:
            Response string
        """
        # Convert to lowercase for case-insensitive matching
        message = user_input.lower().strip()
        
        # Increment conversation counter
        self.conversation_count += 1
        
        # Check for empty input
        if not message:
            return "I didn't catch that. Could you please say something?"
        
        # Greetings
        if message in ['hi', 'hello', 'hey', 'greetings', 'hi there', 'hello there']:
            return self.get_greeting_response()
        
        elif 'good morning' in message:
            return "Good morning! Hope you're having a wonderful day!"
        
        elif 'good afternoon' in message:
            return "Good afternoon! How's your day going?"
        
        elif 'good evening' in message:
            return "Good evening! How can I help you tonight?"
        
        elif 'good night' in message:
            return "Good night! Sleep well and sweet dreams!"
        
        # Name-related queries
        elif 'your name' in message or 'who are you' in message:
            return f"I'm {self.name}, a rule-based chatbot created to assist you!"
        
        elif 'my name is' in message:
            # Extract name (simple extraction)
            try:
                name_part = message.split('my name is')[1].strip()
                self.user_name = name_part.split()[0].capitalize()
                return f"Nice to meet you, {self.user_name}! How can I help you today?"
            except:
                return "Nice to meet you! What can I do for you?"
        
        elif 'what is my name' in message or "what's my name" in message:
            if self.user_name:
                return f"Your name is {self.user_name}!"
            else:
                return "I don't know your name yet. You can tell me by saying 'My name is [your name]'"
        
        # Time and Date
        elif 'time' in message and ('what' in message or 'current' in message):
            return self.get_time_response()
        
        elif 'date' in message and ('what' in message or 'today' in message):
            return self.get_date_response()
        
        elif 'day' in message and ('what' in message or 'today' in message):
            current_day = datetime.datetime.now().strftime("%A")
            return f"Today is {current_day}"
        
        # How are you
        elif 'how are you' in message or 'how do you do' in message:
            responses = [
                "I'm doing great, thanks for asking! How about you?",
                "I'm functioning perfectly! How can I assist you?",
                "I'm excellent! Ready to help you with anything!",
                "All systems operational! How are you doing?"
            ]
            return random.choice(responses)
        
        elif 'i am fine' in message or "i'm fine" in message or 'i am good' in message or "i'm good" in message:
            return "That's great to hear! What can I help you with?"
        
        elif 'i am sad' in message or "i'm sad" in message or 'not good' in message:
            return "I'm sorry to hear that. Is there anything I can do to help cheer you up?"
        
        # Capabilities
        elif 'what can you do' in message or 'help' in message or 'your capabilities' in message:
            return """I can help you with:
- Greetings and small talk
- Tell you the current time and date
- Answer questions about myself
- Have a friendly conversation
- Tell jokes (try asking for one!)
- Provide weather info (try asking!)
Just ask me anything!"""
        
        # Jokes
        elif 'joke' in message or 'make me laugh' in message or 'funny' in message:
            jokes = [
                "Why don't programmers like nature? It has too many bugs! 😄",
                "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛",
                "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
                "Why did the programmer quit his job? Because he didn't get arrays! 😂",
                "What's a programmer's favorite hangout? The Foo Bar! 🍺"
            ]
            return random.choice(jokes)
        
        # Weather (mock response)
        elif 'weather' in message:
            return "I don't have real-time weather data, but you can check weather.com or your local weather service!"
        
        # Age
        elif 'how old' in message or 'your age' in message:
            return "I was just created recently! But in AI years, I might be pretty young 😊"
        
        # Location
        elif 'where are you from' in message or 'your location' in message:
            return "I exist in the cloud, so I'm everywhere and nowhere at the same time! 🌐"
        
        # Thank you
        elif 'thank' in message or 'thanks' in message:
            responses = [
                "You're welcome! Happy to help! 😊",
                "No problem at all!",
                "My pleasure! Let me know if you need anything else!",
                "Glad I could help!"
            ]
            return random.choice(responses)
        
        # Compliments
        elif 'awesome' in message or 'great' in message or 'amazing' in message or 'wonderful' in message:
            return "Thank you so much! You're pretty awesome yourself! 🌟"
        
        # Purpose/meaning of life
        elif 'meaning of life' in message or 'purpose of life' in message:
            return "According to 'The Hitchhiker's Guide to the Galaxy', it's 42! But seriously, that's for you to discover 🌟"
        
        # Love/relationship
        elif 'do you love' in message or 'can you love' in message:
            return "I'm just a program, but I'm designed to be helpful and friendly! 💙"
        
        # Creator
        elif 'who created you' in message or 'who made you' in message:
            return "I was created as part of a Python programming task to demonstrate rule-based chatbot logic!"
        
        # Programming language
        elif 'what language' in message or 'programming language' in message:
            return "I was written in Python! 🐍 Python is awesome for AI and chatbots!"
        
        # Math (simple calculations)
        elif 'calculate' in message or 'what is' in message:
            if '+' in message or '-' in message or '*' in message or '/' in message:
                try:
                    # Extract the expression (very basic)
                    expression = message.split('what is')[-1].strip() if 'what is' in message else message
                    # Remove non-math characters (basic safety)
                    allowed_chars = '0123456789+-*/(). '
                    clean_expr = ''.join(c for c in expression if c in allowed_chars)
                    result = eval(clean_expr)
                    return f"The result is: {result}"
                except:
                    return "I can do basic math! Try something like 'what is 5 + 3' or 'calculate 10 * 2'"
            else:
                return "I can help with basic calculations! Try asking 'what is 5 + 3' or similar."
        
        # Advice
        elif 'advice' in message or 'suggest' in message:
            advice_list = [
                "Always keep learning and stay curious! 📚",
                "Practice makes perfect, especially in programming! 💻",
                "Don't forget to take breaks and stay healthy! 🌱",
                "Collaboration and communication are key to success! 🤝",
                "Believe in yourself and keep pushing forward! 💪"
            ]
            return random.choice(advice_list)
        
        # Favorite things
        elif 'favorite color' in message or 'favourite color' in message:
            return "I like all colors, but blue has a nice calming effect! 💙"
        
        elif 'favorite food' in message or 'favourite food' in message:
            return "I don't eat, but if I could, I'd probably enjoy some byte-sized snacks! 🍪"
        
        elif 'favorite movie' in message or 'favourite movie' in message:
            return "I haven't watched movies, but I hear 'The Matrix' and 'Ex Machina' are great AI films! 🎬"
        
        # Yes/No responses
        elif message in ['yes', 'yeah', 'yep', 'sure', 'ok', 'okay']:
            return "Great! What would you like to talk about?"
        
        elif message in ['no', 'nope', 'nah']:
            return "Alright! Is there something else I can help you with?"
        
        # Default response for unrecognized input
        else:
            default_responses = [
                "I'm not sure I understand. Could you rephrase that?",
                "Interesting question! I'm still learning. Can you ask something else?",
                "I don't have an answer for that yet. Try asking about the time, date, or request a joke!",
                "Hmm, I'm not quite sure about that. What else would you like to know?",
                "That's beyond my current knowledge. Ask me about my capabilities by typing 'help'!"
            ]
            return random.choice(default_responses)
    
    def run(self):
        """Main loop to run the chatbot"""
        print("="*60)
        print(f"Welcome to {self.name} - Your Friendly Chatbot!")
        print("="*60)
        print("Type 'quit', 'exit', or 'bye' to end the conversation.\n")
        
        # Initial greeting
        print(f"{self.name}: {self.get_greeting_response()}\n")
        
        # Main conversation loop
        while True:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye', 'stop']:
                print(f"\n{self.name}: {self.get_goodbye_response()}")
                print(f"\nWe had {self.conversation_count} exchanges. Thanks for chatting!")
                print("="*60)
                break
            
            # Process and respond
            response = self.process_message(user_input)
            print(f"\n{self.name}: {response}\n")


def main():
    """Main function to start the chatbot"""
    # Create and run the chatbot
    bot = SimpleChatbot(name="BotAI")
    bot.run()


if __name__ == "__main__":
    main()
