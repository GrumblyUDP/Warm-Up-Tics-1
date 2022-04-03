create table AnnioF(Annio integer, primary key(Annio));

create table Tabla_RIA(Annio integer,Rango integer,Inicio decimal, Final decimal, Factor decimal, Cant_Rebajar integer, primary key(Annio, Rango));
alter table Tabla_RIA add foreign key (Annio) references AnnioF(Annio);

create table Porcentaje(Annio integer, Porcen decimal, primary key(Annio));
alter table Porcentaje add foreign key (Annio) references AnnioF(Annio);

create table Tabla_Presuncion(Annio integer, limite decimal, primary key(Annio));
alter table Tabla_Presuncion add foreign key (Annio) references AnnioF(Annio);






create table Usuario(Rut varchar(12), Nombre varchar(50), primary key(Rut));

create table Tabla_Honorarios(Rut varchar(12), Mes1 integer,Mes2 integer,Mes3 integer,Mes4 integer,Mes5 integer,Mes6 integer,Mes7 integer,Mes8 integer,Mes9 integer,Mes10 integer,Mes11 integer,Mes12 integer, primary key(Rut));
alter table Tabla_Honorarios add foreign key (Rut) references Usuario(Rut);

create table Tabla_Sueldos(Rut varchar(12), Mes1 integer,Mes2 integer,Mes3 integer,Mes4 integer,Mes5 integer,Mes6 integer,Mes7 integer,Mes8 integer,Mes9 integer,Mes10 integer,Mes11 integer,Mes12 integer, primary key(Rut));
alter table Tabla_Sueldos add foreign key (Rut) references Usuario(Rut);



INSERT INTO AnnioF VALUES (2021); 
INSERT INTO Tabla_RIA VALUES (2021, 1, 0, 8.266.698, 0, 0);




insert into Usuario values('12.345.678-9','Juan Martin');
insert into Tabla_Sueldos values('12.345.678-9',900000,900000,900000,900000,900000,900000,900000,0,0,0,0,1000000);
insert into Tabla_Honorarios values('12.345.678-9',99000,5000,75000,150000,80000,0,78000,50000,50000,11000,0,500000);