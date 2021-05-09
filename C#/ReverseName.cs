using System;
using System.IO;
using System.Linq;

namespace ConsoleApp1
{

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(" What is your name? ");
            var name = Console.ReadLine();
            var reversed = ReverseString(name);
            Console.WriteLine("Reversed name: " + reversed);
        }

        public static string ReverseString(string name)
        {
            var array = new char[name.Length];
            for(var i = name.Length; i> 0; i--)
            {
                array[name.Length - i] = name[i - 1];

            }
            var reversed = new string(array);

            return reversed;
        }
    }
}
