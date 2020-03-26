-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-03-2020 a las 19:15:03
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `little_caesers4`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `idCliente` int(11) NOT NULL,
  `Nombres` varchar(50) NOT NULL,
  `PrimerApellido` varchar(30) NOT NULL,
  `SegundoApellido` varchar(30) NOT NULL,
  `Edad` int(3) NOT NULL,
  `Celular` int(10) NOT NULL,
  `NombreSucursal` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`idCliente`, `Nombres`, `PrimerApellido`, `SegundoApellido`, `Edad`, `Celular`, `NombreSucursal`) VALUES
(1, 'Juan', 'Perez', 'Lopez', 20, 449494, 'Norte'),
(2, 'Alan', 'Guitierrez', 'Cedillo', 18, 45494, 'Norte'),
(3, 'Ricardo', 'Flores', 'Pasillas', 20, 4459494, 'Norte'),
(4, 'Guadalupe', 'Robles', 'Reyes', 19, 44933, 'Norte'),
(5, 'Constantin', 'Marquez', 'Reyes', 18, 44944, 'Norte'),
(6, 'Ulises', 'Robles', 'Reyes', 17, 449477, 'Sur'),
(7, 'Valentina', 'Bonilla', 'Reyes', 30, 4497764, 'Sur'),
(8, 'Mauricio', 'Marquez', 'Reyes', 20, 4494984, 'Sur'),
(9, 'Elliot', 'Flores', 'Robles', 29, 44889, 'Sur'),
(10, 'Josue', 'Montanez', 'Ruan', 22, 44954494, 'Sur'),
(11, 'Christian', 'Aguilar', 'Esparza', 30, 44923, 'Centro'),
(12, 'Andy', 'Robles', 'Salas', 25, 4479494, 'Centro'),
(13, 'Roberto', 'Bravo', 'Juarez', 23, 4494794, 'Centro'),
(14, 'Leonardo', 'Padilla', 'Chaides', 12, 4494894, 'Centro'),
(15, 'Alberto', 'Perez', 'Juarez', 20, 4494947, 'Centro'),
(16, 'Alfredo', 'Mercurio', 'Lopez', 20, 449494, 'Oriente'),
(17, 'Juan', 'Perez', 'Rivera', 20, 449494, 'Oriente'),
(18, 'Pedro', 'Serrano', 'Lopez', 20, 449494, 'Oriente'),
(19, 'Ivanjo', 'Ramirez', 'Reyes', 20, 449494, 'Oriente'),
(20, 'Oswaldo', 'Santos', 'Sandoval', 20, 449494, 'Oriente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sucursal`
--

CREATE TABLE `sucursal` (
  `NombreSucursal` text NOT NULL,
  `NombreCliente` text NOT NULL,
  `ApellidoCliente` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sucursal`
--

INSERT INTO `sucursal` (`NombreSucursal`, `NombreCliente`, `ApellidoCliente`) VALUES
('Norte', 'Juan', 'Perez'),
('Norte', 'Alan', 'Guitierrez'),
('Norte', 'Ricardo', 'Flores'),
('Norte', 'Guadalupe', 'Robles'),
('Norte', 'Constantin', 'Marquez'),
('Sur', 'Ulises', 'Robles'),
('Sur', 'Valentina', 'Bonilla'),
('Sur', 'Mauricio', 'Marquez'),
('Sur', 'Elliot', 'Flores'),
('Sur', 'Josue', 'Montanez'),
('Centro', 'Christian', 'Aguilar'),
('Centro', 'Andy', 'Robles'),
('Centro', 'Roberto', 'Bravo'),
('Centro', 'Leonardo', 'Padilla'),
('Centro', 'Alberto', 'Perez'),
('Oriente', 'Alfredo', 'Mercurio'),
('Oriente', 'Juan', 'Perez'),
('Oriente', 'Pedro', 'Serrano'),
('Oriente', 'Ivanjo', 'Ramirez'),
('Oriente', 'Oswaldo', 'Santos');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`idCliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
