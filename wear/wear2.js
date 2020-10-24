// var sliderWrapper = document.getElementsByClassName('container'),
//     sliderContainer = document.getElementsByClassName('slider-container'),
//     slides = document.getElementsByClassName('slide'),
//     slideCount = 3,
//     currnetIndex = 0,
//     topHeight = 0
//     // navPrev =
//     // navNext =
//     console.log(slides)
//
//
// //슬라이드 가로로 배열
// for(var i = 0; i < 3; i++) {
//     slides[i].style.left = i*100 + '%';
//   }


const recommend = document.getElementById('slide1');
const all_set = document.getElementById('slide2');
const prev_buyPd = document.getElementById('slide3');

const recommend_btn = document.getElementById('recommend');
const all_set_btn = document.getElementById('all_set');
const prev_buyPd_btn = document.getElementById('prev_buyPd');

const imgs1 = recommend.getElementsByTagName("img");
// const imgs2 = all_set.getElementsByTagName("img");
// const imgs3 = prev_buyPd.getElementsByTagName("img");

console.log(imgs1);
const seleted_pd = document.getElementById('selected_pd');




//버튼 작동
recommend_btn.addEventListener('click', function(){
  recommend.classList.add('add_zIndex');
  all_set.classList.remove('add_zIndex');
  prev_buyPd.classList.remove('add_zIndex');
});

all_set_btn.addEventListener('click', function(){
  all_set.classList.add('add_zIndex');
  recommend.classList.remove('add_zIndex');
  prev_buyPd.classList.remove('add_zIndex');
});

prev_buyPd_btn.addEventListener('click', function(){
  prev_buyPd.classList.add('add_zIndex');
  recommend.classList.remove('add_zIndex');
  all_set.classList.remove('add_zIndex');

});

//선택된 상품 view
// function select_img(){
//   for(var i=0; i<=7; i++){
//     if (i >= 0) {
//       imgs1[i].addEventListener('click', function(){
//         seleted_pd.classList.add('up_seletedPd');
//       })
//     }
//     else if (i <= 7) {
//       imgs1[i].addEventListener('click', function(){
//         seleted_pd.classList.add('up_seletedPd');
//       })
//     }
//   }
// };
// select_img();

//
// function select_img(){
//    for(var i=0; i<=7; i++){
//      imgs1[i].addEventListener('onclick', function(){
//        seleted_pd.style.top= "-27%";
//      })
//    }
// }
