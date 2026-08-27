CREATE TABLE "users" (
  "id" integer PRIMARY KEY
);

CREATE TABLE "movies" (
  "id" integer PRIMARY KEY,
  "title" varchar(255) NOT NULL,
  "year" integer
);

CREATE TABLE "genres" (
  "id" integer PRIMARY KEY,
  "name" varchar(100) UNIQUE NOT NULL
);

CREATE TABLE "movie_genres" (
  "movie_id" integer NOT NULL,
  "genre_id" integer NOT NULL,
  PRIMARY KEY ("movie_id", "genre_id")
);

CREATE TABLE "ratings" (
  "user_id" integer NOT NULL,
  "movie_id" integer NOT NULL,
  "rating" real NOT NULL,
  "rated_at" timestamp NOT NULL,
  PRIMARY KEY ("user_id", "movie_id")
);

ALTER TABLE "ratings" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "ratings" ADD FOREIGN KEY ("movie_id") REFERENCES "movies" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "movie_genres" ADD FOREIGN KEY ("movie_id") REFERENCES "movies" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "movie_genres" ADD FOREIGN KEY ("genre_id") REFERENCES "genres" ("id") DEFERRABLE INITIALLY IMMEDIATE;
