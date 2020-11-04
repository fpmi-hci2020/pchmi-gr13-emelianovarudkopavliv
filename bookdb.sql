-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-11-04 16:48:14.61

-- tables
-- Table: account
CREATE TABLE account (
    id int  NOT NULL,
    login varchar(20)  NOT NULL,
    password varchar(50)  NOT NULL,
    name varchar(50)  NULL,
    role varchar(10)  NOT NULL,
    CONSTRAINT account_pk PRIMARY KEY (id)
);

-- Table: book
CREATE TABLE book (
    id int  NOT NULL,
    title varchar(100)  NOT NULL,
    author varchar(100)  NOT NULL,
    genre varchar(20)  NULL,
    description varchar(1000)  NULL,
    price numeric(2,10)  NOT NULL,
    publisher_id int  NOT NULL,
    CONSTRAINT book_pk PRIMARY KEY (id)
);

-- Table: news
CREATE TABLE news (
    id int  NOT NULL,
    title varchar(100)  NOT NULL,
    content varchar(1000)  NOT NULL,
    publisher_id int  NOT NULL,
    CONSTRAINT news_pk PRIMARY KEY (id)
);

-- Table: order
CREATE TABLE "order" (
    id int  NOT NULL,
    paymentMethod varchar(10)  NULL,
    shipmentMethod varchar(10)  NULL,
    type varchar(10)  NOT NULL,
    CONSTRAINT order_pk PRIMARY KEY (id)
);

-- Table: order_account
CREATE TABLE order_account (
    order_id int  NOT NULL,
    account_id int  NOT NULL,
    CONSTRAINT order_account_pk PRIMARY KEY (order_id,account_id)
);

-- Table: order_book
CREATE TABLE order_book (
    order_id int  NOT NULL,
    book_id int  NOT NULL,
    CONSTRAINT order_book_pk PRIMARY KEY (order_id,book_id)
);

-- Table: publisher
CREATE TABLE publisher (
    id int  NOT NULL,
    name varchar(100)  NOT NULL,
    CONSTRAINT publisher_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: book_publisher (table: book)
ALTER TABLE book ADD CONSTRAINT book_publisher
    FOREIGN KEY (publisher_id)
    REFERENCES publisher (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: news_publisher (table: news)
ALTER TABLE news ADD CONSTRAINT news_publisher
    FOREIGN KEY (publisher_id)
    REFERENCES publisher (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: order_account_account (table: order_account)
ALTER TABLE order_account ADD CONSTRAINT order_account_account
    FOREIGN KEY (account_id)
    REFERENCES account (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: order_account_order (table: order_account)
ALTER TABLE order_account ADD CONSTRAINT order_account_order
    FOREIGN KEY (order_id)
    REFERENCES "order" (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: order_book_book (table: order_book)
ALTER TABLE order_book ADD CONSTRAINT order_book_book
    FOREIGN KEY (book_id)
    REFERENCES book (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: order_book_order (table: order_book)
ALTER TABLE order_book ADD CONSTRAINT order_book_order
    FOREIGN KEY (order_id)
    REFERENCES "order" (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- sequences
-- Sequence: account_seq
CREATE SEQUENCE account_seq
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: book_seq
CREATE SEQUENCE book_seq
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: news_seq
CREATE SEQUENCE news_seq
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: order_seq
CREATE SEQUENCE order_seq
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: publisher_seq
CREATE SEQUENCE publisher_seq
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- End of file.

