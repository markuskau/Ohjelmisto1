const targetElement = document.getElementById("target");

const ul = document.createElement("ul");

const firstItem = document.createElement("li");
firstItem.textContent = "First item";
ul.appendChild(firstItem);

const secondItem = document.createElement("li");
secondItem.textContent = "Second item";
secondItem.classList.add("my-item"); // Lisää luokka
ul.appendChild(secondItem);

const thirdItem = document.createElement("li");
thirdItem.textContent = "Third item";
ul.appendChild(thirdItem);

targetElement.appendChild(ul);
