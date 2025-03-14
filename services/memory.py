class ConversationMemory:
    """Stores chat history for context-aware responses."""

    def __init__(self):
        self.history = []

    def add_message(self, user_message, bot_response):
        """Stores a conversation turn."""
        self.history.append({"user": user_message, "bot": bot_response})
        if len(self.history) > 10:  # Keep only the last 10 exchanges
            self.history.pop(0)

    def get_summary(self):
        """Returns a summary of the last few messages."""
        return " ".join([f"User: {msg['user']} | Bot: {msg['bot']}" for msg in self.history])
