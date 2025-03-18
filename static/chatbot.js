async function sendMessage(userMessage) {
    const responseBox = document.getElementById("chat-response");

    try {
        let response = await fetch("http://127.0.0.1:8000/chat", {  // LOCAL API
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        });

        let data = await response.json();
        responseBox.innerHTML += `<div class="bot-message">${data.response}</div>`;
    } catch (error) {
        responseBox.innerHTML += `<div class="bot-message error">Error fetching response</div>`;
    }
}
