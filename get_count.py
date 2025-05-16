import requests

# List of your WordPress site URLs (no trailing slashes)
wordpress_sites = [
    # Add your sites here

    # India sitees

    "https://factcrescendo.com",
    "https://english.factcrescendo.com",
    "https://marathi.factcrescendo.com",
    "https://malayalam.factcrescendo.com",
    "https://tamil.factcrescendo.com",
    "https://gujarati.factcrescendo.com",
    "https://odia.factcrescendo.com",
    "https://assamese.factcrescendo.com",
    "https://bangla.factcrescendo.com",
    "https://manipuri.factcrescendo.com",

    # APAC Sites

    "https://afghanistan.factcrescendo.com",
    "https://afghanistan.factcrescendo.com/pashto",
    "https://srilanka.factcrescendo.com",
    "https://cambodia.factcrescendo.com",
    "https://myanmar.factcrescendo.com",
    "https://afghanistan.factcrescendo.com/english",
    "https://bangladesh.factcrescendo.com",
    "https://srilanka.factcrescendo.com/tamil",
    "https://cambodia.factcrescendo.com/english",
    "https://myanmar.factcrescendo.com/english",
    "https://srilanka.factcrescendo.com/english",
    "https://thailand.factcrescendo.com",
    "https://thailand.factcrescendo.com/english",
]

def get_post_count(site_url):
    try:
        api_url = f"{site_url}/wp-json/wp/v2/posts?per_page=1"
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        total_posts = int(response.headers.get('X-WP-Total', 0))
        return total_posts
    except Exception as e:
        print(f"Error fetching from {site_url}: {e}")
        return 0

def main():
    total = 0
    for site in wordpress_sites:
        count = get_post_count(site)
        print(f"{site} → {count} posts")
        total += count
    print(f"\n🧮 Total posts across all sites: {total}")

if __name__ == "__main__":
    main()
