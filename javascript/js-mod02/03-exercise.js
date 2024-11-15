document.addEventListener("DOMContentLoaded", function() {
    collectDogNames();
});

function collectDogNames() {
    const numberOfDogs = 6;
    let dogNames = [];


    for (let i = 0; i < numberOfDogs; i++) {
        let name = prompt(`Enter the name of dog ${i + 1}:`);
        dogNames.push(name);
    }


    dogNames.sort().reverse();

    let listContainer = document.getElementById("dogNamesList");
    if (!listContainer) {
        console.error("The element with id 'dogNamesList' was not found.");
        return;
    }

    let ul = document.createElement("ul");
    dogNames.forEach(function (name) {
        let li = document.createElement("li");
        li.textContent = name;
        ul.appendChild(li);
    });

    listContainer.appendChild(ul);
}
