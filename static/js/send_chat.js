$(document).ready(function() {
            $('#send-message').on('click', function() {
                var conversationId = $('#conversation-id').val();
                var text = $('#message-text').val();
                $.ajax({
                    url: "{% url 'users:send_message_ajax' %}",
                    type: "POST",
                    data: {
                        'conversation_id': conversationId,
                        'text': text,
                        'csrfmiddlewaretoken': '{{ csrf_token }}'
                    },
                    success: function(response) {
                        if (response.status === 'ok') {
                            var message = response.message;
                            var messageHtml = '<div class="chat-message sent">' +
                                              '<div class="message-content">' +
                                              '<p>' + message.body + '</p>' +
                                              '<span class="timestamp">' + message.timestamp + '</span>' +
                                              '<button class="delete-chat" data-message-id="' + message.id + '">Delete</button>' +
                                              '</div>' +
                                              '</div>';
                            $('#chat-messages').append(messageHtml);
                            $('#message-text').val(''); // Clear the textarea
                        } else {
                            alert('Error sending message.');
                        }
                    },
                    error: function(xhr, status, error) {
                        alert('An error occurred: ' + error);
                        console.log("Status: " + status);
                        console.log("Error: " + error);
                    }
                });
            });

            // Delete chat functionality
            $(document).on('click', '.delete-chat', function() {
                var messageId = $(this).data('message-id');
                var $message = $(this).closest('.chat-message');

                // Confirm deletion
                if (confirm('Do you want to delete this chat message?')) {
                    $.ajax({
                        url: "{% url 'users:delete_chat' %}",
                        type: "POST",
                        data: {
                            'message_id': messageId,
                            'csrfmiddlewaretoken': '{{ csrf_token }}'
                        },
                        success: function(response) {
                            if (response.status === 'ok') {
                                $message.remove(); // Remove the message from the chat
                            } else {
                                alert('Error deleting message.');
                            }
                        },
                        error: function(xhr, status, error) {
                            alert('An error occurred: ' + error);
                            console.log("Status: " + status);
                            console.log("Error: " + error);
                        }
                    });
                }
            });
        });