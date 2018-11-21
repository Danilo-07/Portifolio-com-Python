$(function() {
	$('.btnMenu').click(function() {
		$('.btnMenu-barra').toggleClass('btnMenu_ativado');
		console.log('menu clicado');
		$('.menuSuperior').toggleClass('menuSuperior_aberta');
		$('.linksMenuSuperior:nth-child(1n+2)').toggleClass('menuOculto')
  });

});
