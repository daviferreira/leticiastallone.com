var timer,
    doc = document.documentElement,
    body = document.body,
    isFixed = false,
    max = 100,
    el = document.getElementById('masthead'),
    contentEl = document.getElementById('main-content'),
    setFixedHeader = function setFixedHeader() {
        'use strict';
        var scrollTop = ((doc && doc.scrollTop) || (body && body.scrollTop) || 0);
        if (scrollTop > max && isFixed === false) {
            isFixed = true;
            el.style.marginTop = el.style.top = '-113px';
            el.className = 'masthead masthead-fixed';
            setTimeout(function () {
                el.style.marginTop = el.style.top = '0';
            }, 100);
            contentEl.style.marginTop = '113px';
        } else if (scrollTop <= max && isFixed === true) {
            isFixed = false;
            el.className = 'masthead sixteen columns';
            el.style.marginTop = el.style.top = '';
            contentEl.style.marginTop = '0';
        }
    };

window.onscroll = function (e) {
    'use strict';
    clearTimeout(timer);
    timer = setTimeout(setFixedHeader, 50);
};
