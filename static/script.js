document.addEventListener("DOMContentLoaded", function () {
    const chatContainer = document.getElementById("chatContainer");
    const chatBody = document.getElementById("chatBody");
    const userInput = document.getElementById("userInput");

    // ✅ Toggle Chat Window
    window.toggleChat = function () {
        chatContainer.classList.toggle("open");
    };

    // ✅ Handle Enter Key Press
    window.handleKeyPress = function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    };

    // ✅ Send Message to Chatbot
    window.sendMessage = async function () {
        const userMessage = userInput.value.trim();
        if (userMessage === "") return;

        // Add user message to chat
        addMessage("You", userMessage);
        userInput.value = "";

        try {
            const response = await fetch("https://minibot-production.up.railway.app/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage }),
            });

            if (!response.ok) throw new Error("Failed to fetch response");
            const data = await response.json();
            addMessage("Bot", data.response);
        } catch (error) {
            addMessage("Bot", "Error connecting to chatbot.");
        }

        // ✅ Scroll to latest message
        chatBody.scrollTop = chatBody.scrollHeight;
    };

    // ✅ Add Message to Chat Window
    function addMessage(sender, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender.toLowerCase());
        messageDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
        chatBody.appendChild(messageDiv);

        // ✅ Auto-scroll to latest message
        chatBody.scrollTop = chatBody.scrollHeight;
    }
});
