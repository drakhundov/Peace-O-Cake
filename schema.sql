CREATE TABLE IF NOT EXISTS jobs (
    "id" INTEGER,
    "title" VARCHAR(100),
    "company" VARCHAR(100),
    "description" VARCHAR(255),
    "salary" INTEGER,
    PRIMARY KEY("id")
);

CREATE INDEX "jobs_index" ON "jobs" (
    "title",
    "company",
    "description"
);
