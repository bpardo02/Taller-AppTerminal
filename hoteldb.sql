create database hotelDB;

use hotelDB;

CREATE TABLE admin_info (
	rut_admin varchar(20) PRIMARY KEY,
    pass_admin char(102),
    name_admin varchar(50));
    
select * from admin_info;
    
insert into admin_info (rut_admin, pass_admin, name_admin)
values ('20290589-7', '123123', 'Miguel');
    
CREATE TABLE encargado_info (
	rut_encargado varchar(20) PRIMARY KEY,
    name_encargado varchar(50),
    pass_encargado char(102));
    
    
    
select * from encargado_info;


CREATE TABLE log_registro (
	id_add INT PRIMARY KEY,
    rut_admin varchar(20),
    rut_encargado varchar(20),
    fecha date,
    
    FOREIGN KEY (rut_admin) references admin_info(rut_admin),
    FOREIGN KEY (rut_encargado) references encargado_info(rut_encargado));
    
    

    
CREATE TABLE huesped (
	rut_huesped varchar(20) PRIMARY KEY,
    nombre_huesped varchar(50),
    responsabilidad varchar(1));
    
alter table huesped modify responsabilidad varchar(1);
select * from huesped;
    

    
    
CREATE TABLE habitacion(
	id_room int PRIMARY KEY,
    numero int,
	cantidad_max int,
    orientacion varchar(50));
    
select * from habitacion;
    
CREATE TABLE asignacion(
	id_asignacion int PRIMARY KEY,
    id_room int,
    rut_encargado varchar(20),
    dia date,
    hora time,
    
    FOREIGN KEY (id_room) references habitacion(id_room),
    FOREIGN KEY (rut_encargado) references encargado_info(rut_encargado));
    
    
    CREATE TABLE log_huesped(
	id_asignacion int,
	rut_huesped varchar(20), 
    
	PRIMARY KEY (id_asignacion, rut_huesped),
    
    FOREIGN KEY (id_asignacion) references asignacion(id_asignacion),
    FOREIGN KEY (rut_huesped) references huesped(rut_huesped));
    
    
CREATE TABLE detalle_boleta(
	id_detalle int PRIMARY KEY,
    id_asignacion int,
    valor_pagado int,
    medio_pago varchar(20),
    fecha date,
    hora time,
    
    FOREIGN KEY (id_asignacion) references asignacion(id_asignacion));
    





drop database hoteldb;    

	
    