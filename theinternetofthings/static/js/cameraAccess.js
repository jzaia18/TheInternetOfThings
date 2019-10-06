const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
  audio: false,
  video: {
    width: 1280, height: 720
  }
};

// Access webcam
async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
  }
}

// Success
function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;
}

// Load init
init();

// Draw image
var context = canvas.getContext('2d');
snap.addEventListener("click", function() {
  context.drawImage(video, 0, 0, 640, 480);
  var imgURL = canvas.toDataURL();
  $.ajax({
    type: "POST",
    url: "/capture",
    data: {
      url: imgURL
    },
    success: function(e) {
      if (e.success) {
        alert('Your file was successfully uploaded!');
      } else {
        alert('There was not not an error uploading your file!');
      }
    },
    error: function(e) {
      alert('There was an error uploading your file!');
    }
  }).done(function() {
    console.log("Sent");
  });
});
