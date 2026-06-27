-- taxa de turnover 
CREATE VIEW vw_Desligados AS 
SELECT * FROM HR
WHERE attrition = 'Yes';

CREATE VIEW vw_Ativos AS 
SELECT * FROM HR
WHERE attrition = 'No';

SELECT ROUND(CAST(COUNT(d.employeenumber) AS FLOAT)/NULLIF(COUNT(HR.employeenumber), 0),2) AS TurnoverGeral FROM HR
FULL JOIN vw_Desligados AS d
ON HR.employeenumber = d.employeenumber;

SELECT COUNT(*) FROM HR;

SELECT department, COUNT(*), ROUND(COUNT(*)/1470.0,3)*100 AS TurnoverDept 
FROM vw_Desligados
GROUP BY department;

SELECT jobrole, COUNT(*), ROUND(COUNT(*)/1470.0,3)*100 AS TurnoverRole
FROM vw_Desligados
GROUP BY jobrole;

SELECT COUNT(*), ROUND(COUNT(*)/1470.0,3)*100 AS TurnoverAge,
CASE WHEN age < 25 THEN 'Jovem'
WHEN age BETWEEN 25 AND 50 THEN 'Adulto'
ELSE 'Idoso'
END AS ClassAge
FROM vw_Desligados
GROUP BY ClassAge;