import { EmojiButton } from 'https://cdn.jsdelivr.net/npm/@joeattardi/emoji-button@4.6.2/dist/index.min.js';

  const picker = new EmojiButton();
  const trigger = document.querySelector('#emoji-button');
  const textarea = document.querySelector('#message-text');

  if (trigger && textarea) {
    picker.on('emoji', emoji => {
      textarea.value += emoji;
    });

    trigger.addEventListener('click', () => {
      picker.togglePicker(trigger);
    });
  }