const form = document.getElementById('question-form');

// Form Validation

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const fileQuestion = form.elements['file-upload'].value; // Question as a file
    const textQuestion = form.elements['question-text'].value; // Question a a text

    if (fileQuestion.files.length == 0 || textQuestion.length == 0) {
        alert('Last opp en fil eller skriv en spørsmål i boksen');
        return;
    };

    if (fileQuestion.files.length ==! 0 && textQuestion.length ==! 0) {
        alert('Du kan kun oppgi en fil eller en spørsmål i boksen');
        return;
    }

    form.submit();
});

function inputData() {
    const fileQuestion = form.elements['file-upload'].files; // Question as a file
    const textQuestion = form.elements['question-text'].value; // Question a a text

    if (fileQuestion.length ==! 0) {
        return fileQuestion
    }
}