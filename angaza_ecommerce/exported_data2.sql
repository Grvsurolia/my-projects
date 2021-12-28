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
-- Name: Admin User; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Admin User" (
    id bigint NOT NULL,
    status boolean NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public."Admin User" OWNER TO angaza;

--
-- Name: Admin User_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Admin User_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Admin User_id_seq" OWNER TO angaza;

--
-- Name: Admin User_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Admin User_id_seq" OWNED BY public."Admin User".id;


--
-- Name: Bill; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Bill" (
    id bigint NOT NULL,
    discount_price double precision NOT NULL,
    "MRP_price" double precision NOT NULL,
    total_price double precision NOT NULL,
    status boolean NOT NULL,
    customer_id bigint NOT NULL,
    order_product_id bigint NOT NULL
);


ALTER TABLE public."Bill" OWNER TO angaza;

--
-- Name: Bill_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Bill_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Bill_id_seq" OWNER TO angaza;

--
-- Name: Bill_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Bill_id_seq" OWNED BY public."Bill".id;


--
-- Name: Booking Form; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Booking Form" (
    id bigint NOT NULL,
    email character varying(255),
    mobile_number character varying(13),
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    address character varying(255) NOT NULL,
    apartment character varying(255),
    city character varying(255) NOT NULL,
    postal_code character varying(255) NOT NULL,
    order_id bigint NOT NULL,
    price double precision,
    prod_name character varying(200)
);


ALTER TABLE public."Booking Form" OWNER TO angaza;

--
-- Name: Booking Form_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Booking Form_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Booking Form_id_seq" OWNER TO angaza;

--
-- Name: Booking Form_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Booking Form_id_seq" OWNED BY public."Booking Form".id;


--
-- Name: Brand; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Brand" (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public."Brand" OWNER TO angaza;

--
-- Name: Brand_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Brand_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Brand_id_seq" OWNER TO angaza;

--
-- Name: Brand_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Brand_id_seq" OWNED BY public."Brand".id;


--
-- Name: Cart; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Cart" (
    id bigint NOT NULL,
    quantity integer NOT NULL,
    product_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public."Cart" OWNER TO angaza;

--
-- Name: Cart_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Cart_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Cart_id_seq" OWNER TO angaza;

--
-- Name: Cart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Cart_id_seq" OWNED BY public."Cart".id;


--
-- Name: Category; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Category" (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    icon character varying(100) NOT NULL
);


ALTER TABLE public."Category" OWNER TO angaza;

--
-- Name: Category_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Category_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Category_id_seq" OWNER TO angaza;

--
-- Name: Category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Category_id_seq" OWNED BY public."Category".id;


--
-- Name: Category_subcategory; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Category_subcategory" (
    id integer NOT NULL,
    category_id bigint NOT NULL,
    subcategories_id bigint NOT NULL
);


ALTER TABLE public."Category_subcategory" OWNER TO angaza;

--
-- Name: Category_subcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Category_subcategory_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Category_subcategory_id_seq" OWNER TO angaza;

--
-- Name: Category_subcategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Category_subcategory_id_seq" OWNED BY public."Category_subcategory".id;


--
-- Name: Colour; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Colour" (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    code character varying(50) NOT NULL
);


ALTER TABLE public."Colour" OWNER TO angaza;

--
-- Name: Colour_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Colour_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Colour_id_seq" OWNER TO angaza;

--
-- Name: Colour_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Colour_id_seq" OWNED BY public."Colour".id;


--
-- Name: Contact; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Contact" (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    subject character varying(255) NOT NULL,
    message text NOT NULL
);


ALTER TABLE public."Contact" OWNER TO angaza;

--
-- Name: Contact_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Contact_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Contact_id_seq" OWNER TO angaza;

--
-- Name: Contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Contact_id_seq" OWNED BY public."Contact".id;


--
-- Name: Customer; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Customer" (
    id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public."Customer" OWNER TO angaza;

--
-- Name: Customer Address; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Customer Address" (
    id bigint NOT NULL,
    house_no character varying(50) NOT NULL,
    colony character varying(255) NOT NULL,
    landmark character varying(255) NOT NULL,
    city character varying(255) NOT NULL,
    state character varying(100) NOT NULL,
    country character varying(255) NOT NULL,
    address_type character varying(100) NOT NULL,
    contact_number character varying(15),
    email character varying(255),
    user_id bigint NOT NULL
);


ALTER TABLE public."Customer Address" OWNER TO angaza;

--
-- Name: Customer Address_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Customer Address_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Customer Address_id_seq" OWNER TO angaza;

--
-- Name: Customer Address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Customer Address_id_seq" OWNED BY public."Customer Address".id;


--
-- Name: Customer_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Customer_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Customer_id_seq" OWNER TO angaza;

--
-- Name: Customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Customer_id_seq" OWNED BY public."Customer".id;


--
-- Name: Deal; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Deal" (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    status boolean NOT NULL
);


ALTER TABLE public."Deal" OWNER TO angaza;

--
-- Name: Deal_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Deal_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Deal_id_seq" OWNER TO angaza;

--
-- Name: Deal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Deal_id_seq" OWNED BY public."Deal".id;


--
-- Name: Home Page Advertisement; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Home Page Advertisement" (
    id bigint NOT NULL,
    image_number integer NOT NULL,
    thumbnail character varying(100) NOT NULL,
    url character varying(255) NOT NULL,
    status boolean NOT NULL,
    CONSTRAINT "Home Page Advertisement_image_number_check" CHECK ((image_number >= 0))
);


ALTER TABLE public."Home Page Advertisement" OWNER TO angaza;

--
-- Name: Home Page Advertisement_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Home Page Advertisement_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Home Page Advertisement_id_seq" OWNER TO angaza;

--
-- Name: Home Page Advertisement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Home Page Advertisement_id_seq" OWNED BY public."Home Page Advertisement".id;


--
-- Name: MPayment; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."MPayment" (
    id bigint NOT NULL,
    "BusinessShortCode" integer NOT NULL,
    "Password" character varying(255) NOT NULL,
    "Timestamp" character varying(255) NOT NULL,
    "TransactionType" character varying(255) NOT NULL,
    "Amount" integer NOT NULL,
    "PartyA" integer NOT NULL,
    "PartyB" integer NOT NULL,
    "PhoneNumber" integer NOT NULL,
    "CallBackURL" character varying(200) NOT NULL,
    "AccountReference" character varying(255) NOT NULL,
    description text NOT NULL,
    order_id bigint NOT NULL
);


ALTER TABLE public."MPayment" OWNER TO angaza;

--
-- Name: MPayment_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."MPayment_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."MPayment_id_seq" OWNER TO angaza;

--
-- Name: MPayment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."MPayment_id_seq" OWNED BY public."MPayment".id;


--
-- Name: Notification; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Notification" (
    id bigint NOT NULL,
    created_date timestamp with time zone NOT NULL,
    title text NOT NULL,
    category character varying(255) NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public."Notification" OWNER TO angaza;

--
-- Name: Notification_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Notification_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Notification_id_seq" OWNER TO angaza;

--
-- Name: Notification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Notification_id_seq" OWNED BY public."Notification".id;


--
-- Name: Order; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Order" (
    id bigint NOT NULL,
    ordered_date date NOT NULL,
    delivered_date date,
    being_delivered boolean NOT NULL,
    order_cancel boolean NOT NULL,
    status character varying(255),
    buy boolean NOT NULL,
    booking boolean NOT NULL,
    customer_id bigint NOT NULL
);


ALTER TABLE public."Order" OWNER TO angaza;

--
-- Name: Order Product; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Order Product" (
    id bigint NOT NULL,
    quantity integer NOT NULL,
    status character varying(255),
    order_id bigint NOT NULL,
    product_id bigint NOT NULL,
    CONSTRAINT "Order Product_quantity_check" CHECK ((quantity >= 0))
);


ALTER TABLE public."Order Product" OWNER TO angaza;

--
-- Name: Order Product_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Order Product_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Order Product_id_seq" OWNER TO angaza;

--
-- Name: Order Product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Order Product_id_seq" OWNED BY public."Order Product".id;


--
-- Name: Order_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Order_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Order_id_seq" OWNER TO angaza;

--
-- Name: Order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Order_id_seq" OWNED BY public."Order".id;


--
-- Name: Product; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Product" (
    id bigint NOT NULL,
    title character varying(255) NOT NULL,
    price double precision NOT NULL,
    sale_price double precision NOT NULL,
    description text NOT NULL,
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    sku character varying(255) NOT NULL,
    thumbnail character varying(100) NOT NULL,
    depot integer NOT NULL,
    is_sale boolean NOT NULL,
    inventory integer NOT NULL,
    discount_percent double precision NOT NULL,
    product_option character varying(255) NOT NULL,
    visit_product integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    brand_id bigint,
    store_id bigint NOT NULL,
    price_type character varying(150),
    CONSTRAINT "Product_visit_product_check" CHECK ((visit_product >= 0))
);


ALTER TABLE public."Product" OWNER TO angaza;

--
-- Name: ProductCategory; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductCategory" (
    id bigint NOT NULL,
    product_id bigint NOT NULL,
    product_category_id bigint NOT NULL,
    product_sub_category_id bigint
);


ALTER TABLE public."ProductCategory" OWNER TO angaza;

--
-- Name: ProductCategory_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductCategory_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductCategory_id_seq" OWNER TO angaza;

--
-- Name: ProductCategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductCategory_id_seq" OWNED BY public."ProductCategory".id;


--
-- Name: ProductColour; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductColour" (
    id bigint NOT NULL,
    product_id bigint NOT NULL,
    product_color_id bigint NOT NULL
);


ALTER TABLE public."ProductColour" OWNER TO angaza;

--
-- Name: ProductColour_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductColour_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductColour_id_seq" OWNER TO angaza;

--
-- Name: ProductColour_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductColour_id_seq" OWNED BY public."ProductColour".id;


--
-- Name: ProductDeal; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductDeal" (
    id bigint NOT NULL,
    status boolean NOT NULL,
    product_id bigint NOT NULL,
    product_deals_id bigint NOT NULL
);


ALTER TABLE public."ProductDeal" OWNER TO angaza;

--
-- Name: ProductDeal_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductDeal_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductDeal_id_seq" OWNER TO angaza;

--
-- Name: ProductDeal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductDeal_id_seq" OWNED BY public."ProductDeal".id;


--
-- Name: ProductDescription; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductDescription" (
    id bigint NOT NULL,
    title character varying(255) NOT NULL,
    description text,
    thumbnail character varying(100),
    product_id bigint NOT NULL
);


ALTER TABLE public."ProductDescription" OWNER TO angaza;

--
-- Name: ProductDescription_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductDescription_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductDescription_id_seq" OWNER TO angaza;

--
-- Name: ProductDescription_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductDescription_id_seq" OWNED BY public."ProductDescription".id;


--
-- Name: ProductImage; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductImage" (
    id bigint NOT NULL,
    product_image1 character varying(100) NOT NULL,
    product_image2 character varying(100),
    product_image3 character varying(100),
    product_image4 character varying(100),
    product_id bigint NOT NULL
);


ALTER TABLE public."ProductImage" OWNER TO angaza;

--
-- Name: ProductImage_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductImage_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductImage_id_seq" OWNER TO angaza;

--
-- Name: ProductImage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductImage_id_seq" OWNED BY public."ProductImage".id;


--
-- Name: ProductQuestion; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductQuestion" (
    id bigint NOT NULL,
    question character varying(255) NOT NULL,
    answer text NOT NULL,
    product_id bigint NOT NULL,
    user_id bigint
);


ALTER TABLE public."ProductQuestion" OWNER TO angaza;

--
-- Name: ProductQuestion_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductQuestion_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductQuestion_id_seq" OWNER TO angaza;

--
-- Name: ProductQuestion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductQuestion_id_seq" OWNED BY public."ProductQuestion".id;


--
-- Name: ProductReview; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductReview" (
    id bigint NOT NULL,
    feedback text NOT NULL,
    star_point integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(254) NOT NULL,
    deal_id bigint NOT NULL,
    CONSTRAINT "ProductReview_star_point_check" CHECK ((star_point >= 0))
);


ALTER TABLE public."ProductReview" OWNER TO angaza;

--
-- Name: ProductReview_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductReview_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductReview_id_seq" OWNER TO angaza;

--
-- Name: ProductReview_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductReview_id_seq" OWNED BY public."ProductReview".id;


