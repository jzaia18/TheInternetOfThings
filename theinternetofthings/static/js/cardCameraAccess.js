const video = document.getElementById('video');
// const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');
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
var imgURL;

function changePic(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#show-img')
        .attr('src', e.target.result);
      imgURL = e.srcElement.result;
      console.log(e.srcElement.result);
    };

    reader.readAsDataURL(input.files[0]);
    //console.log(reader.result);
  }
}


snap.addEventListener("click", function() {
  $.ajax({
    type: "POST",
    url: "/cardcapture",
    data: {
      url: imgURL
    },
    success: function(e) {
      console.log(e);
      e = e.replace(/'/g, '"');
      e = JSON.parse(e);

      console.log(e);
      //$("#info")[0].innerText = e;
      $("#cardlink")[0].href = e.link;
      $("#cardname")[0].innerText = e.name;
      $("#price")[0].innerText = "$" + e.price + " Regular";
      $("#foilprice")[0].innerText = "$" + e.foil + " Foil";
    },
  });
});
