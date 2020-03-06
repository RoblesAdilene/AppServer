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

?>

