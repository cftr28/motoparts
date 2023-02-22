(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el Artículo?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();


(function () {

    const btnComprar = document.querySelectorAll(".btnComprar");

    btnComprar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el Artículo?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();
