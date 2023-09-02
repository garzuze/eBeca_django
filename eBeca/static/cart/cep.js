function buscaCep() {
    let cep = document.getElementById('cep').value;
    if (cep !== '') {
        let url = 'https://brasilapi.com.br/api/cep/v1/' + cep;

        let request = new XMLHttpRequest();
        request.open('GET', url);
        request.send();

        // tratar a resposta dada pela API
        request.onload = function () {
            if (request.status == 200) {
                let endereco = JSON.parse(request.response);
                document.getElementById('address').value = endereco.street + ", - " +
                    endereco.neighborhood + ", " + endereco.city + ", " + endereco.state;
            }
            else if (request.status == 404) {
                alert('CEP inválido.');
            } else {
                alert('Algo estranho aconteceu...');
            }
        }
    }
}

window.onload = function () {
    let cep = document.getElementById('cep');
    cep.addEventListener('blur', buscaCep);
}