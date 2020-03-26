
<?php
$mysqli = new mysqli("localhost", "root", "", "little_caesers4");
if ($mysqli->connect_errno) {
    echo "Fallo al conectar a MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
if(isset($_POST['cliente']))
{
	echo "<center>";
		echo "<h2>";
			echo "Informacion acerca de los clientes";
		echo "</h2>";
	echo "</center>";
	$nombre = $_POST['nombre'];

	$Query = "SELECT * FROM clientes WHERE Nombres = '$nombre'";
	$Resultado = mysqli_query($mysqli, $Query);
	if (!$Resultado) 
    {
    	echo "Hubo un error al cargar los datos, recarga la página.";
        ///echo "Error MySQL: ".mysqli_error();
        exit();
    }
    while ($fila = mysqli_fetch_assoc($Resultado)) 
    {
    	$nombre = $fila['Nombres'];
    	$paterno = $fila['PrimerApellido'];
    	$materno = $fila['SegundoApellido'];
    	$edad = $fila['Edad'];
    	$celular = $fila['Celular'];
    	$NombreSucursal = $fila['NombreSucursal'];
    
?>
<center>
<table border="1" width="600" >

  <tr>
    <th>Nombre</th>
    <th>Ap Paterno</th>
    <th>Ap Materno</th>
    <th>Edad</th>
    <th>Celular</th>
    <th>Sucursal</th>
  </tr>

  <tr>
    <td><?php echo $nombre; ?></td>
    <td><?php echo $paterno; ?></td>
    <td><?php echo $materno; ?></td>
    <td><?php echo $edad; ?></td>
    <td><?php echo $celular; ?></td>
    <td><?php echo $NombreSucursal; ?></td>
  </tr>
  <tr>


</table>
</tr>

<?php 

} }  

if(isset($_POST['sucursal']))
{
	echo "<center>";
		echo "<h2>";
			echo "Informacion acerca de la sucursal";
		echo "</h2>";
	echo "</center>";

	$sucursal = $_POST['nomsucursal'];

	$Query1 = "SELECT * FROM sucursal WHERE NombreSucursal = '$sucursal'";
	$Resultado1 = mysqli_query($mysqli, $Query1);
	if (!$Resultado1) 
    {
    	echo "Hubo un error al cargar los datos, recarga la página.";
        ///echo "Error MySQL: ".mysqli_error();
        exit();
    }
    while ($fila = mysqli_fetch_assoc($Resultado1)) 
    {
    	$NombreSucursal = $fila['NombreSucursal'];
    	$NombreCliente = $fila['NombreCliente'];
    	$ApellidoCliente = $fila['ApellidoCliente'];
    	
    
?>
<center>
<table border="1" width="600" >

  <tr>
    <th>Nombre Sucursal</th>
    <th>Nombre Cliente</th>
    <th>Ap Paterno Cliente</th>
  </tr>

  <tr>
    <td><?php echo $NombreSucursal; ?></td>
    <td><?php echo $NombreCliente; ?></td>
    <td><?php echo $ApellidoCliente; ?></td>
  </tr>
  <tr>


</table>
</tr>

<?php } }  ?>




