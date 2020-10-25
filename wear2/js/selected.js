// var slide = document.querySelectorAll('.multiple_slider1 li'),
//     slideCount = slide.length
// console.log(slide.length);


var photo1 = document.getElementById('selected_pd');
var photo2 = document.getElementById('click1');
var all_set = document.getElementById('click2');




photo2.addEventListener('click', function() {
  photo1.style.opacity = "1";
});

all_set.addEventListener('click', function() {
  photo1.style.opacity = "0";
});
