SELECT A.docid, B.docid, SUM(A.count * B.count) 
FROM frequency AS A,frequency AS B 
-- WHERE A.term = B.term AND A.docid = '10080_txt_crude' AND B.docid =  '17035_txt_earn'
GROUP BY A.docid, B.docid;
