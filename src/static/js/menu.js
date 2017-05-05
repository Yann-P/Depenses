var layout   = document.getElementById('layout'),
    menu     = document.getElementById('menu'),
    menuLink = document.getElementById('menuLink'),
    content  = document.getElementById('main');

function toggleClass(element, className) {
    var classes = element.className.split(/\s+/),
        length = classes.length,
        i = 0;

    for(; i < length; i++) {
      if (classes[i] === className) {
        classes.splice(i, 1);
        break;
      }
    }
    // The className is not found
    if (length === classes.length) {
        classes.push(className);
    }

    element.className = classes.join(' ');
}

function toggleAll() {
    layout.classList.toggle('active');
    menu.classList.toggle('active');
    menuLink.classList.toggle('active');
}

menuLink.onclick = function (e) {
    e.preventDefault();
    toggleAll();
};

content.onclick = function(e) {
    e.preventDefault();
    if (menu.className.contains('active')) {
        toggleAll();
    }
};