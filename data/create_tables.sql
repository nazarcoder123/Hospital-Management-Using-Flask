CREATE TABLE IF NOT EXISTS patient (
    pat_id SERIAL PRIMARY KEY,
    pat_first_name TEXT NOT NULL,
    pat_last_name TEXT NOT NULL,
    pat_insurance_no TEXT NOT NULL,
    pat_ph_no TEXT NOT NULL,
    pat_date DATE DEFAULT CURRENT_DATE,
    pat_address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS doctor (
    doc_id SERIAL PRIMARY KEY,
    doc_first_name TEXT NOT NULL,
    doc_last_name TEXT NOT NULL,
    doc_ph_no TEXT NOT NULL,
    doc_date DATE DEFAULT CURRENT_DATE,
    doc_address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS nurse (
    nur_id SERIAL PRIMARY KEY,
    nur_first_name TEXT NOT NULL,
    nur_last_name TEXT NOT NULL,
    nur_ph_no TEXT NOT NULL,
    nur_date DATE DEFAULT CURRENT_DATE,
    nur_address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS appointment (
    app_id SERIAL PRIMARY KEY,
    pat_id INTEGER NOT NULL REFERENCES patient(pat_id),
    doc_id INTEGER NOT NULL REFERENCES doctor(doc_id),
    appointment_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS room (
    room_no INTEGER PRIMARY KEY,
    room_type TEXT NOT NULL,
    available INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS medication (
    code INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS department (
    department_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    head_id INTEGER NOT NULL REFERENCES doctor(doc_id)
);

-- Using double quotes for reserved keyword "procedure"
CREATE TABLE IF NOT EXISTS "procedure" (
    code INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    cost INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS undergoes (
    pat_id INTEGER NOT NULL REFERENCES patient(pat_id),
    proc_code INTEGER NOT NULL REFERENCES "procedure"(code),
    u_date DATE NOT NULL,
    doc_id INTEGER REFERENCES doctor(doc_id),
    nur_id INTEGER REFERENCES nurse(nur_id),
    room_no INTEGER REFERENCES room(room_no),
    PRIMARY KEY (pat_id, proc_code, u_date)
);

CREATE TABLE IF NOT EXISTS prescribes (
    doc_id INTEGER REFERENCES doctor(doc_id),
    pat_id INTEGER REFERENCES patient(pat_id),
    med_code INTEGER REFERENCES medication(code),
    p_date DATE NOT NULL,
    app_id INTEGER NOT NULL REFERENCES appointment(app_id),
    dose INTEGER NOT NULL,
    PRIMARY KEY (doc_id, pat_id, med_code, p_date)
);