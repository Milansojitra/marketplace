# marketplace
apis : - 

1)  http://127.0.0.1:8000/core/internal-recommand/

description : - this will accept 10 argument from our app and send recommandation
from our side and also from outside of the app.

curl command : - 

"curl --location --request POST 'http://127.0.0.1:8000/core/internal-recommand/' \
--header 'Authorization: Token 20a2fc002dc5973626148e8a55071e29d97223be' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'par_1=par_1' \
--data-urlencode 'par_2=par_2' \
--data-urlencode 'par_3=par_3' \
--data-urlencode 'par_4=par_4' \
--data-urlencode 'par_5=par_5' \
--data-urlencode 'par_6=par_6' \
--data-urlencode 'par_7=par_7' \
--data-urlencode 'par_8=par_8' \
--data-urlencode 'par_9=par_9' \
--data-urlencode 'par_10=par_10'"

3)  http://127.0.0.1:8000/partner/internal-recommand/

description : - this will provide same functionality as 1st one but provide 
risk and recommandation from our side for other partner.

curl command : - 

curl --location --request POST 'http://127.0.0.1:8000/partner/internal-recommand/' \
--header 'Authorization: Token 20a2fc002dc5973626148e8a55071e29d97223be' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'par_1=par_1' \
--data-urlencode 'par_2=par_2' \
--data-urlencode 'par_3=par_3' \
--data-urlencode 'par_4=par_4' \
--data-urlencode 'par_5=par_5' \
--data-urlencode 'par_6=par_6' \
--data-urlencode 'par_7=par_7' \
--data-urlencode 'par_8=par_8' \
--data-urlencode 'par_9=par_9' \
--data-urlencode 'par_10=par_10'

3) http://127.0.0.1:8000/partner/internal-recommand/

description : - this will take 5 argument from outside of the app (ex: welltory)
and consume 5 argument from our side and show risk and recommandation.

curl command : - 

curl --location --request POST 'http://127.0.0.1:8000/core/external-recommand/' \
--header 'Authorization: Token 20a2fc002dc5973626148e8a55071e29d97223be' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'par_1=par_1' \
--data-urlencode 'par_2=par_2' \
--data-urlencode 'par_3=par_3' \
--data-urlencode 'par_4=par_4' \
--data-urlencode 'par_5=par_5'



