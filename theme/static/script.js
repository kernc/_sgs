"use strict";
if (location.hash == '#menu')
    location.hash = '';

function toggleMenu(visible, ev) {
    ev.preventDefault();
    if (visible)
        location.hash = 'menu';
    else
        history.back();
}
