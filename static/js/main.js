document.addEventListener('scroll', () => {
  const header = document.querySelector('header');
  
  if (window.scrollY > 0) {
    header.classList.add('scrolled')
  }else{
    header.classList.remove('scrolled');
  }
})

var swiper = new Swiper(".slide-content", {
  slidesPerView: 3,
  spaceBetween: 25,
  centerSlide:'true',
  fade: 'true',
  loop: true,
  gragCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets:true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  
  breakpoints:{
    100:{
      slidesPerView: 1,
    },
    520:{
      slidesPerView: 2,
    } ,
     950:{
      slidesPerView: 3,
    },
  },
});
