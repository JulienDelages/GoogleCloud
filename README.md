# GoogleCloud

Le code python fonctionne en local. 

La création de l'image sur google cloud via "gcloud builds submit --tag gcr.io/plasma-backbone-327312/myimage" met énormément de temps (+1h) et finit par timeout. 

Une image avec une erreur dans le code python a réussi à être mise en ligne à l'adresse suivante https://myimage-67y5rgdn7q-ew.a.run.app.

Malgré cela, le modèle de Machine Learning est obtenable via le lien suivant : https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english

Pour télécharger en local le modèle il faut se placer dans le dossier avec le Dockerfile et éxécuter les commandes suivantes : "git lfs install" et ensuite "git clone https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english"
