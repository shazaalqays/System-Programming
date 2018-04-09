--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.3
-- Dumped by pg_dump version 10.0

-- Started on 2018-04-09 18:41:01

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12387)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2194 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 186 (class 1259 OID 49608)
-- Name: Bolumler; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Bolumler" (
    "Bolum_Kodu" "char"[] NOT NULL,
    "Bolum_Adi" "char"[] NOT NULL
);


ALTER TABLE "Bolumler" OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 49602)
-- Name: Dersler; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Dersler" (
    "Ders_Kodu" "char"[] NOT NULL,
    "Grup_No" integer NOT NULL,
    "Dersin_Adi" "char"[] NOT NULL,
    "Hoca_Kodu" "char"[] NOT NULL
);


ALTER TABLE "Dersler" OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 49616)
-- Name: DerslerDetaylari; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "DerslerDetaylari" (
    "Ders_Kodu" "char"[] NOT NULL,
    "Ders_Adi" "char"[] NOT NULL,
    "Teori" integer NOT NULL,
    "Practice" integer NOT NULL,
    "Lab" integer NOT NULL,
    "Toplam_Kredi" integer NOT NULL,
    "Acan_Bolum_Kodu" "char"[] NOT NULL
);


ALTER TABLE "DerslerDetaylari" OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 49624)
-- Name: Fakulte_Bolum; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Fakulte_Bolum" (
    "Fakulte_Kodu" "char"[] NOT NULL,
    "Bolum_Kodu" "char"[] NOT NULL
);


ALTER TABLE "Fakulte_Bolum" OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 49630)
-- Name: Fakulteler; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Fakulteler" (
    "Fakulte_Kodu" "char"[] NOT NULL,
    "Fakulte_Adi" "char"[] NOT NULL
);


ALTER TABLE "Fakulteler" OWNER TO postgres;

--
-- TOC entry 190 (class 1259 OID 49638)
-- Name: Hocalar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Hocalar" (
    "Hoca_Kodu" "char"[] NOT NULL,
    "Adi" "char"[] NOT NULL,
    "Soyadi" "char"[] NOT NULL,
    "Bolum_Kodu" "char"[] NOT NULL
);


ALTER TABLE "Hocalar" OWNER TO postgres;

--
-- TOC entry 191 (class 1259 OID 49646)
-- Name: Ogrenci_Ders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Ogrenci_Ders" (
    "Ogrenci_No" "char"[] NOT NULL,
    "Ders_Kodu" "char"[] NOT NULL,
    "Grubu" integer NOT NULL
);


ALTER TABLE "Ogrenci_Ders" OWNER TO postgres;

--
-- TOC entry 192 (class 1259 OID 49652)
-- Name: Ogrenciler; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE "Ogrenciler" (
    "Ogrenci_No" "char"[] NOT NULL,
    "Adi" "char"[] NOT NULL,
    "Soyadi" "char"[] NOT NULL,
    "Bolum_Kodu" "char"[] NOT NULL
);


ALTER TABLE "Ogrenciler" OWNER TO postgres;

--
-- TOC entry 2181 (class 0 OID 49608)
-- Dependencies: 186
-- Data for Name: Bolumler; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Bolumler" ("Bolum_Kodu", "Bolum_Adi") FROM stdin;
\.


--
-- TOC entry 2180 (class 0 OID 49602)
-- Dependencies: 185
-- Data for Name: Dersler; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Dersler" ("Ders_Kodu", "Grup_No", "Dersin_Adi", "Hoca_Kodu") FROM stdin;
\.


--
-- TOC entry 2182 (class 0 OID 49616)
-- Dependencies: 187
-- Data for Name: DerslerDetaylari; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "DerslerDetaylari" ("Ders_Kodu", "Ders_Adi", "Teori", "Practice", "Lab", "Toplam_Kredi", "Acan_Bolum_Kodu") FROM stdin;
\.


