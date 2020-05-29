-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-05-2020 a las 18:57:28
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
-- Base de datos: `r_humanos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuncio`
--

CREATE TABLE `anuncio` (
  `idAnuncio` int(11) NOT NULL,
  `idSolicitud` int(11) NOT NULL,
  `Num_Solicitantes` int(11) NOT NULL,
  `FechaPublicacion` date NOT NULL,
  `FechaCierre` date NOT NULL,
  `idcontacto` int(11) NOT NULL,
  `idMedioPublicidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `anuncio`
--

INSERT INTO `anuncio` (`idAnuncio`, `idSolicitud`, `Num_Solicitantes`, `FechaPublicacion`, `FechaCierre`, `idcontacto`, `idMedioPublicidad`) VALUES
(1, 23, 17, '2020-05-05', '2020-05-18', 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `idArea` int(11) NOT NULL,
  `AreaDescripcion` varchar(45) DEFAULT NULL,
  `AreaNombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`idArea`, `AreaDescripcion`, `AreaNombre`) VALUES
(1, 'Desarrollo de aplicaciones ', 'Desarrollo '),
(2, '¨Prueba de aplicaciones', 'Pruebas '),
(3, 'descripción de esta área', 'Testing');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato`
--

CREATE TABLE `candidato` (
  `Curp` varchar(18) NOT NULL,
  `RFC` varchar(13) DEFAULT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Domicilio` varchar(45) DEFAULT NULL,
  `Telefono` varchar(45) DEFAULT NULL,
  `E_Mail` varchar(45) DEFAULT NULL,
  `Sexo` varchar(45) DEFAULT NULL,
  `Edad` tinyint(2) DEFAULT NULL,
  `NSS` int(11) DEFAULT NULL,
  `Fotografia` blob,
  `idEstadoCivil` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `candidato`
--

