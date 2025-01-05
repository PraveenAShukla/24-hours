// scripts.js

// Add an event listener to validate the form before submission
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        // Prevent the form from submitting if validation fails
        if (!validateForm()) {
            event.preventDefault();
            alert("Please fill out all fields correctly before submitting!");
        } else {
            showLoader();
        }
    });
});

// Validate form inputs
function validateForm() {
    const income = document.querySelector('input[name="Income"]').value;
    const debtRatio = document.querySelector('input[name="DebtToIncomeRatio"]').value;
    const utility = document.querySelector('input[name="UtilityTimeliness"]').value;
    const sentiment = document.querySelector('input[name="SocialSentiment"]').value;
    const geolocation = document.querySelector('input[name="GeolocationScore"]').value;

    // Ensure all fields are filled and values are within acceptable ranges
    if (
        !income || income <= 0 ||
        !debtRatio || debtRatio < 0 || debtRatio > 1 ||
        (utility !== "0" && utility !== "1") ||
        !sentiment || sentiment < 0 || sentiment > 1 ||
        !geolocation || geolocation < 0 || geolocation > 1
    ) {
        return false;
    }

    return true;
}

// Show a loader animation
function showLoader() {
    const container = document.querySelector(".container");
    container.innerHTML = `
        <div class="loader"></div>
        <p>Processing your request, please wait...</p>
    `;
}
