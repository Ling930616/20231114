import firebase_admin
from firebase_admin import credentials,firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#doc_ref = db.document("人選之人-造浪者/hVZLyb38Vgl51WG62N9R")

collection_ref = db.collection("人選之人-造浪者")
#docs = collection_ref.where(filter=Fieldilter("name","==","朱芷伶")).get()
#docs = collection_ref.where(filter=Fieldilter("birth",">","2004")).get()
docs = collection_ref.order_by("birth", direction=firestore.Query.DESCENDING).limit(4).get()
for doc in docs:
	x = doc.to_dict()
	print("演員:{},劇中角色是{},出生於{}".format(x["name"],x["role"],x["birth"]))