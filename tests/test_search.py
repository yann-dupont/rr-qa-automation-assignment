# This is a sample test file. Replace its content with your actual tests.

def test_search(session):
    r = session.get('https://tmdb-discover.surge.sh')
    r.html.render(sleep=5, timeout=30)
    output = r.html.html.encode('utf-8', errors='replace')
