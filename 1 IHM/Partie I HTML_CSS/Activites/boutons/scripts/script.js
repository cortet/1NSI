
/*evenements sur le bouton cliquer*/

function fonctionClic(event){
	let h1=document.querySelector("h1")	
	if (i==0){
			h1.style.color="red";
			i=1;
		}
	else {
			h1.style.color="blue";
			i=0;
		}
	}

	let l1=document.querySelector(".cliquer");
	l1.addEventListener("click",fonctionClic);
	let i=0;


	/*Evenements sur le paragraphe passer dessus */

function entreSouris(event){
	let para=document.querySelector("#para");
	para.style.color="red";
	para.style.background="blue"
	}
function sortieSouris(event){
	let para=document.querySelector("#para");
	para.style.color="black";
	para.style.background="white"
	}

let para=document.querySelector("#para");
para.addEventListener('mouseenter',entreSouris);
para.addEventListener('mouseleave',sortieSouris);

/*Evenements sur les boutons plus petit et plus grand */

	function clicPlusGrand (){
	document.querySelector("#style").style.fontSize='larger';
}
	function clicPlusPetit (){
	document.querySelector("#style").style.fontSize='smaller';
}
let bouton1=document.querySelector("#textePlusGrand");
bouton1.addEventListener("click",clicPlusGrand);
let bouton2=document.querySelector("#textePlusPetit");
bouton2.addEventListener("click",clicPlusPetit);

/*Evenements changement de l'image*/

function fonctionClicImage(){
	image=document.querySelector("img");
		if (i==0){
			image.setAttribute("src","images/image2.jpeg");
			i=1;
		}
	else {
			image.setAttribute("src","images/image1.jpeg");
			i=0;
		}

	}

let image=document.querySelector("img");
image.addEventListener("click",fonctionClicImage);

/*Evenement id valider*/

	function fonctionChangePolice(){
		let police=document.querySelector("#tailleTexte");
		let Tpolice=police.value;
		document.querySelector("#style").style.fontSize=Tpolice;
		}
let valider=document.querySelector("#valider");
valider.addEventListener("click",fonctionChangePolice);

/*Evenements sur la jauge*/
	
	function changeInput(){
		let jauge=document.querySelector("#jauge");
		let vjauge=jauge.value;
		let jaugeChange=document.querySelector("span");
		jaugeChange.textContent=vjauge;
		
		}
	function changeAffichage(){
		let jauge=document.querySelector("#jauge");
		let vjauge=jauge.value;
		document.querySelector("img").style.width=vjauge+'%'	;
		}
let jauge=document.querySelector("#jauge");
jauge.addEventListener("change",changeAffichage);
jauge.addEventListener("input",changeInput);
