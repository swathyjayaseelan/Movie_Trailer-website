import media
import fresh_tomatoes

'''The instances of the class Movie are instantiated here with the arguments
    of Movie title, Story line, Poster image and the youtube trailer url '''
avatar = media.Movie(
         "Avatar",
         "On the lush alien world of Pandora live the Na'vi," +
         "beings who appear primitive but are highly evolved." +
         "Because the planet's environment is poisonous, human/Na'vi" +
         "hybrids,called Avatars, must link to human minds" +
         "to allow for free movement on Pandora. Jake Sully " +
         "(Sam Worthington), a paralyzed former Marine," +
         "becomes mobile again through one such Avatar" +
         "and falls in love with" +
         "a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn" +
         "into a battle for the survival of her world.",
         "https://upload.wikimedia.org/wikipedia" +
         "/en/b/b0/Avatar-Teaser-Poster.jpg",
         "https://www.youtube.com/watch?v=5PSNL1qE6VY")

beauty_and_beast = media.Movie(
        "Beauty and the Beast",
        "An arrogant young prince (Robby Benson) and his castle's servants" +
        "fall under the spell of a wicked enchantress," +
        "who turns him into the hideous Beast until he" +
        "learns to love and be loved in return." +
        "The spirited, headstrong village girl Belle (Paige O'Hara)" +
        "enters the Beast's castle after he" +
        "imprisons her father Maurice (Rex Everhart)." +
        "With the help of his enchanted servants," +
        "including the matronly Mrs. Potts (Angela Lansbury)," +
        "Belle begins to draw the cold-hearted Beast" +
        "out of his isolation.",
        "https://media1.popsugar-assets.com/files/thumbor/" +
        "8wedSPI4RyNdIbYuQr9w9zy0sLA/fit-in/1024x1024/filters:" +
        "format_auto-!!-:strip_icc-!!-/2017/01/26/813/n/1922283/" +
        "055dc333c3280d59_BeautyAndTheBeast58726d5b9fac8/i/" +
        "Beauty-Beast-2017-Movie-Posters.jpg",
        "https://www.youtube.com/watch?v=OvW_L8sTu5E")

boss_baby = media.Movie(
        "The Boss Baby",
        "A suit-wearing briefcase-carrying baby pairs" +
        "up with his seven-year old brother to stop the" +
        "dastardly plot of the CEO of Puppy Co",
        "https://www.flickeringmyth.com/wp-content/" +
        "uploads/2016/07/Boss-Baby-poster.jpg",
        "https://www.youtube.com/watch?v=tquIfapGVqs")

smurfs = media.Movie(
        "Smurfs: The Lost Village",
        "Best friends Smurfette (Demi Lovato), Brainy (Danny Pudi)," +
        "Clumsy (Jack McBrayer) and Hefty (Joe Manganiello) use a" +
        "special map that guides them through the Forbidden Forest," +
        "an enchanted wonderland that's filled with magical creatures." +
        "Their adventure leads them on a course to discover the biggest" +
        "secret in Smurf history as they race against time and the evil" +
        "wizard Gargamel (Rainn Wilson) to find" +
        "a mysterious village.",
        "http://www.impawards.com/2017/posters/" +
        "smurfs_the_lost_village_ver7.jpg",
        "https://www.youtube.com/watch?v=9NO8wk4n1Cs")

logan = media.Movie(
        " Logan",
        "In the near future, a weary Logan (Hugh Jackman) cares" +
        "for an ailing Professor X (Patrick Stewart) at a remote outpost" +
        "on the Mexican border. His plan to hide from the outside world" +
        "gets upended when he meets a young mutant (Dafne Keen) who is" +
        "very much like him. Logan must now protect the girl and battle" +
        "the dark forces that want to capture her.",
        "http://screencrush.com/files/2017/01/loganposter2.jpg",
        "https://www.youtube.com/watch?v=Div0iP65aZo")

twilight = media.Movie(
        "Twilight",
        "High-school student Bella Swan (Kristen Stewart), always" +
        "a bit of a misfit, doesn't expect life to change much when" +
        "she moves from sunny Arizona to rainy Washington state." +
        "Then she meets Edward Cullen (Robert Pattinson), a handsome" +
        "but mysterious teen whose eyes seem to peer directly into her soul." +
        "Edward is a vampire whose family does not drink blood, and Bella," +
        "far from being frightened, enters into a dangerous" +
        "romance with her immortal soulmate.",
        "http://i.ebayimg.com/00/s/NDUwWDMwMg==/z/" +
        "f94AAOxyOlhSsl2Z/$_3.JPG?set_id=2",
        "https://www.youtube.com/watch?v=fFLrRlPBg0A")
movie_list = [avatar, beauty_and_beast, boss_baby, smurfs, logan, twilight]
fresh_tomatoes.open_movies_page(movie_list)

