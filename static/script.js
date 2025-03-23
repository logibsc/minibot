document.addEventListener("DOMContentLoaded", function () {
    const chatContainer = document.getElementById("chatContainer");
    const chatBody = document.getElementById("chatBody");
    const userInput = document.getElementById("userInput");
    const sendButton = document.getElementById("sendButton");

    // Toggle Chat Visibility
    window.toggleChat = function () {
        chatContainer.style.display = chatContainer.style.display === "flex" ? "none" : "flex";
    };

    // Send Message
    window.sendMessage = function () {
        const message = userInput.value.trim();
        if (!message) return;

        addMessage(message, "user-message");
        userInput.value = "";
        sendButton.disabled = true; // Disable button to prevent multiple clicks
        addMessage("Typing...", "bot-message", true); // Show typing indicator

        fetch("https://minibot-production.up.railway.app/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        })
        .then(response => response.json())
        .then(data => {
            removeTypingIndicator(); // Remove "Typing..." message
            const botReply = data.response || "🤖 I'm not sure how to answer that.";
            addMessage(botReply, "bot-message");
        })
        .catch(() => {
            removeTypingIndicator();
            addMessage("⚠️ Error connecting to chatbot. Please try again.", "bot-message");
        })
        .finally(() => {
            sendButton.disabled = false; // Re-enable button after response
        });
    };

    // Handle Enter Key Press
    window.handleKeyPress = function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    };

    // Add Messages to Chat
    function addMessage(text, className, isTemporary = false) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", className);
        messageDiv.textContent = text;
        chatBody.appendChild(messageDiv);
        chatBody.scrollTop = chatBody.scrollHeight;

        if (isTemporary) {
            messageDiv.setAttribute("id", "typingIndicator");
        }
    }

    // Remove Typing Indicator
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById("typingIndicator");
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
});
