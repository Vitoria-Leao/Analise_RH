SELECT attrition, yearsatcompany
FROM HR 
WHERE attrition = 'Yes';

SELECT attrition, yearsatcompany
FROM HR 
GROUP BY attrition;