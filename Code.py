import requests
import json
from difflib import SequenceMatcher

API_URL = "https://devapi.beyondchats.com/api/get_message_with_sources"

def fetch_data(api_url):
    """Fetch data from the paginated API"""
    data = []
    page = 1
    while True:
        response = requests.get(f"{api_url}?page={page}")
        if response.status_code != 200:
            break
        page_data = response.json()
        if not page_data:
            break
        data.extend(page_data)
        page += 1
    return data

def find_citations(response_text, sources):
    """Find the sources for a given response text"""
    citations = []
    for source in sources:
        if source['context'].strip() in response_text:
            citations.append({
                "id": source['id'],
                "link": source.get('link', '')
            })
    return citations

def process_data(data):
    """Process the data to find citations for each response"""
    result = []
    for item in data:
        response_text = item['response']
        sources = item['source']
        citations = find_citations(response_text, sources)
        result.append({
            "response": response_text,
            "citations": citations
        })
    return result

def main():
    data = fetch_data(API_URL)
    result = process_data(data)
    with open('citations.json', 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    main()
