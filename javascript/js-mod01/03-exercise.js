'use strict';
let num1 = parseInt(prompt('Enter the first integer:'), 10);
let num2 = parseInt(prompt('Enter the second integer:'), 10);
let num3 = parseInt(prompt('Enter the third integer:'), 10);

let sum = num1 + num2 + num3;
let product = num1 * num2 * num3;
let average = sum / 3;

document.getElementById('output').innerHTML = `
            <p>Sum: ${sum}</p>
            <p>Product: ${product}</p>
            <p>Average: ${average.toFixed(2)}</p>`;