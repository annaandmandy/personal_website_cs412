from django.shortcuts import render
import os
from groq import Groq
import requests
from datetime import date
import random
import re
from django.conf import settings

# Create your views here.
def quotes(request):
    try:
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        seed = random.randint(1, 100)
        prompt = f"""
        You have a numbered list of at least 100 famous historical figures.
        Select the person at position #{seed} from your list.
        Then output one of their most well-known quotes, strictly formatted as:
        "Quote text" — Author Name
        """
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=1,
        top_p=1.0
        )
        quote_all = chat_completion.choices[0].message.content
        match = re.search(r'"(.+?)"\s*[—-]\s*(.+)', quote_all)
        if match:
            quote = f"\"{match.group(1).strip()}\" — {match.group(2).strip()}"
        else:
             quote = quote_all
        # quote = quote_all.split(":")[-1].strip()
        image_not_found = False
        img_person = "William Shakespeare"
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/William_Shakespeare_by_John_Taylor%2C_edited.jpg/500px-William_Shakespeare_by_John_Taylor%2C_edited.jpg"
    except Exception as e:
        quote = "\"To be, or not to be.\" - William Shakespeare"
        image_not_found = False
        img_person = "William Shakespeare"
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/William_Shakespeare_by_John_Taylor%2C_edited.jpg/500px-William_Shakespeare_by_John_Taylor%2C_edited.jpg"
    
    if ' — ' in quote:
            img_person = quote.split('—')[1].strip()
            # go to wiki and search for person's image
            wiki_url = f"https://en.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'titles': img_person,
                'prop': 'pageimages',
                'format': 'json',
                'pithumbsize': 500
            }
            headers = {
                'User-Agent': 'QuoteApp/1.0 (https://example.com/contact)'
            }
            wiki_response = requests.get(wiki_url, params=params,  headers=headers)
            wiki_data = wiki_response.json()
            pages = wiki_data.get('query', {}).get('pages', {})
            image_url = None
            image_not_found = True
            for page_id, page_data in pages.items():
                if 'missing' not in page_data and 'thumbnail' in page_data:
                    image_url = page_data['thumbnail']['source']
                    image_not_found = False
                    break
    else:
        img_person = "Unknown Author"
        image_url = None
        image_not_found = True

    try:
        quotes_file = os.path.join(settings.BASE_DIR, "quotes", "quotes.txt")
        if not os.path.exists(quotes_file):
            open(quotes_file, 'w').close()
        with open(quotes_file, 'r', encoding='utf-8') as f:
            existing_quotes = set(line.strip() for line in f if line.strip())
        if quote not in existing_quotes:
            with open(quotes_file, 'a', encoding='utf-8') as f:
                f.write(quote + "\n") 
    except Exception as e:
        print("Error writing to quotes.txt:", e)
    
    return render(request, 'quotes/quoteofaday.html', {
    'quote': quote, 
    'img_person': img_person,
    'image_url': image_url, 
    'image_not_found': image_not_found,
    'img_person': img_person,
    'existing_quotes': existing_quotes
})

def showall(request):
    quotes_file = os.path.join(settings.BASE_DIR, "quotes", "quotes.txt")
    if not os.path.exists(quotes_file):
        open(quotes_file, 'w').close()
    with open(quotes_file, 'r', encoding='utf-8') as f:
        existing_quotes = set(line.strip() for line in f if line.strip())
    return render(request, 'quotes/show_all.html', {'existing_quotes':existing_quotes})