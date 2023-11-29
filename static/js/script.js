
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
        window.location.href = "./html/login.html";
    }
     function irParaCadastro() {
      window.location.href = "./html/cadastro.html";
    }
    function irParaMinhaSessao() {
        window.location.href = "./minhaSessao.html";
      }
      function irParaMinhasMetricas() {
        window.location.href = "./minhaMetricas.html";
      }


    menu()  



    
