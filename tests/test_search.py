
def test_seach(session):
    r = session.get('https://tmdb-discover.surge.sh')
    r.html.render(sleep=5, timeout=30)
    output = r.html.html.encode('utf-8', errors='replace')