--
-- Name: ProductSize; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductSize" (
    id bigint NOT NULL,
    product_id bigint NOT NULL,
    product_size_id bigint NOT NULL
);


ALTER TABLE public."ProductSize" OWNER TO angaza;

--
-- Name: ProductSize_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductSize_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductSize_id_seq" OWNER TO angaza;

--
-- Name: ProductSize_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductSize_id_seq" OWNED BY public."ProductSize".id;


--
-- Name: ProductSpecification; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."ProductSpecification" (
    id bigint NOT NULL,
    the_json jsonb NOT NULL,
    product_id bigint NOT NULL
);


ALTER TABLE public."ProductSpecification" OWNER TO angaza;

--
-- Name: ProductSpecification_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."ProductSpecification_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ProductSpecification_id_seq" OWNER TO angaza;

--
-- Name: ProductSpecification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."ProductSpecification_id_seq" OWNED BY public."ProductSpecification".id;


--
-- Name: Product_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Product_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Product_id_seq" OWNER TO angaza;

--
-- Name: Product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Product_id_seq" OWNED BY public."Product".id;


--
-- Name: Product_sub_product; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Product_sub_product" (
    id integer NOT NULL,
    product_id bigint NOT NULL,
    subproduct_id bigint NOT NULL
);


ALTER TABLE public."Product_sub_product" OWNER TO angaza;

--
-- Name: Product_sub_product_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Product_sub_product_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Product_sub_product_id_seq" OWNER TO angaza;

--
-- Name: Product_sub_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Product_sub_product_id_seq" OWNED BY public."Product_sub_product".id;


--
-- Name: Product_tags; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Product_tags" (
    id integer NOT NULL,
    product_id bigint NOT NULL,
    tag_id bigint NOT NULL
);


ALTER TABLE public."Product_tags" OWNER TO angaza;

--
-- Name: Product_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Product_tags_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Product_tags_id_seq" OWNER TO angaza;

--
-- Name: Product_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Product_tags_id_seq" OWNED BY public."Product_tags".id;


--
-- Name: Size; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Size" (
    id bigint NOT NULL,
    size_or_weight character varying(10) NOT NULL
);


ALTER TABLE public."Size" OWNER TO angaza;

--
-- Name: Size_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Size_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Size_id_seq" OWNER TO angaza;

--
-- Name: Size_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Size_id_seq" OWNED BY public."Size".id;


--
-- Name: Slider; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Slider" (
    id bigint NOT NULL,
    image character varying(100) NOT NULL,
    url character varying(255)
);


ALTER TABLE public."Slider" OWNER TO angaza;

--
-- Name: Slider_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Slider_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Slider_id_seq" OWNER TO angaza;

--
-- Name: Slider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Slider_id_seq" OWNED BY public."Slider".id;


--
-- Name: Store; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Store" (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    mobile_number character varying(13) NOT NULL,
    website character varying(255),
    location character varying(255) NOT NULL,
    thumbnail character varying(100) NOT NULL,
    describe text NOT NULL,
    store_portal_admin character varying(255) NOT NULL,
    status boolean NOT NULL,
    owner_id bigint NOT NULL
);


ALTER TABLE public."Store" OWNER TO angaza;

--
-- Name: StoreOwner; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."StoreOwner" (
    id bigint NOT NULL,
    status boolean NOT NULL,
    store_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public."StoreOwner" OWNER TO angaza;

--
-- Name: StoreOwner_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."StoreOwner_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."StoreOwner_id_seq" OWNER TO angaza;

--
-- Name: StoreOwner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."StoreOwner_id_seq" OWNED BY public."StoreOwner".id;


--
-- Name: Store_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Store_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Store_id_seq" OWNER TO angaza;

--
-- Name: Store_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Store_id_seq" OWNED BY public."Store".id;


--
-- Name: Sub Category; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Sub Category" (
    id bigint NOT NULL,
    sub_name character varying(255) NOT NULL
);


ALTER TABLE public."Sub Category" OWNER TO angaza;

--
-- Name: Sub Category_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Sub Category_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Sub Category_id_seq" OWNER TO angaza;

--
-- Name: Sub Category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Sub Category_id_seq" OWNED BY public."Sub Category".id;


--
-- Name: Subscribe; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Subscribe" (
    id bigint NOT NULL,
    email character varying(255) NOT NULL
);


ALTER TABLE public."Subscribe" OWNER TO angaza;

--
-- Name: Subscribe_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Subscribe_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Subscribe_id_seq" OWNER TO angaza;

--
-- Name: Subscribe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Subscribe_id_seq" OWNED BY public."Subscribe".id;


