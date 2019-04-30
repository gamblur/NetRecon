from googleapiclient.discovery import build

q = "site:github.com cyber"
domain = "github.com"
fileType = "pdf"
exactTerms = "github.com"
relatedSite = "github.com"
siteSearch = "github.com"

my_cse_id = "017997342119786234129:cctuxygcpgo"
dev_key = "AIzaSyCLtdoZUsabrEofhDx7BBVnTNOsjBOh5aQ"

def google_search(search_term, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=dev_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(q, my_cse_id, num=10, cr="countryIN", lr="lang_en")
for result in results:
    print(result.get('title'))
    print(result.get('link'))
    print(result.get('snippet'))
    print('\n')