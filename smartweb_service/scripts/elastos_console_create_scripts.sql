set schema 'public';

CREATE TABLE IF NOT EXISTS COUNTRY(
   ID INTEGER PRIMARY KEY NOT NULL,
   NAME VARCHAR(20) NOT NULL,
   UNIQUE(ID, NAME)
);

CREATE TABLE IF NOT EXISTS USER_TYPE(
   ID INTEGER PRIMARY KEY NOT NULL,
   TYPE VARCHAR(20) NOT NULL,
   UNIQUE(ID, TYPE)
);

CREATE TABLE IF NOT EXISTS USERS(
   ID INTEGER PRIMARY KEY NOT NULL,
   USER_ID VARCHAR(20) NOT NULL,
   DID VARCHAR(50) NOT NULL,
   NAME VARCHAR(80)  NOT NULL,
   EMAIL VARCHAR(30) NOT NULL,
   ORGANIZATION VARCHAR(50),
   PHONE_NUMBER BIGINT,
   CITY VARCHAR(20) NOT NULL,
   COUNTRY INTEGER NOT NULL,
   USER_TYPE INTEGER NOT NULL,
   CREATED_ON TIMESTAMP NOT NULL,
   LAST_LOGGED_ON TIMESTAMP NOT NULL,
   UNIQUE(ID, DID),
   FOREIGN KEY (COUNTRY) REFERENCES COUNTRY(ID),
   FOREIGN KEY (USER_TYPE) REFERENCES USER_TYPE(ID)
);

CREATE TABLE IF NOT EXISTS USER_API_RELATION(
   ID INTEGER PRIMARY KEY NOT NULL,
   USER_ID INTEGER REFERENCES USERS(ID) NOT NULL,
   API_KEY VARCHAR(32) NOT NULL,
   UNIQUE (API_KEY)
);