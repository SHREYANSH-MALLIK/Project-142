import csv

with open("articles.csv",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

with open("article_links.csv",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_article_links = data[1:]

for article_item in all_articles:
    poster_found = any(article_item[8] in article_link_items for article_link_items in all_article_links)
    if poster_found : 
        for article_link_items in all_article_links:
            if article_item[8] == article_link_items[0]:
                article_item.append(article_link_items[1])
                if len(article_item) == 28:
                    with open("final.csv","a+",encoding="utf-8") as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow(article_item)