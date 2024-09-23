-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-09-2024 a las 19:08:10
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `deportes`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `RegistrarReglaDeporte` (IN `p_deporte_nombre` VARCHAR(50), IN `p_regla_nombre` VARCHAR(50), IN `p_regla_descripcion` VARCHAR(250))   BEGIN
    DECLARE v_deporte_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Manejo de errores
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ha ocurrido un error durante la inserción de la regla.';
    END;

    -- Comienza una transacción
    START TRANSACTION;

    -- Verificar si el deporte existe
    SELECT Id INTO v_deporte_id
    FROM deporte
    WHERE Nombre = p_deporte_nombre;

    -- Si el deporte no existe, salir con error personalizado
    IF v_deporte_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El deporte no existe.';
    ELSE
        -- Insertar la nueva regla en la tabla reglas
        INSERT INTO reglas (DeporteId, Nombre, Descripcion, FechaCreacion)
        VALUES (v_deporte_id, p_regla_nombre, p_regla_descripcion, CURDATE());
        
        -- Si todo es correcto, hacer COMMIT
        COMMIT;
    END IF;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `registrar_regla` (IN `p_nombre_deporte` VARCHAR(50), IN `p_nombre_regla` VARCHAR(50), IN `p_descripcion` VARCHAR(250))   BEGIN
    DECLARE deporte_id INT;

    -- Verificar si el deporte existe
    SELECT id INTO deporte_id FROM deporte WHERE nombre = p_nombre_deporte;

    -- Si el deporte existe, insertar la regla
    IF deporte_id IS NOT NULL THEN
        INSERT INTO reglas (DeporteId, Nombre, Descripcion, FechaCreacion)
        VALUES (deporte_id, p_nombre_regla, p_descripcion, CURDATE());
        SELECT 'Regla registrada exitosamente' AS mensaje;
    ELSE
        SELECT 'El deporte no existe' AS mensaje;
    END IF;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deporte`
--

CREATE TABLE `deporte` (
  `id` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reglas`
--

CREATE TABLE `reglas` (
  `id` int(11) NOT NULL,
  `DeporteId` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(250) NOT NULL,
  `FechaCreacion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `deporte`
--
ALTER TABLE `deporte`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `reglas`
--
ALTER TABLE `reglas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reglas_deporte` (`DeporteId`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `deporte`
--
ALTER TABLE `deporte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reglas`
--
ALTER TABLE `reglas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `reglas`
--
ALTER TABLE `reglas`
  ADD CONSTRAINT `fk_reglas_deporte` FOREIGN KEY (`DeporteId`) REFERENCES `deporte` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
