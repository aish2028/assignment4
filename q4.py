try:
    with open("u_story.txt") as f:
        lines=f.readlines()
    w_count={}
    for line in lines:
        words=line.split(" ")
            for word in word:
                word=word.strip().strip("\n").replace(',','').replace(',','')
            try:
                w_count[word]+=1
            except KeyError:
                w_count[word]=1
        max-vla=max(w_count.values())
        for k,v in w_count.items():
            if v==max_val:
                print(f"{k} : {v}")
        count=0
        for key in w_count.keys():
            if keys in ['and','but','if']

except Exception as e:
    print(f"file not found please check path {e}")
