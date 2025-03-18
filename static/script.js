const API_URL = "https://minibot-production.up.railway.app/chat";  // ✅ Update with your backend URL

async function sendMessage() {
    let inputField = document.getElementById('userInput');
    let message = inputField.value.trim();
    if (!message) return;

    let chatBody = document.getElementById('chatBody');
    chatBody.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
    inputField.value = '';

    try {
        let response = await fetch(API_URL, {  // ✅ Use full API URL
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        });
        let data = await response.json();
        chatBody.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
    } catch (error) {
        chatBody.innerHTML += `<div><strong>Bot:</strong> Error connecting to chatbot.</div>`;
    }
}

function toggleChat() {
    let chatBox = document.getElementById("chatContainer");
    if (chatBox.style.display === "none" || chatBox.style.display === "") {
        chatBox.style.display = "block";
    } else {
        chatBox.style.display = "none";
    }
}
