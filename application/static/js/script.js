const dropdowns = document.querySelectorAll('.dropdown-search');

dropdowns.forEach(dropdown => {
  const select = dropdown.querySelector('.select');
  const caret = dropdown.querySelector('.caret');
  const menu = dropdown.querySelector('.menu-dropdown');
  const options = dropdown.querySelectorAll('.menu-dropdown li');
  const selected = dropdown.querySelector('.selected');

  select.addEventListener('click', () => {
    // Menutup dropdown lainnya sebelum membuka dropdown saat ini
    dropdowns.forEach(otherDropdown => {
      if (otherDropdown !== dropdown) {
        const otherMenu = otherDropdown.querySelector('.menu-dropdown');
        otherMenu.classList.remove('menu-open');
        removeCaretRotate()
      }
    });

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

      options.forEach(otherOption => {
        otherOption.classList.remove('dropdown-active');
      });
      option.classList.add('dropdown-active');
    });
  });
});

document.addEventListener('click', (event) => {
  const isDropdownClick = Array.from(event.target.classList).some(className =>
    className.includes('dropdown-search') || className.includes('select') || className.includes('caret')
  );
  if (!isDropdownClick) {
    closeAllDropdowns();
    removeCaretRotate();
  }
});

function closeOtherDropdowns(currentDropdown) {
  dropdowns.forEach(dropdown => {
    if (dropdown !== currentDropdown) {
      const menu = dropdown.querySelector('.menu-dropdown');
      menu.classList.remove('menu-open');
    }
  });
}

function toggleDropdown() {
  select.classList.toggle('select-clicked');
  caret.classList.toggle('caret-rotate');
  menu.classList.toggle('menu-open');
}

function closeAllDropdowns() {
  dropdowns.forEach(dropdown => {
    const menu = dropdown.querySelector('.menu-dropdown');
    menu.classList.remove('menu-open');
  });
}

function removeCaretRotate() {
  dropdowns.forEach(dropdown => {
    const caret = dropdown.querySelector('.caret');
    caret.classList.remove('caret-rotate');
  });
}

//==================================================================================

function onlyNumberKey(evt) {
              
  var key = evt.keyCode || evt.which;
  var char = String.fromCharCode(key);
  var allowedCharacters = /^[0-9+\-&]+$/;
  if (!allowedCharacters.test(char)) {
      evt.preventDefault();
  }
}
function formatHarga(input) {
  Number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  input.value = formattedAngka;
}

//==================================================================================

const filters = document.querySelectorAll('.search-set');
const navbar = document.querySelector('.navbar');
const ul_link = document.querySelector('.links');
const menuItems = document.querySelectorAll('.links li');
const menu_btn = document.querySelector('.menu-btn');
const mobile_menu = document.querySelector('.navbar-mobile');

function toggleNavbarClass() {
  if (window.innerWidth <= 859) {
    // navbar.classList.add('swiper');
    navbar.classList.add('navbar-mobile');
    navbar.classList.remove('navbar');
    // ul_link.classList.add('swiper-wrapper');
    // menuItems.forEach((menuItem) => {
    //   menuItem.classList.add('swiper-slide');
    // });
  } else {
    // navbar.classList.remove('swiper');
    navbar.classList.remove('navbar-mobile');
    navbar.classList.add('navbar');
    // ul_link.classList.remove('swiper-wrapper');
    // menuItems.forEach((menuItem) => {
    //   menuItem.classList.remove('swiper-slide');
    // });
  }
}

menu_btn.addEventListener('click', function () {
  menu_btn.classList.toggle('is-active');
  mobile_menu.classList.toggle('is-active');
});

filters.forEach(dropdown => {
  const filter = dropdown.querySelector('.filter-btn');
  const filterlist = dropdown.querySelector('.filter-search');

  filter.addEventListener('click', () => {
    filter.classList.toggle('filter-clicked');
    filterlist.classList.toggle('filter-open');
  });
});

window.addEventListener('DOMContentLoaded', toggleNavbarClass);
window.addEventListener('resize', toggleNavbarClass);

//==================================================================================

var swiper1 = new Swiper(".swiping", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".next",
    prevEl: ".previous ",
  },
});

//==================================================================================

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

//==================================================================================

const activePage = window.location.pathname.split('/')[1];
const navLinks = document.querySelectorAll('nav li a');
const pageTitleMap = {
  '': 'Era Sky Bekasi',
  'beli': 'Beli Properti',
  'sewa': 'Sewa Properti',
  'properti-baru': 'Properti Baru',
  'berita': 'Berita',
  'agen-kami-summarecon-bekasi': 'Agen Summarecon Bekasi',
  'agen-kami-harapan-indah': 'Agen Harapan Indah Bekasi',
  'tentang-kami': 'Tentang Kami',
  'join-us': 'Join Us',
  'buat-listing': 'Buat Listing',
  'konfirm-listing': 'Konfirm Listing'
};

// Mengubah judul website sesuai dengan halaman aktif
document.title = pageTitleMap[activePage] || 'Halaman Tidak Diketahui';

// Hapus kelas "active" dari semua elemen navbar
navLinks.forEach(link => {
  link.classList.remove('active');
});

// Tambahkan kelas "active" pada elemen yang sesuai dengan halaman aktif
if (activePage !== "") {
  navLinks.forEach(link => {
    if (link.href.includes(`${activePage}`)) {
      link.classList.add('active');
    }
  });
// } if (activePage == 'beli') {
//   var titleElement = document.querySelector('.left-title h2');
//   var propertyTitle = titleElement.textContent;
//   document.title = propertyTitle;
};

//==================================================================================

document.addEventListener("DOMContentLoaded", () => {
  const rows = document.querySelectorAll("tr[data-href]");
  console.log(rows);
  rows.forEach (row => {
    row.addEventListener("click", () => {
      window.location.href = row.dataset.href;
    });
  });
});

// // Mengambil semua elemen <tr> dalam tabel
// var tableRows = document.getElementsByTagName('tr');

// // Menambahkan fungsi klik pada setiap baris
// for (var i = 0; i < tableRows.length; i++) {
//   tableRows[i].addEventListener('click', function() {
//     // Mengambil tautan dari atribut data-href
//     var link = this.getAttribute('data-href');
    
//     // Membuka tautan di jendela baru/tab baru
//     window.location.href = link;
//   });
// }

//==================================================================================

// const slides = document.querySelectorAll("[data-slide]");
// const buttons = document.querySelectorAll("[data-button]");

// let currSlide = 0;
// let maxSlide = slides.length - 1;

// const updateCarousel = (number = 0) => {
//   slides.forEach((slide, index) => {
//     slide.style.transform = `translateX(${(index - number) * 100}%)`;
//   });
// };

// buttons.forEach((button) => {
//   button.addEventListener("click", () => {
//     button.dataset.button == "next" ? ++currSlide : --currSlide;

//     if (currSlide > maxSlide) {
//       currSlide = 0;
//     } else if (currSlide < 0) {
//       currSlide = maxSlide;
//     }
//     updateCarousel(currSlide);
//   });
// });

// updateCarousel();