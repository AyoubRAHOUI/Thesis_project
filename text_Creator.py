from elasticsearch import Elasticsearch



es=Elasticsearch([{'host':'localhost','port':9200}])

s = es.search(index='lepic_articles_en',body={
        "size": 610,
        "query": {
        "match_all": {}
    }
})

hits = s['hits']['hits']

l=[]
for i in range(0,len(hits)):
    l.append(hits[i]['_source']['full-text'])

n= l[609].split('\r\n\r\n')


for i in range(0,610):
    full_text= l[i].split('\r\n\r\n')
    filename = "text"+str(i)
    f= open(filename+".input","w+")
    for x in full_text:
        f.write(x)
    f.close() 
