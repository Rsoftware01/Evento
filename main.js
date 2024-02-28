document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("investment-form");
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit_form"); // Endpoint onde você irá lidar com o envio do formulário
    xhr.onload = function () {
      if (xhr.status === 200) {
        console.log("Formulário enviado com sucesso");
        // Você pode adicionar aqui alguma lógica para mostrar uma mensagem de sucesso ao usuário, por exemplo
      } else {
        console.error("Erro ao enviar formulário");
        // Você pode adicionar aqui alguma lógica para mostrar uma mensagem de erro ao usuário, por exemplo
      }
    };
    xhr.send(formData);
  });
});
