-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-03-2020 a las 19:15:19
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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
