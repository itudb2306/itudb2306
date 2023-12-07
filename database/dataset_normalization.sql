select parkname, country, state, city from parks where state is null or city is null;

UPDATE parks
SET country = 'US',
    state = 'IL',
    city = 'Chicago'
WHERE parkname = '23rd Street Grounds';

UPDATE parks
SET city = 'Richmond',
    state = 'VA',
    country = 'US'
WHERE parkname = 'Allen Pasture';

UPDATE parks
SET city = 'Arlington',
    state = 'TX',
    country = 'US'
WHERE parkname = 'Ameriquest Field';

UPDATE parks
SET city = 'Anaheim',
    state = 'CA',
    country = 'US'
WHERE parkname = 'Anaheim Stadium';

UPDATE parks
SET city = 'Anaheim',
    state = 'CA',
    country = 'US'
WHERE parkname = 'Angel Stadium';

-- anaheim'den 2 tane var, teams'i de güncelle

UPDATE parks
SET country = 'US',
    state = 'PA',
    city = 'Philadelphia'
WHERE parkname = 'Centennial Grounds';

UPDATE parks
SET country = 'PR',
    state = 'NULL',
    city = 'San Juan'
WHERE parkname = 'Estadio Hiram Bithorn';

UPDATE parks
SET country = 'US',
    state = 'DC',
    city = 'Washington D.C.'
WHERE parkname = 'Nationals Park';

UPDATE parks
SET country = 'US',
    state = 'CA',
    city = 'Los Angeles'
WHERE parkname = 'Olympics Grounds';

UPDATE parks
SET country = 'US',
    state = 'MO',
    city = 'St. Louis'
WHERE parkname = 'Red Stocking Baseball Park';

UPDATE parks
SET country = 'US',
    state = 'NY',
    city = 'Brooklyn'
    parkname = 'Union Grounds'
WHERE parkname = 'Union Grounds (Brooklyn)';