window.onload = function() {
  let numbers = [];
  for (let i = 0; i < 5; i++) {
    let number = prompt('Enter number' + (i + 1) + ':');
    numbers.push(Number(number));
  }

  let result = 'Numbers in reverse order:';
  for (let i = numbers.length - 1; i >= 0; i--) {
    result += numbers[i] + '';
  }
  document.getElementById('output').innerText = result;
}

