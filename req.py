import http.client

conn = http.client.HTTPSConnection("www.dnb.com")
payload = ''
headers = {
  'authority': 'www.dnb.com',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
  'accept': '*/*',
  'sec-gpc': '1',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.dnb.com/business-directory/top-results.html?term=marico&page=1',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'chosen_visitorFrom_cookie_new=DIR; HID=1622213872486; drift_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; driftt_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; DMCP=1; _bcvm_vrid_2775810355515379163=648726101229444880T6742C0D0B425ECB757510091BC42867E6A799D64629757287E89CD272F8EA87346D5CF123FD01D3EC8FE1A02739C2F02578B2CF21FA53BC943315EC219E9C85D; SSLB=0; AMCVS_8E4767C25245B0B80A490D4C%40AdobeOrg=1; drift_campaign_refresh=4a4bb7a5-087d-4bd0-960c-97a653f15734; bm_mi=E39DC73ADFEF82928C9D8CBC85E94990~Tn7vEBZovI2Dd2hZD9TH0W/ObdSKyOZcOhfUlGfBMHL66QWubZLRSFXMlvz1Yc/GCUuUX9GcGSJd3cVZNuKCW7O42DSCy98TpgLuqUqCWgu8bea+g6cixT9JbQZ8JCC2BDwliFnEZcVFpCAj3rgBoo1W6wwJY7tqyIU8aQsHbTBN4OVtcpRnf3w4zEzDFQ6JHKkSypoHWKZXAzNdE8IkGhIH0XgE8zijBvcz8JHh9msfI2r9U8Fd9v2k+iT8gOGOmF9zy3R7zWTLEz7X1lT2pg==; bm_sv=2E1F8D8021A09178FC0DB5FADFB74678~Xi6qfE/e00tTtqdx+e29SqZYKBm20TzExsLH0xGzUaphmNosUpoXsbCsv/9ueosooC3Drt84UqTVgWEPtFPfVNT4tF4/s85Lf3U5uR2eq2ViuCGNStXF4eZBytAuDiKxyJ+e5gHN+jRsQJujuBmeNg==; ak_bmsc=7E90BA2D417CA34F1A39291B9CF9B0D2~000000000000000000000000000000~YAAQJ40sMQOVTex5AQAAmIv8Lgzwre8YzrE6CWlqZFT3PMo0v4hE0d4zEA3IBgN6zHfVStXb6cYEMu5JBImBeKmfiTJmOKevsQJefoo6BNFN1OBuYPJfMeszJGnYOtme4hEf6X1TxokUOCKHJeEKI/2EBh6mJLTIFvr4EMbHgGbn4NtNT+kZLQMMAsg/lyiXqY/VO9VOivvYN+VkLr1O/Nos8da9GyOUJzzSqV+nhQnhNrcCF6nBztnvpSi3sgeb7/fNesDwef5iOmfkIorP8jKFfhoGfZrUklA//38IsEkyHqZ8XpobycfGXZI+Wg4WTo9H8EQ0tNQcmgH4XrIx67GA/fnIgcLCdenbuoYd5oHDh25hFt6Zqj92MUL5G5VtnJbKIF8VBEhyPTljubLhkcuP/5nBzFgSRKStONRIbZpQuBWGnMNs/CDYfBFK84+1wjQ7WNk2cvoSjmjt; AWSALB=Zx7IFGkNAupkfnOrytSpk2/+49z0yKg38SMTYTHx/geS0JRcAA+FC/KBNKaD0FiatbnYh032vOb0fqDF7eC2NE05X9RDtgRvl6Yxb34NltQw7a9tlViGzdkgSmyq; AWSALBCORS=Zx7IFGkNAupkfnOrytSpk2/+49z0yKg38SMTYTHx/geS0JRcAA+FC/KBNKaD0FiatbnYh032vOb0fqDF7eC2NE05X9RDtgRvl6Yxb34NltQw7a9tlViGzdkgSmyq; integrated_search_query=marico; AMCV_8E4767C25245B0B80A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C18799%7CMCMID%7C75832162905368450318841924916097556759%7CMCOPTOUT-1624293230s%7CNONE%7CvVersion%7C5.2.0; SSLB=0; AWSALB=QxzjAxvB8/eFIDnT1vToX0NJSlnJ1QVKiNWVqRqw62V4yROCKLo/OIt1xQP8iP19Rx9uxmy/clAj+F5ZtSyFD7YPGL18QaYRdIYkYJVD3A1EjBr7JiO+rYTO4Dky; AWSALBCORS=QxzjAxvB8/eFIDnT1vToX0NJSlnJ1QVKiNWVqRqw62V4yROCKLo/OIt1xQP8iP19Rx9uxmy/clAj+F5ZtSyFD7YPGL18QaYRdIYkYJVD3A1EjBr7JiO+rYTO4Dky'
}
conn.request("GET", "/apps/dnb/thirdparty/dnbdirectutil?limited=false&captchaDone=true&pageSize=5&pageNumber=1&criteriasearch=true&searchTerm=motherson", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))