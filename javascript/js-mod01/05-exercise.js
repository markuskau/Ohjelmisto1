'use strict'
let year = parseInt(prompt('Enter a year:'));

function isleapYear(year) {
  if (year % 4 === 0) {
    if (year % 100 === 0) {
      if (year % 400 === 0) {
        return true;
      } else {
        return false;
      }
    } else {
      return true;
    }
  } else {
    return false;
  }
}

if (isleapYear(year)) {
  document.getElementById('Print').innerHTML = `${year} is a leap year.`;
} else {
  document.getElementById('Print').innerHTML = `${year} is not a leap year.`;}