import Big from "big.js";

function finalizarCompra() {
    const form = document.getElementById("carrinho-form");
    form.action = "{% url 'confirmar_compra' %}";
    form.method = "get";
    form.submit();
}

document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener("pageshow", function (event) {
        if (
            event.persisted ||
            (window.performance && window.performance.navigation.type === 2)
        ) {
            atualizarTotais();
            console.log("O usuário voltou à página.");
        } else {
            console.log("A página foi carregada normalmente.");
        }
    });

    const form = document.getElementById("carrinho-form");
    const totalCarrinhoElement = document.getElementById("total-carrinho");
    const subtotalCarrinhoElement =
        document.getElementById("subtotal-carrinho");
    const finalizarCompraButton = document.getElementById("finalizar-compra");

    function atualizarTotais() {
        let totalCarrinho = new Big(0);
        const itens = document.querySelectorAll("#carrinho-list > tr");

        itens.forEach((item) => {
            const preco = new Big(item.dataset.preco || "0");
            const quantidadeInput = item.querySelector(".quantidade-input");
            const quantidade = parseInt(quantidadeInput.value, 10) || 0;
            const totalItem = preco.times(quantidade);

            item.querySelector(".total-item").textContent =
                "R$ " + totalItem.toFixed(2);

            totalCarrinho = totalCarrinho.plus(totalItem);
        });

        totalCarrinhoElement.textContent = "R$ " + totalCarrinho.toFixed(2);
        subtotalCarrinhoElement.textContent = "R$ " + totalCarrinho.toFixed(2);

        finalizarCompraButton.disabled = false;
    }

    // Atualiza totais inicialmente
    atualizarTotais();
});
