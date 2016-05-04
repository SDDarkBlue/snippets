-- snap two points to a line geometry, and calculate
-- the length of the subline
SELECT
  ST_Length(ST_GeographyFromText(ST_AsText(ST_Line_Substring(line,ST_Line_Locate_Point(line,ST_ClosestPoint(line,fpt)),ST_Line_Locate_Point(line,ST_ClosestPoint(line,tpt)))))) As length_in_m,
FROM ( 
  select a.location::geometry as fpt,
  b.location::geometry as tpt,
  c.geom as line
  from app_station as a, 
  app_station as b, 
  app_lineriver as c 
  where a.name='antwerp-1' and b.name='gent-1' and c.name='schelde'
) As foo;

-- now do the same, but use a multiline geometry instead of a line
SELECT 
ST_Line_Substring(line,ST_Line_Locate_Point(line,ST_ClosestPoint(line,fpt)),ST_Line_Locate_Point(line,ST_ClosestPoint(line,tpt)))
FROM ( 
  select a.location::geometry as fpt,
  b.location::geometry as tpt,
  c.geom as line
  from app_station as a, 
  app_station as b, 
  app_lineriver as c 
  where a.name='antwerp-1' and b.name='faraway-1' and c.name='rivers_flanders'
) As foo;
