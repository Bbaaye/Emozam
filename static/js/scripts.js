// document.addEventListener('DOMContentLoaded', function() {
//     const startCaptureButton = document.getElementById('startCapture');
//     const restartButton = document.getElementById('restart');
//     const resultDiv = document.getElementById('result');
//     const statusDiv = document.getElementById('status');
//     const emotionElement = document.getElementById('emotion');
//     const songElement = document.getElementById('song');
//     const songLink = document.getElementById('songLink');

//     startCaptureButton.addEventListener('click', function() {
//         fetch('/start_capture', { method: 'POST' })
//             .then(response => response.json())
//             .then(data => {
//                 emotionElement.textContent = `Detected Emotion: ${data.emotion}`;
//                 songElement.textContent = `Suggested Song: ${data.songName}`;
//                 songLink.href = data.songUrl;
//                 statusDiv.style.display = 'none';
//                 resultDiv.style.display = 'block';
//             })
//             .catch(error => console.error('Error:', error));
//     });

//     restartButton.addEventListener('click', function() {
//         fetch('/restart', { method: 'POST' })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.redirect) {
//                     window.location.href = data.redirect;
//                 }
//             })
//             .catch(error => console.error('Error:', error));
//     });
// });


document.addEventListener('DOMContentLoaded', function() {
    const startCaptureButton = document.getElementById('startCapture');
    const restartButton = document.getElementById('restart');
    const resultDiv = document.getElementById('result');
    const statusDiv = document.getElementById('status');
    const emotionElement = document.getElementById('emotion');
    const songElement = document.getElementById('song');
    const songLink = document.getElementById('songLink');

    startCaptureButton.addEventListener('click', function() {
        fetch('/start_capture', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                emotionElement.textContent = `Detected Emotion: ${data.emotion}`;
                songElement.textContent = `Suggested Song: ${data.songName}`;
                songLink.href = data.songUrl;
                statusDiv.style.display = 'none';
                resultDiv.style.display = 'block';
            })
            .catch(error => console.error('Error:', error));
    });

    restartButton.addEventListener('click', function() {
        fetch('/restart', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                if (data.redirect) {
                    window.location.href = data.redirect;
                }
            })
            .catch(error => console.error('Error:', error));
    });
});
