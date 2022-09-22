
my_list = [1,0,1,0,1,0,1,0]

def wiki_woko(value):

    if value == 1:
        return "wiki"
    
    else:
        return "woko"

new_result = list(map(wiki_woko, my_list))

print(new_result)