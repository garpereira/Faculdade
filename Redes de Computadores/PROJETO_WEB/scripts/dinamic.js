require('dotenv').config();

function atualizarConteudo() {
    
    fetch('https://api64.ipify.org?format=json', {family: 4})
        .then(response => response.json())
        .then(data => {
            document.getElementById('ip').textContent = data.ip;
        })
        .catch(error => {
            console.error('Erro ao obter o endereço IP:', error);
        });

    //Obter endereco do servidor que no caso é o localhost
    const enderecoServidor = window.location.href;
    document.getElementById('servidorAddress').textContent = enderecoServidor;

    // Obter a data atual
    const dataAtual = new Date();
    document.getElementById('data').textContent = dataAtual.toLocaleDateString();

    // Obter a hora atual
    function atualizarHora(){
        const dataAtual = new Date();
        document.getElementById('hora').textContent = dataAtual.toLocaleTimeString();
    }

    setInterval(atualizarHora, 1000);
    
    // Obter o local do usuário usando o objeto 'navigator'
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            const apikey = process.env.OPENCAGE_API_KEY;

            // Usar uma API de geolocalização reversa (OpenCage Data) para obter o nome do local
            fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=${apikey}`)
                .then(response => response.json())
                .then(data => {
                    const localName = data.results[0].formatted;
                    document.getElementById('local').textContent = localName;
                })
                .catch(error => {
                    console.error('Erro ao obter o nome do local:', error);
                });
        }, function (error) {
            console.error('Erro ao obter a localização:', error);
        });
    } else {
        console.error('Geolocalização não suportada pelo navegador.');
    }
}
atualizarConteudo();
