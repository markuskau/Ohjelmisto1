function collectNumbers() {
    let numbers = [];

    while (true) {
        let input = parseFloat(prompt("Enter a number (0 will stop):"));

        if (input === 0) {
            break;
        }

        if (!isNaN(input)) {
            numbers.push(input);
        } else {
            alert("Please enter a valid number.");
        }
    }

    numbers.sort((a, b) => b - a);

    console.log("Numbers from largest to smallest:");
    console.log(numbers);
}

collectNumbers();