--
-- TOC entry 2183 (class 0 OID 49624)
-- Dependencies: 188
-- Data for Name: Fakulte_Bolum; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Fakulte_Bolum" ("Fakulte_Kodu", "Bolum_Kodu") FROM stdin;
\.


--
-- TOC entry 2184 (class 0 OID 49630)
-- Dependencies: 189
-- Data for Name: Fakulteler; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Fakulteler" ("Fakulte_Kodu", "Fakulte_Adi") FROM stdin;
\.


--
-- TOC entry 2185 (class 0 OID 49638)
-- Dependencies: 190
-- Data for Name: Hocalar; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Hocalar" ("Hoca_Kodu", "Adi", "Soyadi", "Bolum_Kodu") FROM stdin;
\.


--
-- TOC entry 2186 (class 0 OID 49646)
-- Dependencies: 191
-- Data for Name: Ogrenci_Ders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Ogrenci_Ders" ("Ogrenci_No", "Ders_Kodu", "Grubu") FROM stdin;
\.


--
-- TOC entry 2187 (class 0 OID 49652)
-- Dependencies: 192
-- Data for Name: Ogrenciler; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "Ogrenciler" ("Ogrenci_No", "Adi", "Soyadi", "Bolum_Kodu") FROM stdin;
\.


--
-- TOC entry 2038 (class 2606 OID 49615)
-- Name: Bolumler Bolumler_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Bolumler"
    ADD CONSTRAINT "Bolumler_pkey" PRIMARY KEY ("Bolum_Kodu");


--
-- TOC entry 2040 (class 2606 OID 49623)
-- Name: DerslerDetaylari DerslerDetaylari_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "DerslerDetaylari"
    ADD CONSTRAINT "DerslerDetaylari_pkey" PRIMARY KEY ("Ders_Kodu");


--
-- TOC entry 2045 (class 2606 OID 49637)
-- Name: Fakulteler Fakulteler_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Fakulteler"
    ADD CONSTRAINT "Fakulteler_pkey" PRIMARY KEY ("Fakulte_Kodu");


--
-- TOC entry 2047 (class 2606 OID 49645)
-- Name: Hocalar Hocalar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Hocalar"
    ADD CONSTRAINT "Hocalar_pkey" PRIMARY KEY ("Hoca_Kodu");


--
-- TOC entry 2052 (class 2606 OID 49659)
-- Name: Ogrenciler Ogrenciler_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Ogrenciler"
    ADD CONSTRAINT "Ogrenciler_pkey" PRIMARY KEY ("Ogrenci_No");


--
-- TOC entry 2041 (class 1259 OID 49701)
-- Name: fki_DerslerDetaylari_Acan_Bolum_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_DerslerDetaylari_Acan_Bolum_Kodu" ON "DerslerDetaylari" USING btree ("Acan_Bolum_Kodu");


--
-- TOC entry 2035 (class 1259 OID 49707)
-- Name: fki_Dersler_Ders_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Dersler_Ders_Kodu" ON "Dersler" USING btree ("Ders_Kodu");


--
-- TOC entry 2036 (class 1259 OID 49713)
-- Name: fki_Dersler_Hoca_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Dersler_Hoca_Kodu" ON "Dersler" USING btree ("Hoca_Kodu");


--
-- TOC entry 2042 (class 1259 OID 49689)
-- Name: fki_Fakulte_Bolum_Bolum_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Fakulte_Bolum_Bolum_Kodu" ON "Fakulte_Bolum" USING btree ("Bolum_Kodu");


--
-- TOC entry 2043 (class 1259 OID 49683)
-- Name: fki_Fakulte_Bolum_Fakulte_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Fakulte_Bolum_Fakulte_Kodu" ON "Fakulte_Bolum" USING btree ("Fakulte_Kodu");


--
-- TOC entry 2048 (class 1259 OID 49665)
-- Name: fki_Hocalar_Bolum_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Hocalar_Bolum_Kodu" ON "Hocalar" USING btree ("Bolum_Kodu");


