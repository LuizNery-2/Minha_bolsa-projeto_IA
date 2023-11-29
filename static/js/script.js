
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
    function irParaLogin() {
        carregarPagina('login');
    }
    
    function irParaCadastro() {
        carregarPagina('cadastro');
    }
    
    function irParaMinhaSessao() {
        carregarPagina('minhaSessao');
    }
    
    function irParaMinhasMetricas() {
        carregarPagina('minhaMetricas');
    }
    function irParaIniciarSessao(){
        carregarPagina('IniciarSessao');
    }
    
    function carregarPagina(pagina) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                document.documentElement.innerHTML = xhr.responseText;
            }
        };
        xhr.open('GET', '/pagina/' + pagina, true);
        xhr.send();
    }


    menu()  



    
