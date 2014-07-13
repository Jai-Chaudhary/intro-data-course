SELECT A.docid, B.docid, SUM(A.count * B.count) AS similarity
FROM 
(SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) AS A,
frequency AS B
WHERE A.term = B.term AND A.docid = 'q'
GROUP BY A.docid, B.docid
ORDER BY similarity DESC
LIMIT 10;
