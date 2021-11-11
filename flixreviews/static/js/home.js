$('.owl-carousel').owlCarousel({
    nav: true,
    responsiveClass: true,
    loop: true,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    responsive: {
      0: {
        items: 1,
        nav: false
      },
      500: {
        items: 2
      },
      700: {
        items: 3
      },
      1000: {
        items: 4
      }
    }
  });
  $(".owl-dot").attr('aria-label',"slide-dot");