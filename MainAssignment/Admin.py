e = {}
l = []
added_movies=[]

def admin():
    try:
        print("**********Welcome Admin**************")
        print("1:Add new movie info")
        print("2:Edit movie title")
        print("3:Delete movies")
        print("4:Logout")
        adminchoice = int(input("Enter the choice: "))
        if adminchoice == 1:
            def add_movies():
                Movies = {"title": " ", "genre": " ", "length": " ", "cast": " ", "director": " ", "rating": " ", "language": " ",
                          "shows": " ", "first_show": " ", "interval": " ", "gap": " ", "capacity": " "}

                mov_name = input("Enter the name of the movie to be added:-")
                mov_name = mov_name.upper()
                Movies.update({"title": mov_name})

                mov_genre = input("Enter the genre of the movie:-")
                Movies.update({"genre": mov_genre})

                mov_length = input("Enter the length of the movie(in minutes):-")
                Movies.update({"length": mov_length})

                mov_cast = input("Enter the cast of the movie:-")
                Movies.update({"cast": mov_cast})

                mov_director = input("Enter the director of the movie:-")
                Movies.update({"director": mov_director})

                mov_rating = input("Enter the rating of the movie:-")
                Movies.update({"rating": mov_rating})

                mov_lang = input("Enter the language of the movie:-")
                Movies.update({"language": mov_lang})

                no_shows = input("Enter number of shows:-")
                Movies.update({"shows": no_shows})

                show_hr = int(input("Enter first show hour :-"))
                show_mn = int(input("Enter first show minutes:-"))
                first_show = "{}:{}".format(show_hr, show_mn)
                Movies.update({"first_show": first_show})

                interval = input("Enter interval time:- ")
                Movies.update({"interval": interval})

                gap = input("Enter gap between shows:- ")
                Movies.update({"gap": gap})

                capacity = input("Enter seating capacity:- ")
                Movies.update({"capacity": capacity})

                print(Movies)
                added_movies.append(Movies)
                admin()


            add_movies()



        if adminchoice == 2:
            def update_movies():
                for i in range(len(added_movies)):
                    print(added_movies[i]["title"])

                toEditTitle = input("Enter the movie title which you want to be updated")
                print("Enter which data you want to edit")
                print(
                    "1.Genre\n2.Cast\n3.Director\n4.Admin Rating\n5.Language\n6.Length\tTimings\tNumber of Shows\t.First Show\tInterval\tTimeGap\n7.Capacity")
                while True:
                    n = int(input("Enter your choice which you want to edit or -1 to exit\n"))

                    if (n == -1):
                        break
                    elif (n == 1):
                        new_genre = input("Enter the new genre\n")
                        for i in range(len(added_movies)):
                            if added_movies[i]["title"] == toEditTitle:
                                d = added_movies[i]
                                d.update({"genre": new_genre})
                                print("Updated")
                                break

                    elif (n == 2):
                        new_cast = input("Enter the new cast\n")
                        for i in range(len(added_movies)):
                            if added_movies[i]["title"] == toEditTitle:
                                d = added_movies[i]
                                d.update({"cast": new_cast})
                                print("Updated")
                                break
                    elif (n == 3):
                        new_director = input("Enter the new director\n")
                        for i in range(len(added_movies)):
                            if added_movies[i]["title"] == toEditTitle:
                                d = added_movies[i]
                                d.update({"director": new_director})
                                print("Updated")
                                break

                    elif (n == 4):
                        new_rating = input("Enter the new rating\n")
                        for i in range(len(added_movies)):
                            if added_movies[i]["title"] == toEditTitle:
                                d = added_movies[i]
                                d.update({"rating": new_rating})
                                print("Updated")
                                break
                    elif (n == 5):
                        new_lang = input("Enter the new language\n")
                        for i in range(len(added_movies)):
                            if added_movies[i]["title"] == toEditTitle:
                                d = added_movies[i]
                                d.update({"language": new_lang})
                                print("Updated")
                                break



                    elif (n == 6):
                        new_capacity = input("Enter the new capacity")
                        for i in range(len(added_movies)):
                            if added_movies[i]["title"] == toEditTitle:
                                d = added_movies[i]
                                d.update({"capacity": new_capacity})
                                print("Updated")
                                break

                print(added_movies)
                admin()
            update_movies()

        if adminchoice == 3:
            def delete_movies():
                if (len(added_movies) == 0):
                    print("first enter the details")
                    add_movies()
                for i in range(len(added_movies)):
                    print(added_movies[i]["title"])
                toDeleteMovie = input("Enter the movie name to be deleted")
                flag = 0
                flag1 = 0
                for i in range(len(added_movies)):
                    if added_movies[i]["title"] == toDeleteMovie:
                        del added_movies[i]
                        flag = 1
                        flag1 = 1
                        break
                if (flag == 0):
                    print("enter correct details")
                if (flag1):
                    print(added_movies)

                admin()
            delete_movies()





    except:
        print("Somewhere has gone wrong")



    if adminchoice == 4:
        print("*********Logout Successfull*************")