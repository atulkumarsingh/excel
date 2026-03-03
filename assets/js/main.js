/**
* Template Name: Restaurantly - v3.7.0
* Template URL: https://bootstrapmade.com/restaurantly-restaurant-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener, { passive: true })
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  let selectTopbar = select('#topbar')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.add('topbar-scrolled')
        }
      } else {
        selectHeader.classList.remove('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.remove('topbar-scrolled')
        }
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  const ensureBackToTopButton = () => {
    let button = select('.back-to-top')
    if (button) return button
    button = document.createElement('button')
    button.type = 'button'
    button.className = 'back-to-top d-flex align-items-center justify-content-center'
    button.setAttribute('aria-label', 'Back to top')
    button.innerHTML = '<i class="bi bi-arrow-up-short" aria-hidden="true"></i>'
    document.body.appendChild(button)
    return button
  }

  let backtotop = ensureBackToTopButton()
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    backtotop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: prefersReducedMotion ? 'auto' : 'smooth'
      })
    })
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  const getTopLevelMenuList = (navbar) => {
    if (!navbar) return null
    let menuList = null
    try {
      menuList = navbar.querySelector(':scope > ul')
    } catch (e) {
      menuList = null
    }
    return menuList || navbar.querySelector('ul')
  }

  const navToggleButton = select('.mobile-nav-toggle')
  if (navToggleButton) {
    navToggleButton.setAttribute('aria-label', 'Toggle menu')
    navToggleButton.setAttribute('aria-expanded', 'false')
  }

  const getMobileMenuPanel = () => {
    let panel = document.getElementById('mobile-menu-panel')
    if (panel) return panel

    panel = document.createElement('div')
    panel.id = 'mobile-menu-panel'
    document.body.appendChild(panel)

    panel.addEventListener('click', (e) => {
      const navbar = select('#navbar')
      if (!navbar) return
      const menuList = getTopLevelMenuList(navbar)
      const closeMenu = () => {
        if (!navbar.classList.contains('navbar-mobile')) return
        closeMobileMenu(navbar, menuList)
        const navbarToggle = select('.mobile-nav-toggle')
        if (navbarToggle) {
          navbarToggle.classList.add('bi-list')
          navbarToggle.classList.remove('bi-x')
        }
      }

      // Close on backdrop click or explicit close button click
      if (e.target === panel || e.target.closest('.mobile-menu-close')) {
        e.preventDefault()
        closeMenu()
        return
      }

      const dropdownTrigger = e.target.closest('.dropdown > a')
      if (dropdownTrigger) {
        e.preventDefault()
        const dropdown = dropdownTrigger.parentElement
        if (dropdown) {
          dropdown.classList.toggle('dropdown-open')
        }
        return
      }

      const clickedLink = e.target.closest('a')
      if (!clickedLink) return

      const href = clickedLink.getAttribute('href') || ''
      if (href === '#') return

      closeMenu()
    })

    return panel
  }

  const buildMobileMenuPanel = (menuList) => {
    const panel = getMobileMenuPanel()
    panel.innerHTML = ''
    if (!menuList) return panel

    const closeButton = document.createElement('button')
    closeButton.type = 'button'
    closeButton.className = 'mobile-menu-close bi bi-x'
    closeButton.setAttribute('aria-label', 'Close menu')
    panel.appendChild(closeButton)

    const clonedMenu = menuList.cloneNode(true)
    clonedMenu.classList.add('mobile-menu-clone')
    clonedMenu.removeAttribute('style')
    clonedMenu.querySelectorAll('[style]').forEach(el => el.removeAttribute('style'))
    panel.appendChild(clonedMenu)
    return panel
  }

  const openMobileMenu = (navbar, menuList) => {
    const panel = buildMobileMenuPanel(menuList)
    navbar.classList.add('navbar-mobile')
    document.body.classList.add('mobile-nav-open')
    const navbarToggle = select('.mobile-nav-toggle')
    if (navbarToggle) {
      navbarToggle.classList.remove('bi-list')
      navbarToggle.classList.add('bi-x')
      navbarToggle.setAttribute('aria-expanded', 'true')
    }
    panel.classList.remove('closing')
    panel.classList.add('open')
  }

  const closeMobileMenu = (navbar, menuList) => {
    navbar.classList.remove('navbar-mobile')
    document.body.classList.remove('mobile-nav-open')
    const navbarToggle = select('.mobile-nav-toggle')
    if (navbarToggle) {
      navbarToggle.classList.add('bi-list')
      navbarToggle.classList.remove('bi-x')
      navbarToggle.setAttribute('aria-expanded', 'false')
    }

    const panel = document.getElementById('mobile-menu-panel')
    if (panel) {
      panel.classList.add('closing')
      panel.classList.remove('open')
      window.setTimeout(() => {
        if (panel.classList.contains('open')) return
        panel.classList.remove('closing')
        panel.innerHTML = ''
      }, 280)
    }

    if (menuList) {
      menuList.classList.remove('mobile-menu-open')
      menuList.removeAttribute('style')
    }
  }

  on('click', '.mobile-nav-toggle', function(e) {
    e.preventDefault()
    const navbar = select('#navbar')
    if (!navbar) return
    const menuList = getTopLevelMenuList(navbar)
    if (navbar.classList.contains('navbar-mobile')) {
      closeMobileMenu(navbar, menuList)
    } else {
      openMobileMenu(navbar, menuList)
    }
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (this.hash && select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        const menuList = getTopLevelMenuList(navbar)
        closeMobileMenu(navbar, menuList)
      }
      scrollto(this.hash)
    }
  }, true)

  window.addEventListener('resize', () => {
    if (window.innerWidth > 991) {
      const navbar = select('#navbar')
      if (!navbar || !navbar.classList.contains('navbar-mobile')) return
      const menuList = getTopLevelMenuList(navbar)
      closeMobileMenu(navbar, menuList)
      const navbarToggle = select('.mobile-nav-toggle')
      if (navbarToggle) {
        navbarToggle.classList.add('bi-list')
        navbarToggle.classList.remove('bi-x')
        navbarToggle.setAttribute('aria-expanded', 'false')
      }
    }
  })

  const initMediaPerformanceTweaks = () => {
    const images = select('img', true)
    const eagerLimit = window.innerWidth < 768 ? 2 : 3
    let eagerCount = 0
    if (images.length) {
      images.forEach((img) => {
        if (!img.hasAttribute('decoding')) {
          img.setAttribute('decoding', 'async')
        }
        const inViewport = img.getBoundingClientRect().top < window.innerHeight * 1.2
        if (!img.hasAttribute('loading')) {
          if (inViewport && eagerCount < eagerLimit) {
            img.setAttribute('loading', 'eager')
            eagerCount += 1
          } else {
            img.setAttribute('loading', 'lazy')
          }
        }
        if (img.getAttribute('loading') === 'lazy' && !img.hasAttribute('fetchpriority')) {
          img.setAttribute('fetchpriority', 'low')
        }
      })
    }

    const videoSources = select('video source[data-src]', true)
    if (videoSources.length) {
      const loadVideo = (sourceEl) => {
        const sourceUrl = sourceEl.getAttribute('data-src')
        if (!sourceUrl || sourceEl.getAttribute('src')) return
        sourceEl.setAttribute('src', sourceUrl)
        const video = sourceEl.closest('video')
        if (video) {
          video.load()
        }
      }

      if (!('IntersectionObserver' in window)) {
        videoSources.forEach(loadVideo)
      } else {
        const videoObserver = new IntersectionObserver((entries, obs) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return
            const sourceEl = entry.target.querySelector('source[data-src]')
            if (sourceEl) {
              loadVideo(sourceEl)
            }
            obs.unobserve(entry.target)
          })
        }, {
          rootMargin: '120px 0px',
          threshold: 0.01
        })

        videoSources.forEach((sourceEl) => {
          const video = sourceEl.closest('video')
          if (video) {
            videoObserver.observe(video)
          }
        })
      }
    }

    const embeds = select('iframe', true)
    embeds.forEach((frame) => {
      if (!frame.hasAttribute('loading')) {
        frame.setAttribute('loading', 'lazy')
      }
    })
  }

  const initRevealAnimations = () => {
    const targets = select('main section, #footer .footer-top, .wedding-card, .contact-resorts .resort-card, #galleryItems .GB-media', true)
    if (!targets.length) return

    targets.forEach((el, index) => {
      if (el.classList.contains('reveal-on-scroll')) return
      el.classList.add('reveal-on-scroll')
      el.style.setProperty('--reveal-delay', `${Math.min((index % 6) * 70, 320)}ms`)
    })

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      targets.forEach(el => el.classList.add('reveal-visible'))
      return
    }

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return
        entry.target.classList.add('reveal-visible')
        obs.unobserve(entry.target)
      })
    }, {
      rootMargin: '0px 0px -12% 0px',
      threshold: 0.12
    })

    targets.forEach(el => observer.observe(el))
  }

  const initMobileGalleryTap = () => {
    if (window.innerWidth > 991) return
    const cards = select('#galleryItems .GB-media', true)
    cards.forEach((card) => {
      if (card.dataset.tapReady === 'true') return
      card.dataset.tapReady = 'true'
      card.addEventListener('click', (event) => {
        if (event.target.closest('a, button, select, input, textarea, label')) return
        const trigger = card.querySelector('a.gallery-lightbox')
        if (trigger) {
          trigger.click()
        }
      })
    })
  }

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Menu isotope and filter
   */
  window.addEventListener('load', () => {
    let menuContainer = select('.menu-container');
    if (menuContainer && typeof Isotope !== 'undefined') {
      let menuIsotope = new Isotope(menuContainer, {
        itemSelector: '.menu-item',
        layoutMode: 'fitRows'
      });

      let menuFilters = select('#menu-flters li', true);

      on('click', '#menu-flters li', function(e) {
        e.preventDefault();
        menuFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        menuIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        menuIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Initiate glightbox 
   */
  if (typeof GLightbox !== 'undefined' && select('.glightbox')) {
    GLightbox({
      selector: '.glightbox'
    });
  }

  /**
   * Events slider
   */
  if (typeof Swiper !== 'undefined' && select('.events-slider')) {
    new Swiper('.events-slider', {
      speed: 600,
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false
      },
      slidesPerView: 'auto',
      pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
      }
    });
  }

  /**
   * Testimonials slider
   */
  if (typeof Swiper !== 'undefined' && select('.testimonials-slider')) {
    new Swiper('.testimonials-slider', {
      speed: 600,
      loop: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false
      },
      slidesPerView: 'auto',
      pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 20
        },

        1200: {
          slidesPerView: 3,
          spaceBetween: 20
        }
      }
    });
  }

  /**
   * Initiate gallery lightbox 
   */
  if (typeof GLightbox !== 'undefined' && select('.gallery-lightbox')) {
    GLightbox({
      selector: '.gallery-lightbox'
    });
  }

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    initMediaPerformanceTweaks()
    initRevealAnimations()
    initMobileGalleryTap()
    if (typeof AOS !== 'undefined') {
      AOS.init({
        duration: 1000,
        easing: 'ease-in-out',
        once: true,
        mirror: false
      })
    }
  });

})()
