<?php 
$hostname = "localhost";
$nombreUsuario = "root";
$contraseña = "";
$nombreBD = "little_caesers4";

$nombreConexion = mysqli_connect($hostname , $nombreUsuario , $contraseña); 
mysqli_select_db ($nombreConexion, $nombreBD); 
if($nombreConexion == TRUE)
{
echo "Conectado a la BD";
echo "<br>";
}
else
{
	echo "Salio un error";
}
if (isset($_POST['eliminar_cliente_boton'])) 
{
	$NombreCliente = $_POST['eliminar_cliente'];
    $query = "DELETE FROM clientes WHERE Nombres='$NombreCliente'";
    $eliminacion = $nombreConexion->query($query);
    if ($eliminacion) 
    {
    	echo "Se elimino el cliente";
    } 
    else 
    { 
     	echo "Ocurrio un error";  
    }
}

if (isset($_POST['actualiza_cliente_boton'])) 
{
	$CelularCliente_Actualiza = $_POST['celular_cliente'];
	$NombreCliente_Actualiza = $_POST['nombre_cliente_actualiza'];
    mysqli_query($nombreConexion, "UPDATE clientes SET Celular='$CelularCliente_Actualiza' WHERE Nombres = '$NombreCliente_Actualiza'") or die(mysqli_error($nombreConexion));
    echo "Se actualizo correctamente";
}

if(isset($_POST['insertar_cliente_boton']))
{
	$NombreCliente_Insertar = $_POST['nombre_cliente_insertar'];
	$PaternoCliente_Insertar = $_POST['paterno_cliente_insertar'];
	$MaternoCliente_Insertar = $_POST['materno_cliente_insertar'];
	$EdadCliente_Insertar = $_POST['edad_cliente_insertar'];
	$CelularCliente_Insertar = $_POST['celular_cliente_insertar'];
	$SucursalCliente_Insertar = $_POST['sucursal_cliente_insertar'];

	$sql = "INSERT INTO clientes (Nombres,PrimerApellido,SegundoApellido,Edad,Celular,NombreSucursal)  
	VALUES ('".$NombreCliente_Insertar."','".$PaternoCliente_Insertar."','".$MaternoCliente_Insertar."','".$EdadCliente_Insertar."','".$CelularCliente_Insertar."','".$SucursalCliente_Insertar."')";

    $resultado=mysqli_query($nombreConexion,$sql) or die(mysqli_error($nombreConexion));
    if ($resultado===TRUE) 
    {
    	echo "Cliente registrado";
    }
    else
    {
       echo "Hubo un error";       
    }
}


if (isset($_POST['eliminar_cliente_boton_sucursal'])) 
{
	$NombreCliente = $_POST['eliminar_cliente'];
    $query = "DELETE FROM sucursal WHERE NombreCliente='$NombreCliente'";
    $eliminacion = $nombreConexion->query($query);
    if ($eliminacion) 
    {
    	echo "Se elimino el cliente de la sucursal";
    } 
    else 
    { 
     	echo "Ocurrio un error";  
    }
}

if (isset($_POST['actualiza_cliente_boton_sucursal'])) 
{
	$SucursalCliente_Actualiza = $_POST['sucursal_cliente'];
	$NombreCliente_Actualiza = $_POST['nombre_cliente_actualiza'];
    mysqli_query($nombreConexion, "UPDATE sucursal SET NombreSucursal='$SucursalCliente_Actualiza' WHERE NombreCliente = '$NombreCliente_Actualiza'") or die(mysqli_error($nombreConexion));
    echo "Se actualizo correctamente";
}

if(isset($_POST['insertar_cliente_boton_sucursal']))
{
	$nombre_sucursal_insertar = $_POST['nombre_sucursal_insertar'];
	$nombre_cliente_insertar = $_POST['nombre_cliente_insertar'];
	$paterno_cliente_insertar = $_POST['paterno_cliente_insertar'];
	

	$sql = "INSERT INTO sucursal (NombreSucursal,NombreCliente,ApellidoCliente)  
	VALUES ('".$nombre_sucursal_insertar."','".$nombre_cliente_insertar."','".$paterno_cliente_insertar."')";

    $resultado=mysqli_query($nombreConexion,$sql) or die(mysqli_error($nombreConexion));
    if ($resultado===TRUE) 
    {
    	echo "Sucursal registrada";
    }
    else
    {
       echo "Hubo un error";       
    }
}


mysqli_close($nombreConexion);
?>