
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
    

    menu()  



    
