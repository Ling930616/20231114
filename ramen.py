import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
      "名稱": "大蒜拳骨拉麵",
      "價格": "198元",
},
{
      "名稱": "大蒜拳骨白濃拉麵",
      "價格": "198元",
},
{
      "名稱": "大蒜拳骨味噌拉麵",
      "價格": "198元",
},
{
      "名稱": "大蒜拳骨激辣拉麵",
      "價格": "220元",
},
{
      "名稱": "銀次郎魚豚拉麵",
      "價格": "250元",
},
{
      "名稱": "黃金味噌拉麵",
      "價格": "250元",
},
{
      "名稱": "大蒜拳骨叉燒拉麵",
      "價格": "258元",
},
{
      "名稱": "大蒜拳骨白濃叉燒拉麵",
      "價格": "258元",
},
{
      "名稱": "大蒜拳骨味噌叉燒拉麵",
      "價格": "258元",
},
{
      "名稱": "大蒜拳骨激辣叉燒拉麵",
      "價格": "280元",
},
{
      "名稱": "藤崎家拉麵",
      "價格": "250元",
},
{
      "名稱": "竹下食堂醬油拉麵",
      "價格": "210元",
}

]

collection_ref = db.collection("拉麵MENU")
for doc in docs:
  collection_ref.add(doc)
