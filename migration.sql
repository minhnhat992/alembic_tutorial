BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 2cdbd6535f5a

CREATE TABLE account (
    id SERIAL NOT NULL, 
    name VARCHAR(50) NOT NULL, 
    description VARCHAR(200), 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('2cdbd6535f5a') RETURNING alembic_version.version_num;

-- Running upgrade 2cdbd6535f5a -> 79891bffab08

ALTER TABLE account ADD COLUMN last_transaction_date TIMESTAMP WITHOUT TIME ZONE;

UPDATE alembic_version SET version_num='79891bffab08' WHERE alembic_version.version_num = '2cdbd6535f5a';

COMMIT;

