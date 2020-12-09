var x =document.getElementsByClassName('navBtns')

	for(i=0; i<x.length; i++){
		x[i].addEventListener("mouseover", function(){
			let chain = document.getElementById('tach')
			    chain.innerHTML = "&#xf62d";
          
			    setTimeout(function(){
			        chain.innerHTML = "&#xf62c"
			    }, 500)
			    setTimeout(function(){
			        chain.innerHTML = "&#xf629"
			    }, 1000)
			    setTimeout(function(){
			        chain.innerHTML = "&#xf62a"
			    }, 1500)
			    setTimeout(function(){
			        chain.innerHTML = "&#xf62b"
			    }, 2000)
                
		});
    
	}
