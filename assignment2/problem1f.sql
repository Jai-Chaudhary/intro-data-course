SELECT f1.docid FROM frequency AS f1 INNER JOIN frequency AS f2 WHERE f1.term  = 'transactions' AND f2.term = 'world' AND f1.docid = f2.docid;
