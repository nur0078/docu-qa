function submitQuestion() {
  const fileInput = document.getElementById("documentUpload");
  const questionInput = document.getElementById("questionInput");
  const answerDisplay = document.getElementById("answerDisplay");

  const file = fileInput.files[0];
  const question = questionInput.value;

  const formData = new FormData();
  formData.append("document", file);
  formData.append("question", question);

  fetch("/answer", {
    method: "POST",
    body: formData
  })
    .then(response => response.text())
    .then(answer => {
      answerDisplay.innerText = answer;
    })
    .catch(error => {
      console.error(error);
    });
}

// Auto resize textarea
const questionInput = document.getElementById("questionInput");

questionInput.addEventListener('input', autoResize, false);

function autoResize() {
  this.style.height = 'auto';
  this.style.height = (this.scrollHeight) + 'px';
}
