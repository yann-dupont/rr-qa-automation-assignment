# Test Case Description

Every test case will use the API to get a list of movies according to certain parameters (filtering, page number, ...).
The result of the API call would be compared to a reference result, in the case where the database of the website did not change, but of course this is unlikely to be the case. As such, the results will instead be check of coherence (do the movies we get correspond to the criteria we used to filter ?).

## Unit tests
### Filtering by type
- Movies
- TV Shows

### Filtering by genre
- Action
- Adventure, Documentary
- Every genre at the same time

### Filtering by year
- 1900 to 2025
- 1995 to 2010
- 2000 to 2000
- 2001 to 2000
- 1000 to 2000
- -1000 to 2000
- 2000 to 2030
- 2000 to 3000
- 2000 to 9999999999999
- 2000.5 to 2025
- abc to def
- $%? to &*È

### Rating
- 0 and up
- 3 and up
- 5 and up
- 2.5 and up
- 2.222 and up
- -1 and up
- 10 and up
- abc and up
- $%? and up

### Search
- Superman
- Super
- lsdifhbsdfjkl
- (empty string)
- (whitespace)
- a
- aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- 123
- #$%?&*(

### Pagination
- Next page
- Page 10
- Page 1000
- Last page

### Slugs
- Base URL
- Popular
- Trend
- Newest
- Top rated

## Component integration tests
- A few test cases that make queries that are the union of two or more of the previous test cases
- A few test cases that make several queries of the previous test cases in a row

## Performance tests
- Measure response time on a query that returns just a few movies
- Measure response time on a query that returns every movie
- Measure response time on a query for page 10000
