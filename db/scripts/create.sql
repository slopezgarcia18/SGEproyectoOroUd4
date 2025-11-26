--
-- PostgreSQL database dump
--

\restrict Rt04BvKM076fdtpBbXD7Q1W1yBiKIfgeAnnT62PiUjMmzk5TauFffzDE2xsXGv5

-- Dumped from database version 16.10
-- Dumped by pg_dump version 16.10

-- Started on 2025-11-26 22:12:49

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 8 (class 2615 OID 16527)
-- Name: proyecto; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA proyecto;


--
-- TOC entry 236 (class 1259 OID 16536)
-- Name: seq_cliente_id; Type: SEQUENCE; Schema: proyecto; Owner: -
--

CREATE SEQUENCE proyecto.seq_cliente_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 20000
    CACHE 1;


SET default_table_access_method = heap;

--
-- TOC entry 235 (class 1259 OID 16531)
-- Name: cliente; Type: TABLE; Schema: proyecto; Owner: -
--

CREATE TABLE proyecto.cliente (
    id bigint DEFAULT nextval('proyecto.seq_cliente_id'::regclass) NOT NULL,
    nombre character varying(50) NOT NULL,
    apellidos character varying(50) NOT NULL,
    fecha_nacim date NOT NULL,
    dni character varying(10) NOT NULL,
    email character varying(50) NOT NULL,
    nacionalidad character varying(50) NOT NULL,
    telefono bigint NOT NULL,
    direccion character varying(50) NOT NULL,
    activo boolean DEFAULT true NOT NULL
);


--
-- TOC entry 237 (class 1259 OID 16538)
-- Name: cotizacion; Type: TABLE; Schema: proyecto; Owner: -
--

CREATE TABLE proyecto.cotizacion (
    id bigint DEFAULT nextval('proyecto.seq_cliente_id'::regclass) NOT NULL,
    fecha date NOT NULL,
    precio bigint NOT NULL
);


--
-- TOC entry 239 (class 1259 OID 16550)
-- Name: estado; Type: TABLE; Schema: proyecto; Owner: -
--

CREATE TABLE proyecto.estado (
    id bigint DEFAULT nextval('proyecto.seq_cliente_id'::regclass) NOT NULL,
    nombre character varying(50) NOT NULL
);


--
-- TOC entry 238 (class 1259 OID 16544)
-- Name: venta; Type: TABLE; Schema: proyecto; Owner: -
--

CREATE TABLE proyecto.venta (
    id bigint DEFAULT nextval('proyecto.seq_cliente_id'::regclass) NOT NULL,
    fecha_venta date NOT NULL,
    id_cliente bigint NOT NULL,
    id_precio bigint NOT NULL,
    id_estado bigint NOT NULL,
    cantidad bigint NOT NULL
);


--
-- TOC entry 4791 (class 2606 OID 16535)
-- Name: cliente clientes_pkey; Type: CONSTRAINT; Schema: proyecto; Owner: -
--

ALTER TABLE ONLY proyecto.cliente
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- TOC entry 4793 (class 2606 OID 16543)
-- Name: cotizacion cotizacion_pkey; Type: CONSTRAINT; Schema: proyecto; Owner: -
--

ALTER TABLE ONLY proyecto.cotizacion
    ADD CONSTRAINT cotizacion_pkey PRIMARY KEY (id);


--
-- TOC entry 4797 (class 2606 OID 16555)
-- Name: estado estado_pkey; Type: CONSTRAINT; Schema: proyecto; Owner: -
--

ALTER TABLE ONLY proyecto.estado
    ADD CONSTRAINT estado_pkey PRIMARY KEY (id);


--
-- TOC entry 4795 (class 2606 OID 16549)
-- Name: venta venta_pkey; Type: CONSTRAINT; Schema: proyecto; Owner: -
--

ALTER TABLE ONLY proyecto.venta
    ADD CONSTRAINT venta_pkey PRIMARY KEY (id);


--
-- TOC entry 4798 (class 2606 OID 16556)
-- Name: venta fk_cliente_id; Type: FK CONSTRAINT; Schema: proyecto; Owner: -
--

ALTER TABLE ONLY proyecto.venta
    ADD CONSTRAINT fk_cliente_id FOREIGN KEY (id_cliente) REFERENCES proyecto.cliente(id) NOT VALID;


--
-- TOC entry 4799 (class 2606 OID 16566)
-- Name: venta fk_estado_id; Type: FK CONSTRAINT; Schema: proyecto; Owner: -
--

ALTER TABLE ONLY proyecto.venta
    ADD CONSTRAINT fk_estado_id FOREIGN KEY (id_estado) REFERENCES proyecto.estado(id) NOT VALID;


--
-- TOC entry 4800 (class 2606 OID 16561)
-- Name: venta fk_precio_id; Type: FK CONSTRAINT; Schema: proyecto; Owner: -
--

ALTER TABLE ONLY proyecto.venta
    ADD CONSTRAINT fk_precio_id FOREIGN KEY (id_precio) REFERENCES proyecto.cotizacion(id) NOT VALID;


-- Completed on 2025-11-26 22:12:50

--
-- PostgreSQL database dump complete
--

\unrestrict Rt04BvKM076fdtpBbXD7Q1W1yBiKIfgeAnnT62PiUjMmzk5TauFffzDE2xsXGv5

