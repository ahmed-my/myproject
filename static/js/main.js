document.addEventListener('DOMContentLoaded', function() {
    const successMessages = document.querySelectorAll('.messages .success');
    if (successMessages.length > 0) {
        successMessages.forEach(message => {
            alert(message.textContent);
        });
    }
});

/* confirm delete */
document.addEventListener('DOMContentLoaded', function() {
    console.log('Document loaded, adding event listeners.');
    document.querySelectorAll('.delete-link').forEach(function(link) {
        console.log('Adding event listener to:', link);
        link.addEventListener('click', function(event) {
            event.preventDefault();
            console.log('Delete link clicked.');
            const url = this.getAttribute('data-url');
            const confirmDelete = confirm('Are you sure you want to delete this post?');
            
            if (confirmDelete) {
                console.log('User confirmed delete.');
                window.location.href = url;
            } else {
                console.log('User canceled delete.');
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
  const phrases = ["Create.", "Share.", "Inspire.", "Entertain."];
  const el = document.querySelector('.typewriter-text');
  let phraseIndex = 0;
  let letterIndex = 0;
  let typing = true;

  function type() {
    const currentPhrase = phrases[phraseIndex];
    
    if (typing) {
      el.textContent = currentPhrase.slice(0, ++letterIndex);
      if (letterIndex === currentPhrase.length) {
        typing = false;
        setTimeout(type, 1200); // pause before deleting
        return;
      }
    } else {
      el.textContent = currentPhrase.slice(0, --letterIndex);
      if (letterIndex === 0) {
        typing = true;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        setTimeout(type, 400); // pause before next phrase
        return;
      }
    }
    setTimeout(type, typing ? 100 : 60); // speed control
  }

  type();
});
