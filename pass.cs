using System;

namespace Startapplication
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What is your age? ");
            int age = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("The age is " + age);

            Console.WriteLine("What is your age? ");
            int age2 = Int32.Parse(Console.ReadLine());
            Console.WriteLine("The age is " + age2);
        }
    }
}
