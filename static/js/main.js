var fenetreOuverte;

function ouvrirFenetre()
{
	const url = 'https://accounts.spotify.com/en/logout';                                                                                                                                                                                                                                                                    
	fenetreOuverte = window.open(url, 'Spotify Logout', 'width=700,height=500,top=40,left=40');
}
function fermerFenetreOuverte()
{
 	fenetreOuverte.close();
}

function logout(){
	var userImage = document.getElementById('btnLogout');
	ouvrirFenetre()
	setTimeout(() => fermerFenetreOuverte(), 3000)
	setTimeout(btnLogout.click(), 4000)
}