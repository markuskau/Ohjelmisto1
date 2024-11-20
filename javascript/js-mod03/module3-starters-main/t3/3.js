'use strict';
const names = ['John', 'Paul', 'Jones'];

const targetElement = document.getElementById('target');

let HTMLlist = '<ul>';
for (let i = 0; i < names.length; i++) {
  HTMLlist += `<li>${names[i]}</li>`;
}
HTMLlist += '</ul>';

targetElement.innerHTML = HTMLlist;
