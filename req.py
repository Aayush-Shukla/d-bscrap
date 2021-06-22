import http.client
import json

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
  'referer': 'https://www.dnb.com/business-directory/top-results.html?term=alphabet&page=1',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'chosen_visitorFrom_cookie_new=DIR; HID=1622213872486; drift_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; driftt_aid=fd01f143-56e2-4af3-80f1-37b95896ac7e; DMCP=1; _bcvm_vrid_2775810355515379163=648726101229444880T6742C0D0B425ECB757510091BC42867E6A799D64629757287E89CD272F8EA87346D5CF123FD01D3EC8FE1A02739C2F02578B2CF21FA53BC943315EC219E9C85D; SSLB=0; ak_bmsc=4C15E8204A7EAB6450D336418140EBBA~000000000000000000000000000000~YAAQJ40sMRUFTux5AQAA0Qq0MQxt5GVPbVe9ciBgcACJhOkOk03VPIUIVWG1s0wgc/BSib00i77yPl3oybravFJbSm22bdsr2/mrhTyZZfF8HE/9IDAMp2nfw+NfrlD5puAc1et4pXwCaifncrAj4q/IDHI3RZPiWQkCslw32iscAyHjygEkBJaRltuip8EzcQMZCPiyAkvX7rDS4D5mW/aHNFmXMfKCOeNtUqKYLUUnYQuXIZvIwdfrAF9501ZxpFBRzjSb9qTQjOquKUD3/a7C8YZtnRzJOqsNr6n8tHYoWfGdjGr/ORtFifhQv15BGCxJrSNt5xW44kg367xsweBgUScOBoHKZNUYVem/qV8g/PZj8Y21KWhm9CST0vxqGr6nx1/r; AMCVS_8E4767C25245B0B80A490D4C%40AdobeOrg=1; drift_campaign_refresh=50799ad7-6046-499d-b950-5fa218ded004; integrated_search_query=alphabet; bm_mi=189B9331BA57C51D28572BD60F56C38A~Tn7vEBZovI2Dd2hZD9TH0bmwDL9uBbZig7yCoiiH2rhY95Yow7GwzIH8q5KeqWFCIQok6Kp6l1AkAJt6HbN/o7eOIN2USvWSHxrnEkWRSms4EiosjAirwEyFu4TNbvZ/7rOMy2TfB644PotgLaC1+tN+/k44CjaTPLuZEd9f6IMG/Dx8K7A2zpQjyPy4Jwy2zhQ+P/MBJ2vPo4OPNN/v7zsN1p2zUytpW50hbQ9PTIVeI/oj0UvkboiaQCkyxUbgRii4DNxfZh/5xv4Ttbfd0g==; AWSALB=mU4et1H7GawHknCnOY8dBmsG8pgtHthzxOl5zjC6zTgVEUwQWgs31CNO0NdMYha44BsPfFotqb+Lo94XHtl2Q6iuga8gbMEtHtN8BeuZMFg7pLgsjgLgQC8Gp8OA; AWSALBCORS=mU4et1H7GawHknCnOY8dBmsG8pgtHthzxOl5zjC6zTgVEUwQWgs31CNO0NdMYha44BsPfFotqb+Lo94XHtl2Q6iuga8gbMEtHtN8BeuZMFg7pLgsjgLgQC8Gp8OA; bm_sv=E563E561D67B35391BEC8F8C4134EFFE~Xi6qfE/e00tTtqdx+e29SoVKZUCsSqFQ92Do4UkeGH4Ukafg0Rk4F6yMXNqEzwlDueOfR3A4whLmIr771fbGNgNiFmui23s2dmRj3HRRooHoDypzaUV/gBKMF7K6VI+7jgJK9+dnFq650ehqKiOHcg==; AMCV_8E4767C25245B0B80A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C18801%7CMCMID%7C75832162905368450318841924916097556759%7CMCOPTOUT-1624338735s%7CNONE%7CvVersion%7C5.2.0; ak_bmsc=4C15E8204A7EAB6450D336418140EBBA~000000000000000000000000000000~YAAQJ40sMSMGTux5AQAAnhS7MQz2CDTJBR8ir1SDDWenDUvmScAB/f23z4aFH0bv4YsFWOZhhUcJwcT4UgTidKvlD1rrNTD4pYHsuq2uW3df2Rmsoh4Wcg5XiYQTAZngdqFRzVKfXIH1TKJao+UMgc42E0opkZ7ErrZtutmGWgpdgS/ioOd+1lj4Pwe43P8Vs0CNBuh0K0jiEPdfhLjvbT7qGnJ02JPDzrwaT09vXGlST+iktoERiYgbhTwLzOWM3mk38m2XK2w0fSNiaR2U0Vigd2aQW8Sp2sxEMNHn4I6gfU1Fje4Dgevfu+T16VJZP7CwmVX8esR8am15oapjer008PDlSjwnABduTjQ96R/KX76Trkv2TDB+GPTdbBP//m7BBx0PV/o=; AWSALB=2Y9NEMPDpqYp+vB5QacNwpOE0aphUpksDtwKkgciBEfbfnWAWmXyBYB1wGiecpJuCk/7o5fED7SmJy6v0nNG5OJXLME77Nm1AyeMKuQIFYmDnQBePuxw4BiQsk3J; AWSALBCORS=2Y9NEMPDpqYp+vB5QacNwpOE0aphUpksDtwKkgciBEfbfnWAWmXyBYB1wGiecpJuCk/7o5fED7SmJy6v0nNG5OJXLME77Nm1AyeMKuQIFYmDnQBePuxw4BiQsk3J; bm_sv=E563E561D67B35391BEC8F8C4134EFFE~Xi6qfE/e00tTtqdx+e29SoVKZUCsSqFQ92Do4UkeGH4Ukafg0Rk4F6yMXNqEzwlDueOfR3A4whLmIr771fbGNgNiFmui23s2dmRj3HRRooG0xhDud7TFzsfhczTmKYJHiDL4qVsgYJci25ypu5KDMg=='
}
conn.request("GET", "/apps/dnb/thirdparty/dnbdirectutil?limited=false&captchaDone=true&pageSize=5&pageNumber=1&criteriasearch=true&searchTerm=alphabet", payload, headers)
res = conn.getresponse()
data = res.read()
first_comp=json.loads(data.decode("utf-8"))["searchCandidates"][0]["organization"]
print(first_comp)
base_link="https://www.dnb.com/business-directory/company-profiles."
link=base_link+first_comp["primaryNameForUrl"]+"."+first_comp["duns"]+".html"
print(link)