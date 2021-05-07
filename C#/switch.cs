using System;

namespace Freecode
{
    class Program
    {
        static void Main(String[] args)
        {
            string WeekDay = "Sunday";
            switch (WeekDay)
            {
                case "Monday":
                    Console.WriteLine("The day is Monday.");
                    break;
                case "Sunday":
                    Console.WriteLine("Yay! today is holiday.");
                    break;
                default:
                    Console.WriteLine("Not mentioned");
                    break;
            }
        }
        
    }
}
