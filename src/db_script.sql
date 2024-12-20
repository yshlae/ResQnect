CREATE DATABASE DisasterResponseDB;
USE DisasterResponseDB;

CREATE TABLE Volunteers (
    volunteer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    v_type ENUM('medical', 'rescue', 'general') NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE Resources (
    resource_id INT PRIMARY KEY AUTO_INCREMENT,
    r_type VARCHAR(50) NOT NULL,
    quantity DECIMAL(10, 2) DEFAULT 0
);

CREATE TABLE Tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    task_type ENUM('rescue', 'medical', 'food distribution') NOT NULL,
    volunteer_id INT,
    status VARCHAR(20) DEFAULT 'Assigned',
    assigned_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    completion_time DATETIME,
    FOREIGN KEY (volunteer_id) REFERENCES Volunteers(volunteer_id)
);

INSERT INTO Volunteers (name, v_type, available) VALUES
('Wennie Cascalla', 'medical', TRUE),
('John Loyd Bunyi', 'rescue', TRUE),
('Marianito Frane', 'general', TRUE),
('Rayla Qui', 'medical', TRUE),
('Poul Aranas', 'rescue', TRUE),
('Kyle Banaag', 'general', TRUE),
('Lei Salvador', 'general', TRUE),
('Edsel Rosales', 'rescue', TRUE),
('Glennzel Gonda', 'rescue', TRUE),
('Romulo Rosales', 'medical', TRUE);

INSERT INTO Resources (r_type, quantity) VALUES
('Water', 1000),
('Food', 500),
('Medicine', 200),
('Blankets', 100),
('Money', 15000),
('First Aid Kits', 50),
('Rescue Boats', 5),
('Tents', 30),
('Masks', 300),
('Sanitizers', 250);

INSERT INTO Tasks (task_type, volunteer_id, status, completion_time) VALUES
('rescue', 1, 'Completed', '2024-11-10 14:00:00'),
('medical', 2, 'In Progress', NULL),
('food distribution', 3, 'Assigned', NULL),
('rescue', 4, 'Completed', '2024-11-11 09:30:00'),
('medical', 5, 'Assigned', NULL),
('food distribution', 6, 'Completed', '2024-11-09 16:45:00'),
('rescue', 7, 'In Progress', NULL),
('medical', 8, 'Assigned', NULL),
('food distribution', 9, 'Completed', '2024-11-12 11:20:00'),
('rescue', 10, 'Completed', '2024-11-12 13:30:00');

SELECT 
    T.task_id,
    T.task_type,
    T.status,
    V.name AS volunteer_name,
    R.r_type AS resource_type
FROM 
    Tasks T
LEFT JOIN Volunteers V ON T.volunteer_id = V.volunteer_id
LEFT JOIN Resources R ON T.task_type = R.r_type;

UPDATE Volunteers
SET available = FALSE
WHERE name = 'John Loyd Bunyi';

DELETE FROM Resources
WHERE r_type = 'Masks';

SELECT 
    SUM(quantity) AS total_resources
FROM 
    Resources;

SELECT 
    V.volunteer_id,
    V.name,
    COUNT(T.task_id) AS completed_tasks
FROM 
    Volunteers V
INNER JOIN Tasks T ON V.volunteer_id = T.volunteer_id
WHERE 
    T.status = 'Completed'
GROUP BY 
    V.volunteer_id, V.name
HAVING 
    COUNT(T.task_id) > 0
ORDER BY 
    completed_tasks DESC;