--
-- Name: Tag; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."Tag" (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public."Tag" OWNER TO angaza;

--
-- Name: Tag_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."Tag_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Tag_id_seq" OWNER TO angaza;

--
-- Name: Tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."Tag_id_seq" OWNED BY public."Tag".id;


--
-- Name: User; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."User" (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    is_staff boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    email character varying(255) NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    phone_number character varying(12),
    profile_image character varying(100) NOT NULL,
    "lastEmailOtp" character varying(255) NOT NULL,
    passsword character varying(30) NOT NULL,
    role smallint,
    is_active boolean NOT NULL,
    CONSTRAINT "User_role_check" CHECK ((role >= 0))
);


ALTER TABLE public."User" OWNER TO angaza;

--
-- Name: User_groups; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."User_groups" (
    id integer NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public."User_groups" OWNER TO angaza;

--
-- Name: User_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."User_groups_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."User_groups_id_seq" OWNER TO angaza;

--
-- Name: User_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."User_groups_id_seq" OWNED BY public."User_groups".id;


--
-- Name: User_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."User_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."User_id_seq" OWNER TO angaza;

--
-- Name: User_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."User_id_seq" OWNED BY public."User".id;


--
-- Name: User_user_permissions; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."User_user_permissions" (
    id integer NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public."User_user_permissions" OWNER TO angaza;

--
-- Name: User_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."User_user_permissions_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."User_user_permissions_id_seq" OWNER TO angaza;

--
-- Name: User_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."User_user_permissions_id_seq" OWNED BY public."User_user_permissions".id;


--
-- Name: WishList; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public."WishList" (
    id bigint NOT NULL,
    is_delete boolean NOT NULL,
    product_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public."WishList" OWNER TO angaza;

--
-- Name: WishList_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public."WishList_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."WishList_id_seq" OWNER TO angaza;

--
-- Name: WishList_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public."WishList_id_seq" OWNED BY public."WishList".id;


--
-- Name: admin_user_detailpagesadvertisement; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.admin_user_detailpagesadvertisement (
    id bigint NOT NULL,
    thumbnail character varying(100) NOT NULL,
    url character varying(255) NOT NULL,
    status boolean NOT NULL
);


ALTER TABLE public.admin_user_detailpagesadvertisement OWNER TO angaza;

--
-- Name: admin_user_detailpagesadvertisement_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.admin_user_detailpagesadvertisement_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admin_user_detailpagesadvertisement_id_seq OWNER TO angaza;

--
-- Name: admin_user_detailpagesadvertisement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.admin_user_detailpagesadvertisement_id_seq OWNED BY public.admin_user_detailpagesadvertisement.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO angaza;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO angaza;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO angaza;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO angaza;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO angaza;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO angaza;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO angaza;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO angaza;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO angaza;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO angaza;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO angaza;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO angaza;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO angaza;

--
-- Name: order_bill; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.order_bill (
    id bigint NOT NULL,
    discount_price double precision NOT NULL,
    "MRP_price" double precision NOT NULL,
    total_price double precision NOT NULL,
    status boolean NOT NULL,
    customer_id bigint NOT NULL,
    order_id bigint NOT NULL
);


ALTER TABLE public.order_bill OWNER TO angaza;

--
-- Name: order_bill_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.order_bill_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_bill_id_seq OWNER TO angaza;

--
-- Name: order_bill_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.order_bill_id_seq OWNED BY public.order_bill.id;


--
-- Name: product_specification; Type: TABLE; Schema: public; Owner: angaza
--

CREATE TABLE public.product_specification (
    id bigint NOT NULL,
    color character varying(100) NOT NULL,
    size character varying(100) NOT NULL,
    weight character varying(100) NOT NULL,
    bluetooth boolean NOT NULL,
    battery_life character varying(100) NOT NULL,
    wireless boolean NOT NULL,
    product_id bigint NOT NULL
);


ALTER TABLE public.product_specification OWNER TO angaza;

--
-- Name: product_specification_id_seq; Type: SEQUENCE; Schema: public; Owner: angaza
--

CREATE SEQUENCE public.product_specification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_specification_id_seq OWNER TO angaza;

--
-- Name: product_specification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: angaza
--

ALTER SEQUENCE public.product_specification_id_seq OWNED BY public.product_specification.id;


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
-- Name: Admin User id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Admin User" ALTER COLUMN id SET DEFAULT nextval('public."Admin User_id_seq"'::regclass);


--
-- Name: Bill id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Bill" ALTER COLUMN id SET DEFAULT nextval('public."Bill_id_seq"'::regclass);


--
-- Name: Booking Form id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Booking Form" ALTER COLUMN id SET DEFAULT nextval('public."Booking Form_id_seq"'::regclass);


--
-- Name: Brand id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Brand" ALTER COLUMN id SET DEFAULT nextval('public."Brand_id_seq"'::regclass);


--
-- Name: Cart id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Cart" ALTER COLUMN id SET DEFAULT nextval('public."Cart_id_seq"'::regclass);


--
-- Name: Category id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Category" ALTER COLUMN id SET DEFAULT nextval('public."Category_id_seq"'::regclass);


--
-- Name: Category_subcategory id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Category_subcategory" ALTER COLUMN id SET DEFAULT nextval('public."Category_subcategory_id_seq"'::regclass);


--
-- Name: Colour id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Colour" ALTER COLUMN id SET DEFAULT nextval('public."Colour_id_seq"'::regclass);


--
-- Name: Contact id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Contact" ALTER COLUMN id SET DEFAULT nextval('public."Contact_id_seq"'::regclass);


--
-- Name: Customer id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Customer" ALTER COLUMN id SET DEFAULT nextval('public."Customer_id_seq"'::regclass);


--
-- Name: Customer Address id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Customer Address" ALTER COLUMN id SET DEFAULT nextval('public."Customer Address_id_seq"'::regclass);


--
-- Name: Deal id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Deal" ALTER COLUMN id SET DEFAULT nextval('public."Deal_id_seq"'::regclass);


--
-- Name: Home Page Advertisement id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Home Page Advertisement" ALTER COLUMN id SET DEFAULT nextval('public."Home Page Advertisement_id_seq"'::regclass);


--
-- Name: MPayment id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."MPayment" ALTER COLUMN id SET DEFAULT nextval('public."MPayment_id_seq"'::regclass);


--
-- Name: Notification id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Notification" ALTER COLUMN id SET DEFAULT nextval('public."Notification_id_seq"'::regclass);


--
-- Name: Order id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Order" ALTER COLUMN id SET DEFAULT nextval('public."Order_id_seq"'::regclass);


--
-- Name: Order Product id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Order Product" ALTER COLUMN id SET DEFAULT nextval('public."Order Product_id_seq"'::regclass);


--
-- Name: Product id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product" ALTER COLUMN id SET DEFAULT nextval('public."Product_id_seq"'::regclass);


--
-- Name: ProductCategory id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductCategory" ALTER COLUMN id SET DEFAULT nextval('public."ProductCategory_id_seq"'::regclass);


--
-- Name: ProductColour id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductColour" ALTER COLUMN id SET DEFAULT nextval('public."ProductColour_id_seq"'::regclass);


--
-- Name: ProductDeal id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductDeal" ALTER COLUMN id SET DEFAULT nextval('public."ProductDeal_id_seq"'::regclass);


--
-- Name: ProductDescription id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductDescription" ALTER COLUMN id SET DEFAULT nextval('public."ProductDescription_id_seq"'::regclass);


--
-- Name: ProductImage id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductImage" ALTER COLUMN id SET DEFAULT nextval('public."ProductImage_id_seq"'::regclass);


--
-- Name: ProductQuestion id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductQuestion" ALTER COLUMN id SET DEFAULT nextval('public."ProductQuestion_id_seq"'::regclass);


--
-- Name: ProductReview id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductReview" ALTER COLUMN id SET DEFAULT nextval('public."ProductReview_id_seq"'::regclass);


--
-- Name: ProductSize id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSize" ALTER COLUMN id SET DEFAULT nextval('public."ProductSize_id_seq"'::regclass);


--
-- Name: ProductSpecification id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSpecification" ALTER COLUMN id SET DEFAULT nextval('public."ProductSpecification_id_seq"'::regclass);


--
-- Name: Product_sub_product id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_sub_product" ALTER COLUMN id SET DEFAULT nextval('public."Product_sub_product_id_seq"'::regclass);


--
-- Name: Product_tags id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_tags" ALTER COLUMN id SET DEFAULT nextval('public."Product_tags_id_seq"'::regclass);


--
-- Name: Size id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Size" ALTER COLUMN id SET DEFAULT nextval('public."Size_id_seq"'::regclass);


--
-- Name: Slider id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Slider" ALTER COLUMN id SET DEFAULT nextval('public."Slider_id_seq"'::regclass);


--
-- Name: Store id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Store" ALTER COLUMN id SET DEFAULT nextval('public."Store_id_seq"'::regclass);


--
-- Name: StoreOwner id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."StoreOwner" ALTER COLUMN id SET DEFAULT nextval('public."StoreOwner_id_seq"'::regclass);


--
-- Name: Sub Category id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Sub Category" ALTER COLUMN id SET DEFAULT nextval('public."Sub Category_id_seq"'::regclass);


--
-- Name: Subscribe id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Subscribe" ALTER COLUMN id SET DEFAULT nextval('public."Subscribe_id_seq"'::regclass);


--
-- Name: Tag id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Tag" ALTER COLUMN id SET DEFAULT nextval('public."Tag_id_seq"'::regclass);


--
-- Name: User id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User" ALTER COLUMN id SET DEFAULT nextval('public."User_id_seq"'::regclass);


--
-- Name: User_groups id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_groups" ALTER COLUMN id SET DEFAULT nextval('public."User_groups_id_seq"'::regclass);


--
-- Name: User_user_permissions id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_user_permissions" ALTER COLUMN id SET DEFAULT nextval('public."User_user_permissions_id_seq"'::regclass);


--
-- Name: WishList id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."WishList" ALTER COLUMN id SET DEFAULT nextval('public."WishList_id_seq"'::regclass);


--
-- Name: admin_user_detailpagesadvertisement id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.admin_user_detailpagesadvertisement ALTER COLUMN id SET DEFAULT nextval('public.admin_user_detailpagesadvertisement_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: order_bill id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.order_bill ALTER COLUMN id SET DEFAULT nextval('public.order_bill_id_seq'::regclass);


--
-- Name: product_specification id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.product_specification ALTER COLUMN id SET DEFAULT nextval('public.product_specification_id_seq'::regclass);


--
-- Name: product_subproduct id; Type: DEFAULT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.product_subproduct ALTER COLUMN id SET DEFAULT nextval('public.product_subproduct_id_seq'::regclass);


--
-- Data for Name: Admin User; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Admin User" (id, status, user_id) FROM stdin;
\.


--
-- Data for Name: Bill; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Bill" (id, discount_price, "MRP_price", total_price, status, customer_id, order_product_id) FROM stdin;
1	213.75	1425	1211.25	t	1	1
2	213.75	1425	1211.25	t	1	2
3	213.75	1425	1211.25	t	1	3
4	213.75	1425	1211.25	t	1	4
5	213.75	1425	1211.25	t	1	5
6	213.75	1425	1211.25	t	1	6
7	213.75	1425	1211.25	t	1	7
8	50	500	450	t	1	8
9	50	500	450	t	1	9
10	50	500	450	t	1	10
11	0	0	0	t	1	11
12	213.75	1425	1211.25	t	1	12
13	213.75	1425	1211.25	t	1	13
14	150	1500	1350	t	1	14
15	0	0	0	t	1	15
16	0	0	0	t	1	16
17	0	0	0	t	1	17
18	0	0	0	t	1	18
19	0	0	0	t	1	19
20	213.75	1425	1211.25	t	1	20
21	213.75	1425	1211.25	t	1	21
22	213.75	1425	1211.25	t	1	22
23	213.75	1425	1211.25	t	1	23
24	0	0	0	t	1	24
25	0	0	0	t	1	25
26	0	0	0	t	1	26
27	0	0	0	t	1	27
28	0	0	0	t	1	28
37	25000	25000	0	t	1	37
38	0	0	0	t	1	38
39	0	0	0	t	1	39
\.


--
-- Data for Name: Booking Form; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Booking Form" (id, email, mobile_number, first_name, last_name, address, apartment, city, postal_code, order_id, price, prod_name) FROM stdin;
1	shuklaanurag249@gmail.com	\N	Anurag	Shukla	Ho no 5 Durga chowk talliya		Bhopal	462001	13	0	\N
2	shukla@gmail.com	\N	Anurag	vdsvfs	ffvvxc	fxfxcvxc	fxcvxc	123456	23	50	Monthly Bill
3	shukla@gmail.com	\N	Anurag	DShukla	cvxzvxc	cxvcxvxc	dvx	123456	27	100	newcardio
4	shik@gmail.com	\N	dfdsfs	dfds	dcdsf	CVCXV	DFDSF	123456	29	0	Cardio
5	SHUKLA@GMAIL.COM	\N	anURAB	sHUKLA	ADASDSA	CDFSDFS	SDFDSF	12346	31	50	Monthly Bill
6	shukla@gmail.com	\N	dadfdf	dfdsfds	dfsdds	fdgfd	dsfs	123345	32	50	Monthly Bill
\.


--
-- Data for Name: Brand; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Brand" (id, name, user_id) FROM stdin;
1	zara	2
2	test	1
3	Dell	1
\.


--
-- Data for Name: Cart; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Cart" (id, quantity, product_id, user_id) FROM stdin;
\.


--
-- Data for Name: Category; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Category" (id, name, icon) FROM stdin;
\.


--
-- Data for Name: Category_subcategory; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Category_subcategory" (id, category_id, subcategories_id) FROM stdin;
\.


--
-- Data for Name: Colour; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Colour" (id, name, code) FROM stdin;
1	Red	#0000
\.


--
-- Data for Name: Contact; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Contact" (id, name, email, subject, message) FROM stdin;
\.


--
-- Data for Name: Customer; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Customer" (id, user_id) FROM stdin;
1	2
\.


--
-- Data for Name: Customer Address; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Customer Address" (id, house_no, colony, landmark, city, state, country, address_type, contact_number, email, user_id) FROM stdin;
\.


--
-- Data for Name: Deal; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Deal" (id, name, status) FROM stdin;
1	FeatureDeal	t
\.


--
-- Data for Name: Home Page Advertisement; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Home Page Advertisement" (id, image_number, thumbnail, url, status) FROM stdin;
\.


--
-- Data for Name: MPayment; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."MPayment" (id, "BusinessShortCode", "Password", "Timestamp", "TransactionType", "Amount", "PartyA", "PartyB", "PhoneNumber", "CallBackURL", "AccountReference", description, order_id) FROM stdin;
\.


--
-- Data for Name: Notification; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Notification" (id, created_date, title, category, user_id) FROM stdin;
1	2021-10-12 12:41:41.406519+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
2	2021-10-12 12:41:46.405151+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
3	2021-10-12 12:41:46.40976+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
4	2021-10-12 12:41:46.545421+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
5	2021-10-12 12:41:46.984887+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
6	2021-10-12 12:41:47.092458+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
7	2021-10-12 12:41:48.540758+05:30	You have order ['test'] successfully	purchase	1
8	2021-10-12 12:41:48.981901+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
9	2021-10-12 12:41:49.97617+05:30	You have order ['test'] successfully	purchase	1
10	2021-10-12 12:41:50.001028+05:30	You have order ['test'] successfully	purchase	1
11	2021-10-12 12:41:51.547404+05:30	You have order ['test'] successfully	purchase	1
12	2021-10-12 12:41:54.331944+05:30	You have order ['test'] successfully	purchase	1
13	2021-10-12 12:41:56.299227+05:30	You have order ['test'] successfully	purchase	1
14	2021-10-12 12:41:57.230953+05:30	You have order ['test'] successfully	purchase	1
15	2021-10-12 15:21:04.01444+05:30	You have recieved a new order test product quality 1 From admin@gmail.com	sale	1
16	2021-10-12 15:21:07.702942+05:30	You have recieved a new order test product quality 1 From admin@gmail.com	sale	1
17	2021-10-12 15:21:07.703638+05:30	You have recieved a new order test product quality 1 From admin@gmail.com	sale	1
18	2021-10-12 15:21:10.30565+05:30	You have order ['test product'] successfully	purchase	1
19	2021-10-12 15:21:11.641251+05:30	You have order ['test product'] successfully	purchase	1
20	2021-10-12 15:21:11.642886+05:30	You have order ['test product'] successfully	purchase	1
21	2021-10-12 15:25:59.619522+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
22	2021-10-12 15:26:05.996795+05:30	You have order ['new product'] successfully	purchase	1
23	2021-10-12 16:21:20.468778+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
24	2021-10-12 16:21:26.105596+05:30	You have order ['test'] successfully	purchase	1
25	2021-10-12 16:27:58.580751+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
26	2021-10-12 16:28:07.179788+05:30	You have order ['test'] successfully	purchase	1
27	2021-10-12 16:29:03.913594+05:30	You have recieved a new order test product quality 3 From admin@gmail.com	sale	1
28	2021-10-12 16:29:09.521501+05:30	You have order ['test product'] successfully	purchase	1
29	2021-10-13 09:43:22.484151+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
30	2021-10-13 09:43:24.607423+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
31	2021-10-13 09:43:24.612084+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
32	2021-10-13 09:43:24.685576+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
33	2021-10-13 09:43:29.453287+05:30	You have order ['new product'] successfully	purchase	1
34	2021-10-13 09:43:29.454406+05:30	You have order ['new product'] successfully	purchase	1
35	2021-10-13 09:43:29.455465+05:30	You have order ['new product'] successfully	purchase	1
36	2021-10-13 09:43:29.456685+05:30	You have order ['new product'] successfully	purchase	1
37	2021-10-13 09:45:58.419556+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
38	2021-10-13 09:46:04.980038+05:30	You have order ['new product'] successfully	purchase	1
39	2021-10-13 09:48:43.321713+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
40	2021-10-13 09:48:47.367765+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
41	2021-10-13 09:48:49.492041+05:30	You have order ['test'] successfully	purchase	1
42	2021-10-13 09:48:50.178449+05:30	You have order ['test'] successfully	purchase	1
43	2021-10-13 09:51:09.663531+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
44	2021-10-13 09:51:16.936211+05:30	You have order ['test'] successfully	purchase	1
45	2021-10-13 09:55:58.29621+05:30	You have recieved a new order test quality 1 From admin@gmail.com	sale	1
46	2021-10-13 09:56:04.169354+05:30	You have order ['test'] successfully	purchase	1
47	2021-10-13 10:27:05.017105+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
48	2021-10-13 10:27:18.226766+05:30	You have order ['new product'] successfully	purchase	1
49	2021-10-13 10:30:40.493607+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
50	2021-10-13 10:30:49.558378+05:30	You have order ['new product'] successfully	purchase	1
51	2021-10-13 10:32:19.900581+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
52	2021-10-13 10:32:29.350911+05:30	You have order ['new product'] successfully	purchase	1
53	2021-10-13 10:34:16.042949+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
54	2021-10-13 10:34:26.119877+05:30	You have order ['new product'] successfully	purchase	1
55	2021-10-13 14:41:55.147367+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
56	2021-10-13 14:42:02.96954+05:30	You have order ['new product'] successfully	purchase	1
57	2021-10-13 15:09:36.005373+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
58	2021-10-13 15:09:41.795058+05:30	You have order ['Mobile'] successfully	purchase	1
59	2021-10-13 15:11:21.23358+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
60	2021-10-13 15:11:26.525149+05:30	You have order ['Mobile'] successfully	purchase	1
61	2021-10-13 15:11:39.925607+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
62	2021-10-13 15:11:45.941077+05:30	You have order ['Mobile'] successfully	purchase	1
63	2021-10-13 15:14:55.576529+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
64	2021-10-13 15:15:01.611974+05:30	You have order ['Mobile'] successfully	purchase	1
65	2021-10-14 13:13:44.512233+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
66	2021-10-14 13:13:50.302855+05:30	You have order ['Mobile'] successfully	purchase	1
67	2021-10-14 13:13:50.615751+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
68	2021-10-14 13:13:53.211751+05:30	You have order ['Mobile'] successfully	purchase	1
69	2021-10-14 15:49:39.178779+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
70	2021-10-14 15:49:44.989623+05:30	You have order ['Mobile'] successfully	purchase	1
71	2021-10-14 16:21:31.191893+05:30	you have successfully test product accept order	order accept	1
72	2021-10-14 16:33:31.431914+05:30	You have recieved a new order Mobile quality 1 From admin@gmail.com	sale	1
73	2021-10-14 16:33:35.841885+05:30	You have order ['Mobile'] successfully	purchase	1
74	2021-10-18 11:24:00.067301+05:30	You have recieved a new order TV quality 1 From admin@gmail.com	sale	1
75	2021-10-18 11:24:04.790988+05:30	You have order ['TV'] successfully	purchase	1
76	2021-10-18 13:40:19.545629+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
77	2021-10-18 13:40:22.843677+05:30	You have recieved a new order new product quality 1 From admin@gmail.com	sale	1
78	2021-10-18 13:40:23.558769+05:30	You have order ['new product'] successfully	purchase	1
79	2021-10-18 13:40:24.544061+05:30	You have order ['new product'] successfully	purchase	1
80	2021-10-18 14:10:38.758449+05:30	you have successfully TV accept order	order accept	1
81	2021-10-18 14:10:46.510308+05:30	you have successfully new product declain order	order decalin	1
82	2021-10-18 14:10:49.676123+05:30	you have successfully new product declain order	order decalin	1
\.


--
-- Data for Name: Order; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Order" (id, ordered_date, delivered_date, being_delivered, order_cancel, status, buy, booking, customer_id) FROM stdin;
1	2021-10-12	2021-10-12	f	f	\N	f	f	1
2	2021-10-12	2021-10-12	f	f	\N	f	f	1
3	2021-10-12	2021-10-12	f	f	\N	f	f	1
4	2021-10-12	2021-10-12	f	f	\N	f	f	1
5	2021-10-12	2021-10-12	f	f	\N	f	f	1
6	2021-10-12	2021-10-12	f	f	\N	f	f	1
7	2021-10-12	2021-10-12	f	f	\N	f	f	1
8	2021-10-12	2021-10-12	f	f	\N	t	f	1
9	2021-10-12	2021-10-12	f	f	\N	t	f	1
10	2021-10-12	2021-10-12	f	f	\N	t	f	1
12	2021-10-12	2021-10-12	f	f	\N	f	f	1
13	2021-10-12	2021-10-12	f	f	\N	f	f	1
15	2021-10-13	2021-10-13	f	f	\N	f	f	1
16	2021-10-13	2021-10-13	f	f	\N	f	f	1
17	2021-10-13	2021-10-13	f	f	\N	f	f	1
18	2021-10-13	2021-10-13	f	f	\N	f	f	1
19	2021-10-13	2021-10-13	f	f	\N	f	f	1
20	2021-10-13	2021-10-13	f	f	\N	f	f	1
21	2021-10-13	2021-10-13	f	f	\N	f	f	1
22	2021-10-13	2021-10-13	f	f	\N	f	f	1
23	2021-10-13	2021-10-13	f	f	\N	f	f	1
24	2021-10-13	2021-10-13	f	f	\N	f	f	1
25	2021-10-13	2021-10-13	f	f	\N	f	f	1
26	2021-10-13	2021-10-13	f	f	\N	f	f	1
27	2021-10-13	2021-10-13	f	f	\N	f	f	1
28	2021-10-13	2021-10-13	f	f	\N	f	f	1
29	2021-10-13	2021-10-13	f	f	\N	f	f	1
30	2021-10-13	2021-10-13	f	f	\N	f	f	1
31	2021-10-13	2021-10-13	f	f	\N	f	f	1
32	2021-10-13	2021-10-13	f	f	\N	f	f	1
33	2021-10-14	2021-10-14	f	f	\N	f	f	1
34	2021-10-14	2021-10-14	f	f	\N	f	f	1
35	2021-10-14	2021-10-14	f	f	\N	f	f	1
14	2021-10-12	2021-10-12	f	f	Accept	t	f	1
36	2021-10-14	2021-10-14	f	f	\N	f	f	1
38	2021-10-18	2021-10-18	f	f	\N	f	t	1
39	2021-10-18	2021-10-18	f	f	\N	f	t	1
37	2021-10-18	2021-10-18	f	f	Accept	f	f	1
11	2021-10-12	2021-10-12	f	f	Declain	f	f	1
\.


--
-- Data for Name: Order Product; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Order Product" (id, quantity, status, order_id, product_id) FROM stdin;
1	1	\N	1	27
2	1	\N	2	27
3	1	\N	3	27
4	1	\N	4	27
5	1	\N	5	27
6	1	\N	6	27
7	1	\N	7	27
8	1	\N	8	1
9	1	\N	9	1
10	1	\N	10	1
12	1	\N	12	27
13	1	\N	13	27
15	1	\N	15	2
16	1	\N	16	2
17	1	\N	17	2
18	1	\N	18	2
19	1	\N	19	2
20	1	\N	20	27
21	1	\N	21	27
22	1	\N	22	27
23	1	\N	23	27
24	1	\N	24	2
25	1	\N	25	2
26	1	\N	26	2
27	1	\N	27	2
28	1	\N	28	2
14	3	Accept	14	1
38	1	\N	38	2
39	1	\N	39	2
37	1	Accept	37	37
11	1	Declain	11	2
\.


--
-- Data for Name: Product; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Product" (id, title, price, sale_price, description, start_time, end_time, sku, thumbnail, depot, is_sale, inventory, discount_percent, product_option, visit_product, created_at, updated_at, brand_id, store_id, price_type) FROM stdin;
37	TV	25000	0	Sony	2021-10-18 05:51:03.711+05:30	2021-10-21 05:51:03.711+05:30	Oled	Advertisement/2587476_TZTK1TX.jpg	0	t	1	0	Booking	3	2021-10-18 11:22:57.731265+05:30	2021-10-18 12:01:55.674772+05:30	2	1	\N
29	Giorgio Armani Si Eau de Parfum Spray for Women	8000	4000	Brand\tGiorgio Armani\r\nIngredients\tIngredients -alcohol, parfum / fragrance, aqua / water, benzyl salicylate, benzyl alcohol, ethylhexyl methoxycinnamate, linalool, limonene, butyl methoxydibenzoylmethane, ethylhexyl salicylate, hydroxycitronellal, hexyl cinnamal, geraniol, cinnamyl alcohol, bht, alpha-isomethyl ionone, citronellol, eugenol, citral, benzyl benzoate, farnesol, coumarin .Ingredients -alcohol, parfum / fragrance, aqua / water, benzyl salicylate, benzyl alcohol, ethylhex… See more\r\nItem Form\tSpray\r\nProduct Dimensions\t15.01 x 6.2 x 5.59 cm; 0.1 Grams\r\nItem Volume\t100 Millilitres	2021-07-30 00:00:00+05:30	2021-11-09 00:00:00+05:30	R5-3450U	Advertisement/3fd_mFJ2e67.jpg	100	f	100	50	Buy	12	2021-10-12 13:52:07.696945+05:30	2021-10-18 11:07:14.464969+05:30	1	1	\N
2	new product	0	0	qwfsaf	\N	\N	15	Advertisement/3fd_K0kNG6K.jpg	0	t	0	0	Booking	11	2021-10-11 15:47:10.388838+05:30	2021-10-12 12:47:00.774111+05:30	1	1	\N
1	test product	500	450	test	\N	\N	15	Advertisement/3fd.jpg	-5	t	0	90	Buy	6	2021-10-11 11:44:46.622093+05:30	2021-10-14 11:52:11.212134+05:30	1	1	\N
27	test	1425	1211.25	ssss	2021-10-12 04:04:02.924+05:30	2021-11-10 04:01:20.475+05:30	.	Advertisement/Screenshot_from_2021-09-29_18-21-06_83obovk.png	-7	t	5	85	Booking	43	2021-10-12 10:11:32.976238+05:30	2021-10-18 09:53:43.82337+05:30	2	1	\N
47	Led	12000	0	Car	2021-10-18 07:09:51.027+05:30	2021-10-28 07:09:51.027+05:30	dsfcdscs	Advertisement/Black_Technology_LinkedIn_Banner_1.png	1	t	1	0	Booking	3	2021-10-18 12:41:10.25688+05:30	2021-10-18 14:52:21.041467+05:30	2	1	Led
46	AC	45000	0	AC	2021-10-18 07:01:12.709+05:30	2021-10-28 07:01:12.709+05:30	Voltas	Advertisement/Black_Technology_LinkedIn_Banner_3.png	1	t	1	0	Booking	2	2021-10-18 12:33:17.641999+05:30	2021-10-18 12:35:09.672339+05:30	2	1	\N
33	newnew	8000	4000	Brand\tGiorgio Armani\r\nIngredients\tIngredients -alcohol, parfum / fragrance, aqua / water, benzyl salicylate, benzyl alcohol, ethylhexyl methoxycinnamate, linalool, limonene, butyl methoxydibenzoylmethane, ethylhexyl salicylate, hydroxycitronellal, hexyl cinnamal, geraniol, cinnamyl alcohol, bht, alpha-isomethyl ionone, citronellol, eugenol, citral, benzyl benzoate, farnesol, coumarin .Ingredients -alcohol, parfum / fragrance, aqua / water, benzyl salicylate, benzyl alcohol, ethylhex… See more\r\nItem Form\tSpray\r\nProduct Dimensions\t15.01 x 6.2 x 5.59 cm; 0.1 Grams\r\nItem Volume\t100 Millilitres	2021-07-30 00:00:00+05:30	2021-11-26 00:00:00+05:30	R5-3450U	Advertisement/3fd_fIJ2PK3.jpg	100	f	100	50	Buy	6	2021-10-13 14:52:44.362274+05:30	2021-10-18 16:10:48.463584+05:30	1	1	\N
45	AC	35000	0	Voltas	2021-10-18 06:59:04.865+05:30	2021-10-18 06:59:04.865+05:30	AC	Advertisement/Vintage_Typewriter_LinkedIn_Banner_2_x8FVUHk.png	1	f	1	0	Booking	0	2021-10-18 12:31:06.284159+05:30	2021-10-18 16:10:54.373298+05:30	2	1	\N
42	AC	35000	0	Voltas	2021-10-18 06:59:04.865+05:30	2021-10-18 06:59:04.865+05:30	AC	Advertisement/Vintage_Typewriter_LinkedIn_Banner_2_pXLMyQp.png	1	f	1	0	Booking	0	2021-10-18 12:30:48.228708+05:30	2021-10-18 16:10:54.379621+05:30	2	1	\N
36	Laptop	25000	0	Dell Laptop	2021-10-14 12:05:22.742+05:30	2021-10-30 12:05:22.742+05:30	Aaaaaaaaaaaaaaaaaa	Advertisement/2587502_gUnWNtu.jpg	15000	t	15000	0	Booking	10	2021-10-14 17:37:22.920082+05:30	2021-10-18 16:10:56.115882+05:30	3	1	\N
\.


--
-- Data for Name: ProductCategory; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductCategory" (id, product_id, product_category_id, product_sub_category_id) FROM stdin;
\.


--
-- Data for Name: ProductColour; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductColour" (id, product_id, product_color_id) FROM stdin;
2	27	1
4	29	1
7	33	1
10	36	1
11	37	1
13	46	1
14	47	1
\.


--
-- Data for Name: ProductDeal; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductDeal" (id, status, product_id, product_deals_id) FROM stdin;
1	t	2	1
\.


--
-- Data for Name: ProductDescription; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductDescription" (id, title, description, thumbnail, product_id) FROM stdin;
\.


--
-- Data for Name: ProductImage; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductImage" (id, product_image1, product_image2, product_image3, product_image4, product_id) FROM stdin;
1	product/images/Black_Technology_LinkedIn_Banner_3.png				47
\.


--
-- Data for Name: ProductQuestion; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductQuestion" (id, question, answer, product_id, user_id) FROM stdin;
\.


--
-- Data for Name: ProductReview; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductReview" (id, feedback, star_point, name, email, deal_id) FROM stdin;
\.


--
-- Data for Name: ProductSize; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductSize" (id, product_id, product_size_id) FROM stdin;
1	27	2
4	36	2
5	37	1
7	46	3
8	47	1
\.


--
-- Data for Name: ProductSpecification; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."ProductSpecification" (id, the_json, product_id) FROM stdin;
2	{"ss": "ss"}	27
4	{"Department": "‎Women's", "Manufacturer": "GIORGIO+ARMANI", "Country of Origin": "Italy", "Item model number": "‎3605521816658", "Product Dimensions": "‎15.01 x 6.2 x 5.59 cm; 0.1 Grams"}	29
7	{"Department": "‎Women's", "Manufacturer": "GIORGIO+ARMANI", "Country of Origin": "Italy", "Item model number": "‎3605521816658", "Product Dimensions": "‎15.01 x 6.2 x 5.59 cm; 0.1 Grams"}	33
10	{"RAM": "16 GB"}	36
11	{"Ultra HD": "Full"}	37
13	{"Ac": "12"}	46
14	"{\\"Car\\":\\"Lxd\\"}"	47
\.


--
-- Data for Name: Product_sub_product; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Product_sub_product" (id, product_id, subproduct_id) FROM stdin;
1	2	1
2	2	2
5	33	1
6	33	2
11	36	3
12	37	2
17	42	3
20	45	3
21	46	2
23	47	1
24	47	2
\.


--
-- Data for Name: Product_tags; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Product_tags" (id, product_id, tag_id) FROM stdin;
1	1	1
2	2	1
4	27	1
6	29	1
10	33	1
13	36	1
14	37	1
19	42	1
22	45	1
23	46	1
24	47	1
\.


--
-- Data for Name: Size; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Size" (id, size_or_weight) FROM stdin;
1	15
2	12
3	14
\.


--
-- Data for Name: Slider; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Slider" (id, image, url) FROM stdin;
\.


--
-- Data for Name: Store; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Store" (id, name, email, mobile_number, website, location, thumbnail, describe, store_portal_admin, status, owner_id) FROM stdin;
1	new store	test@gmail.com	9660222632	http://store@gmail.com	test	store/3fd.jpg	hy this is test store	ashutosh	t	1
\.


--
-- Data for Name: StoreOwner; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."StoreOwner" (id, status, store_id, user_id) FROM stdin;
\.


--
-- Data for Name: Sub Category; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Sub Category" (id, sub_name) FROM stdin;
\.


--
-- Data for Name: Subscribe; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Subscribe" (id, email) FROM stdin;
\.


--
-- Data for Name: Tag; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."Tag" (id, name) FROM stdin;
1	test
\.


--
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."User" (id, password, last_login, is_superuser, is_staff, date_joined, email, first_name, last_name, phone_number, profile_image, "lastEmailOtp", passsword, role, is_active) FROM stdin;
2	pbkdf2_sha256$260000$h7i155QIxmWHKFmnRYwfus$XqwVmrdK71V/E7BrurvWghcUe10C2OdxYVJ59qG8Ffw=	\N	f	f	2021-09-30 15:06:47+05:30	shuvikagupta@externlabs.com	Shuvika	Gupta	\N		001792		1	t
1	pbkdf2_sha256$260000$to7WA9c8Qc21vVn6ycnxbR$MVIiTOMfoGjT0BaRXbOK5ynBo/Ul2PjkeljQwSc7AFk=	2021-10-18 17:51:43.692325+05:30	t	t	2021-09-30 12:24:42+05:30	admin@gmail.com	admin	user	\N				3	t
\.


--
-- Data for Name: User_groups; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."User_groups" (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: User_user_permissions; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."User_user_permissions" (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: WishList; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public."WishList" (id, is_delete, product_id, user_id) FROM stdin;
4	f	2	1
\.


--
-- Data for Name: admin_user_detailpagesadvertisement; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.admin_user_detailpagesadvertisement (id, thumbnail, url, status) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add User	6	add_user
22	Can change User	6	change_user
23	Can delete User	6	delete_user
24	Can view User	6	view_user
25	Can add Contact	7	add_contact
26	Can change Contact	7	change_contact
27	Can delete Contact	7	delete_contact
28	Can view Contact	7	view_contact
29	Can add Subscribe	8	add_subscribe
30	Can change Subscribe	8	change_subscribe
31	Can delete Subscribe	8	delete_subscribe
32	Can view Subscribe	8	view_subscribe
33	Can add Customer Address	9	add_customeraddress
34	Can change Customer Address	9	change_customeraddress
35	Can delete Customer Address	9	delete_customeraddress
36	Can view Customer Address	9	view_customeraddress
37	Can add Customer	10	add_customer
38	Can change Customer	10	change_customer
39	Can delete Customer	10	delete_customer
40	Can view Customer	10	view_customer
41	Can add Brand	11	add_brand
42	Can change Brand	11	change_brand
43	Can delete Brand	11	delete_brand
44	Can view Brand	11	view_brand
45	Can add Cart	12	add_cart
46	Can change Cart	12	change_cart
47	Can delete Cart	12	delete_cart
48	Can view Cart	12	view_cart
49	Can add Category	13	add_category
50	Can change Category	13	change_category
51	Can delete Category	13	delete_category
52	Can view Category	13	view_category
53	Can add Colour	14	add_colour
54	Can change Colour	14	change_colour
55	Can delete Colour	14	delete_colour
56	Can view Colour	14	view_colour
57	Can add Deal	15	add_deal
58	Can change Deal	15	change_deal
59	Can delete Deal	15	delete_deal
60	Can view Deal	15	view_deal
61	Can add Product	16	add_product
62	Can change Product	16	change_product
63	Can delete Product	16	delete_product
64	Can view Product	16	view_product
65	Can add ProductCategory	17	add_productcategory
66	Can change ProductCategory	17	change_productcategory
67	Can delete ProductCategory	17	delete_productcategory
68	Can view ProductCategory	17	view_productcategory
69	Can add ProductColour	18	add_productcolour
70	Can change ProductColour	18	change_productcolour
71	Can delete ProductColour	18	delete_productcolour
72	Can view ProductColour	18	view_productcolour
73	Can add ProductDeal	19	add_productdeal
74	Can change ProductDeal	19	change_productdeal
75	Can delete ProductDeal	19	delete_productdeal
76	Can view ProductDeal	19	view_productdeal
77	Can add ProductDescription	20	add_productdescription
78	Can change ProductDescription	20	change_productdescription
79	Can delete ProductDescription	20	delete_productdescription
80	Can view ProductDescription	20	view_productdescription
81	Can add ProductImage	21	add_productimage
82	Can change ProductImage	21	change_productimage
83	Can delete ProductImage	21	delete_productimage
84	Can view ProductImage	21	view_productimage
85	Can add ProductQuestion	22	add_productquestion
86	Can change ProductQuestion	22	change_productquestion
87	Can delete ProductQuestion	22	delete_productquestion
88	Can view ProductQuestion	22	view_productquestion
89	Can add ProductReview	23	add_productreview
90	Can change ProductReview	23	change_productreview
91	Can delete ProductReview	23	delete_productreview
92	Can view ProductReview	23	view_productreview
93	Can add ProductSize	24	add_productsize
94	Can change ProductSize	24	change_productsize
95	Can delete ProductSize	24	delete_productsize
96	Can view ProductSize	24	view_productsize
97	Can add Size	25	add_size
98	Can change Size	25	change_size
99	Can delete Size	25	delete_size
100	Can view Size	25	view_size
101	Can add Slider	26	add_slider
102	Can change Slider	26	change_slider
103	Can delete Slider	26	delete_slider
104	Can view Slider	26	view_slider
105	Can add specification	27	add_specification
106	Can change specification	27	change_specification
107	Can delete specification	27	delete_specification
108	Can view specification	27	view_specification
109	Can add Store	28	add_store
110	Can change Store	28	change_store
111	Can delete Store	28	delete_store
112	Can view Store	28	view_store
113	Can add Sub Category	29	add_subcategories
114	Can change Sub Category	29	change_subcategories
115	Can delete Sub Category	29	delete_subcategories
116	Can view Sub Category	29	view_subcategories
117	Can add Tag	30	add_tag
118	Can change Tag	30	change_tag
119	Can delete Tag	30	delete_tag
120	Can view Tag	30	view_tag
121	Can add WishList	31	add_wishlist
122	Can change WishList	31	change_wishlist
123	Can delete WishList	31	delete_wishlist
124	Can view WishList	31	view_wishlist
125	Can add ProductSpecification	32	add_productspecification
126	Can change ProductSpecification	32	change_productspecification
127	Can delete ProductSpecification	32	delete_productspecification
128	Can view ProductSpecification	32	view_productspecification
129	Can add StoreOwner	33	add_storeowner
130	Can change StoreOwner	33	change_storeowner
131	Can delete StoreOwner	33	delete_storeowner
132	Can view StoreOwner	33	view_storeowner
133	Can add Admin User	34	add_adminuser
134	Can change Admin User	34	change_adminuser
135	Can delete Admin User	34	delete_adminuser
136	Can view Admin User	34	view_adminuser
137	Can add Detail Page Advertisement	35	add_detailpagesadvertisement
138	Can change Detail Page Advertisement	35	change_detailpagesadvertisement
139	Can delete Detail Page Advertisement	35	delete_detailpagesadvertisement
140	Can view Detail Page Advertisement	35	view_detailpagesadvertisement
141	Can add Home Page Advertisement	36	add_homepagesadvertisement
142	Can change Home Page Advertisement	36	change_homepagesadvertisement
143	Can delete Home Page Advertisement	36	delete_homepagesadvertisement
144	Can view Home Page Advertisement	36	view_homepagesadvertisement
145	Can add bill	37	add_bill
146	Can change bill	37	change_bill
147	Can delete bill	37	delete_bill
148	Can view bill	37	view_bill
149	Can add Booking Form	38	add_bookingform
150	Can change Booking Form	38	change_bookingform
151	Can delete Booking Form	38	delete_bookingform
152	Can view Booking Form	38	view_bookingform
153	Can add Order	39	add_order
154	Can change Order	39	change_order
155	Can delete Order	39	delete_order
156	Can view Order	39	view_order
157	Can add Order Product	40	add_orderproduct
158	Can change Order Product	40	change_orderproduct
159	Can delete Order Product	40	delete_orderproduct
160	Can view Order Product	40	view_orderproduct
161	Can add Bill	41	add_subbill
162	Can change Bill	41	change_subbill
163	Can delete Bill	41	delete_subbill
164	Can view Bill	41	view_subbill
165	Can add MPayment	42	add_mpayment
166	Can change MPayment	42	change_mpayment
167	Can delete MPayment	42	delete_mpayment
168	Can view MPayment	42	view_mpayment
169	Can add Notification	43	add_notification
170	Can change Notification	43	change_notification
171	Can delete Notification	43	delete_notification
172	Can view Notification	43	view_notification
173	Can add sub product	44	add_subproduct
174	Can change sub product	44	change_subproduct
175	Can delete sub product	44	delete_subproduct
176	Can view sub product	44	view_subproduct
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-09-30 15:07:47.544863+05:30	2	shuvikagupta@externlabs.com	2	[{"changed": {"fields": ["Is active"]}}]	6	1
2	2021-10-11 11:43:45.164284+05:30	1	new store	1	[{"added": {}}]	28	1
3	2021-10-11 11:44:02.739161+05:30	1	zara	1	[{"added": {}}]	11	1
4	2021-10-11 11:44:33.99913+05:30	1	test	1	[{"added": {}}]	30	1
5	2021-10-11 11:44:46.633493+05:30	1	test product	1	[{"added": {}}]	16	1
6	2021-10-11 15:47:10.39791+05:30	2	new product	1	[{"added": {}}]	16	1
7	2021-10-11 16:22:56.999862+05:30	1	Cardio	1	[{"added": {}}]	44	1
8	2021-10-11 16:23:34.138423+05:30	2	Monthly Bill	1	[{"added": {}}]	44	1
9	2021-10-11 16:38:44.283888+05:30	2	new product	2	[{"changed": {"fields": ["Sub product"]}}]	16	1
10	2021-10-11 16:42:02.953236+05:30	1	Red	1	[{"added": {}}]	14	1
11	2021-10-11 16:42:11.165311+05:30	1	15	1	[{"added": {}}]	25	1
12	2021-10-11 17:31:55.525366+05:30	1	FeatureDeal	1	[{"added": {}}]	15	1
13	2021-10-11 17:31:58.071852+05:30	2	new product	2	[{"added": {"name": "ProductDeal", "object": "new product"}}]	16	1
14	2021-10-12 09:30:34.429169+05:30	1	admin@gmail.com	2	[{"changed": {"fields": ["Role", "First name", "Last name"]}}]	6	1
15	2021-10-12 09:31:09.825408+05:30	1	new store	2	[{"changed": {"fields": ["Owner"]}}]	28	1
16	2021-10-12 10:14:13.460453+05:30	2	new product	2	[{"changed": {"fields": ["Sub product"]}}]	16	1
17	2021-10-12 13:52:05.296853+05:30	28	Giorgio Armani Si Eau de Parfum Spray for Women	3		16	1
18	2021-10-12 14:20:17.648365+05:30	2	Monthly Bill	2	[{"changed": {"fields": ["Sale price"]}}]	44	1
19	2021-10-12 14:21:08.182092+05:30	3	Cardio	1	[{"added": {}}]	44	1
20	2021-10-12 14:21:37.443645+05:30	3	Cardio	2	[]	44	1
21	2021-10-13 14:20:31.049019+05:30	32	newnew	3		16	1
22	2021-10-13 14:20:31.05552+05:30	31	newnew	3		16	1
23	2021-10-13 14:20:31.057864+05:30	30	newnew	3		16	1
24	2021-10-13 15:09:01.360968+05:30	34	Mobile	2	[{"added": {"name": "ProductDeal", "object": "Mobile"}}]	16	1
25	2021-10-13 15:37:27.649346+05:30	33	newnew	2	[{"changed": {"fields": ["Description", "End time"]}}]	16	1
26	2021-10-13 15:37:44.702108+05:30	29	Giorgio Armani Si Eau de Parfum Spray for Women	2	[{"changed": {"fields": ["Description", "End time"]}}]	16	1
27	2021-10-13 15:39:29.579082+05:30	34	Mobile	2	[{"changed": {"fields": ["End time"]}}]	16	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	users	user
7	users	contact
8	users	subscribe
9	users	customeraddress
10	users	customer
11	product	brand
12	product	cart
13	product	category
14	product	colour
15	product	deal
16	product	product
17	product	productcategory
18	product	productcolour
19	product	productdeal
20	product	productdescription
21	product	productimage
22	product	productquestion
23	product	productreview
24	product	productsize
25	product	size
26	product	slider
27	product	specification
28	product	store
29	product	subcategories
30	product	tag
31	product	wishlist
32	stores	productspecification
33	stores	storeowner
34	admin_user	adminuser
35	admin_user	detailpagesadvertisement
36	admin_user	homepagesadvertisement
37	order	bill
38	order	bookingform
39	order	order
40	order	orderproduct
41	order	subbill
42	payment	mpayment
43	Notifications	notification
44	product	subproduct
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-09-30 12:19:11.290816+05:30
2	contenttypes	0002_remove_content_type_name	2021-09-30 12:19:11.303949+05:30
3	auth	0001_initial	2021-09-30 12:19:11.360144+05:30
4	auth	0002_alter_permission_name_max_length	2021-09-30 12:19:11.379894+05:30
5	auth	0003_alter_user_email_max_length	2021-09-30 12:19:11.402055+05:30
6	auth	0004_alter_user_username_opts	2021-09-30 12:19:11.422235+05:30
7	auth	0005_alter_user_last_login_null	2021-09-30 12:19:11.442403+05:30
8	auth	0006_require_contenttypes_0002	2021-09-30 12:19:11.448524+05:30
9	auth	0007_alter_validators_add_error_messages	2021-09-30 12:19:11.470724+05:30
10	auth	0008_alter_user_username_max_length	2021-09-30 12:19:11.492217+05:30
11	auth	0009_alter_user_last_name_max_length	2021-09-30 12:19:11.515518+05:30
12	auth	0010_alter_group_name_max_length	2021-09-30 12:19:11.538415+05:30
13	auth	0011_update_proxy_permissions	2021-09-30 12:19:11.558975+05:30
14	auth	0012_alter_user_first_name_max_length	2021-09-30 12:19:11.578537+05:30
15	users	0001_initial	2021-09-30 12:19:11.782891+05:30
16	Notifications	0001_initial	2021-09-30 12:19:11.802466+05:30
17	Notifications	0002_notification_user	2021-09-30 12:19:11.844415+05:30
18	admin	0001_initial	2021-09-30 12:19:11.907421+05:30
19	admin	0002_logentry_remove_auto_add	2021-09-30 12:19:11.943692+05:30
20	admin	0003_logentry_add_action_flag_choices	2021-09-30 12:19:11.988159+05:30
21	admin_user	0001_initial	2021-09-30 12:19:12.031167+05:30
22	admin_user	0002_adminuser_user	2021-09-30 12:19:12.082115+05:30
23	product	0001_initial	2021-09-30 12:19:12.362674+05:30
24	order	0001_initial	2021-09-30 12:19:12.437218+05:30
25	order	0002_initial	2021-09-30 12:19:12.674831+05:30
26	payment	0001_initial	2021-09-30 12:19:12.713081+05:30
27	product	0002_initial	2021-09-30 12:19:13.524826+05:30
28	sessions	0001_initial	2021-09-30 12:19:13.554209+05:30
29	stores	0001_initial	2021-09-30 12:19:13.756208+05:30
30	stores	0002_initial	2021-09-30 12:19:13.877233+05:30
31	product	0003_product_price_type	2021-10-07 13:01:02.013902+05:30
32	product	0004_auto_20211011_1546	2021-10-11 15:46:15.153229+05:30
33	product	0005_remove_product_sub_product	2021-10-12 09:38:08.239966+05:30
34	product	0003_product_sub_product	2021-10-12 10:12:47.977249+05:30
35	product	0004_auto_20211012_1418	2021-10-12 14:18:52.59876+05:30
36	product	0005_alter_subproduct_discount_percent	2021-10-12 14:27:27.085882+05:30
37	order	0003_auto_20211012_1632	2021-10-12 16:32:30.455568+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
5xixp5en22d0j5jmzajn0hg31b6r4led	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1mVsV1:C-KeN5NxV3NFPjBkgmvNkRr3di6_B7vlNiM5q7YQV44	2021-10-14 15:07:07.010555+05:30
ze8oxhw8wpxel7dtyjxmimjdiatdurkt	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1mZo9h:u3mFdDNO2L1XBl4gsyvuJfrHHo27GpB0aI0Q-kRzeC4	2021-10-25 11:17:21.64441+05:30
jt5en95982sko3h062woxmcfwjzh72c1	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1mZtyu:F8HIP8Mbj5S5Vdmt2tnc4Up3iFi-zDs7lWtmkTIb_P0	2021-10-25 17:30:36.122882+05:30
n1z7a83m6q3jcvk7sf85shn2rm87ovgj	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1ma8xA:tMn2OIxPY4kyPjZkkR3tjaX1fmMzhGcLD6qlOcx612Y	2021-10-26 09:29:48.922621+05:30
jep673x2dkofghy4o2dkna16jdhqdjpn	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1ma8y1:AHf9Cd2yJBAgq-0IJW1xCSPkJ7AbAXF99Y2QugBJ_Jg	2021-10-26 09:30:41.201838+05:30
9h5tou22s8vz2lt6xgdbqytho0txg5qz	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1maB56:saiPd5YlRS1XfaVrsQcHM7j-BPYPmMgtcRojhFfu62c	2021-10-26 11:46:08.297699+05:30
8z2p00171ud251bl5xf2iv5pidnbkts7	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1maXpQ:VK0H0Ziv2vEcQQao5q7IX3udvK9NO2rMd2flGWgnA6E	2021-10-27 12:03:28.249028+05:30
qfz7ssku8x6czaqyc278iljqnhdr03zc	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1mcLge:xLfTTZ8tzNuVpndmPGkzJttbtn_qhO9kJ5AtctD9ZSo	2021-11-01 11:29:52.566636+05:30
pejki74v8j19jdstbzoszod6nsx3vhca	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1mcLgz:jRysC4k8SkmkkWE0rFS8yb88RhLgegHXP3NgP-Z4V1o	2021-11-01 11:30:13.179226+05:30
hb4fcunlax5xz4q5ghcdkveif7d76aod	.eJxVjMsOwiAQRf-FtSFMC5Rx6d5vIMNjpGogKe3K-O_apAvd3nPOfQlP21r81vPi5yTOAsTpdwsUH7nuIN2p3pqMra7LHOSuyIN2eW0pPy-H-3dQqJdvHUlpHFWyk2VGzaAtAtNorXM4Zg7ZGMUqWjakFaAacHDA4GjKDKjF-wPPhTcp:1mcReB:nFadPn3sWpkZ3xcF5VUcaX2vnFTVuhiAfwsUBLwfJ54	2021-11-01 17:51:43.69524+05:30
\.


--
-- Data for Name: order_bill; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.order_bill (id, discount_price, "MRP_price", total_price, status, customer_id, order_id) FROM stdin;
1	50	500	450	t	1	8
2	50	500	450	t	1	10
3	50	500	450	t	1	9
4	150	1500	1350	t	1	14
\.


--
-- Data for Name: product_specification; Type: TABLE DATA; Schema: public; Owner: angaza
--

COPY public.product_specification (id, color, size, weight, bluetooth, battery_life, wireless, product_id) FROM stdin;
\.


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
-- Name: Admin User_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Admin User_id_seq"', 1, false);


--
-- Name: Bill_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Bill_id_seq"', 39, true);


--
-- Name: Booking Form_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Booking Form_id_seq"', 6, true);


--
-- Name: Brand_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Brand_id_seq"', 3, true);


--
-- Name: Cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Cart_id_seq"', 25, true);


--
-- Name: Category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Category_id_seq"', 1, false);


--
-- Name: Category_subcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Category_subcategory_id_seq"', 1, false);


--
-- Name: Colour_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Colour_id_seq"', 1, true);


--
-- Name: Contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Contact_id_seq"', 1, false);


--
-- Name: Customer Address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Customer Address_id_seq"', 1, false);


--
-- Name: Customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Customer_id_seq"', 1, true);


--
-- Name: Deal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Deal_id_seq"', 1, true);


--
-- Name: Home Page Advertisement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Home Page Advertisement_id_seq"', 1, false);


--
-- Name: MPayment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."MPayment_id_seq"', 1, false);


--
-- Name: Notification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Notification_id_seq"', 82, true);


--
-- Name: Order Product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Order Product_id_seq"', 39, true);


--
-- Name: Order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Order_id_seq"', 39, true);


--
-- Name: ProductCategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductCategory_id_seq"', 1, false);


--
-- Name: ProductColour_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductColour_id_seq"', 14, true);


--
-- Name: ProductDeal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductDeal_id_seq"', 2, true);


--
-- Name: ProductDescription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductDescription_id_seq"', 1, false);


--
-- Name: ProductImage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductImage_id_seq"', 1, true);


--
-- Name: ProductQuestion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductQuestion_id_seq"', 1, false);


--
-- Name: ProductReview_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductReview_id_seq"', 1, false);


--
-- Name: ProductSize_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductSize_id_seq"', 8, true);


--
-- Name: ProductSpecification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."ProductSpecification_id_seq"', 14, true);


--
-- Name: Product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Product_id_seq"', 47, true);


--
-- Name: Product_sub_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Product_sub_product_id_seq"', 24, true);


--
-- Name: Product_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Product_tags_id_seq"', 24, true);


--
-- Name: Size_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Size_id_seq"', 3, true);


--
-- Name: Slider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Slider_id_seq"', 1, false);


--
-- Name: StoreOwner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."StoreOwner_id_seq"', 1, false);


--
-- Name: Store_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Store_id_seq"', 1, true);


--
-- Name: Sub Category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Sub Category_id_seq"', 1, false);


--
-- Name: Subscribe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Subscribe_id_seq"', 1, false);


--
-- Name: Tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."Tag_id_seq"', 1, true);


--
-- Name: User_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."User_groups_id_seq"', 1, false);


--
-- Name: User_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."User_id_seq"', 2, true);


--
-- Name: User_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."User_user_permissions_id_seq"', 1, false);


--
-- Name: WishList_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public."WishList_id_seq"', 4, true);


--
-- Name: admin_user_detailpagesadvertisement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.admin_user_detailpagesadvertisement_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 176, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 27, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 44, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 37, true);


--
-- Name: order_bill_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.order_bill_id_seq', 4, true);


--
-- Name: product_specification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.product_specification_id_seq', 1, false);


--
-- Name: product_subproduct_id_seq; Type: SEQUENCE SET; Schema: public; Owner: angaza
--

SELECT pg_catalog.setval('public.product_subproduct_id_seq', 4, true);


--
-- Name: Admin User Admin User_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Admin User"
    ADD CONSTRAINT "Admin User_pkey" PRIMARY KEY (id);


--
-- Name: Bill Bill_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Bill"
    ADD CONSTRAINT "Bill_pkey" PRIMARY KEY (id);


--
-- Name: Booking Form Booking Form_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Booking Form"
    ADD CONSTRAINT "Booking Form_pkey" PRIMARY KEY (id);


--
-- Name: Brand Brand_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Brand"
    ADD CONSTRAINT "Brand_pkey" PRIMARY KEY (id);


--
-- Name: Cart Cart_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Cart"
    ADD CONSTRAINT "Cart_pkey" PRIMARY KEY (id);


--
-- Name: Category Category_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Category"
    ADD CONSTRAINT "Category_pkey" PRIMARY KEY (id);


--
-- Name: Category_subcategory Category_subcategory_category_id_subcategories_id_98739ec9_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Category_subcategory"
    ADD CONSTRAINT "Category_subcategory_category_id_subcategories_id_98739ec9_uniq" UNIQUE (category_id, subcategories_id);


--
-- Name: Category_subcategory Category_subcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Category_subcategory"
    ADD CONSTRAINT "Category_subcategory_pkey" PRIMARY KEY (id);


--
-- Name: Colour Colour_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Colour"
    ADD CONSTRAINT "Colour_pkey" PRIMARY KEY (id);


--
-- Name: Contact Contact_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Contact"
    ADD CONSTRAINT "Contact_pkey" PRIMARY KEY (id);


--
-- Name: Customer Address Customer Address_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Customer Address"
    ADD CONSTRAINT "Customer Address_pkey" PRIMARY KEY (id);


--
-- Name: Customer Customer_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Customer"
    ADD CONSTRAINT "Customer_pkey" PRIMARY KEY (id);


--
-- Name: Deal Deal_name_key; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Deal"
    ADD CONSTRAINT "Deal_name_key" UNIQUE (name);


--
-- Name: Deal Deal_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Deal"
    ADD CONSTRAINT "Deal_pkey" PRIMARY KEY (id);


--
-- Name: Home Page Advertisement Home Page Advertisement_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Home Page Advertisement"
    ADD CONSTRAINT "Home Page Advertisement_pkey" PRIMARY KEY (id);


--
-- Name: MPayment MPayment_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."MPayment"
    ADD CONSTRAINT "MPayment_pkey" PRIMARY KEY (id);


--
-- Name: Notification Notification_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Notification"
    ADD CONSTRAINT "Notification_pkey" PRIMARY KEY (id);


--
-- Name: Order Product Order Product_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Order Product"
    ADD CONSTRAINT "Order Product_pkey" PRIMARY KEY (id);


--
-- Name: Order Order_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Order"
    ADD CONSTRAINT "Order_pkey" PRIMARY KEY (id);


--
-- Name: ProductCategory ProductCategory_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductCategory"
    ADD CONSTRAINT "ProductCategory_pkey" PRIMARY KEY (id);


--
-- Name: ProductColour ProductColour_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductColour"
    ADD CONSTRAINT "ProductColour_pkey" PRIMARY KEY (id);


--
-- Name: ProductDeal ProductDeal_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductDeal"
    ADD CONSTRAINT "ProductDeal_pkey" PRIMARY KEY (id);


--
-- Name: ProductDescription ProductDescription_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductDescription"
    ADD CONSTRAINT "ProductDescription_pkey" PRIMARY KEY (id);


--
-- Name: ProductImage ProductImage_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductImage"
    ADD CONSTRAINT "ProductImage_pkey" PRIMARY KEY (id);


--
-- Name: ProductQuestion ProductQuestion_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductQuestion"
    ADD CONSTRAINT "ProductQuestion_pkey" PRIMARY KEY (id);


--
-- Name: ProductReview ProductReview_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductReview"
    ADD CONSTRAINT "ProductReview_pkey" PRIMARY KEY (id);


--
-- Name: ProductSize ProductSize_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSize"
    ADD CONSTRAINT "ProductSize_pkey" PRIMARY KEY (id);


--
-- Name: ProductSpecification ProductSpecification_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSpecification"
    ADD CONSTRAINT "ProductSpecification_pkey" PRIMARY KEY (id);


--
-- Name: ProductSpecification ProductSpecification_product_id_key; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSpecification"
    ADD CONSTRAINT "ProductSpecification_product_id_key" UNIQUE (product_id);


--
-- Name: Product Product_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_pkey" PRIMARY KEY (id);


--
-- Name: Product_sub_product Product_sub_product_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_sub_product"
    ADD CONSTRAINT "Product_sub_product_pkey" PRIMARY KEY (id);


--
-- Name: Product_sub_product Product_sub_product_product_id_subproduct_id_f4b4fb2f_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_sub_product"
    ADD CONSTRAINT "Product_sub_product_product_id_subproduct_id_f4b4fb2f_uniq" UNIQUE (product_id, subproduct_id);


--
-- Name: Product_tags Product_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_tags"
    ADD CONSTRAINT "Product_tags_pkey" PRIMARY KEY (id);


--
-- Name: Product_tags Product_tags_product_id_tag_id_a91d2775_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_tags"
    ADD CONSTRAINT "Product_tags_product_id_tag_id_a91d2775_uniq" UNIQUE (product_id, tag_id);


--
-- Name: Size Size_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Size"
    ADD CONSTRAINT "Size_pkey" PRIMARY KEY (id);


--
-- Name: Slider Slider_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Slider"
    ADD CONSTRAINT "Slider_pkey" PRIMARY KEY (id);


--
-- Name: StoreOwner StoreOwner_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."StoreOwner"
    ADD CONSTRAINT "StoreOwner_pkey" PRIMARY KEY (id);


--
-- Name: Store Store_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Store"
    ADD CONSTRAINT "Store_pkey" PRIMARY KEY (id);


--
-- Name: Sub Category Sub Category_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Sub Category"
    ADD CONSTRAINT "Sub Category_pkey" PRIMARY KEY (id);


--
-- Name: Subscribe Subscribe_email_key; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Subscribe"
    ADD CONSTRAINT "Subscribe_email_key" UNIQUE (email);


--
-- Name: Subscribe Subscribe_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Subscribe"
    ADD CONSTRAINT "Subscribe_pkey" PRIMARY KEY (id);


--
-- Name: Tag Tag_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Tag"
    ADD CONSTRAINT "Tag_pkey" PRIMARY KEY (id);


--
-- Name: User User_email_key; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_email_key" UNIQUE (email);


--
-- Name: User_groups User_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_groups"
    ADD CONSTRAINT "User_groups_pkey" PRIMARY KEY (id);


--
-- Name: User_groups User_groups_user_id_group_id_d63e199e_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_groups"
    ADD CONSTRAINT "User_groups_user_id_group_id_d63e199e_uniq" UNIQUE (user_id, group_id);


--
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (id);


--
-- Name: User_user_permissions User_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_user_permissions"
    ADD CONSTRAINT "User_user_permissions_pkey" PRIMARY KEY (id);


--
-- Name: User_user_permissions User_user_permissions_user_id_permission_id_af0f54ec_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_user_permissions"
    ADD CONSTRAINT "User_user_permissions_user_id_permission_id_af0f54ec_uniq" UNIQUE (user_id, permission_id);


--
-- Name: WishList WishList_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."WishList"
    ADD CONSTRAINT "WishList_pkey" PRIMARY KEY (id);


--
-- Name: admin_user_detailpagesadvertisement admin_user_detailpagesadvertisement_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.admin_user_detailpagesadvertisement
    ADD CONSTRAINT admin_user_detailpagesadvertisement_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: order_bill order_bill_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.order_bill
    ADD CONSTRAINT order_bill_pkey PRIMARY KEY (id);


--
-- Name: product_specification product_specification_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.product_specification
    ADD CONSTRAINT product_specification_pkey PRIMARY KEY (id);


--
-- Name: product_subproduct product_subproduct_pkey; Type: CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.product_subproduct
    ADD CONSTRAINT product_subproduct_pkey PRIMARY KEY (id);


--
-- Name: Admin User_user_id_6b491b17; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Admin User_user_id_6b491b17" ON public."Admin User" USING btree (user_id);


--
-- Name: Bill_customer_id_fdc05edb; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Bill_customer_id_fdc05edb" ON public."Bill" USING btree (customer_id);


--
-- Name: Bill_order_product_id_e3635da7; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Bill_order_product_id_e3635da7" ON public."Bill" USING btree (order_product_id);


--
-- Name: Booking Form_order_id_5243c5b6; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Booking Form_order_id_5243c5b6" ON public."Booking Form" USING btree (order_id);


--
-- Name: Brand_user_id_cef454b9; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Brand_user_id_cef454b9" ON public."Brand" USING btree (user_id);


--
-- Name: Cart_product_id_7cabc995; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Cart_product_id_7cabc995" ON public."Cart" USING btree (product_id);


--
-- Name: Cart_user_id_c44ac99e; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Cart_user_id_c44ac99e" ON public."Cart" USING btree (user_id);


--
-- Name: Category_subcategory_category_id_0b8105c6; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Category_subcategory_category_id_0b8105c6" ON public."Category_subcategory" USING btree (category_id);


--
-- Name: Category_subcategory_subcategories_id_e70e72eb; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Category_subcategory_subcategories_id_e70e72eb" ON public."Category_subcategory" USING btree (subcategories_id);


--
-- Name: Customer Address_user_id_e63de8c1; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Customer Address_user_id_e63de8c1" ON public."Customer Address" USING btree (user_id);


--
-- Name: Customer_user_id_b3dbf5c1; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Customer_user_id_b3dbf5c1" ON public."Customer" USING btree (user_id);


--
-- Name: Deal_name_3ad77dfa_like; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Deal_name_3ad77dfa_like" ON public."Deal" USING btree (name varchar_pattern_ops);


--
-- Name: MPayment_order_id_eddb263e; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "MPayment_order_id_eddb263e" ON public."MPayment" USING btree (order_id);


--
-- Name: Notification_user_id_27901a99; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Notification_user_id_27901a99" ON public."Notification" USING btree (user_id);


--
-- Name: Order Product_order_id_6f6a0bb6; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Order Product_order_id_6f6a0bb6" ON public."Order Product" USING btree (order_id);


--
-- Name: Order Product_product_id_53060350; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Order Product_product_id_53060350" ON public."Order Product" USING btree (product_id);


--
-- Name: Order_customer_id_66bfa5c2; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Order_customer_id_66bfa5c2" ON public."Order" USING btree (customer_id);


--
-- Name: ProductCategory_product_category_id_4a0af2f3; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductCategory_product_category_id_4a0af2f3" ON public."ProductCategory" USING btree (product_category_id);


--
-- Name: ProductCategory_product_id_6583d383; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductCategory_product_id_6583d383" ON public."ProductCategory" USING btree (product_id);


--
-- Name: ProductCategory_product_sub_category_id_c0f6ba0a; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductCategory_product_sub_category_id_c0f6ba0a" ON public."ProductCategory" USING btree (product_sub_category_id);


--
-- Name: ProductColour_product_color_id_7c50be15; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductColour_product_color_id_7c50be15" ON public."ProductColour" USING btree (product_color_id);


--
-- Name: ProductColour_product_id_d937b171; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductColour_product_id_d937b171" ON public."ProductColour" USING btree (product_id);


--
-- Name: ProductDeal_product_deals_id_c33db44a; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductDeal_product_deals_id_c33db44a" ON public."ProductDeal" USING btree (product_deals_id);


--
-- Name: ProductDeal_product_id_a4ccdf90; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductDeal_product_id_a4ccdf90" ON public."ProductDeal" USING btree (product_id);


--
-- Name: ProductDescription_product_id_3348b974; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductDescription_product_id_3348b974" ON public."ProductDescription" USING btree (product_id);


--
-- Name: ProductImage_product_id_f70724f4; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductImage_product_id_f70724f4" ON public."ProductImage" USING btree (product_id);


--
-- Name: ProductQuestion_product_id_b4c89073; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductQuestion_product_id_b4c89073" ON public."ProductQuestion" USING btree (product_id);


--
-- Name: ProductQuestion_user_id_f30fed50; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductQuestion_user_id_f30fed50" ON public."ProductQuestion" USING btree (user_id);


--
-- Name: ProductReview_deal_id_02ebaf10; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductReview_deal_id_02ebaf10" ON public."ProductReview" USING btree (deal_id);


--
-- Name: ProductSize_product_id_fdb40400; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductSize_product_id_fdb40400" ON public."ProductSize" USING btree (product_id);


--
-- Name: ProductSize_product_size_id_4df409be; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "ProductSize_product_size_id_4df409be" ON public."ProductSize" USING btree (product_size_id);


--
-- Name: Product_brand_id_bb588269; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Product_brand_id_bb588269" ON public."Product" USING btree (brand_id);


--
-- Name: Product_store_id_65a88807; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Product_store_id_65a88807" ON public."Product" USING btree (store_id);


--
-- Name: Product_sub_product_product_id_4d893218; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Product_sub_product_product_id_4d893218" ON public."Product_sub_product" USING btree (product_id);


--
-- Name: Product_sub_product_subproduct_id_0b614770; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Product_sub_product_subproduct_id_0b614770" ON public."Product_sub_product" USING btree (subproduct_id);


--
-- Name: Product_tags_product_id_009fa4e2; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Product_tags_product_id_009fa4e2" ON public."Product_tags" USING btree (product_id);


--
-- Name: Product_tags_tag_id_fc2895ef; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Product_tags_tag_id_fc2895ef" ON public."Product_tags" USING btree (tag_id);


--
-- Name: StoreOwner_store_id_f36b7389; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "StoreOwner_store_id_f36b7389" ON public."StoreOwner" USING btree (store_id);


--
-- Name: StoreOwner_user_id_627986d9; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "StoreOwner_user_id_627986d9" ON public."StoreOwner" USING btree (user_id);


--
-- Name: Store_owner_id_8c609f25; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Store_owner_id_8c609f25" ON public."Store" USING btree (owner_id);


--
-- Name: Subscribe_email_36642002_like; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "Subscribe_email_36642002_like" ON public."Subscribe" USING btree (email varchar_pattern_ops);


--
-- Name: User_email_667201b5_like; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "User_email_667201b5_like" ON public."User" USING btree (email varchar_pattern_ops);


--
-- Name: User_groups_group_id_328392a3; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "User_groups_group_id_328392a3" ON public."User_groups" USING btree (group_id);


--
-- Name: User_groups_user_id_8f675f72; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "User_groups_user_id_8f675f72" ON public."User_groups" USING btree (user_id);


--
-- Name: User_user_permissions_permission_id_8e998ba4; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "User_user_permissions_permission_id_8e998ba4" ON public."User_user_permissions" USING btree (permission_id);


--
-- Name: User_user_permissions_user_id_2c6da4d4; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "User_user_permissions_user_id_2c6da4d4" ON public."User_user_permissions" USING btree (user_id);


--
-- Name: WishList_product_id_6411d132; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "WishList_product_id_6411d132" ON public."WishList" USING btree (product_id);


--
-- Name: WishList_user_id_e0523ed2; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX "WishList_user_id_e0523ed2" ON public."WishList" USING btree (user_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: order_bill_customer_id_3f539083; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX order_bill_customer_id_3f539083 ON public.order_bill USING btree (customer_id);


--
-- Name: order_bill_order_id_b8e8cd37; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX order_bill_order_id_b8e8cd37 ON public.order_bill USING btree (order_id);


--
-- Name: product_specification_product_id_9bd3432e; Type: INDEX; Schema: public; Owner: angaza
--

CREATE INDEX product_specification_product_id_9bd3432e ON public.product_specification USING btree (product_id);


--
-- Name: Admin User Admin User_user_id_6b491b17_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Admin User"
    ADD CONSTRAINT "Admin User_user_id_6b491b17_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Bill Bill_customer_id_fdc05edb_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Bill"
    ADD CONSTRAINT "Bill_customer_id_fdc05edb_fk_User_id" FOREIGN KEY (customer_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Bill Bill_order_product_id_e3635da7_fk_Order Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Bill"
    ADD CONSTRAINT "Bill_order_product_id_e3635da7_fk_Order Product_id" FOREIGN KEY (order_product_id) REFERENCES public."Order Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Booking Form Booking Form_order_id_5243c5b6_fk_Order_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Booking Form"
    ADD CONSTRAINT "Booking Form_order_id_5243c5b6_fk_Order_id" FOREIGN KEY (order_id) REFERENCES public."Order"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brand Brand_user_id_cef454b9_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Brand"
    ADD CONSTRAINT "Brand_user_id_cef454b9_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Cart Cart_product_id_7cabc995_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Cart"
    ADD CONSTRAINT "Cart_product_id_7cabc995_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Cart Cart_user_id_c44ac99e_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Cart"
    ADD CONSTRAINT "Cart_user_id_c44ac99e_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Category_subcategory Category_subcategory_category_id_0b8105c6_fk_Category_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Category_subcategory"
    ADD CONSTRAINT "Category_subcategory_category_id_0b8105c6_fk_Category_id" FOREIGN KEY (category_id) REFERENCES public."Category"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Category_subcategory Category_subcategory_subcategories_id_e70e72eb_fk_Sub Categ; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Category_subcategory"
    ADD CONSTRAINT "Category_subcategory_subcategories_id_e70e72eb_fk_Sub Categ" FOREIGN KEY (subcategories_id) REFERENCES public."Sub Category"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Customer Address Customer Address_user_id_e63de8c1_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Customer Address"
    ADD CONSTRAINT "Customer Address_user_id_e63de8c1_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Customer Customer_user_id_b3dbf5c1_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Customer"
    ADD CONSTRAINT "Customer_user_id_b3dbf5c1_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: MPayment MPayment_order_id_eddb263e_fk_Order_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."MPayment"
    ADD CONSTRAINT "MPayment_order_id_eddb263e_fk_Order_id" FOREIGN KEY (order_id) REFERENCES public."Order"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Notification Notification_user_id_27901a99_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Notification"
    ADD CONSTRAINT "Notification_user_id_27901a99_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Order Product Order Product_order_id_6f6a0bb6_fk_Order_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Order Product"
    ADD CONSTRAINT "Order Product_order_id_6f6a0bb6_fk_Order_id" FOREIGN KEY (order_id) REFERENCES public."Order"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Order Product Order Product_product_id_53060350_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Order Product"
    ADD CONSTRAINT "Order Product_product_id_53060350_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Order Order_customer_id_66bfa5c2_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Order"
    ADD CONSTRAINT "Order_customer_id_66bfa5c2_fk_User_id" FOREIGN KEY (customer_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductCategory ProductCategory_product_category_id_4a0af2f3_fk_Category_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductCategory"
    ADD CONSTRAINT "ProductCategory_product_category_id_4a0af2f3_fk_Category_id" FOREIGN KEY (product_category_id) REFERENCES public."Category"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductCategory ProductCategory_product_id_6583d383_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductCategory"
    ADD CONSTRAINT "ProductCategory_product_id_6583d383_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductCategory ProductCategory_product_sub_category_c0f6ba0a_fk_Sub Categ; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductCategory"
    ADD CONSTRAINT "ProductCategory_product_sub_category_c0f6ba0a_fk_Sub Categ" FOREIGN KEY (product_sub_category_id) REFERENCES public."Sub Category"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductColour ProductColour_product_color_id_7c50be15_fk_Colour_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductColour"
    ADD CONSTRAINT "ProductColour_product_color_id_7c50be15_fk_Colour_id" FOREIGN KEY (product_color_id) REFERENCES public."Colour"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductColour ProductColour_product_id_d937b171_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductColour"
    ADD CONSTRAINT "ProductColour_product_id_d937b171_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductDeal ProductDeal_product_deals_id_c33db44a_fk_Deal_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductDeal"
    ADD CONSTRAINT "ProductDeal_product_deals_id_c33db44a_fk_Deal_id" FOREIGN KEY (product_deals_id) REFERENCES public."Deal"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductDeal ProductDeal_product_id_a4ccdf90_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductDeal"
    ADD CONSTRAINT "ProductDeal_product_id_a4ccdf90_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductDescription ProductDescription_product_id_3348b974_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductDescription"
    ADD CONSTRAINT "ProductDescription_product_id_3348b974_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductImage ProductImage_product_id_f70724f4_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductImage"
    ADD CONSTRAINT "ProductImage_product_id_f70724f4_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductQuestion ProductQuestion_product_id_b4c89073_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductQuestion"
    ADD CONSTRAINT "ProductQuestion_product_id_b4c89073_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductQuestion ProductQuestion_user_id_f30fed50_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductQuestion"
    ADD CONSTRAINT "ProductQuestion_user_id_f30fed50_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductReview ProductReview_deal_id_02ebaf10_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductReview"
    ADD CONSTRAINT "ProductReview_deal_id_02ebaf10_fk_Product_id" FOREIGN KEY (deal_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductSize ProductSize_product_id_fdb40400_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSize"
    ADD CONSTRAINT "ProductSize_product_id_fdb40400_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductSize ProductSize_product_size_id_4df409be_fk_Size_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSize"
    ADD CONSTRAINT "ProductSize_product_size_id_4df409be_fk_Size_id" FOREIGN KEY (product_size_id) REFERENCES public."Size"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ProductSpecification ProductSpecification_product_id_3aa7ca57_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."ProductSpecification"
    ADD CONSTRAINT "ProductSpecification_product_id_3aa7ca57_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Product Product_brand_id_bb588269_fk_Brand_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_brand_id_bb588269_fk_Brand_id" FOREIGN KEY (brand_id) REFERENCES public."Brand"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Product Product_store_id_65a88807_fk_Store_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_store_id_65a88807_fk_Store_id" FOREIGN KEY (store_id) REFERENCES public."Store"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Product_sub_product Product_sub_product_product_id_4d893218_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_sub_product"
    ADD CONSTRAINT "Product_sub_product_product_id_4d893218_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Product_sub_product Product_sub_product_subproduct_id_0b614770_fk_product_s; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_sub_product"
    ADD CONSTRAINT "Product_sub_product_subproduct_id_0b614770_fk_product_s" FOREIGN KEY (subproduct_id) REFERENCES public.product_subproduct(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Product_tags Product_tags_product_id_009fa4e2_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_tags"
    ADD CONSTRAINT "Product_tags_product_id_009fa4e2_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Product_tags Product_tags_tag_id_fc2895ef_fk_Tag_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Product_tags"
    ADD CONSTRAINT "Product_tags_tag_id_fc2895ef_fk_Tag_id" FOREIGN KEY (tag_id) REFERENCES public."Tag"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: StoreOwner StoreOwner_store_id_f36b7389_fk_Store_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."StoreOwner"
    ADD CONSTRAINT "StoreOwner_store_id_f36b7389_fk_Store_id" FOREIGN KEY (store_id) REFERENCES public."Store"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: StoreOwner StoreOwner_user_id_627986d9_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."StoreOwner"
    ADD CONSTRAINT "StoreOwner_user_id_627986d9_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Store Store_owner_id_8c609f25_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."Store"
    ADD CONSTRAINT "Store_owner_id_8c609f25_fk_User_id" FOREIGN KEY (owner_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: User_groups User_groups_group_id_328392a3_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_groups"
    ADD CONSTRAINT "User_groups_group_id_328392a3_fk_auth_group_id" FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: User_groups User_groups_user_id_8f675f72_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_groups"
    ADD CONSTRAINT "User_groups_user_id_8f675f72_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: User_user_permissions User_user_permission_permission_id_8e998ba4_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_user_permissions"
    ADD CONSTRAINT "User_user_permission_permission_id_8e998ba4_fk_auth_perm" FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: User_user_permissions User_user_permissions_user_id_2c6da4d4_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."User_user_permissions"
    ADD CONSTRAINT "User_user_permissions_user_id_2c6da4d4_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: WishList WishList_product_id_6411d132_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."WishList"
    ADD CONSTRAINT "WishList_product_id_6411d132_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: WishList WishList_user_id_e0523ed2_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public."WishList"
    ADD CONSTRAINT "WishList_user_id_e0523ed2_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_User_id" FOREIGN KEY (user_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_bill order_bill_customer_id_3f539083_fk_User_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.order_bill
    ADD CONSTRAINT "order_bill_customer_id_3f539083_fk_User_id" FOREIGN KEY (customer_id) REFERENCES public."User"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: order_bill order_bill_order_id_b8e8cd37_fk_Order_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.order_bill
    ADD CONSTRAINT "order_bill_order_id_b8e8cd37_fk_Order_id" FOREIGN KEY (order_id) REFERENCES public."Order"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: product_specification product_specification_product_id_9bd3432e_fk_Product_id; Type: FK CONSTRAINT; Schema: public; Owner: angaza
--

ALTER TABLE ONLY public.product_specification
    ADD CONSTRAINT "product_specification_product_id_9bd3432e_fk_Product_id" FOREIGN KEY (product_id) REFERENCES public."Product"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

