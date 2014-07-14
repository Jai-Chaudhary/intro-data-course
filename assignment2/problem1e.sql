SELECT * FROM (SELECT docid FROM frequency GROUP BY docid HAVING SUM(count) > 300);
