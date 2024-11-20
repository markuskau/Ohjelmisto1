'use strict';

document.addEventListener('DOMContentLoaded', function() {
  const startButton = document.getElementById('start');
  const resultElement = document.getElementById('result');


  startButton.addEventListener('click', function() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;

    let result;

    switch (operation) {
      case 'add':
        result = num1 + num2;
        break;
      case 'sub':
        result = num1 - num2;
        break;
      case 'multi':
        result = num1 * num2;
        break;
      case 'div':
        result = num1 / num2;
        break;
      default:
        result = 'invalid operation';

    }

    resultElement.textContent = `Result: ${result}`;
  });
});

