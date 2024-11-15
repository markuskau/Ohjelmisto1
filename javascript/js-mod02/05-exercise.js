function collectUniqueNumbers() {
    let numbers = [];
    let numberSet = new Set();

    while (true) {
        let input = parseFloat(prompt("Enter number:"));

        if (isNaN(input)) {
            alert("Please enter a valid number.");
            continue;
        }

        if (numberSet.has(input)) {
            alert("This number has already been given.");
            break;
        }

        numberSet.add(input);
        numbers.push(input);
    }

    numbers.sort((a, b) => a - b);

    console.log("Numbers:");
    console.log(numbers);
}

collectUniqueNumbers();
