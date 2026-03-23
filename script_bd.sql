-- Script de Base de Datos para el Sistema de Gestión Académica
CREATE DATABASE IF NOT EXISTS gestion_academica;
USE gestion_academica;

-- Tabla exigida en la Semana 14
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Tabla del proyecto (Expedientes y Trámites)
CREATE TABLE IF NOT EXISTS tramites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    costo DECIMAL(10,2) NOT NULL
);