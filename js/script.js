
document.addEventListener("DOMContentLoaded", () => {
    // Seleciona elementos
    const modal = document.getElementById("modal");
    const closeModal = document.getElementById("closeModal");
    const learnMoreButtons = document.querySelectorAll(".learn-more-btn");
    const modalTitle = document.getElementById("modalTitle");
    const modalDetails = document.getElementById("modalDetails");
  
    // Adiciona evento aos botões "Learn More"
    learnMoreButtons.forEach((button) => {
      button.addEventListener("click", (event) => {
        const destinationItem = event.target.closest(".destination-item");
        const details = destinationItem.dataset.details; // Pega o texto do atributo "data-details"
        const title = destinationItem.querySelector("h3").innerText;
  
        // Atualiza o conteúdo do modal
        modalTitle.textContent = title;
        modalDetails.textContent = details;
  
        // Mostra o modal
        modal.classList.remove("hidden");
      });
    });
  
    // Fecha o modal ao clicar no botão de fechar
    closeModal.addEventListener("click", () => {
      modal.classList.add("hidden");
    });
  
    // Fecha o modal ao clicar fora dele (opcional)
    window.addEventListener("click", (event) => {
      if (event.target === modal) {
        modal.classList.add("hidden");
      }
    });
  });
  
  document.getElementById("search").addEventListener("input", (e) => {
    const query = e.target.value.toLowerCase();
    document.querySelectorAll(".destination-item").forEach(item => {
      item.style.display = item.innerText.toLowerCase().includes(query) ? "block" : "none";
    });
  });
