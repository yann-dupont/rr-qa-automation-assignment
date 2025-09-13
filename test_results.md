
# Test results
This is a list of defects found while working on this test framework. Tickets should be created for each of these, using the following format :
- Title
- Prerequisites (software version, OS version, browser if any, ...)
- Context (description of the issue)
- Occurrence frequency (every time, once in five tries ?)
- Steps to reproduce
- Attachments (logs, screenshots, files)
- Exit criteria

### Last pages
On the Popular or Top Rated views, trying to load one of the last few pages (at least the last 3), the page doesn't load.

### Slugs
Trying to load any of these URLs returns Page not Found :
- https://tmdb-discover.surge.sh/popular
- https://tmdb-discover.surge.sh/trend
- https://tmdb-discover.surge.sh/new
- https://tmdb-discover.surge.sh/top

### Selecting movies and TV shows at the same time
In the UI, you can only see movies or TV shows, but not the union of both at the same time.

### Switching from movies to TV shows resets other filters
Applying filters on genre, year or rating, and then switching from movies to TV shows, resets the other filters.

### Switching from movies to TV shows resets search
Searching by title, and then switching from movies to TV shows, resets the search. The search term is still displayed, and clicking the search bar and pressing enter doesn't update the view.

### Searching and filters
If we search by title, filtering by genre, year or rating doesn't work.

### Different number of entries depending on tab
When selecting Popular / Trend / Newest / Top Rated, the total number of entries is not the same, meaning there are missing entries.

### Year maximum
The highest year the UI allows to set for filtering is 2024, although there are 2025 movies.

### Popular -> Trend -> TV shows
After opening the website, clicking on Trend, then filtering on TV shows : filtering doesn't update the view.
Changing the filter back to movies fixes it.
