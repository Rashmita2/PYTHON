using System;
namespace Freecode
{
     class Movie
    {
  
        public string title;
        public string director;
        private string rating;

        public Movie(string arating, string atitle, string adirector)
        {
            rating = arating;
            title = atitle;
            director = adirector;
        }
    //getter and setter method
    
        public string Rating
        {
           get {
                return rating;
            }
            set {
                if(value == "A" || value == "B" || value == "C")
                {
                    rating = value;
                }
                else
                {
                    rating = "NR";
                }
            }
        }

    }
}
