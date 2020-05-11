<?php
// CONTROL DE ERRORES EN PHP
// METODO DE CONEXION "SAMConnection"
// EJEMPLO 1

$local = "localhost";
$server = "root";
$pass = "";
$bd = "little_caesers4";

$conn = mysqli_connect($local,$server,$pass,$bd);

// ESTE ES EL METODO QUE NO DEVUELVE RESULTADO, PERO PARA ASEGURARNOS QUE ESTE BIEN LE AGREGAMOS UN ELSE MOSTRANDO UN MENSAJE QUE LA CONEXION FUE EXITOSA.	
// PERO SI NOS EQUIVOCAMOS EN ALGUNA LETRA DE LA CONEXION MARCARÁ UN ERROR Y ENTRARA AL IF. 

if (!$conn->commit()) {
    // El commit falló!
    echo "Commit fallido ($conn->errno) $conn->error";
}
else
{
	echo "Conexion exitosa";
}


// EJEMPLO 2. METODO QUE DEVUELVE UN RESULTADO DE ERROR. CON UN SOLO TEMA 
class SAMConnection
{
	public $conn;
	function func()
	{
	  $conn=mysqli_connect(SAM_WMQ, array(SAM_HOST => 'localhost', SAM_PORT => 1506));
	  if($conn==true)
	  {
	  	echo "Conexion establecida";
	  }	
	}
}
class SAMMessage
{
	$msg = "Este es el mensaje";
	$correlid = $conn->send('queue://send/test', $msg);
	if (!$correlid) 
	{
    	// The Send failed!
    	echo "Mensaje fallado ($conn->errno) $conn->error";
	}
	else
	{
		echo "Enviado";
	}
}


$conn = new SAMConnection();
$msg = new SAMMessage();


?>
