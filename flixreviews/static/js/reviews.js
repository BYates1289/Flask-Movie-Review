window.addEventListener('scroll', function(){
  const scroll = document.querySelector('#button-top');
  scroll.classList.toggle("active" , window.scrollY > 500)
})

function scrollToTop(){
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}