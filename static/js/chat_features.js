// chat_features.js

document.addEventListener('DOMContentLoaded', function () {
    const textarea = document.getElementById('message-text');
    const sendButton = document.getElementById('send-message');
    const typingIndicator = document.getElementById('typing-indicator');

    // Auto-height adjustment
    if (textarea) {
        textarea.addEventListener('input', () => {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';

            if (typingIndicator) {
                typingIndicator.style.display = 'block';
                clearTimeout(typingIndicator.timeout);
                typingIndicator.timeout = setTimeout(() => {
                    typingIndicator.style.display = 'none';
                }, 1500);
            }
        });
    }

    // Send message
    if (sendButton && textarea) {
        sendButton.addEventListener('click', () => {
            const conversationId = document.getElementById('conversation-id').value;
            const text = textarea.value.trim();

            if (!text) return;

            fetch('/users/send-message-ajax/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: new URLSearchParams({
                    conversation_id: conversationId,
                    text: text,
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    const message = data.message;
                    const messageHtml = `
                        <div class="chat-message sent">
                            <div class="message-content">
                                <p>${message.body}</p>
                                <span class="timestamp">${message.timestamp}</span>
                                <span class="read-receipt">&#10003;</span>
                            </div>
                        </div>
                    `;
                    document.getElementById('chat-messages').insertAdjacentHTML('beforeend', messageHtml);
                    textarea.value = '';
                    textarea.style.height = 'auto';
                } else {
                    alert('Error sending message.');
                }
            })
            .catch(error => {
                console.error('Message send error:', error);
            });
        });
    }

    function getCSRFToken() {
        const name = 'csrftoken';
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const trimmed = cookie.trim();
            if (trimmed.startsWith(name + '=')) {
                return decodeURIComponent(trimmed.substring(name.length + 1));
            }
        }
        return '';
    }

        // === CONTEXT MENU LOGIC ===
    let currentMessageEl = null;
    const messageMenu = document.getElementById('message-menu');

    // Attach right-click (desktop) and long-press (mobile) listeners
    document.querySelectorAll('.chat-message .message-content').forEach(msg => {
        // Desktop right-click
        msg.addEventListener('contextmenu', e => {
            e.preventDefault();
            currentMessageEl = msg.closest('.chat-message');
            showMessageMenu(e.pageX, e.pageY);
        });

        // Long press for mobile
        let pressTimer;
        msg.addEventListener('touchstart', e => {
            pressTimer = setTimeout(() => {
            currentMessageEl = msg.closest('.chat-message');
            const touch = e.touches[0];
            showMessageMenu(touch.pageX, touch.pageY);
            }, 700);
        });

        msg.addEventListener('touchend', () => clearTimeout(pressTimer));
        });

        function showMessageMenu(x, y) {
        messageMenu.style.top = `${y}px`;
        messageMenu.style.left = `${x}px`;
        messageMenu.style.display = 'block';
        }

        // Hide on click outside
        document.addEventListener('click', e => {
        if (!messageMenu.contains(e.target)) {
            messageMenu.style.display = 'none';
        }
        });

        // Handle menu actions
        messageMenu.querySelectorAll('li').forEach(option => {
        option.addEventListener('click', () => {
            if (!currentMessageEl) return;
            const action = option.getAttribute('data-action');
            const msgText = currentMessageEl.querySelector('p').innerText;

            switch (action) {
            case 'reply':
                textarea.value = `↩️ ${msgText}\n`;
                textarea.focus();
                break;
            case 'star':
                currentMessageEl.classList.toggle('starred');
                break;
            case 'forward':
                alert(`Forwarding: "${msgText}"\n(Not yet implemented)`);
                break;
            case 'delete':
                if (confirm('Delete this message?')) {
                currentMessageEl.remove();
                // Optionally add AJAX here to delete on server
                }
                break;
            }

            messageMenu.style.display = 'none';
        });
    });

    let typingTimer;
    const conversationId = document.getElementById('conversation-id').value;

    // On input
    textarea.addEventListener('input', () => {
        sendTypingStatus(true);
        clearTimeout(typingTimer);
        typingTimer = setTimeout(() => sendTypingStatus(false), 3000);
    });

    function sendTypingStatus(isTyping) {
        fetch('/users/typing-status/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCSRFToken()
            },
            body: `conversation_id=${conversationId}&is_typing=${isTyping}`
        });
    }

    function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    }

    setInterval(() => {
    fetch(`/users/get-typing-status/?conversation_id=${conversationId}`)
    .then(res => res.json())
    .then(data => {
        const indicator = document.getElementById('typing-indicator');
        indicator.style.display = data.is_typing ? 'block' : 'none';
    });
    }, 3000);
});
