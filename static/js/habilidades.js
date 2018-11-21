$(function() {
    $('.habilidades-list').each( function () {

		var valor = $(this).children().last().text();
		valor = Math.round(parseInt(valor)/10);
		$(this).children().last().remove();
		for (var i = 1; i <=10; i++) {
			if (i <= valor) {
				$(this).append(criaPonto("circle-on"))
			} else {
				$(this).append(criaPonto("circle-off"))
			}
		}
	});

	// Cria um elemento com a Classe passada por parametro
	function criaPonto(classe) {

		var ponto = $("<div>");
		ponto.addClass(classe);
		return ponto;
	}
});