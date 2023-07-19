-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT name, SUM(rate) AS rating
  FROM tv_genres AS genre
       INNER JOIN tv_show_genres AS show
       ON show.genre_id = genre.id

       INNER JOIN tv_show_ratings AS tv
       ON tv.show_id = show.show_id
 GROUP BY name
 ORDER BY rating DESC;
 
