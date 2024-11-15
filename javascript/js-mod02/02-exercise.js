document.addEventListener("DOMContentLoaded", function() {
    collectParticipants();
});

function collectParticipants() {

    let numberOfParticipants = parseInt(prompt("Enter the number of participants:"));



    let participants = [];

    for (let i = 0; i < numberOfParticipants; i++) {
        let name = prompt(`Enter the name of participant ${i + 1}:`);
        participants.push(name);
    }

    participants.sort();

    let listContainer = document.getElementById("participantsList");
    listContainer.innerHTML = "";

    let ol = document.createElement("ol");
    participants.forEach(function (name) {
        let li = document.createElement("li");
        li.textContent = name;
        ol.appendChild(li);
    });

    listContainer.appendChild(ol);
}