INSERT INTO `candidato` (`Curp`, `RFC`, `Nombre`, `Domicilio`, `Telefono`, `E_Mail`, `Sexo`, `Edad`, `NSS`, `Fotografia`, `idEstadoCivil`) VALUES
('AAAAA12173gf116', NULL, 'Posillos Juarez Marcelo', 'Calle 2 Colonia 20135', '4493684556', 'cetis@gmail.com', 'M', 23, 98968, NULL, 2),
('AAAAA12173gf12', NULL, 'Martinez Macias Juan', 'Calle 1 Colonia 20135', '4493682767', 'cetis@gmail.com', 'M', 36, 98968, NULL, 2),
('AAAAA12173gf14', NULL, 'Casillas Jimenez Tere', 'Calle 2 Colonia 20134', '4493645698', 'cetis@gmail.com', 'F', 28, 18463, NULL, 1),
('AAAAA12173gf15', NULL, 'Posillos Juarez Marcelo', 'Calle 2 Colonia 20135', '4493684556', 'cetis@gmail.com', 'M', 23, 98968, NULL, 2),
('AAAAA12173gf16', NULL, 'Posillos Juarez Marcelo', 'Calle 2 Colonia 20135', '4493684556', 'cetis@gmail.com', 'M', 23, 98968, NULL, 2),
('AAAAA12173gf17', NULL, 'Marget Salas Brandon', 'Calle 2 Colonia 20135', '4493684556', 'cetis@gmail.com', 'M', 34, 98968, NULL, 2),
('AAAAA12173gf19', NULL, 'Rac Mac Susan', 'Calle 1 Colonia 20134', '4493684556', 'cetis@gmail.com', 'F', 34, 18463, NULL, 1),
('AAAAA12173gf20', NULL, 'Posillos Juarez Marcela', 'Calle 1 Colonia 20131', '4493684552', 'cetis@gmail.com', 'F', 45, 16546, NULL, 2),
('AAAAA12173gfr1', NULL, 'Rac Mac Susana', 'Calle 1 Colonia 20134', '4493684556', 'cetis@gmail.com', 'F', 34, 16546, NULL, 1),
('AAAAA12173gfr10', NULL, 'Mendez Marquez Paulina', 'Calle 1 Colonia 20132', '4493684534', 'cetis@gmail.com', 'F', 34, 16546, NULL, 2),
('AAAAA12173gfr2', NULL, 'Marget Perez Braulio', 'Calle 1 Colonia 20134', '4493684556', 'cetis@gmail.com', 'M', 34, 78780, NULL, 2),
('AAAAA12173gfr3', NULL, 'Santos Sanchez Maria', 'Calle 1 Colonia 20131', '4493684552', 'cetis@gmail.com', 'F', 34, 16546, NULL, 1),
('AAAAA12173gfr4', NULL, 'Ramirez Gallego Jesus', 'Calle 1 Colonia 20134', '4493684556', 'cetis@gmail.com', 'M', 23, 98968, NULL, 2),
('AAAAA12173gfr5', NULL, 'Marget Salas Braulio', 'Calle 1 Colonia 20134', '4493684556', 'cetis@gmail.com', 'M', 35, 31513, NULL, 2),
('AAAAA12173gfr6', NULL, 'Marget Salas Bastio', 'Calle 1 Colonia 20134', '4493684556', 'cetis@gmail.com', 'M', 23, 98968, NULL, 2),
('AAAAA12173gfr7', NULL, 'Rac Mac Susana', 'Calle 1 Colonia 20132', '4493684556', 'cetis@gmail.com', 'F', 23, 98968, NULL, 1),
('FOPB110899HASLS', 'ABCD123', 'BRYAN RICARDO', 'Calle DZilam 29 Inf Morelos 20264', '4495777823', '1ricardo_flores@gmail.com', 'M', 25, 422345, NULL, 1),
('vcvxc', NULL, 'vdvd', 'xcvbxcbc', '2151', 'sdsasd@gmail.com', 'F', 12, 121, NULL, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato_has_funcion`
--

CREATE TABLE `candidato_has_funcion` (
  `Curp` varchar(18) NOT NULL,
  `idFuncion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato_has_habilidad`
--

CREATE TABLE `candidato_has_habilidad` (
  `Curp` varchar(18) NOT NULL,
  `idHabilidad` int(11) NOT NULL,
  `Experiencia` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `candidato_has_habilidad`
--

INSERT INTO `candidato_has_habilidad` (`Curp`, `idHabilidad`, `Experiencia`) VALUES
('AAAAA12173gf12', 1, '2 años'),
('AAAAA12173gfr1', 5, '2 años'),
('AAAAA12173gfr5', 3, '2 años');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato_has_idioma`
--

CREATE TABLE `candidato_has_idioma` (
  `Curp` varchar(18) NOT NULL,
  `idIdioma` int(11) NOT NULL,
  `Nivel` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `candidato_has_idioma`
--

INSERT INTO `candidato_has_idioma` (`Curp`, `idIdioma`, `Nivel`) VALUES
('AAAAA12173gfr1', 1, 'Bueno'),
('AAAAA12173gfr10', 1, 'Bueno'),
('AAAAA12173gfr2', 1, 'Bueno'),
('AAAAA12173gfr3', 1, 'Bueno'),
('AAAAA12173gfr5', 1, 'Expero'),
('AAAAA12173gfr5', 4, 'Bueno'),
('vcvxc', 3, 'medio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato_has_nivelacademico`
--

CREATE TABLE `candidato_has_nivelacademico` (
  `Curp` varchar(18) NOT NULL,
  `idNivelAcademico` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `Institucion` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `candidato_has_nivelacademico`
--

INSERT INTO `candidato_has_nivelacademico` (`Curp`, `idNivelAcademico`, `idCarrera`, `Institucion`) VALUES
('AAAAA12173gf14', 2, 3, 'uaa'),
('FOPB110899HASLS', 1, 2, 'ITA'),
('FOPB110899HASLS', 3, 3, 'ITA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `idCarrera` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`idCarrera`, `Descripcion`) VALUES
(1, 'Tecnico en electricidad'),
(2, 'TICS'),
(3, 'Licenciado en sistemas (o afin) thnty');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `idcontacto` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Domicilio` varchar(45) DEFAULT NULL,
  `Razon_Social` varchar(45) DEFAULT NULL,
  `Telefono` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`idcontacto`, `Nombre`, `Domicilio`, `Razon_Social`, `Telefono`) VALUES
(1, 'dedde', 'ded', 'cd', '24'),
(3, 'Home-Int ', 'cetis 155', '2', '254325');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_de_empresa`
--

CREATE TABLE `datos_de_empresa` (
  `idEmpresa` int(11) NOT NULL,
  `Nombre_de_empresa` varchar(100) NOT NULL,
  `Descripcion` varchar(100) DEFAULT NULL,
  `Telefono` varchar(40) DEFAULT NULL,
  `Domicilio` varchar(100) DEFAULT NULL,
  `E_Mail` varchar(50) DEFAULT NULL,
  `RazonSocial` varchar(50) DEFAULT NULL,
  `Estructura_Juridica` varchar(50) DEFAULT NULL,
  `Encargado` varchar(50) DEFAULT NULL,
  `CIF_Empresa` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `datos_de_empresa`
--

INSERT INTO `datos_de_empresa` (`idEmpresa`, `Nombre_de_empresa`, `Descripcion`, `Telefono`, `Domicilio`, `E_Mail`, `RazonSocial`, `Estructura_Juridica`, `Encargado`, `CIF_Empresa`) VALUES
(1, 'PruebaSist', 'Empresa de prueba para el sistema ', '449-999-8888', '449-999-8888', 'pruebasist@pruebasist.com.mx', 'PruebaSist S.A.', 'S.A', 'Nombre del CEO ', '?????????');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadocivil`
--

CREATE TABLE `estadocivil` (
  `idEstadoCivil` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `estadocivil`
--

INSERT INTO `estadocivil` (`idEstadoCivil`, `Descripcion`) VALUES
(1, 'Soltero'),
(2, 'Casado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estatus_solicitud`
--

CREATE TABLE `estatus_solicitud` (
  `idEstatus_Solicitud` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `estatus_solicitud`
--

INSERT INTO `estatus_solicitud` (`idEstatus_Solicitud`, `Descripcion`) VALUES
(1, 'Pendiente'),
(2, 'Aprobada'),
(3, 'Publicado'),
(4, 'En proceso'),
(5, 'Terminada'),
(6, 'Cancelado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funcion`
--

CREATE TABLE `funcion` (
  `idFuncion` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `funcion`
--

INSERT INTO `funcion` (`idFuncion`, `Descripcion`) VALUES
(1, 'Puesto de prueba ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funcion_has_perfil`
--

CREATE TABLE `funcion_has_perfil` (
  `idFuncion` int(11) NOT NULL,
  `idPerfil` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad`
--

CREATE TABLE `habilidad` (
  `idHabilidad` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `habilidad`
--

INSERT INTO `habilidad` (`idHabilidad`, `Descripcion`) VALUES
(1, 'Mantenimiento de equipo de computo'),
(2, 'Mantenimiento Electrico'),
(3, 'Java experto'),
(4, 'Python experto'),
(5, 'Desarrollo de aplicaciones moviles ddd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad_has_perfil`
--

CREATE TABLE `habilidad_has_perfil` (
  `idHabilidad` int(11) NOT NULL,
  `idPerfil` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idioma`
--

CREATE TABLE `idioma` (
  `idIdioma` int(11) NOT NULL,
  `Lenguaje` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `idioma`
--

INSERT INTO `idioma` (`idIdioma`, `Lenguaje`) VALUES
(1, 'Ingles'),
(2, 'Japones'),
(3, 'Aleman'),
(4, 'Frances');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mediopublicidad`
--

CREATE TABLE `mediopublicidad` (
  `idMedioPublicidad` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mediopublicidad`
--

INSERT INTO `mediopublicidad` (`idMedioPublicidad`, `Descripcion`) VALUES
(1, 'Diarios Locales'),
(2, 'Radio local'),
(3, 'Internet');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivelacademico`
--

CREATE TABLE `nivelacademico` (
  `idNivelAcademico` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `nivelacademico`
--

INSERT INTO `nivelacademico` (`idNivelAcademico`, `Descripcion`) VALUES
(1, 'Tecnico'),
(2, 'Tecnico Superior Universitario'),
(3, 'Licenciatura nueva'),
(4, 'Maestria');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

CREATE TABLE `perfil` (
  `idPerfil` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL,
  `idCarrera` int(11) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `idNivelAcademico` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil_has_idioma`
--

CREATE TABLE `perfil_has_idioma` (
  `idPerfil` int(11) NOT NULL,
  `idIdioma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL,
  `SalarioAnual` int(11) DEFAULT NULL,
  `Beneficios` varchar(250) DEFAULT NULL,
  `Bonos` int(11) DEFAULT NULL,
  `Aprobacion` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `Descripcion`, `SalarioAnual`, `Beneficios`, `Bonos`, `Aprobacion`) VALUES
(1, 'Desarrollador de software', 450000, 'Ninguno', 15, 1),
(2, 'Tester', 54000, 'todos', 4500, 1),
(3, 'Diseñador de Base de Datos ', 45000, 'todos', 4500, 0),
(4, 'Puesto para prueba', 45000, 'todos', 100, 1),
(5, 'Puesto de proceso ', 4500, 'Ninguno', 15000, 1),
(6, 'Puesto de prueba ', 1, 'Ninguno', 100, 0),
(8, 'Puesto para el equipo Alpha ', 54000, 'todos juntos', 100, 0),
(9, 'Puesto de prueba para el nuevo equipo alpha', 100000, 'Ninguno', 100, 0),
(10, 'Puesto de prueba para el equipo Beta', 134, 'Ninguno', 100000, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_habilidad`
--

CREATE TABLE `puesto_has_habilidad` (
  `idPuesto` int(11) NOT NULL,
  `idHabilidad` int(11) NOT NULL,
  `Experiencia` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `puesto_has_habilidad`
--

INSERT INTO `puesto_has_habilidad` (`idPuesto`, `idHabilidad`, `Experiencia`) VALUES
(1, 2, '2 años'),
(1, 3, '2 años'),
(1, 4, '2 años'),
(1, 5, '1 año'),
(2, 3, '2 años'),
(2, 4, '2 años'),
(3, 3, '1 año'),
(3, 4, '2 años'),
(3, 5, '1 año'),
(4, 1, '2 años'),
(4, 5, '1 año'),
(9, 2, '2 años'),
(9, 3, '2 meses');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_idioma`
--

CREATE TABLE `puesto_has_idioma` (
  `idPuesto` int(11) NOT NULL,
  `idIdioma` int(11) NOT NULL,
  `Nivel` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `puesto_has_idioma`
--

INSERT INTO `puesto_has_idioma` (`idPuesto`, `idIdioma`, `Nivel`) VALUES
(1, 1, '80% conversación'),
(1, 2, '80% conversación'),
(1, 3, 'Basico'),
(1, 4, 'Basico'),
(2, 1, '80% conversación'),
(2, 4, 'Basico'),
(3, 1, '80% conversación'),
(4, 1, 'Basico'),
(4, 4, '80% conversación'),
(9, 1, '80% conversación'),
(9, 4, '80% conversación');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultadocandidato`
--

CREATE TABLE `resultadocandidato` (
  `EstatusProceso` varchar(45) DEFAULT NULL,
  `Comentarios` varchar(45) DEFAULT NULL,
  `Aprobacion` varchar(45) DEFAULT NULL,
  `Comentarios_ofertas_salario` varchar(45) DEFAULT NULL,
  `Comentarios_area_seleccion` varchar(45) DEFAULT NULL,
  `Estatus` varchar(45) DEFAULT NULL,
  `idSolicitud` int(11) DEFAULT NULL,
  `Curp` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud`
--

CREATE TABLE `solicitud` (
  `idSolicitud` int(11) NOT NULL,
  `FechaSolicitud` date DEFAULT NULL,
  `NumeroVacante` int(11) DEFAULT NULL,
  `idArea` int(11) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `idNivelAcademico` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `idEstatus_Solicitud` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `solicitud`
--

INSERT INTO `solicitud` (`idSolicitud`, `FechaSolicitud`, `NumeroVacante`, `idArea`, `idPuesto`, `idNivelAcademico`, `idCarrera`, `idEstatus_Solicitud`) VALUES
(14, '2020-04-30', 1, 1, 1, 3, 3, 6),
(15, '2020-04-30', 1, 1, 3, 3, 3, 6),
(16, '2020-04-30', 5, 2, 2, 3, 3, 6),
(17, '2020-04-30', 10, 2, 2, 3, 3, 6),
(19, '2020-04-30', 5, 3, 4, 3, 3, 2),
(22, '2020-04-30', 2, 3, 2, 1, 1, 2),
(23, '2020-04-30', 15, 3, 8, 1, 1, 3),
(24, '2020-04-09', 15, 1, 2, 2, 3, 6),
(25, '2020-04-30', 2, 2, 8, 1, 1, 6),
(26, '2020-05-09', 33, 3, 1, 3, 3, 2),
(27, '2020-05-17', 43, 3, 5, 4, 1, 2),
(28, '0000-00-00', 13, 2, 3, 1, 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario`, `contraseña`) VALUES
('Admin', '4dm1n_t3st');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anuncio`
--
ALTER TABLE `anuncio`
  ADD PRIMARY KEY (`idAnuncio`),
  ADD KEY `fk_Anuncio_Contacto1` (`idcontacto`),
  ADD KEY `fk_Anuncio_Solicitud1` (`idSolicitud`),
  ADD KEY `fk_Anuncio_Publicidad1` (`idMedioPublicidad`);

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`);

--
-- Indices de la tabla `candidato`
--
ALTER TABLE `candidato`
  ADD PRIMARY KEY (`Curp`),
  ADD KEY `fk_Candidato_EstadoCivil1` (`idEstadoCivil`);

--
-- Indices de la tabla `candidato_has_funcion`
--
ALTER TABLE `candidato_has_funcion`
  ADD PRIMARY KEY (`Curp`,`idFuncion`),
  ADD KEY `fk_Candidato_has_Funcion_Funcion1` (`idFuncion`);

--
-- Indices de la tabla `candidato_has_habilidad`
--
ALTER TABLE `candidato_has_habilidad`
  ADD PRIMARY KEY (`Curp`,`idHabilidad`),
  ADD KEY `fk_Candidato_has_Habilidad_Habilidad1` (`idHabilidad`);

--
-- Indices de la tabla `candidato_has_idioma`
--
ALTER TABLE `candidato_has_idioma`
  ADD PRIMARY KEY (`Curp`,`idIdioma`),
  ADD KEY `fk_Candidato_has_Idioma_Idioma1` (`idIdioma`);

--
-- Indices de la tabla `candidato_has_nivelacademico`
--
ALTER TABLE `candidato_has_nivelacademico`
  ADD PRIMARY KEY (`Curp`,`idNivelAcademico`),
  ADD KEY `fk_Candidato_has_NivelAcademico_NivelAcademico1` (`idNivelAcademico`),
  ADD KEY `fk_Candidato_has_NivelAcademico_Carrera1` (`idCarrera`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`idCarrera`);

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`idcontacto`);

--
-- Indices de la tabla `datos_de_empresa`
--
ALTER TABLE `datos_de_empresa`
  ADD PRIMARY KEY (`idEmpresa`);

--
-- Indices de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  ADD PRIMARY KEY (`idEstadoCivil`);

--
-- Indices de la tabla `estatus_solicitud`
--
ALTER TABLE `estatus_solicitud`
  ADD PRIMARY KEY (`idEstatus_Solicitud`);

--
-- Indices de la tabla `funcion`
--
ALTER TABLE `funcion`
  ADD PRIMARY KEY (`idFuncion`);

--
-- Indices de la tabla `funcion_has_perfil`
--
ALTER TABLE `funcion_has_perfil`
  ADD PRIMARY KEY (`idFuncion`,`idPerfil`),
  ADD KEY `fk_Funcion_has_Perfil_Perfil1` (`idPerfil`);

--
-- Indices de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  ADD PRIMARY KEY (`idHabilidad`);

--
-- Indices de la tabla `habilidad_has_perfil`
--
ALTER TABLE `habilidad_has_perfil`
  ADD PRIMARY KEY (`idHabilidad`,`idPerfil`),
  ADD KEY `fk_Habilidad_has_Perfil_Perfil1` (`idPerfil`);

--
-- Indices de la tabla `idioma`
--
ALTER TABLE `idioma`
  ADD PRIMARY KEY (`idIdioma`);

--
-- Indices de la tabla `mediopublicidad`
--
ALTER TABLE `mediopublicidad`
  ADD PRIMARY KEY (`idMedioPublicidad`);

--
-- Indices de la tabla `nivelacademico`
--
ALTER TABLE `nivelacademico`
  ADD PRIMARY KEY (`idNivelAcademico`);

--
-- Indices de la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD PRIMARY KEY (`idPerfil`),
  ADD KEY `fk_Perfil_Carrera1` (`idCarrera`),
  ADD KEY `fk_Perfil_Puesto1` (`idPuesto`),
  ADD KEY `fk_Perfil_NivelAcademico1` (`idNivelAcademico`);

--
-- Indices de la tabla `perfil_has_idioma`
--
ALTER TABLE `perfil_has_idioma`
  ADD PRIMARY KEY (`idPerfil`,`idIdioma`),
  ADD KEY `fk_Perfil_has_Idioma_Idioma1` (`idIdioma`);

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`);

--
-- Indices de la tabla `puesto_has_habilidad`
--
ALTER TABLE `puesto_has_habilidad`
  ADD PRIMARY KEY (`idPuesto`,`idHabilidad`),
  ADD KEY `fk_Puesto_has_habilidad_habilidad` (`idHabilidad`);

--
-- Indices de la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  ADD PRIMARY KEY (`idPuesto`,`idIdioma`),
  ADD KEY `fk_Puesto_has_habilidad_Idioma` (`idIdioma`);

--
-- Indices de la tabla `resultadocandidato`
--
ALTER TABLE `resultadocandidato`
  ADD KEY `fk_ResultadoCandidato_Solicitud1` (`idSolicitud`),
  ADD KEY `fk_ResultadoCandidato_Candidato1` (`Curp`);

--
-- Indices de la tabla `solicitud`
--
ALTER TABLE `solicitud`
  ADD PRIMARY KEY (`idSolicitud`),
  ADD KEY `fk_Solicitud_Area1` (`idArea`),
  ADD KEY `fk_Solicitud_Puesto1` (`idPuesto`),
  ADD KEY `fk_Solicitud_Nivel_Academico1` (`idNivelAcademico`),
  ADD KEY `fk_Solicitud_Carrera1` (`idCarrera`),
  ADD KEY `fk_Solicitud_Estatus_Solicitud1` (`idEstatus_Solicitud`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anuncio`
--
ALTER TABLE `anuncio`
  MODIFY `idAnuncio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `area`
--
ALTER TABLE `area`
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `idCarrera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `idcontacto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `datos_de_empresa`
--
ALTER TABLE `datos_de_empresa`
  MODIFY `idEmpresa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  MODIFY `idEstadoCivil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `estatus_solicitud`
--
ALTER TABLE `estatus_solicitud`
  MODIFY `idEstatus_Solicitud` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `funcion`
--
ALTER TABLE `funcion`
  MODIFY `idFuncion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  MODIFY `idHabilidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `idioma`
--
ALTER TABLE `idioma`
  MODIFY `idIdioma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `mediopublicidad`
--
ALTER TABLE `mediopublicidad`
  MODIFY `idMedioPublicidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `nivelacademico`
--
ALTER TABLE `nivelacademico`
  MODIFY `idNivelAcademico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `perfil`
--
ALTER TABLE `perfil`
  MODIFY `idPerfil` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `solicitud`
--
ALTER TABLE `solicitud`
  MODIFY `idSolicitud` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `anuncio`
--
ALTER TABLE `anuncio`
  ADD CONSTRAINT `fk_Anuncio_Contacto1` FOREIGN KEY (`idcontacto`) REFERENCES `contacto` (`idcontacto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Anuncio_MedioPublicidad1` FOREIGN KEY (`idMedioPublicidad`) REFERENCES `mediopublicidad` (`idMedioPublicidad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Anuncio_Publicidad1` FOREIGN KEY (`idMedioPublicidad`) REFERENCES `mediopublicidad` (`idMedioPublicidad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Anuncio_Solicitud1` FOREIGN KEY (`idSolicitud`) REFERENCES `solicitud` (`idSolicitud`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `candidato`
--
ALTER TABLE `candidato`
  ADD CONSTRAINT `fk_Candidato_EstadoCivil1` FOREIGN KEY (`idEstadoCivil`) REFERENCES `estadocivil` (`idEstadoCivil`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `candidato_has_funcion`
--
ALTER TABLE `candidato_has_funcion`
  ADD CONSTRAINT `fk_Candidato_has_Funcion_Candidato1` FOREIGN KEY (`Curp`) REFERENCES `candidato` (`Curp`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Candidato_has_Funcion_Funcion1` FOREIGN KEY (`idFuncion`) REFERENCES `funcion` (`idFuncion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `candidato_has_habilidad`
--
ALTER TABLE `candidato_has_habilidad`
  ADD CONSTRAINT `fk_Candidato_has_Habilidad_Candidato1` FOREIGN KEY (`Curp`) REFERENCES `candidato` (`Curp`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Candidato_has_Habilidad_Habilidad1` FOREIGN KEY (`idHabilidad`) REFERENCES `habilidad` (`idHabilidad`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `candidato_has_idioma`
--
ALTER TABLE `candidato_has_idioma`
  ADD CONSTRAINT `fk_Candidato_has_Idioma_Candidato1` FOREIGN KEY (`Curp`) REFERENCES `candidato` (`Curp`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Candidato_has_Idioma_Idioma1` FOREIGN KEY (`idIdioma`) REFERENCES `idioma` (`idIdioma`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `candidato_has_nivelacademico`
--
ALTER TABLE `candidato_has_nivelacademico`
  ADD CONSTRAINT `fk_Candidato_has_NivelAcademico_Candidato1` FOREIGN KEY (`Curp`) REFERENCES `candidato` (`Curp`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Candidato_has_NivelAcademico_Carrera1` FOREIGN KEY (`idCarrera`) REFERENCES `carrera` (`idCarrera`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Candidato_has_NivelAcademico_NivelAcademico1` FOREIGN KEY (`idNivelAcademico`) REFERENCES `nivelacademico` (`idNivelAcademico`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `funcion_has_perfil`
--
ALTER TABLE `funcion_has_perfil`
  ADD CONSTRAINT `fk_Funcion_has_Perfil_Funcion1` FOREIGN KEY (`idFuncion`) REFERENCES `funcion` (`idFuncion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Funcion_has_Perfil_Perfil1` FOREIGN KEY (`idPerfil`) REFERENCES `perfil` (`idPerfil`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `habilidad_has_perfil`
--
ALTER TABLE `habilidad_has_perfil`
  ADD CONSTRAINT `fk_Habilidad_has_Perfil_Habilidad1` FOREIGN KEY (`idHabilidad`) REFERENCES `habilidad` (`idHabilidad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Habilidad_has_Perfil_Perfil1` FOREIGN KEY (`idPerfil`) REFERENCES `perfil` (`idPerfil`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD CONSTRAINT `fk_Perfil_Carrera1` FOREIGN KEY (`idCarrera`) REFERENCES `carrera` (`idCarrera`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Perfil_NivelAcademico1` FOREIGN KEY (`idNivelAcademico`) REFERENCES `nivelacademico` (`idNivelAcademico`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Perfil_Puesto1` FOREIGN KEY (`idPuesto`) REFERENCES `puesto` (`idPuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `perfil_has_idioma`
--
ALTER TABLE `perfil_has_idioma`
  ADD CONSTRAINT `fk_Perfil_has_Idioma_Idioma1` FOREIGN KEY (`idIdioma`) REFERENCES `idioma` (`idIdioma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Perfil_has_Idioma_Perfil1` FOREIGN KEY (`idPerfil`) REFERENCES `perfil` (`idPerfil`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `puesto_has_habilidad`
--
ALTER TABLE `puesto_has_habilidad`
  ADD CONSTRAINT `fk_Puesto_has_habilidad_habilidad` FOREIGN KEY (`idHabilidad`) REFERENCES `habilidad` (`idHabilidad`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Puesto_has_habilidad_puesto` FOREIGN KEY (`idPuesto`) REFERENCES `puesto` (`idPuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  ADD CONSTRAINT `fk_Puesto_has_Idioma_Puesto` FOREIGN KEY (`idPuesto`) REFERENCES `puesto` (`idPuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Puesto_has_habilidad_Idioma` FOREIGN KEY (`idIdioma`) REFERENCES `idioma` (`idIdioma`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `resultadocandidato`
--
ALTER TABLE `resultadocandidato`
  ADD CONSTRAINT `fk_ResultadoCandidato_Candidato1` FOREIGN KEY (`Curp`) REFERENCES `candidato` (`Curp`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_ResultadoCandidato_Solicitud1` FOREIGN KEY (`idSolicitud`) REFERENCES `solicitud` (`idSolicitud`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `solicitud`
--
ALTER TABLE `solicitud`
  ADD CONSTRAINT `fk_Solicitud_Area1` FOREIGN KEY (`idArea`) REFERENCES `area` (`idArea`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Solicitud_Carrera1` FOREIGN KEY (`idCarrera`) REFERENCES `carrera` (`idCarrera`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Solicitud_Estatus_Solicitud1` FOREIGN KEY (`idEstatus_Solicitud`) REFERENCES `estatus_solicitud` (`idEstatus_Solicitud`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Solicitud_Nivel_Academico1` FOREIGN KEY (`idNivelAcademico`) REFERENCES `nivelacademico` (`idNivelAcademico`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Solicitud_Puesto1` FOREIGN KEY (`idPuesto`) REFERENCES `puesto` (`idPuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
