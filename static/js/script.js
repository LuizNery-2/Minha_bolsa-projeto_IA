
    const menuImg = document.querySelector(".menu");
    const menuLateral = document.querySelector(".menulateral");
    let isActive = false;
    function menu() {
    

        menuImg.addEventListener('click',()=>{
            menuLateral.style.display = 'flex';
            isActive = true;
            
        })
         document.addEventListener('click',(event) =>{
            
             if (!menuLateral.contains(event.target) && !menuImg.contains(event.target) ){

                 menuLateral.style.display = 'none';
    
    
            }
        })
            
    }
    function carregarPagina(pagina) {
        $.ajax({
            type: 'GET',
            url: '/' + pagina,
            success: function (data) {
                $('body').html(data);
                
                history.replaceState({}, '', '/' + pagina);
                location.reload();
            },
            error: function (error) {
                console.log('Erro ao carregar a página:', error);
            }
        });
    }
    
    function irParaLogin() {
        carregarPagina('login');
    }
    
    function irParaCadastro() {
        carregarPagina('cadastro');
    }
    
    function irParaMinhaSessao() {
        carregarPagina('minhasessao');
    }
    
    function irParaMinhasMetricas() {
        carregarPagina('minhasmetricas');
    }
    
    function irParaIniciarSessao() {
        carregarPagina('iniciarsessao');
    }
    
    function expandirImagem(imagem) {
        var overlay = document.getElementById("overlay");
        var imagemExpandida = document.getElementById("imagem-expandida");
    
        overlay.style.display = "block";
        imagemExpandida.innerHTML = "<img src='" + imagem.src + "' alt='" + imagem.alt + "'>";
        imagemExpandida.style.display = "block";
    }
    
    function fecharImagem() {
        var overlay = document.getElementById("overlay");
        var imagemExpandida = document.getElementById("imagem-expandida");
    
        overlay.style.display = "none";
        imagemExpandida.style.display = "none";
    }

    menu()  



    
