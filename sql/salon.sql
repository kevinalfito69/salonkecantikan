--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

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
-- Name: kategori; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kategori (
    idkategori integer NOT NULL,
    kode_kategori character varying(255) NOT NULL,
    nama_kategori character varying(100) NOT NULL
);


ALTER TABLE public.kategori OWNER TO postgres;

--
-- Name: kategori_idkategori_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kategori_idkategori_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kategori_idkategori_seq OWNER TO postgres;

--
-- Name: kategori_idkategori_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kategori_idkategori_seq OWNED BY public.kategori.idkategori;


--
-- Name: pegawai; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pegawai (
    idpegawai integer NOT NULL,
    nama character varying(255) NOT NULL,
    posisi character varying(255) NOT NULL
);


ALTER TABLE public.pegawai OWNER TO postgres;

--
-- Name: pegawai_idpegawai_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pegawai_idpegawai_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pegawai_idpegawai_seq OWNER TO postgres;

--
-- Name: pegawai_idpegawai_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pegawai_idpegawai_seq OWNED BY public.pegawai.idpegawai;


--
-- Name: produk; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produk (
    idproduk integer NOT NULL,
    kode_produk character varying(255) NOT NULL,
    nama_produk character varying(255) NOT NULL,
    kode_kategori character varying(255) NOT NULL
);


ALTER TABLE public.produk OWNER TO postgres;

--
-- Name: produk_idproduk_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produk_idproduk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.produk_idproduk_seq OWNER TO postgres;

--
-- Name: produk_idproduk_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produk_idproduk_seq OWNED BY public.produk.idproduk;


--
-- Name: spesialis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spesialis (
    id integer NOT NULL,
    kode_spesialis character varying(255) NOT NULL,
    nama_spesialis character varying(100) NOT NULL,
    kategori character varying(100) NOT NULL
);


ALTER TABLE public.spesialis OWNER TO postgres;

--
-- Name: spesialis_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spesialis_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.spesialis_id_seq OWNER TO postgres;

--
-- Name: spesialis_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spesialis_id_seq OWNED BY public.spesialis.id;


--
-- Name: transaksi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaksi (
    idtransaksi integer NOT NULL,
    kode_transaksi character varying(255) NOT NULL,
    nama_pelanggan character varying(255) NOT NULL,
    tanggal_transaksi date NOT NULL,
    spesialis character varying(255) NOT NULL,
    kategori character varying(255) NOT NULL
);


ALTER TABLE public.transaksi OWNER TO postgres;

--
-- Name: transaksi_idtransaksi_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transaksi_idtransaksi_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.transaksi_idtransaksi_seq OWNER TO postgres;

--
-- Name: transaksi_idtransaksi_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transaksi_idtransaksi_seq OWNED BY public.transaksi.idtransaksi;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    iduser integer NOT NULL,
    username character varying(255) NOT NULL,
    password character varying(100) NOT NULL,
    rolename character varying(100) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_iduser_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_iduser_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_iduser_seq OWNER TO postgres;

--
-- Name: users_iduser_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_iduser_seq OWNED BY public.users.iduser;


--
-- Name: kategori idkategori; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kategori ALTER COLUMN idkategori SET DEFAULT nextval('public.kategori_idkategori_seq'::regclass);


--
-- Name: pegawai idpegawai; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pegawai ALTER COLUMN idpegawai SET DEFAULT nextval('public.pegawai_idpegawai_seq'::regclass);


--
-- Name: produk idproduk; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produk ALTER COLUMN idproduk SET DEFAULT nextval('public.produk_idproduk_seq'::regclass);


--
-- Name: spesialis id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spesialis ALTER COLUMN id SET DEFAULT nextval('public.spesialis_id_seq'::regclass);


--
-- Name: transaksi idtransaksi; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaksi ALTER COLUMN idtransaksi SET DEFAULT nextval('public.transaksi_idtransaksi_seq'::regclass);


--
-- Name: users iduser; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN iduser SET DEFAULT nextval('public.users_iduser_seq'::regclass);


--
-- Data for Name: kategori; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kategori (idkategori, kode_kategori, nama_kategori) FROM stdin;
\.


--
-- Data for Name: pegawai; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pegawai (idpegawai, nama, posisi) FROM stdin;
\.


--
-- Data for Name: produk; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produk (idproduk, kode_produk, nama_produk, kode_kategori) FROM stdin;
\.


--
-- Data for Name: spesialis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spesialis (id, kode_spesialis, nama_spesialis, kategori) FROM stdin;
\.


--
-- Data for Name: transaksi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaksi (idtransaksi, kode_transaksi, nama_pelanggan, tanggal_transaksi, spesialis, kategori) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (iduser, username, password, rolename) FROM stdin;
1	admin	123	admin
2	pegawai	123	pegawai
\.


--
-- Name: kategori_idkategori_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kategori_idkategori_seq', 1, false);


--
-- Name: pegawai_idpegawai_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pegawai_idpegawai_seq', 1, false);


--
-- Name: produk_idproduk_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produk_idproduk_seq', 1, false);


--
-- Name: spesialis_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.spesialis_id_seq', 1, false);


--
-- Name: transaksi_idtransaksi_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transaksi_idtransaksi_seq', 1, false);


--
-- Name: users_iduser_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_iduser_seq', 2, true);


--
-- Name: kategori kategori_kode_kategori_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kategori
    ADD CONSTRAINT kategori_kode_kategori_key UNIQUE (kode_kategori);


--
-- Name: kategori kategori_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kategori
    ADD CONSTRAINT kategori_pkey PRIMARY KEY (idkategori);


--
-- Name: pegawai pegawai_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pegawai
    ADD CONSTRAINT pegawai_pkey PRIMARY KEY (idpegawai);


--
-- Name: produk produk_kode_kategori_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produk
    ADD CONSTRAINT produk_kode_kategori_key UNIQUE (kode_kategori);


--
-- Name: produk produk_kode_produk_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produk
    ADD CONSTRAINT produk_kode_produk_key UNIQUE (kode_produk);


--
-- Name: produk produk_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produk
    ADD CONSTRAINT produk_pkey PRIMARY KEY (idproduk);


--
-- Name: spesialis spesialis_kode_spesialis_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spesialis
    ADD CONSTRAINT spesialis_kode_spesialis_key UNIQUE (kode_spesialis);


--
-- Name: spesialis spesialis_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spesialis
    ADD CONSTRAINT spesialis_pkey PRIMARY KEY (id);


--
-- Name: transaksi transaksi_kode_transaksi_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_kode_transaksi_key UNIQUE (kode_transaksi);


--
-- Name: transaksi transaksi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_pkey PRIMARY KEY (idtransaksi);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (iduser);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: produk produk_kode_kategori_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produk
    ADD CONSTRAINT produk_kode_kategori_fkey FOREIGN KEY (kode_kategori) REFERENCES public.kategori(kode_kategori);


--
-- Name: transaksi transaksi_spesialis_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_spesialis_fkey FOREIGN KEY (spesialis) REFERENCES public.spesialis(kode_spesialis);


--
-- PostgreSQL database dump complete
--

