import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

TAG_FIELDS = [
    'title', 'header', 'paragraph', 'section', 'footer',
    'hyperlink', 'image', 'unordered_list', 'ordered_list', 'working-urls'
]
TAG_COLUMN_NAMES = {tag: f'Used {tag.replace("_", " ").capitalize()} Tag' for tag in TAG_FIELDS}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

def is_valid_url(url, referer):
    try:
        dynamic_headers = HEADERS.copy()
        dynamic_headers['Referer'] = referer
        r = requests.get(url, allow_redirects=True, headers=dynamic_headers, timeout=5)
        if r.status_code == 403:
            print("\t WARNING:", r.status_code, url)
            return True
        return r.ok
    except Exception as e:
        print(f"Error on {url}: {e}")
        return False

def check_tag(soup, tags):
    return any(soup.find(tag) for tag in tags)

def check_working_urls(soup, tag, attr, base_url):
    urls = []

    for el in soup.find_all(tag):
        value = el.get(attr)

        if tag == 'img' and (not value or value.startswith('data:image') or value.strip() == ''):
            value = el.get('data-src')

        if value:
            absolute_url = urljoin(base_url, value)
            urls.append(absolute_url)

    return any(is_valid_url(u, referer=base_url) for u in urls)

def grade_website(html, base_url):
    from grading_utils import TAG_COLUMN_NAMES

    soup = BeautifulSoup(html, 'html.parser')
    line_count = len(html.strip().split('\n'))

    tag_results = {
        'title': check_tag(soup, ['title']),
        'header': check_tag(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']),
        'paragraph': check_tag(soup, ['p']),
        'section': check_tag(soup, ['section']),
        'footer': check_tag(soup, ['footer']),
        'unordered_list': check_tag(soup, ['ul']),
        'ordered_list': check_tag(soup, ['ol']),
        'image': check_tag(soup, ['img']),
        'hyperlink': check_tag(soup, ['a']),
        'working-urls': check_working_urls(soup, 'a', 'href', base_url) and check_working_urls(soup, 'img', 'src', base_url)
    }

    tag_points = {TAG_COLUMN_NAMES[tag]: int(present) for tag, present in tag_results.items()}

    css_used = bool(
        soup.find('link', rel='stylesheet') or
        soup.find('style') or
        any('style=' in str(tag) for tag in soup.find_all())
    )

    return {
        'Reachable': 60,
        'Line Count': line_count,
        'Line Count >= 50': 10 if line_count >= 50 else 0,
        'Line Count > 100': 10 if line_count > 100 else 0,
        'CSS Used': 10 if css_used else 0,
        **tag_points
    }, tag_results
