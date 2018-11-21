$(function() {
	$('#btn-enviar').click(function() {
		console.log('botão enviar clicado')
		$('#btn-enviar').attr('disabled', true);
		$('#btn-enviar').addClass('enviando');

		// 'O nome precisa ter pelo menos 4 caracteres'
		nome = $('#nome').val();
		nomeOk = /[A-ZÀ-Ÿa-zà-ÿ ']{4,}/.test(nome);

		// 'O e-email deve obedecer o formato: [nome] @ [serviço de email] [.] [com/gov/br/etc...]'
		email = $.trim($('#email').val()).toLowerCase()
		emailOk = /[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+/.test(email);

		if (nomeOk && emailOk) {
			grecaptcha.execute();
		} else {
			validaNome(nomeOk);
			validaEmail(emailOk);
			$('#btn-enviar').removeClass('enviando');
			$('#btn-enviar').attr('disabled', false);
		}
	});

	$('#fechar-popUp').click(function() {
		$('#sombra').toggleClass( "oculto" );
		$('#btn-enviar').attr('disabled', false);
	});

	function exibePopup(resposta){
		if (resposta) {
			$('.popUp_titulo').text('Obrigado por entrar em contato!');
			$('.popUp_msg:first').text('Sua mensagem foi enviada para o meu email. Assim que possivel, enviarei uma resposta.');
			$('.popUp_msg:last').text('Até logo!');
			$('#sombra').toggleClass( "oculto" );
		} else {
			$('.popUp_titulo').text('Opps...');
			$('.popUp_msg:first').html('Parece que algo de errado não está certo.<br>Por favor tente mais tarde.');
			$('.popUp_msg:last').text('Obrigado.');
			$('#sombra').toggleClass( "oculto" );
		}
	}

	// 'O nome precisa ter pelo menos 4 caracteres'
	function validaNome (nomeOk) {
		if (!nomeOk) {
			$('#nome-ok').addClass('alerta');
			$('#nome-ok').attr('id', 'nome-erro');
			$('#nome-erro').text('O nome precisa ter pelo menos 4 caracteres');
		} else {
			$('#nome-erro').text('Ok!');
			$('#nome-erro').attr('id', 'nome-ok');
		}
	}

	// 'O e-email deve obedecer o formato: <br> [nome] @ [serviço de email] [.] [com/gov/br/etc...]'
	function validaEmail (emailOk) {
		if (!emailOk) {
			$('#email-ok').addClass('alerta');
			$('#email-ok').attr('id', 'email-erro');
			$('#email-erro').html('O e-email deve obedecer o formato: <br> [nome] @ [serviço de email] [.] [com/gov/br/etc...]');
		} else {
			$('#email-erro').text('Ok!');
			$('#email-erro').attr('id', 'email-ok');
		}
	}



});

function enviarMensagem () {
	console.log('Antes ' + grecaptcha.getResponse());
	$.ajax({
		url: '/mensagem',
		data: $('form').serialize(),
		type: 'POST',
		success: function(response) {
			// Limpa o formulário após enviar
			// a mensagem com sucesso
			$('form p').text('');
			$('form p').removeClass('alerta');
			$('form input').val('');
			$('form textarea').val('');
			// Exibe pop-up informando que a mensagem
			// foi enviada com sucesso
			exibePopup(true);
		},
		error: function(error) {
			// Exibe pop-up informando que houve um erro
			// ao tentar enviar a mensagem
			exibePopup(false);
		}
	});

    grecaptcha.reset();
    console.log('depois ' + grecaptcha.getResponse());
}

function exibePopup(resposta){
    $('#btn-enviar').removeClass('enviando');
	if (resposta) {
		$('.popUp_titulo').text('Obrigado por entrar em contato!');
		$('.popUp_msg:first').text('Sua mensagem foi enviada para o meu email. Assim que possivel, enviarei uma resposta.');
		$('.popUp_msg:last').text('Até logo!');
		$('#sombra').toggleClass( "oculto" );
	} else {
		$('.popUp_titulo').text('Opps...');
		$('.popUp_msg:first').html('Parece que algo de errado não está certo.<br>Por favor tente mais tarde.');
		$('.popUp_msg:last').text('Obrigado.');
		$('#sombra').toggleClass( "oculto" );
	}
}
