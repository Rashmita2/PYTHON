using System;
using System.IO;
using System.Linq;

namespace ConsoleApp1
{

    class Program
    {
        static void Main(string[] args)
        {
            var random = new Random();
            //creating random numbers
            for(var i = 0; i<10; i++)
            {
                Console.WriteLine(random.Next(1, 10));
            }
            //Printing the ASCII value of a
            Console.WriteLine((int)'a');
        }
    }
}
