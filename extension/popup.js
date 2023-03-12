document.addEventListener('DOMContentLoaded', function() {
  const input = document.getElementById("input");
  const output = document.getElementById("output");
  const submitButton = document.getElementById("submit");

  submitButton.addEventListener("click", () => {
    const text = input.value;

    fetch("http://127.0.0.1:5000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
      mode: "no-cors"
    })
    
    });
  });

