-- all tasks by _id 
SELECT * FROM tasks WHERE user_id = 1;

-- with status  'new'
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- uodate status with status to  'in progress'
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

--list of users without task
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- addition new task for user 
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Jump ', 'Jump on one feet', 1, 2);

-- get all incompleted task
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- delete task 
DELETE FROM tasks WHERE id = 41;

-- find user with email
SELECT * FROM users WHERE email LIKE '%@example.com';

-- update users name 
UPDATE users SET fullname = 'Clinton Chupakabrov' WHERE id = 2;

-- get number of tasks for status 
SELECT s.name, COUNT(t.id) AS task_count FROM status s LEFT JOIN tasks t ON s.id = t.status_id GROUP BY s.name;

--get the task for user with email 
SELECT t.* FROM tasks t JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%@example.com';

--get tasks list without description 
SELECT * FROM tasks WHERE description IS NULL OR description = '';

-- choose the user and their task with status 'in progress'
SELECT u.fullname, t.title, t.description FROM users u JOIN tasks t ON u.id = t.user_id JOIN status s ON t.status_id = s.id WHERE s.name = 'in progress';

--get users and amount of their tasks
SELECT u.fullname, COUNT(t.id) AS task_count FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.fullname;