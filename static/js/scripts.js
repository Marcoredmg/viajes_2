function CalcularDescuento(){
	precio_unitario = parseInt(document.getElementById('tbPrecio').value);
	num_personas = document.getElementById('selectPersonas').value;
	


	if(num_personas == 5){
		precio_final = precio_unitario - (precio_unitario * .20);
		precioFinal.textContent = "$" + precio_final + " USD c/u"
	}
	if(num_personas == 10){
		precio_final = precio_unitario - (precio_unitario * .30);
		precioFinal.textContent = "$" + precio_final + " USD c/u"
	}

}