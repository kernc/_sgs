"use strict";
(()=>{
    const toggle = document.getElementById('menu-toggle');
    toggle.checked = false;

    toggle.addEventListener('keyup', ev => {
        if (ev.code === 'Enter') {
            toggle.checked = !toggle.checked;
        }
        if (ev.code === 'Escape') {
            toggle.checked = false;
        }
    });

    document.getElementById('menu').addEventListener('keyup', ev => {
        if (ev.code === 'Escape') {
            toggle.checked = false;
        }
    });
})();

document.addEventListener('copy', ev => {
    ev.clipboardData.setData('text/plain', document.getSelection().toString() + '\n \n' + window.location);
    ev.preventDefault();
});
