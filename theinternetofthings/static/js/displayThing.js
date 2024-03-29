// const canvas = document.getElementById('canvas');
const like = document.getElementById('like');
const dislike = document.getElementById('dislike');
const errorMsgElement = document.querySelector('span#errorMsg');

// const constraints = {
//   audio: false,
//   video: {
//     width: 1280, height: 720
//   }
// };

// Access webcam
// async function init() {
//   try {
//     const stream = await navigator.mediaDevices.getUserMedia(constraints);
//     handleSuccess(stream);
//   } catch (e) {
//     errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
//   }
// }

// // Success
// function handleSuccess(stream) {
//   window.stream = stream;
//   video.srcObject = stream;
// }

// Load init
//init();

// Draw image
//var context = canvas.getContext('2d');

var mid = document.getElementById('mid').innerText.substring(3);

dislike.addEventListener("click", function() {
  $.ajax({
    type: "POST",
    url: "/dislike/" + mid,
    data: {
      xhrFields: { withCredentials: true }
    },
    success: function(e) {
      console.log(e);
    },
  });
});


like.addEventListener("click", function() {
  $.ajax({
    type: "POST",
    url: "/like/" + mid,
    data: {
      xhrFields: { withCredentials: true }
    },
    success: function(e) {
      console.log(e);
    },
  });
});
