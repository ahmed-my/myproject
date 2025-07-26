// chat-menu-container.js
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

document.addEventListener('DOMContentLoaded', () => {
      const chatOptionsBtn = document.getElementById('chat-options-btn');
      const chatOptionsMenu = document.getElementById('chat-options-menu');
      const contextMenu = document.getElementById('message-menu');

      // Toggle header menu
      chatOptionsBtn?.addEventListener('click', e => {
        e.stopPropagation();
        chatOptionsMenu.style.display = chatOptionsMenu.style.display === 'block' ? 'none' : 'block';
      });

      document.addEventListener('click', () => {
        chatOptionsMenu.style.display = 'none';
        contextMenu.style.display = 'none';
      });

      // Handle Clear Chat action
      document.querySelector('#chat-options-menu li[data-action="clear"]')?.addEventListener('click', () => {
        const conversationId = document.getElementById('conversation-id').value;
        if (confirm("Are you sure you want to clear this chat?")) {
            fetch(`/users/clear-chat/${conversationId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie('csrftoken'),
                },
            })
            .then(res => {
                if (res.ok) {
                    document.getElementById('chat-messages').innerHTML = '';
                } else {
                    alert("Failed to clear chat.");
                }
            });
        }
      });


      // Right-click context menu for messages
      document.querySelectorAll('.chat-message .message-content').forEach(msg => {
        msg.addEventListener('contextmenu', e => {
          e.preventDefault();
          contextMenu.style.display = 'block';
          contextMenu.style.top = `${e.clientY}px`;
          contextMenu.style.left = `${e.clientX}px`;
        });
      });
    });