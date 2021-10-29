--
-- File generated with SQLiteStudio v3.3.3 on jue. oct. 28 23:18:30 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: activities
CREATE TABLE activities (activity_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, activity_course INTEGER REFERENCES courses (course_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, activity_name VARCHAR (32) NOT NULL, activity_description VARCHAR (64) NOT NULL, activity_deadline DATETIME NOT NULL, activity_note DECIMAL DEFAULT (5) NOT NULL);
INSERT INTO activities (activity_id, activity_course, activity_name, activity_description, activity_deadline, activity_note) VALUES (1, 1, 'diagramas de flujo', 'desarrollar un diagrama de flujo, acorde a la tarea asignada', '2021-10-26', 5);
INSERT INTO activities (activity_id, activity_course, activity_name, activity_description, activity_deadline, activity_note) VALUES (2, 1, 'algoritmia básica', 'desarrollo deprocedimientos simples mediante pasos estructurados y lógicos', '2021-12-01', 5);

-- Table: comments
CREATE TABLE comments (comment_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, comment_body VARCHAR (128) NOT NULL, comment_user INTEGER REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, comment_activity INTEGER REFERENCES activities (activity_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, comment_to INTEGER REFERENCES comments (comment_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL);

-- Table: courses
CREATE TABLE courses (course_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, course_professor INTEGER REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE, course_name VARCHAR (32) NOT NULL, course_description VARCHAR (64) NOT NULL, course_schedule DATETIME NOT NULL, course_limit INTEGER (2) DEFAULT (20) NOT NULL);
INSERT INTO courses (course_id, course_professor, course_name, course_description, course_schedule, course_limit) VALUES (1, 8, 'programación básica', 'Programación básica, tocando temas como algoritmia, varaibles, tipos de datos y otros', '2021-10-24', 15);
INSERT INTO courses (course_id, course_professor, course_name, course_description, course_schedule, course_limit) VALUES (2, 12, 'programacion orientada a objetos', 'Se enseñan los principios básicos de la programacion orientada a objetos mediante ejemplos practicos', '2021-10-28', 15);

-- Table: roles
CREATE TABLE roles (role_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, role_name STRING (20) NOT NULL);
INSERT INTO roles (role_id, role_name) VALUES (1, 'ADMINISTRADOR');
INSERT INTO roles (role_id, role_name) VALUES (2, 'PROFESOR');
INSERT INTO roles (role_id, role_name) VALUES (3, 'ESTUDIANTE');

-- Table: users
CREATE TABLE users (user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, user_role INTEGER (1) NOT NULL, user_name STRING (32) NOT NULL, user_lastname STRING (32) NOT NULL, user_dateborn DATETIME, user_email VARCHAR (64) UNIQUE NOT NULL, user_phone NUMERIC UNIQUE, user_password STRING (64), user_active BOOLEAN DEFAULT (TRUE), create_at DATETIME DEFAULT (CURRENT_TIMESTAMP));
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (1, 1, 'Edwin Fernando', 'Marroquin Bustos', '1984-08-17', 'marrokin2@gmail.com', 4004567891, '286d9278d5d0ac2cb070b3eb026fdd5b411462589c443a37f0c81a528feb5a7d', 1, '2021-10-23 02:09:57');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (2, 3, 'Mauro', 'Simon', '1980-08-23', 'mauro.simon@example.com', 3009876542, '63d9so9u935', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (3, 3, 'Alba', 'Jimenez', '2001-10-12', 'alba.jimenez@example.com', 2001824931, 'sekvmlwuoj', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (4, 3, 'Bartosz', 'Baumann', '2003-01-02', 'bartosz.baumann@example.com', 1004568263, 'xiskp61oxha', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (5, 3, 'Caroline', 'Madsen', '1979-10-10', 'caroline.madsen@example.com', 2507943682, 'wnb2h1y2ce', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (6, 3, 'Sophia', 'Riviere', '1928-12-12', 'sophia.riviere@example.com', 1804268379, 'k88v5zf7bgs', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (7, 2, 'Marianne', 'Ross', '1922-01-05', 'marianne.ross@example.com', 7004852935, 'z953moqoib', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (8, 2, 'Tonya', 'Lewis', '1975-07-05', 'tonya.lewis@example.com', 4001567891, 'ag31tb7zkhf', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (9, 2, 'Erika', 'Skrede', '1952-05-02', 'erika.skrede@example.com', 3019876542, 'ib1yiofiquj', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (10, 3, 'Daniel', 'Manninen', '1962-06-02', 'daniel.manninen@example.com', 2011824931, 'h6w2f4mqcd', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (11, 2, 'Emily', 'Poulsen', '1978-08-07', 'emily.poulsen@example.com', 1014568263, 'yixsbha1ru8', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (12, 2, 'Vernon', 'Kelly', '1972-11-01', 'vernon.kelly@example.com', 2527943682, 'mtsnh3bo8y', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (13, 3, 'David', 'Taylor', '1944-01-03', 'david.taylor@example.com', 1834268379, 'yx5bw9m3fqo', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (14, 3, 'Mason', 'Bélanger', '1917-12-31', 'mason.belanger@example.com', 7034852935, '4rvq8sg88aq', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (15, 3, 'Emily', 'Pedersen', '1975-08-28', 'emily.pedersen@example.com', 4034567891, 'cujrb592fea', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (16, 2, 'Lily', 'Gauthier', '2012-02-27', 'lily.gauthier@example.com', 3059876542, '8204gxfqo7y', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (17, 3, 'Valdemar', 'Poulsen', '1964-12-08', 'valdemar.poulsen@example.com', 2051824931, 'bbscojj9via', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (18, 3, 'Ivan', 'Bryant', '1970-01-14', 'ivan.bryant@example.com', 1054568263, 'bt8yk7g0oqv', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (19, 3, 'Jardel', 'Barbosa', '1947-08-14', 'jardel.barbosa@example.com', 2567943682, '9qehh1wx80o', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (20, 3, 'Edward', 'Hall', '1926-05-12', 'edward.hall@example.com', 1864268379, 'vxq4flc7w3m', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (21, 3, 'Caleb', 'Hayes', '1926-04-12', 'caleb.hayes@example.com', 7664852935, '5lav0r5vajv', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (22, 3, 'Yassmina', 'Medendorp', '1960-09-23', 'yassmina.medendorp@example.com', 4651234567, 'ch5cjblsrpf', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (23, 3, 'Aurelio', 'Carpentier', '1973-12-13', 'aurelio.carpentier@example.com', 9287891234, 'uad1kljqt1', 1, '25-10-2021 12:18:28');
INSERT INTO users (user_id, user_role, user_name, user_lastname, user_dateborn, user_email, user_phone, user_password, user_active, create_at) VALUES (24, 1, 'Diego Edison', 'Marroquin Bustos', '1987-10-31', 'bumarroco@gmail.com', 3213764482, 'aaf197f37e13926359d3b473b03a63eb0eade707030f815c947180cbd484817c', 1, '2021-10-28 19:52:53');

-- Table: users_activities
CREATE TABLE users_activities (id INTEGER PRIMARY KEY UNIQUE NOT NULL, user_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, activity_id INTEGER REFERENCES activities (activity_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, activity_send DATETIME, activity_note DECIMAL);

-- Table: users_courses
CREATE TABLE users_courses (id INTEGER PRIMARY KEY UNIQUE NOT NULL, user_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, course_id INTEGER REFERENCES courses (course_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL);
INSERT INTO users_courses (id, user_id, course_id) VALUES (1, 3, 1);
INSERT INTO users_courses (id, user_id, course_id) VALUES (2, 10, 1);
INSERT INTO users_courses (id, user_id, course_id) VALUES (3, 4, 2);
INSERT INTO users_courses (id, user_id, course_id) VALUES (4, 23, 2);

-- View: count_activities
CREATE VIEW count_activities AS SELECT COUNT(activity_id) FROM activities;

-- View: count_courses
CREATE VIEW count_courses AS SELECT COUNT(course_id) from courses;

-- View: count_professors
CREATE VIEW count_professors AS SELECT COUNT(user_id) FROM users WHERE user_role=2;

-- View: count_students
CREATE VIEW count_students AS SELECT COUNT(user_id) FROM users WHERE user_role=3;

-- View: count_users
CREATE VIEW count_users AS SELECT COUNT(*) FROM users;

-- View: view_activities
CREATE VIEW view_activities AS SELECT activities.activity_id, activities.activity_name, activities.activity_description, courses.course_name, activities.activity_deadline, activities.activity_note FROM activities, courses WHERE courses.course_id=activities.activity_course;

-- View: view_admins
CREATE VIEW view_admins AS SELECT * FROM users WHERE user_role=1;

-- View: view_courses
CREATE VIEW view_courses AS select courses.course_id, users.user_name, users.user_lastname, courses.course_name, courses.course_schedule
from users, courses
where users.user_id=courses.course_professor;

-- View: view_professors
CREATE VIEW view_professors AS SELECT users.user_id, roles.role_name, users.user_lastname, users.user_name, users.user_email FROM roles, users WHERE users.user_role= roles.role_id and users.user_role=2;

-- View: view_students
CREATE VIEW view_students AS SELECT users.user_id,roles.role_name, users.user_lastname, users.user_name, users.user_email 
FROM roles, users WHERE users.user_role= roles.role_id and users.user_role=3;

-- View: view_users
CREATE VIEW view_users AS SELECT users.user_id,roles.role_name, users.user_lastname, users.user_name, users.user_email FROM roles, users WHERE users.user_role= roles.role_id;

-- View: view_users_course
CREATE VIEW view_users_course AS select users.user_id, users.user_name,users.user_lastname, courses.course_id, courses.course_name, courses.course_schedule 
    from users, courses, users_courses
    where users.user_id=users_courses.user_id and courses.course_id=users_courses.course_id 
    group by users_courses.user_id 
    order by users_courses.course_id;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
