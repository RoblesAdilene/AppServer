<?php
$local = "localhost";

$server = "root";

$pass = "";

$bd  = "proyecto_bd";

$connect = mysqli_connect($local,$server,$pass,$bd);

if(!$connect) 
{
  echo 'Error al conectarnos a la base de datos';
} 
else 
{
  echo 'exito';
}

$name = $_POST['nombre'];
$lastname = $_POST['apellido'];
$age = $_POST['edad'];
$address = $_POST['domicilio'];
$postal_code = $_POST['codigo_postal'];
$phone = $_POST['telefono'];

$consulta = "INSERT INTO formulario (nombre,apellido,edad,domicilio,codigo_postal,telefono) 
VALUES ('".$name."','".$lastname."','".$age."','".$address."','".$postal_code."','".$phone."')" or die('Error');

$resultado=mysqli_query($connect,$consulta) or die(mysqli_error($connect));

echo " Registro guardado";

?>


