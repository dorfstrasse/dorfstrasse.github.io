const dropdowns = document.querySelectorAll('.dropdown-search');

dropdowns.forEach(dropdown => {
  const select = dropdown.querySelector('.select');
  const caret = dropdown.querySelector('.caret');
  const menu = dropdown.querySelector('.menu-dropdown');
  const options = dropdown.querySelectorAll('.menu-dropdown li');
  const selected = dropdown.querySelector('.selected');

  select.addEventListener('click', () => {
    select.classList.toggle('select-clicked');
    caret.classList.toggle('caret-rotate');
    menu.classList.toggle('menu-open');
  });

  options.forEach(option => {
    option.addEventListener('click', () => {
      selected.innerText = option.innerText;
      select.classList.remove('select-clicked');
      caret.classList.remove('caret-rotate');
      menu.classList.remove('menu-open');

      option.forEach(option => {
        option.classList.remove('dropdown-active');
      });
      option.classList.add('dropdown-active');
    });
  });
});

function onlyNumberKey(evt) {
              
  // Only ASCII character in that range allowed
  var ASCIICode = (evt.which) ? evt.which : evt.keyCode
  if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
      return false;
  return true;
}


const filters = document.querySelectorAll('.search-set');

filters.forEach(dropdown => {
  const filter = dropdown.querySelector('.filter-btn');
  const filterlist = dropdown.querySelector('.filter-search');

  filter.addEventListener('click', () => {
    filter.classList.toggle('filter-clicked');
    filterlist.classList.toggle('filter-open');
  });
});

var swiper = new Swiper(".agent-list", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

const tabs = document.querySelectorAll('.tab-btn');
const all_content = document.querySelectorAll('.detail-content');

tabs.forEach((tab, index) => {
  tab.addEventListener('click', () =>{
    tabs.forEach(tab => {tab.classList.remove('active')});
    tab.classList.add('active');

    all_content.forEach(content => {content.classList.remove('active')});
    all_content[index].classList.add('active');
  });
});

const activePage = window.location.pathname.split('/')[1];
const navLinks = document.querySelectorAll('nav li a').forEach(link => {
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active')
  }
  else if (!link.href.includes(`${activePage}`)){
    link.classList.remove('active')
  };
});

var titleElement = document.querySelector('.left-title h2');
var propertyTitle = titleElement.textContent;
document.title = propertyTitle;