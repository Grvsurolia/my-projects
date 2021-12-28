--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4 (Ubuntu 13.4-1.pgdg18.04+1)
-- Dumped by pg_dump version 13.4 (Ubuntu 13.4-1.pgdg18.04+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: product_subproduct; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.product_subproduct (
    id bigint NOT NULL,
    subproduct_name character varying(500),
    price double precision,
    discount_percent double precision,
    sale_price double precision
);


ALTER TABLE public.product_subproduct OWNER TO angaza;

--
-- Name: product_subproduct_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.product_subproduct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_subproduct_id_seq OWNER TO angaza;

--
-- Name: product_subproduct_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.product_subproduct_id_seq OWNED BY public.product_subproduct.id;


--
-- Name: product_subproduct id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.product_subproduct ALTER COLUMN id SET DEFAULT nextval('public.product_subproduct_id_seq'::regclass);


--
-- Data for Name: product_subproduct; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.product_subproduct (id, subproduct_name, price, discount_percent, sale_price) FROM stdin;
1	Cardio	500	0	0
2	Monthly Bill	200	0	50
3	Cardio	15	0	10
4	newcardio	500	20	100
\.


--
-- Name: product_subproduct_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.product_subproduct_id_seq', 4, true);


--
-- Name: product_subproduct product_subproduct_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.product_subproduct
    ADD CONSTRAINT product_subproduct_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

