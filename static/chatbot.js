async function sendMessage() {
    let userMessage = document.getElementById("userInput").value;
    if (!userMessage) return;

    let chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

    let response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    });

    let data = await response.json();
    chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
}
