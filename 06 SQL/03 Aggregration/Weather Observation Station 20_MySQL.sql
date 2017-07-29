SELECT CAST(LAT_N AS DECIMAL (7,4))
FROM
	(select lat_n, @row_num:=@row_num+1 rownu from station, (select @row_num:=0) t order by lat_n
	 ) AS X
WHERE ROWNU = ( SELECT ROUND((COUNT(LAT_N)+1)/2,0) 
				FROM STATION
			   );
