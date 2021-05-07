using System;

namespace Freecode
{
    class Program
    {
        static void Main(String[] args)
        {
            int num = 34;
            int guessnum  = 0;
            while(guessnum != num)
            {
               Console.WriteLine("Enter the number:");
                guessnum = Convert.ToInt32(Console.ReadLine());

            }
            Console.WriteLine("Yay! You guessed it.");
        }
        
    }
}
