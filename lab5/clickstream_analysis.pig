clicks = LOAD 'file:///home/cloudera/clickstream.csv'
  USING PigStorage(',')
  AS (uid:chararray, pid:chararray, action:chararray, timestamp:chararray);

products = LOAD 'file:///home/cloudera/products.csv'
  USING PigStorage(',')
  AS (pid:chararray, category:chararray);

purchases = FILTER clicks BY LOWER(action) == 'purchase';

views = FILTER clicks BY LOWER(action)=='view';
views_grouped = GROUP views BY pid;
views_count = FOREACH views_grouped GENERATE group AS pid, COUNT(views) AS view_count;

joined = JOIN view_counts BY pid, products BY pid;

sorted_views = ORDER joined BY view_count DESC;

STORE purchases INTO 'file:///home/cloudera/output_purchases' USING PigStorage(',');
STORE sorted_views INTO 'file:///home/cloudera/output_views' USING PigStorage(',');
