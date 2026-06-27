SELECT attrition, ROUND(AVG(monthlyincome),2) AS Salario
FROM HR
GROUP BY attrition;