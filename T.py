import webbrowser

User_Search = input("What Do You want to search. All results will open in your default browser")
User_Google = input("Would you like to search on google?, IF YES THEN TYPE 1, IF NO THEN TYPE 0")
User_Bing = input("Would you like to search on Bing?, IF YES THEN TYPE 1, IF NO THEN TYPE 0")
User_Yahoo = input("Would you like to search on Yahoo?, IF YES THEN TYPE 1, IF NO THEN TYPE 0")
User_YouTube = input("Would you like to search on YouTube?, IF YES THEN TYPE 1, IF NO THEN TYPE 0")
User_DuckDuckGo = input("Would you like to search on DuckDuckgo?, IF YES THEN TYPE 1, IF NO THEN TYPE 0")
User_Qmamu  = input("Would you like to search on Qmamu?, IF YES THEN TYPE 1, IF NO THEN TYPE 0")
def open_websites():
    if User_Google == '1':
        URL_Google = "https://www.google.com/search?q=" + User_Search
        print(URL_Google)
    else:
        print("Let's skip Google")
    if User_Bing == "1":
        URL_Bing = "https://www.bing.com/search?q=" + User_Search
        print(URL_Bing)
    else:
        print("Let's skip Bing")
    if User_Yahoo == "1":
        URL_Yahoo = "https://search.yahoo.com/search?p=" + User_Search
        webbrowser.open(URL_Yahoo)
    else:
        print("Lets skip Yahoo")
    if User_YouTube == "1":
        Search_Query_Req = User_Search.replace(' ', '+')
        URL_YouTube = "https://www.youtube.com/results?search_query=" + Search_Query_Req
        webbrowser.open(URL_YouTube)
    if User_DuckDuckGo == "1":
        Search_Query_Req = User_Search.replace(' ', '+')
        URL_DuckDuckGo = "https://duckduckgo.com/?q=" + Search_Query_Req
        webbrowser.open(URL_DuckDuckGo)
    if User_Qmamu == "1":
        Search_Query_Req = User_Search.replace(' ', '+')
        URL_Qmamu = "https://qmamu.com/search?q=" + Search_Query_Req
        webbrowser.open(URL_Qmamu)


with open ('Choices and Name.txt', 'a') as f:
    Set_Default_Which = input("Which Website do you prefer to search? Google , Bing , Qmamu , Yahoo , DuckDuckGo , YouTube")
    Name_User = input("Can you tell me your name?")
    f.writelines((Name_User, ' prefers ', Set_Default_Which, '\n'))
print("Thank You for using this tool!")
open_websites()