--
-- TOC entry 2049 (class 1259 OID 49695)
-- Name: fki_Ogrenci_Ders_Ders_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Ogrenci_Ders_Ders_Kodu" ON "Ogrenci_Ders" USING btree ("Ders_Kodu");


--
-- TOC entry 2050 (class 1259 OID 49677)
-- Name: fki_Ogrenci_Ders_Ogrenci_No; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Ogrenci_Ders_Ogrenci_No" ON "Ogrenci_Ders" USING btree ("Ogrenci_No");


--
-- TOC entry 2053 (class 1259 OID 49671)
-- Name: fki_Ogrenciler_Bolum_Kodu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_Ogrenciler_Bolum_Kodu" ON "Ogrenciler" USING btree ("Bolum_Kodu");


--
-- TOC entry 2056 (class 2606 OID 49696)
-- Name: DerslerDetaylari DerslerDetaylari_Acan_Bolum_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "DerslerDetaylari"
    ADD CONSTRAINT "DerslerDetaylari_Acan_Bolum_Kodu" FOREIGN KEY ("Acan_Bolum_Kodu") REFERENCES "Bolumler"("Bolum_Kodu");


--
-- TOC entry 2054 (class 2606 OID 49702)
-- Name: Dersler Dersler_Ders_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Dersler"
    ADD CONSTRAINT "Dersler_Ders_Kodu" FOREIGN KEY ("Ders_Kodu") REFERENCES "DerslerDetaylari"("Ders_Kodu");


--
-- TOC entry 2055 (class 2606 OID 49708)
-- Name: Dersler Dersler_Hoca_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Dersler"
    ADD CONSTRAINT "Dersler_Hoca_Kodu" FOREIGN KEY ("Hoca_Kodu") REFERENCES "Hocalar"("Hoca_Kodu");


--
-- TOC entry 2058 (class 2606 OID 49684)
-- Name: Fakulte_Bolum Fakulte_Bolum_Bolum_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Fakulte_Bolum"
    ADD CONSTRAINT "Fakulte_Bolum_Bolum_Kodu" FOREIGN KEY ("Bolum_Kodu") REFERENCES "Bolumler"("Bolum_Kodu");


--
-- TOC entry 2057 (class 2606 OID 49678)
-- Name: Fakulte_Bolum Fakulte_Bolum_Fakulte_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Fakulte_Bolum"
    ADD CONSTRAINT "Fakulte_Bolum_Fakulte_Kodu" FOREIGN KEY ("Fakulte_Kodu") REFERENCES "Fakulteler"("Fakulte_Kodu");


--
-- TOC entry 2059 (class 2606 OID 49660)
-- Name: Hocalar Hocalar_Bolum_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Hocalar"
    ADD CONSTRAINT "Hocalar_Bolum_Kodu" FOREIGN KEY ("Bolum_Kodu") REFERENCES "Bolumler"("Bolum_Kodu");


--
-- TOC entry 2061 (class 2606 OID 49690)
-- Name: Ogrenci_Ders Ogrenci_Ders_Ders_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Ogrenci_Ders"
    ADD CONSTRAINT "Ogrenci_Ders_Ders_Kodu" FOREIGN KEY ("Ders_Kodu") REFERENCES "DerslerDetaylari"("Ders_Kodu");


--
-- TOC entry 2060 (class 2606 OID 49672)
-- Name: Ogrenci_Ders Ogrenci_Ders_Ogrenci_No; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Ogrenci_Ders"
    ADD CONSTRAINT "Ogrenci_Ders_Ogrenci_No" FOREIGN KEY ("Ogrenci_No") REFERENCES "Ogrenciler"("Ogrenci_No");


--
-- TOC entry 2062 (class 2606 OID 49666)
-- Name: Ogrenciler Ogrenciler_Bolum_Kodu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Ogrenciler"
    ADD CONSTRAINT "Ogrenciler_Bolum_Kodu" FOREIGN KEY ("Bolum_Kodu") REFERENCES "Bolumler"("Bolum_Kodu");


-- Completed on 2018-04-09 18:41:01

--
-- PostgreSQL database dump complete
--

