document.addEventListener("DOMContentLoaded", function () {
    const chatContainer = document.getElementById("chatContainer");
    const chatBody = document.getElementById("chatBody");
    const userInput = document.getElementById("userInput");

    window.toggleChat = function () {
        chatContainer.style.display = chatContainer.style.display === "flex" ? "none" : "flex";
    };

    window.sendMessage = function () {
        const message = userInput.value.trim();
        if (!message) return;

        addMessage(message, "user-message");
        userInput.value = "";

        fetch("https://minibot-production.up.railway.app/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            const botReply = data.response || "Sorry, I didn't understand that.";
            addMessage(botReply, "bot-message");
        })
        .catch(() => {
            addMessage("Error connecting to chatbot.", "bot-message");
        });
    };

    window.handleKeyPress = function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    };

    function addMessage(text, className) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", className);
        messageDiv.textContent = text;
        chatBody.appendChild(messageDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }
});
