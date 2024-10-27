# Written by Nate Malek
#
# Libraries Used
library(dplyr)

# Downloads of Health Insurance Questionnaire files
download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HIQ_I.XPT", tf <- tempfile(), mode="wb")
HealthIns_2015 = foreign::read.xport(tf)

download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/HIQ_J.XPT", tf <- tempfile(), mode="wb")
HealthIns_2017 = foreign::read.xport(tf)


# Downloads of Medical Conditions Questionnaire files
download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/MCQ_I.XPT", tf <- tempfile(), mode="wb")
MedCon_2015 = foreign::read.xport(tf)

download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/MCQ_J.XPT", tf <- tempfile(), mode="wb")
MedCon_2017 = foreign::read.xport(tf)


# Downloads of Immunization Questionnaire files
download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/IMQ_I.XPT", tf <- tempfile(), mode="wb")
Immuno_2015 = foreign::read.xport(tf)

download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/IMQ_J.XPT", tf <- tempfile(), mode="wb")
Immuno_2017 = foreign::read.xport(tf)


# Downloads of Hepatitis Questionnaire files
download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HEQ_I.XPT", tf <- tempfile(), mode="wb")
HepQ_2015 = foreign::read.xport(tf)

download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/HEQ_J.XPT", tf <- tempfile(), mode="wb")
HepQ_2017 = foreign::read.xport(tf)


# Downloads of Demographic data files
download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT", tf <- tempfile(), mode="wb")
Demo_2015 = foreign::read.xport(tf)

download.file("https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT", tf <- tempfile(), mode="wb")
Demo_2017 = foreign::read.xport(tf)


# Binding each set of data together
HealthIns = bind_rows(HealthIns_2015, HealthIns_2017)
MedCon = bind_rows(MedCon_2015, MedCon_2017)
Immuno = bind_rows(Immuno_2015, Immuno_2017)
HepQ = bind_rows(HepQ_2015, HepQ_2017)
Demo = bind_rows(Demo_2015, Demo_2017)

# Edits by ET

write.csv(HealthIns, "./data/HealthIns.csv")
write.csv(MedCon, "./data/MedCon.csv")
write.csv(Immuno, "./data/Immuno.csv")
write.csv(HepQ, "./data/HepQ.csv")
write.csv(Demo, "./data/Demo.csv")
