document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("investment-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Impede o comportamento padrão do formulário de enviar a página

    const nome = document.getElementById("starting-name").value;
    const telefone = document.getElementById("telefone").value;
    const email = document.getElementById("email").value;

    console.log("Dados do formulário:", {
      nome: nome,
      telefone: telefone,
      email: email,
    });

    const formData = new FormData();
    formData.append("nome", nome);
    formData.append("telefone", telefone);
    formData.append("email", email);

    // Definindo um tempo limite de 10 segundos para a requisição
    const timeout = 10; // 10 segundos

    // Fazendo a requisição com timeout
    const request = new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        reject(new Error("Tempo limite de requisição excedido"));
      }, timeout);

      fetch("/dados.py", {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          clearTimeout(timer);
          resolve(response);
        })
        .catch((error) => {
          clearTimeout(timer);
          reject(error);
        });
    });

    // Tratando a resposta da requisição
    request
      .then((response) => {
        if (!response.ok) {
          throw new Error("Erro ao enviar dados");
        }
        return response.text();
      })
      .then((data) => {
        console.log("Resposta do servidor:", data);
        alert("Dados enviados com sucesso!");
        // Limpa os campos do formulário após o envio bem-sucedido
        form.reset();
      })
      .catch((error) => {
        console.error("Erro ao enviar dados:", error);
        alert("Erro ao enviar dados. Por favor, tente novamente mais tarde.");
      });
  });
});
