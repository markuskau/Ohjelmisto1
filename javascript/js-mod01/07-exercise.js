function rollDice() {
    let numberOfRolls = parseInt(document.getElementById("diceCount").value);
    let totalSum = 0;
    let results = "";

    for (let i = 0; i < numberOfRolls; i++) {
        let roll = Math.floor(Math.random() * 6) + 1;
        totalSum += roll;
        results += `Roll ${i + 1}: ${roll}<br>`;
    }

    document.getElementById("results").innerHTML = results + `<br>Total Sum: ${totalSum}`;
}
