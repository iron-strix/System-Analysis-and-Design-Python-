my_text = "Winter is coming!".lower()
my_clean_text = my_text.replace(" ","").replace("!","")    
print("Original text: {}".format(my_text))
print("Cleaned text: {}".format(my_clean_text))
 
#calculate number of times the characters appear in a string
my_dict={}
for i in my_clean_text:
    my_dict[i]=my_dict.get(i,0)+1
 
print("\nFrequency of characters:")
#print the characters in descending order from most frequent to least frequent
for j in sorted(my_dict, key=my_dict.get, reverse=True):
    print(j+":",my_dict[j],"time(s)")