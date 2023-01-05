fission spec init
fission env create --spec --name onb-br-enum-activity-env --image nexus.sigame.com.br/fission-onboarding-br-enum-activity-type:0.1.0 --poolsize 0 --version 3 --imagepullsecret "nexus-v3" --spec
fission fn create --spec --name onb-br-enum-activity-fn --env onb-br-enum-activity-env --code fission.py --targetcpu 80 --executortype newdeploy --maxscale 3 --requestsperpod 10000 --spec
fission route create --spec --name onb-br-enum-activity-rt --method GET --url /enum/activity_type --function onb-br-enum-activity-fn
