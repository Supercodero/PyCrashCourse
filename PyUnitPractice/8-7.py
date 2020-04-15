def make_album(singer_name,album_name,num=''):
    album = {"singer":singer_name.title(),"album":album_name.title()}

    if num:
        album["num"] = num
    return album
    
while True:
    print("please input your favorite album's message (you can exit if you input'q')")
    a_n = input("album's name is :")
    if a_n == 'q': break
    s_n = input("singer name is :")
    if s_n == 'q': break
    nu = input("how many cd in that albums?")
    if nu == 'q': break

    album_sample = make_album(album_name=a_n,singer_name=s_n,num=nu)
    print(album_sample)
    