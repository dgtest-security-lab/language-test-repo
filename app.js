// Main JavaScript application

const appName = "GitHub Language Test Repository";

function greetUser(name) {
    return `Hello, ${name}! Welcome to ${appName}.`;
}

function calculateSum(a, b) {
    return a + b;
}

function getUserDetails() {
    return {
        name: "GitHub Tester",
        language: "JavaScript",
        active: true
    };
}

function displayInformation() {
    console.log(greetUser("Developer"));

    const result = calculateSum(10, 20);
    console.log("Sum:", result);

    const user = getUserDetails();
    console.log("User details:", user);
}

displayInformation();
